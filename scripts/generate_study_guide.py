"""
Generate comprehensive HTML study guide from Uitwerkingen Opgaven

This creates a professional, exam-ready study guide with:
- All problems with full solutions
- All images embedded
- Formula references
- Chapter organization
- Navigation and table of contents
- Educational context and explanations

Output: study-guide/uitwerkingen-complete-guide.html
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Force UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_MD = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
OUTPUT_DIR = PROJECT_ROOT / "study-guide"
OUTPUT_HTML = OUTPUT_DIR / "uitwerkingen-complete-guide.html"
IMAGES_DIR = PROJECT_ROOT / "images" / "uitwerkingen"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Patterns
CHAPTER_PATTERN = re.compile(r'H\s+(\d+)\.(\d+)\s+blz\.?\s+(\d+)', re.IGNORECASE)
OPGAVE_PATTERN = re.compile(r'^Opgave\s+(.+?)[:.]?\s*(.*)$', re.IGNORECASE)
UITWERKING_PATTERN = re.compile(r'^Uitwerking\s+(?:opgave\s+|opdracht\s+)?(.+?)[:.]?\s*(.*)$', re.IGNORECASE)
IMAGE_PATTERN = re.compile(r'!\[.*?\]\((opgave_\d+\.(?:png|emf|gif))\)')
FORMULA_MARKER = re.compile(r'\*\*\[FORMULE\]:\*\*\s*`\[FORMULA\]`')


def parse_document_structure(input_file: Path) -> Dict[str, Any]:
    """Parse document and organize by chapters and problems."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    structure = {
        'title': 'Uitwerkingen Opgaven Energietechniek',
        'version': 'V0.8',
        'chapters': {},
        'problems': []
    }

    current_chapter = None
    current_problem = None
    current_section = None  # 'opgave' or 'uitwerking'
    content_buffer = []

    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Detect chapter
        chapter_match = CHAPTER_PATTERN.search(line_stripped)
        if chapter_match:
            ch_num = int(chapter_match.group(1))
            sec_num = int(chapter_match.group(2))
            page_num = int(chapter_match.group(3))

            chapter_key = f"H{ch_num}.{sec_num}"
            if chapter_key not in structure['chapters']:
                structure['chapters'][chapter_key] = {
                    'chapter': ch_num,
                    'section': sec_num,
                    'page': page_num,
                    'problems': []
                }
            current_chapter = chapter_key
            continue

        # Detect opgave
        opgave_match = OPGAVE_PATTERN.match(line_stripped)
        if opgave_match:
            # Save previous problem
            if current_problem and current_section == 'uitwerking':
                current_problem['uitwerking_content'] = '\n'.join(content_buffer)
                structure['problems'].append(current_problem)

                if current_chapter:
                    structure['chapters'][current_chapter]['problems'].append(
                        len(structure['problems']) - 1
                    )

            # Start new problem
            opgave_id = opgave_match.group(1).strip()
            inline_text = opgave_match.group(2).strip()

            current_problem = {
                'id': opgave_id,
                'chapter': current_chapter,
                'opgave_content': inline_text,
                'uitwerking_content': '',
                'images': []
            }
            current_section = 'opgave'
            content_buffer = [inline_text] if inline_text else []
            continue

        # Detect uitwerking
        uitwerking_match = UITWERKING_PATTERN.match(line_stripped)
        if uitwerking_match and current_problem:
            inline_text = uitwerking_match.group(2).strip()

            current_problem['opgave_content'] = '\n'.join(content_buffer)
            current_section = 'uitwerking'
            content_buffer = [inline_text] if inline_text else []
            continue

        # Collect images
        image_matches = IMAGE_PATTERN.findall(line_stripped)
        if image_matches and current_problem:
            for img in image_matches:
                current_problem['images'].append({
                    'filename': img,
                    'section': current_section
                })

        # Accumulate content
        if current_section and line_stripped:
            if not line_stripped.startswith('*Afbeelding:') and not line_stripped.startswith('!['):
                content_buffer.append(line_stripped)

    # Save last problem
    if current_problem and current_section == 'uitwerking':
        current_problem['uitwerking_content'] = '\n'.join(content_buffer)
        structure['problems'].append(current_problem)

        if current_chapter:
            structure['chapters'][current_chapter]['problems'].append(
                len(structure['problems']) - 1
            )

    return structure


def generate_html_head() -> str:
    """Generate HTML head with styling."""

    return """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven Energietechniek - Volledige Studiegids</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --bg-color: #ecf0f1;
            --card-bg: #ffffff;
            --text-color: #2c3e50;
            --border-color: #bdc3c7;
            --code-bg: #f8f9fa;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 3px solid var(--secondary-color);
        }

        h1 {
            color: var(--primary-color);
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .subtitle {
            color: var(--secondary-color);
            font-size: 1.2em;
            margin-top: 10px;
        }

        .metadata {
            background: var(--code-bg);
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border-left: 4px solid var(--secondary-color);
        }

        nav {
            background: var(--code-bg);
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            position: sticky;
            top: 20px;
            z-index: 100;
        }

        nav h2 {
            color: var(--primary-color);
            margin-bottom: 15px;
        }

        nav ul {
            list-style: none;
            column-count: 3;
            column-gap: 20px;
        }

        nav li {
            margin-bottom: 8px;
        }

        nav a {
            color: var(--secondary-color);
            text-decoration: none;
            transition: color 0.3s;
        }

        nav a:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }

        .chapter {
            margin: 40px 0;
            padding: 30px;
            background: linear-gradient(to right, #f8f9fa 0%, #ffffff 100%);
            border-left: 5px solid var(--secondary-color);
            border-radius: 5px;
        }

        .chapter-header {
            color: var(--primary-color);
            font-size: 1.8em;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .chapter-meta {
            font-size: 0.6em;
            color: #7f8c8d;
        }

        .problem {
            margin: 30px 0;
            padding: 25px;
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        .problem-header {
            background: var(--secondary-color);
            color: white;
            padding: 12px 20px;
            border-radius: 5px 5px 0 0;
            margin: -25px -25px 20px -25px;
            font-size: 1.3em;
            font-weight: bold;
        }

        .opgave-section {
            margin-bottom: 25px;
        }

        .opgave-section h4 {
            color: var(--primary-color);
            margin-bottom: 10px;
            font-size: 1.1em;
            display: flex;
            align-items: center;
        }

        .opgave-section h4:before {
            content: "📝";
            margin-right: 8px;
        }

        .uitwerking-section h4:before {
            content: "✅";
            margin-right: 8px;
        }

        .content {
            line-height: 1.8;
            color: #34495e;
        }

        .content p {
            margin-bottom: 10px;
        }

        .formula-marker {
            display: inline-block;
            background: #fff3cd;
            padding: 2px 8px;
            border-radius: 3px;
            border: 1px solid #ffc107;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #856404;
            margin: 0 2px;
        }

        .image-container {
            margin: 15px 0;
            text-align: center;
            background: #fafafa;
            padding: 10px;
            border-radius: 5px;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border: 1px solid var(--border-color);
            border-radius: 3px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            background: white;
            padding: 5px;
        }

        /* Smaller images are likely formulas - show inline */
        .image-container img[src*=".png"] {
            display: inline-block;
            vertical-align: middle;
        }

        .image-caption {
            font-size: 0.9em;
            color: #7f8c8d;
            margin-top: 8px;
            font-style: italic;
        }

        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: var(--secondary-color);
            color: white;
            padding: 12px 20px;
            border-radius: 50px;
            text-decoration: none;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            transition: all 0.3s;
        }

        .back-to-top:hover {
            background: var(--accent-color);
            transform: translateY(-3px);
        }

        .educational-note {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }

        .educational-note:before {
            content: "💡 ";
            font-weight: bold;
        }

        .exam-tip {
            background: #fff3e0;
            border-left: 4px solid #ff9800;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
        }

        .exam-tip:before {
            content: "⚠️ Examenpunt: ";
            font-weight: bold;
        }

        @media print {
            .back-to-top, nav {
                display: none;
            }

            .problem {
                page-break-inside: avoid;
            }
        }

        @media (max-width: 768px) {
            nav ul {
                column-count: 1;
            }

            .container {
                padding: 20px;
            }

            .chapter-header {
                font-size: 1.4em;
                flex-direction: column;
                align-items: flex-start;
            }
        }
    </style>
</head>
<body>
"""


def format_content_with_formulas(text: str) -> str:
    """Format text content, replacing formula markers with styled spans."""

    # Replace formula markers
    text = FORMULA_MARKER.sub('<span class="formula-marker">[Formule - zie afbeelding]</span>', text)

    # Convert line breaks to <br>
    lines = text.split('\n')
    formatted_lines = []

    for line in lines:
        if line.strip():
            formatted_lines.append(f"<p>{line}</p>")

    return '\n'.join(formatted_lines)


def get_educational_context(problem_id: str, opgave_text: str) -> str:
    """Generate educational context based on problem content."""

    context = []

    # Detect topic and add relevant tips
    if 'kirchhoff' in opgave_text.lower() or 'knooppunt' in opgave_text.lower():
        context.append('<div class="educational-note">Kirchhoff\'s wetten zijn fundamenteel voor netwerk-analyse. '
                      'Onthoud: som van stromen IN = som van stromen UIT (knooppuntwet), '
                      'en som van spanningen in een gesloten kring = 0 (maaswet).</div>')

    if 'thévenin' in opgave_text.lower() or 'norton' in opgave_text.lower():
        context.append('<div class="exam-tip">Thévenin en Norton equivalenten zijn examen-kritisch! '
                      'Oefen het vinden van Uth (open klemspanning) en Ik (kortsluitstroom).</div>')

    if 'vermogen' in opgave_text.lower() or 'arbeidsfactor' in opgave_text.lower():
        context.append('<div class="educational-note">Vermogensberekeningen: P = U·I·cos(φ) (actief), '
                      'Q = U·I·sin(φ) (reactief), S = U·I (schijnbaar). '
                      'Vermogensdriehoek helpt bij visualisatie!</div>')

    if 'driefase' in opgave_text.lower() or 'ster' in opgave_text.lower():
        context.append('<div class="exam-tip">Driefasensystemen: In ster-schakeling geldt Ul = √3·Uf. '
                      'In driehoek geldt Il = √3·If. Let op de factor √3!</div>')

    return '\n'.join(context)


def generate_problem_html(problem: Dict[str, Any], index: int, images_rel_path: str) -> str:
    """Generate HTML for a single problem."""

    html = [f'<div class="problem" id="problem-{index}">']
    html.append(f'<div class="problem-header">Opgave {problem["id"]}</div>')

    # Add educational context
    educational_context = get_educational_context(problem['id'], problem['opgave_content'])
    if educational_context:
        html.append(educational_context)

    # Opgave section
    html.append('<div class="opgave-section">')
    html.append('<h4>Vraagstelling</h4>')
    html.append('<div class="content">')
    html.append(format_content_with_formulas(problem['opgave_content']))
    html.append('</div>')

    # Add opgave images (include ALL - they contain formulas AND diagrams)
    opgave_images = [img for img in problem['images'] if img['section'] == 'opgave']
    if opgave_images:
        html.append('<div class="educational-note">De onderstaande afbeeldingen bevatten de vraagstelling, '
                   'schema\'s en formules die bij deze opgave horen.</div>')
        for img in opgave_images:  # Show ALL opgave images
            html.append('<div class="image-container">')
            html.append(f'<img src="{images_rel_path}/{img["filename"]}" alt="Schema {img["filename"]}">')
            html.append('</div>')

    html.append('</div>')  # End opgave-section

    # Uitwerking section
    if problem['uitwerking_content']:
        html.append('<div class="uitwerking-section">')
        html.append('<h4>Uitwerking</h4>')
        html.append('<div class="content">')
        html.append(format_content_with_formulas(problem['uitwerking_content']))
        html.append('</div>')

        # Add uitwerking images (ALL - contain step-by-step formulas and calculations)
        uitwerking_images = [img for img in problem['images'] if img['section'] == 'uitwerking']
        if uitwerking_images:
            html.append('<div class="educational-note">Bekijk de onderstaande stappen zorgvuldig. '
                       'Elke afbeelding toont een belangrijke rekenstap, formule of tussenstap.</div>')

            for img in uitwerking_images:  # Show ALL uitwerking images
                html.append('<div class="image-container">')
                html.append(f'<img src="{images_rel_path}/{img["filename"]}" alt="Uitwerking {img["filename"]}">')
                html.append('</div>')

        html.append('</div>')  # End uitwerking-section

    html.append('</div>')  # End problem

    return '\n'.join(html)


def generate_html_guide(structure: Dict[str, Any]) -> str:
    """Generate complete HTML study guide."""

    # Calculate relative path from output to images
    images_rel_path = "../images/uitwerkingen"

    html = []

    # Head
    html.append(generate_html_head())

    # Container start
    html.append('<div class="container">')

    # Header
    html.append('<header>')
    html.append(f'<h1>{structure["title"]}</h1>')
    html.append(f'<div class="subtitle">Versie {structure["version"]} - Volledige Studiegids</div>')
    html.append('<div class="metadata">')
    html.append('<p><strong>Bron:</strong> Ir. JGM van der Zanden</p>')
    html.append('<p><strong>Referentie:</strong> Holmes - Elektrische Netwerken (3e editie)</p>')
    html.append(f'<p><strong>Aantal opgaven:</strong> {len(structure["problems"])}</p>')
    html.append(f'<p><strong>Hoofdstukken:</strong> {", ".join(sorted(structure["chapters"].keys()))}</p>')
    html.append('</div>')
    html.append('</header>')

    # Navigation / Table of Contents
    html.append('<nav id="toc">')
    html.append('<h2>📚 Inhoudsopgave</h2>')
    html.append('<ul>')

    for chapter_key in sorted(structure['chapters'].keys()):
        chapter = structure['chapters'][chapter_key]
        problem_count = len(chapter['problems'])
        html.append(f'<li><a href="#chapter-{chapter_key}">{chapter_key} '
                   f'({problem_count} opgaven, blz. {chapter["page"]})</a></li>')

    html.append('</ul>')
    html.append('</nav>')

    # Chapters and problems
    for chapter_key in sorted(structure['chapters'].keys()):
        chapter = structure['chapters'][chapter_key]

        html.append(f'<div class="chapter" id="chapter-{chapter_key}">')
        html.append(f'<div class="chapter-header">')
        html.append(f'<span>Hoofdstuk {chapter_key}</span>')
        html.append(f'<span class="chapter-meta">Bladzijde {chapter["page"]} | '
                   f'{len(chapter["problems"])} opgaven</span>')
        html.append('</div>')

        # Add problems in this chapter
        for problem_idx in chapter['problems']:
            problem = structure['problems'][problem_idx]
            html.append(generate_problem_html(problem, problem_idx, images_rel_path))

        html.append('</div>')  # End chapter

    # Back to top button
    html.append('<a href="#toc" class="back-to-top">↑ Terug naar boven</a>')

    # Container end
    html.append('</div>')

    # Body and HTML end
    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("GENERATING COMPLETE STUDY GUIDE")
    print("="*70 + "\n")

    print(f"Reading: {INPUT_MD.relative_to(PROJECT_ROOT)}")

    # Parse document
    structure = parse_document_structure(INPUT_MD)

    print(f"✓ Found {len(structure['problems'])} problems")
    print(f"✓ Found {len(structure['chapters'])} chapters")

    # Count images
    total_images = sum(len(p['images']) for p in structure['problems'])
    print(f"✓ Found {total_images} image references")

    # Generate HTML
    print(f"\nGenerating HTML study guide...")
    html_content = generate_html_guide(structure)

    # Write to file
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ HTML written to: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")

    # File size
    file_size_kb = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ File size: {file_size_kb:.1f} KB")

    print("\n" + "="*70)
    print("GENERATION COMPLETE")
    print("="*70)
    print(f"\nStudy guide ready:")
    print(f"  File: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"  Open in browser to view")
    print(f"\nFeatures:")
    print(f"  ✓ Table of contents with navigation")
    print(f"  ✓ All {len(structure['problems'])} problems with solutions")
    print(f"  ✓ {total_images} embedded diagrams and formulas")
    print(f"  ✓ Educational context and exam tips")
    print(f"  ✓ Professional styling and layout")
    print(f"  ✓ Print-friendly format")


if __name__ == "__main__":
    main()
