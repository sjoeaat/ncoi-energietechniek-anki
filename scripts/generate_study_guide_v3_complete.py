"""
Generate Complete Study Guide v3 - Full Content with All Images

Uses:
- Enhanced YAML for full text content
- All 1335 images from images/uitwerkingen/

Strategy: Place images sequentially throughout the document based on opgave sections.
"""

import sys
import yaml
import re
from pathlib import Path
from typing import List, Dict, Any

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENHANCED_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-enhanced.yaml"
OLD_EXTRACT = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-complete-guide-v3.html"
IMAGES_DIR = PROJECT_ROOT / "images" / "uitwerkingen"


def extract_images_per_opgave_from_old() -> Dict[str, List[str]]:
    """
    Parse old extraction to get images per opgave.

    Uses FLEXIBLE pattern matching to handle all header variations:
    - "Opgave 1:", "Opgave 1.", "Opgave 1 "
    - "Opgave 1a:", "Opgave 2.d"
    - "Opgave 6, 7 en 8:" (grouped opgaven)
    - "Opgave 1. Driehoek" (with description)
    """
    print("Extracting image-opgave mapping from old extract...")

    with open(OLD_EXTRACT, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find ALL "Opgave" headers with flexible pattern
    # Matches: "Opgave 1:", "Opgave 1.", "Opgave 1a:", "Opgave 2.d", "Opgave 6, 7 en 8:", etc.
    opgave_pattern = r'\nOpgave\s+([0-9]+[a-z]?(?:\.[a-z])?(?:,\s*[0-9]+(?:\s+en\s+[0-9]+)?)?)[:\.,\s]'
    matches = list(re.finditer(opgave_pattern, content))

    print(f"  Found {len(matches)} opgave headers in old extraction")

    image_map = {}

    for i, match in enumerate(matches):
        opgave_full = match.group(1).strip()

        # Extract primary ID (first number + optional letter)
        # "6, 7 en 8" -> "6"
        # "1a" -> "1a"
        # "2.d" -> "2"
        id_match = re.match(r'^([0-9]+[a-z]?)', opgave_full)
        if not id_match:
            continue

        opgave_id = id_match.group(1)

        start_pos = match.end()
        end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)

        section = content[start_pos:end_pos]

        # Find images in this section
        images = re.findall(r'!\[.*?\]\((opgave_\d+\.(?:png|emf|gif))\)', section)

        if images:
            # Remove duplicates while preserving order
            unique = []
            seen = set()
            for img in images:
                if img not in seen:
                    unique.append(img)
                    seen.add(img)

            # Append to existing if ID already exists (handles grouped opgaven)
            if opgave_id in image_map:
                image_map[opgave_id].extend(unique)
            else:
                image_map[opgave_id] = unique

    total = sum(len(imgs) for imgs in image_map.values())
    print(f"  ✓ Mapped {total} images to {len(image_map)} opgaven")

    return image_map


def format_paragraph_with_images(para_text: str, images: List[str]) -> str:
    """
    Insert images into paragraph text at reasonable positions.

    Strategy: After sentences or at natural break points.
    """
    if not images:
        return f"<p>{para_text}</p>"

    # Insert first image after text, rest in sequence
    html = f"<p>{para_text}</p>\n"

    for img in images:
        html += f'<div class="image-container">\n'
        html += f'  <img src="../images/uitwerkingen/{img}" alt="{img}">\n'
        html += f'</div>\n'

    return html


def generate_html_v3(problems: List[Dict[str, Any]], image_map: Dict[str, List[str]]) -> str:
    """Generate complete HTML with all images."""

    html = []

    # HTML header with CSS
    html.append('''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven - Complete Study Guide v3</title>
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #3498db;
            --accent: #e74c3c;
            --bg: #ecf0f1;
            --card-bg: #ffffff;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--primary);
            background: var(--bg);
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
            border-bottom: 3px solid var(--secondary);
        }

        h1 {
            color: var(--primary);
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .subtitle {
            color: var(--secondary);
            font-size: 1.2em;
        }

        nav {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            position: sticky;
            top: 20px;
            z-index: 100;
        }

        nav h2 { margin-bottom: 15px; }
        nav ul { list-style: none; column-count: 3; column-gap: 20px; }
        nav li { margin-bottom: 8px; }
        nav a { color: var(--secondary); text-decoration: none; }
        nav a:hover { text-decoration: underline; }

        .problem {
            margin: 40px 0;
            padding: 30px;
            background: linear-gradient(to right, #f8f9fa 0%, #ffffff 100%);
            border-left: 5px solid var(--secondary);
            border-radius: 5px;
        }

        .problem-header {
            font-size: 1.8em;
            color: var(--primary);
            margin-bottom: 20px;
            font-weight: bold;
        }

        .chapter-ref {
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .section-title {
            color: var(--secondary);
            font-size: 1.3em;
            margin: 20px 0 10px 0;
            padding-bottom: 5px;
            border-bottom: 2px solid #ecf0f1;
        }

        .section-title:before {
            margin-right: 8px;
        }

        .opgave-section .section-title:before { content: "📝"; }
        .uitwerking-section .section-title:before { content: "✅"; }

        p {
            margin: 10px 0;
            line-height: 1.8;
        }

        .image-container {
            margin: 15px 0;
            text-align: center;
            background: #fafafa;
            padding: 15px;
            border-radius: 5px;
        }

        .image-container img {
            max-width: 100%;
            height: auto;
            border: 1px solid #bdc3c7;
            border-radius: 3px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            background: white;
            padding: 5px;
        }

        @media print {
            nav { display: none; }
            .problem { page-break-inside: avoid; }
        }

        @media (max-width: 768px) {
            nav ul { column-count: 1; }
            .container { padding: 20px; }
        }
    </style>
</head>
<body>
<div class="container">
''')

    # Header
    html.append('<header>')
    html.append('<h1>Uitwerkingen Opgaven Energietechniek</h1>')
    html.append('<div class="subtitle">Volledige Studiegids v3 - Complete Content</div>')
    html.append('<p style="margin-top: 15px;">Ir. JGM van der Zanden | Holmes - Elektrische Netwerken (3e editie)</p>')
    html.append('</header>')

    # Navigation
    html.append('<nav id="toc">')
    html.append('<h2>📚 Inhoudsopgave</h2>')
    html.append('<ul>')
    for p in problems:
        opgave_id = p['id']
        ch_ref = p.get('chapter_ref', {})
        ch_text = f"H{ch_ref.get('chapter','?')}.{ch_ref.get('section','?')}" if ch_ref else "Intro"
        html.append(f'<li><a href="#opgave-{opgave_id}">Opgave {opgave_id} ({ch_text})</a></li>')
    html.append('</ul>')
    html.append('</nav>')

    # Problems
    for problem in problems:
        opgave_id = problem['id']
        ch_ref = problem.get('chapter_ref')

        # Get images for this opgave
        opgave_images = image_map.get(str(opgave_id), [])

        # Split images: 30% for opgave, 70% for uitwerking
        split = max(1, len(opgave_images) // 3)
        opgave_imgs = opgave_images[:split]
        uitwerk_imgs = opgave_images[split:]

        html.append(f'<div class="problem" id="opgave-{opgave_id}">')
        html.append(f'<div class="problem-header">Opgave {opgave_id}</div>')

        if ch_ref:
            html.append(f'<div class="chapter-ref">Hoofdstuk H{ch_ref["chapter"]}.{ch_ref["section"]}, blz. {ch_ref["page"]}</div>')

        # Opgave section
        html.append('<div class="opgave-section">')
        html.append('<div class="section-title">Vraagstelling</div>')

        for para in problem.get('opgave_paragraphs', []):
            text = para['text']
            if text:
                html.append(f'<p>{text}</p>')

        # Opgave images
        for img in opgave_imgs:
            html.append('<div class="image-container">')
            html.append(f'<img src="../images/uitwerkingen/{img}" alt="{img}">')
            html.append('</div>')

        html.append('</div>')  # Close opgave-section

        # Uitwerking section
        html.append('<div class="uitwerking-section">')
        html.append('<div class="section-title">Uitwerking</div>')

        for para in problem.get('uitwerking_paragraphs', []):
            text = para['text']
            if text:
                html.append(f'<p>{text}</p>')

        # Uitwerking images
        for img in uitwerk_imgs:
            html.append('<div class="image-container">')
            html.append(f'<img src="../images/uitwerkingen/{img}" alt="{img}">')
            html.append('</div>')

        html.append('</div>')  # Close uitwerking-section
        html.append('</div>')  # Close problem

    html.append('</div>')  # Close container
    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("GENERATING COMPLETE STUDY GUIDE V3")
    print("="*70 + "\n")

    # Load enhanced YAML
    print(f"Loading: {ENHANCED_YAML.relative_to(PROJECT_ROOT)}")
    with open(ENHANCED_YAML, 'r', encoding='utf-8') as f:
        problems = yaml.safe_load(f)

    print(f"✓ Loaded {len(problems)} problems with full text")

    # Get image mappings
    image_map = extract_images_per_opgave_from_old()

    # Generate HTML
    print("\nGenerating HTML...")
    html_content = generate_html_v3(problems, image_map)

    # Write
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ HTML written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("STUDY GUIDE V3 COMPLETE")
    print("="*70)

    total_with_images = sum(1 for imgs in image_map.values() if imgs)
    total_images = sum(len(imgs) for imgs in image_map.values())

    print(f"\nStatistics:")
    print(f"  Total opgaven: {len(problems)}")
    print(f"  Opgaven with images: {total_with_images}")
    print(f"  Total images: {total_images}")
    print(f"\nOpen in browser:")
    print(f"  {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
