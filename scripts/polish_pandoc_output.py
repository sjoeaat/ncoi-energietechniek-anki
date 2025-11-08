"""
Polish Pandoc HTML Output

Takes raw pandoc HTML and creates a polished study guide with:
- Fixed image paths
- Professional CSS styling
- Navigation menu
- Chapter structure
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-pandoc-raw.html"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-complete-guide-v4.html"


def fix_image_paths(html: str) -> str:
    """Fix image paths from 'study-guide/media/media/imageN.PNG' to 'media/media/imageN.PNG'"""
    fixed = re.sub(r'src="study-guide/', r'src="', html)
    return fixed


def extract_opgaven_structure(html: str) -> List[Tuple[str, int, str]]:
    """
    Extract opgave headers and positions for navigation.

    Returns: [(opgave_id, position, header_text), ...]
    """
    # Match patterns like:
    # <p><strong>Opgave 1:</strong></p>
    # <p><img ...><strong>Opgave 3:</strong></p>
    pattern = r'<p><(?:strong|img[^>]*>\s*<strong)>Opgave\s+([^:<]+):'

    opgaven = []
    for match in re.finditer(pattern, html):
        opgave_id = match.group(1).strip()
        position = match.start()
        opgaven.append((opgave_id, position, f"Opgave {opgave_id}"))

    return opgaven


def insert_navigation(html: str, opgaven: List[Tuple[str, int, str]]) -> str:
    """Insert table of contents navigation"""

    # Create anchor IDs in the HTML
    for opgave_id, _, _ in opgaven:
        # Escape special characters for regex
        opgave_pattern = f'(<p><(?:strong|img[^>]*>\\s*<strong)>Opgave\\s+{re.escape(opgave_id)}:)'
        replacement = f'<div id="opgave-{opgave_id}">\\1'
        html = re.sub(opgave_pattern, replacement, html, count=1)

        # Close div after next few paragraphs (before next opgave or end)
        # This is approximate - we'll close before next opgave header

    # Build navigation HTML
    nav_html = []
    nav_html.append('<nav id="toc">')
    nav_html.append('<h2>📚 Inhoudsopgave</h2>')
    nav_html.append('<ul>')

    for opgave_id, _, title in opgaven:
        nav_html.append(f'<li><a href="#opgave-{opgave_id}">{title}</a></li>')

    nav_html.append('</ul>')
    nav_html.append('</nav>')
    nav_html.append('\n\n')

    # Insert after first heading
    nav_block = '\n'.join(nav_html)

    # Insert after the title section (after "In de losse Xcel sheet...")
    insertion_point = html.find('<p><strong>Fouten</strong></p>')
    if insertion_point > 0:
        html = html[:insertion_point] + nav_block + html[insertion_point:]

    return html


def add_professional_styling(html: str) -> str:
    """Wrap content with HTML structure and CSS"""

    css = '''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven Energietechniek - Complete Guide v4</title>
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
            line-height: 1.8;
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

        nav {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
            position: sticky;
            top: 20px;
            z-index: 100;
            max-height: 400px;
            overflow-y: auto;
        }

        nav h2 {
            margin-bottom: 15px;
            color: var(--primary);
        }

        nav ul {
            list-style: none;
            column-count: 3;
            column-gap: 20px;
        }

        nav li { margin-bottom: 8px; }
        nav a {
            color: var(--secondary);
            text-decoration: none;
            font-size: 0.9em;
        }
        nav a:hover {
            text-decoration: underline;
            font-weight: bold;
        }

        p {
            margin: 15px 0;
            line-height: 1.8;
        }

        strong {
            color: var(--primary);
            font-weight: 600;
        }

        em {
            font-style: italic;
            color: #555;
        }

        img {
            max-width: 100%;
            height: auto;
            display: inline-block;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 5px;
            background: white;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        /* Math formula styling */
        math {
            font-size: 1.1em;
            margin: 0 2px;
        }

        /* Opgave sections */
        div[id^="opgave-"] {
            margin: 40px 0;
            padding: 30px;
            background: linear-gradient(to right, #f8f9fa 0%, #ffffff 100%);
            border-left: 5px solid var(--secondary);
            border-radius: 5px;
        }

        /* Links */
        a {
            color: var(--secondary);
            text-decoration: underline;
        }

        a:hover {
            color: var(--accent);
        }

        /* Lists */
        ol, ul {
            margin: 15px 0 15px 30px;
        }

        li {
            margin: 8px 0;
        }

        /* Blockquotes */
        blockquote {
            margin: 15px 0;
            padding: 10px 20px;
            background: #f9f9f9;
            border-left: 4px solid var(--secondary);
            font-style: italic;
        }

        @media print {
            nav { display: none; }
            div[id^="opgave-"] { page-break-inside: avoid; }
        }

        @media (max-width: 768px) {
            nav ul { column-count: 1; }
            .container { padding: 20px; }
        }
    </style>
</head>
<body>
<div class="container">
'''

    footer = '''
</div>
</body>
</html>
'''

    return css + html + footer


def main():
    """Main execution"""

    print("\n" + "="*70)
    print("POLISHING PANDOC HTML OUTPUT")
    print("="*70 + "\n")

    # Read raw HTML
    print(f"Reading: {INPUT_HTML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"✓ Loaded {len(html)} characters")

    # Fix image paths
    print("\nFixing image paths...")
    html = fix_image_paths(html)
    print("✓ Image paths corrected")

    # Extract opgaven structure
    print("\nExtracting opgave structure...")
    opgaven = extract_opgaven_structure(html)
    print(f"✓ Found {len(opgaven)} opgaven")

    # Insert navigation
    print("\nInserting navigation...")
    html = insert_navigation(html, opgaven)
    print("✓ Navigation added")

    # Add styling
    print("\nAdding professional styling...")
    html = add_professional_styling(html)
    print("✓ Styling applied")

    # Write output
    print("\nWriting polished HTML...")
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("POLISHING COMPLETE")
    print("="*70)

    print(f"\nOpen in browser:")
    print(f"  {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
