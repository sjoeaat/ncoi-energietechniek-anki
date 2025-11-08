"""
Extract content from "Uitwerkingen Opgaven Energietechniek V0.8.docx"

This script extracts:
- Text content with structure (headings, paragraphs, lists)
- Mathematical formulas (equations)
- Embedded images (diagrams, circuits, etc.)
- Tables

Output:
- Structured markdown file in analysis/
- Images saved to images/uitwerkingen/
"""

import os
import sys
from pathlib import Path
from docx import Document

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
import base64

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
SOURCE_FILE = PROJECT_ROOT / "source-materials" / "Uitwerkingen Opgaven Energietechniek V0.8.docx"
OUTPUT_MD = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
OUTPUT_IMG_DIR = PROJECT_ROOT / "images" / "uitwerkingen"

# Create output directories
OUTPUT_IMG_DIR.mkdir(parents=True, exist_ok=True)


def extract_images_from_paragraph(paragraph, image_counter):
    """Extract images embedded in a paragraph."""
    images = []

    # Check for inline shapes (images)
    for run in paragraph.runs:
        # Check if run contains images
        if 'graphic' in run._element.xml:
            for rel in paragraph.part.rels.values():
                if "image" in rel.target_ref:
                    try:
                        image_data = rel.target_part.blob

                        # Determine image extension
                        content_type = rel.target_part.content_type
                        if 'png' in content_type:
                            ext = 'png'
                        elif 'jpeg' in content_type or 'jpg' in content_type:
                            ext = 'jpg'
                        elif 'gif' in content_type:
                            ext = 'gif'
                        elif 'emf' in content_type or 'wmf' in content_type:
                            ext = 'emf'  # Windows metafile
                        else:
                            ext = 'bin'

                        # Save image
                        image_filename = f"opgave_{image_counter:03d}.{ext}"
                        image_path = OUTPUT_IMG_DIR / image_filename

                        with open(image_path, 'wb') as img_file:
                            img_file.write(image_data)

                        images.append(image_filename)
                        image_counter += 1

                        print(f"  ✓ Extracted image: {image_filename}")
                    except Exception as e:
                        print(f"  ⚠ Error extracting image: {e}")

    return images, image_counter


def extract_table(table):
    """Convert table to markdown format."""
    md_table = []

    for i, row in enumerate(table.rows):
        cells = [cell.text.strip() for cell in row.cells]
        md_table.append("| " + " | ".join(cells) + " |")

        # Add separator after header row
        if i == 0:
            md_table.append("| " + " | ".join(["---"] * len(cells)) + " |")

    return "\n".join(md_table)


def extract_math_from_paragraph(paragraph):
    """Extract math equations from paragraph (if any)."""
    # OOXML math is stored in <m:oMath> elements
    math_elements = []

    for element in paragraph._element.iter():
        if element.tag.endswith('oMath'):
            # Found math element - extract raw content
            math_text = element.text if element.text else "[FORMULA]"
            math_elements.append(math_text)

    return math_elements


def get_paragraph_style(paragraph):
    """Determine paragraph style (heading level, normal, list)."""
    style_name = paragraph.style.name if paragraph.style else ""

    if 'Heading 1' in style_name:
        return 'h1'
    elif 'Heading 2' in style_name:
        return 'h2'
    elif 'Heading 3' in style_name:
        return 'h3'
    elif 'List' in style_name or paragraph._element.pPr is not None:
        # Check for list numbering
        numPr = paragraph._element.pPr.find('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numPr')
        if numPr is not None:
            return 'list'

    return 'normal'


def extract_docx_content(docx_path):
    """Main extraction function."""
    print(f"\n{'='*70}")
    print(f"EXTRACTING: {docx_path.name}")
    print(f"{'='*70}\n")

    doc = Document(docx_path)

    markdown_output = []
    markdown_output.append(f"# Uitwerkingen Opgaven Energietechniek V0.8\n")
    markdown_output.append(f"**Bron:** {SOURCE_FILE.name}\n")
    markdown_output.append(f"**Extractie datum:** {Path(__file__).stat().st_mtime}\n")
    markdown_output.append(f"\n---\n")

    image_counter = 1
    question_number = 0

    for block in doc.element.body:
        # Handle paragraphs
        if isinstance(block, CT_P):
            paragraph = Paragraph(block, doc)
            text = paragraph.text.strip()

            if not text:
                markdown_output.append("")  # Empty line
                continue

            # Get style
            style = get_paragraph_style(paragraph)

            # Extract images from this paragraph
            images, image_counter = extract_images_from_paragraph(paragraph, image_counter)

            # Extract math formulas
            math_formulas = extract_math_from_paragraph(paragraph)

            # Format based on style
            if style == 'h1':
                markdown_output.append(f"\n## {text}\n")
                question_number += 1
            elif style == 'h2':
                markdown_output.append(f"\n### {text}\n")
            elif style == 'h3':
                markdown_output.append(f"\n#### {text}\n")
            elif style == 'list':
                markdown_output.append(f"- {text}")
            else:
                markdown_output.append(text)

            # Add math formulas if found
            if math_formulas:
                for formula in math_formulas:
                    markdown_output.append(f"\n**[FORMULE]:** `{formula}`\n")

            # Add image references
            if images:
                for img in images:
                    markdown_output.append(f"\n![Diagram]({img})\n")
                    markdown_output.append(f"*Afbeelding: `images/uitwerkingen/{img}`*\n")

        # Handle tables
        elif isinstance(block, CT_Tbl):
            table = Table(block, doc)
            markdown_output.append("\n")
            markdown_output.append(extract_table(table))
            markdown_output.append("\n")

    # Write markdown output
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown_output))

    print(f"\n{'='*70}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'='*70}")
    print(f"✓ Markdown output: {OUTPUT_MD}")
    print(f"✓ Images extracted: {image_counter - 1}")
    print(f"✓ Image directory: {OUTPUT_IMG_DIR}")
    print(f"\nNext steps:")
    print(f"1. Review: {OUTPUT_MD.relative_to(PROJECT_ROOT)}")
    print(f"2. Check images in: {OUTPUT_IMG_DIR.relative_to(PROJECT_ROOT)}")
    print(f"3. Generate Anki cards from structured content")


if __name__ == "__main__":
    if not SOURCE_FILE.exists():
        print(f"ERROR: Source file not found: {SOURCE_FILE}")
        sys.exit(1)

    extract_docx_content(SOURCE_FILE)
