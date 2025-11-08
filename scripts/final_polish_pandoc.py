"""
Final Polish - Match Original Word Document Style

Goals:
1. Compact layout (more content per page)
2. Professional typography (niet te groot)
3. Clean styling (geen rare blauwe boxen overal)
4. Readable formulas and images
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
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-FINAL.html"


def main():
    """Final polishing"""

    print("\n" + "="*70)
    print("FINAL POLISH - MATCHING WORD DOCUMENT STYLE")
    print("="*70 + "\n")

    # Read raw HTML
    print(f"Reading: {INPUT_HTML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix image paths
    print("Fixing image paths...")
    html = html.replace('src="study-guide/', 'src="')

    # Add professional styling matching Word doc
    print("Adding professional styling...")

    css_header = '''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven Energietechniek</title>
    <style>
        /* Reset and base */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.4;
            color: #000;
            background: #fff;
            padding: 40px 60px;
            max-width: 1400px;
            margin: 0 auto;
        }

        /* Paragraphs - compact */
        p {
            margin: 6px 0;
            text-align: justify;
        }

        /* Headers - subtle styling */
        strong {
            font-weight: 600;
            color: #000;
        }

        /* Opgave headers - distinct maar niet overdreven */
        p:has(> strong:first-child) {
            margin-top: 20px;
            margin-bottom: 8px;
        }

        /* Emphasis */
        em {
            font-style: italic;
        }

        /* Images - compact, inline waar mogelijk */
        img {
            max-width: 400px;
            height: auto;
            display: inline-block;
            margin: 8px 0;
            vertical-align: middle;
            border: 1px solid #ccc;
            padding: 4px;
            background: #fff;
        }

        /* Math - readable maar compact */
        math {
            font-size: 1.05em;
            margin: 0 2px;
            vertical-align: middle;
        }

        /* Links */
        a {
            color: #0563c1;
            text-decoration: underline;
        }

        a:hover {
            color: #1f4788;
        }

        /* Lists - compact */
        ol, ul {
            margin: 6px 0 6px 25px;
        }

        li {
            margin: 4px 0;
        }

        /* Blockquotes */
        blockquote {
            margin: 8px 0 8px 20px;
            padding: 6px 12px;
            border-left: 3px solid #ccc;
            background: #f9f9f9;
            font-style: italic;
        }

        /* Print optimization */
        @media print {
            body {
                padding: 20px;
                font-size: 10pt;
            }
            img {
                max-width: 300px;
            }
            p {
                page-break-inside: avoid;
            }
        }

        /* Screen - add subtle separators */
        @media screen {
            /* Add visual break between major sections */
            p > strong:first-child:contains("H "),
            p > strong:first-child:contains("Opgave") {
                display: inline-block;
                padding: 4px 0;
                border-bottom: 1px solid #ddd;
                margin-bottom: 6px;
            }
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

    # Write output
    print("Writing final output...")
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("FINAL VERSION COMPLETE")
    print("="*70)

    print(f"\nKey improvements:")
    print(f"  - Compact layout (11pt font vs 16pt+)")
    print(f"  - Professional typography (Calibri)")
    print(f"  - Clean styling (no colored boxes)")
    print(f"  - Inline images where appropriate")
    print(f"  - Print-optimized")

    print(f"\nOpen in browser:")
    print(f"  {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
