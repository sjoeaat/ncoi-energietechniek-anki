"""
Simple Pandoc Polish - NO FANCY STUFF, JUST BASICS

1. Fix image paths
2. Add basic CSS
3. That's it. No navigation, no divs, no breaking stuff.
"""

import sys
import re
from pathlib import Path

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-pandoc-raw.html"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-simple-v5.html"


def main():
    """Simple processing"""

    print("\n" + "="*70)
    print("SIMPLE PANDOC POLISH (NO BREAKING CHANGES)")
    print("="*70 + "\n")

    # Read raw HTML
    print(f"Reading: {INPUT_HTML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix image paths: "study-guide/media/media/imageN.PNG" → "media/media/imageN.PNG"
    print("\nFixing image paths...")
    html = html.replace('src="study-guide/', 'src="')
    print("✓ Image paths corrected")

    # Add CSS (wrap content)
    print("\nAdding CSS...")

    css_header = '''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven Energietechniek - v5 Simple</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: #ecf0f1;
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        p {
            margin: 15px 0;
            line-height: 1.8;
        }

        strong {
            color: #2c3e50;
            font-weight: 600;
        }

        img {
            max-width: 800px;
            height: auto;
            display: block;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            background: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        math {
            font-size: 1.1em;
            margin: 0 3px;
        }

        a {
            color: #3498db;
            text-decoration: underline;
        }

        a:hover {
            color: #e74c3c;
        }

        ol, ul {
            margin: 15px 0 15px 30px;
        }

        li {
            margin: 8px 0;
        }

        blockquote {
            margin: 15px 0;
            padding: 10px 20px;
            background: #f9f9f9;
            border-left: 4px solid #3498db;
            font-style: italic;
        }

        /* Highlight opgave headers */
        p strong:first-child {
            display: inline-block;
            margin-top: 40px;
            padding: 10px 15px;
            background: linear-gradient(to right, #3498db, #2980b9);
            color: white;
            border-radius: 5px;
        }
    </style>
</head>
<body>
'''

    footer = '''
</body>
</html>
'''

    html = css_header + html + footer
    print("✓ CSS added")

    # Write output
    print("\nWriting output...")
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("SIMPLE POLISH COMPLETE")
    print("="*70)

    print(f"\nOpen in browser:")
    print(f"  {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
