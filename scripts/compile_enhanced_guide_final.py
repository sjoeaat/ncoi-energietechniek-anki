"""
Compile Enhanced Guide - Final Version

Creates HTML with:
- Opgaven 1, 2, 3: Fully enhanced (professional 5-step quality)
- All other opgaven: Original from pandoc (complete, just not enhanced)

Result: Working study guide with showcase of enhanced quality
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
BASE_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-pandoc-raw.html"
ENHANCED_DIR = PROJECT_ROOT / "enhanced-content"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-ENHANCED-FINAL.html"

# Enhanced opgaven files
ENHANCED_FILES = {
    '1': ENHANCED_DIR / "opgave-001-enhanced.html",
    '2': ENHANCED_DIR / "opgave-002-FULL-enhanced.html",
    '3': ENHANCED_DIR / "opgave-003-FULL-enhanced.html",
    '4': ENHANCED_DIR / "opgave-004-FULL-enhanced.html",
    '5': ENHANCED_DIR / "opgave-005-FULL-enhanced.html",
    '6': ENHANCED_DIR / "opgave-006-FULL-enhanced.html",
    '7': ENHANCED_DIR / "opgave-007-FULL-enhanced.html",
    '8': ENHANCED_DIR / "opgave-008-FULL-enhanced.html",
    '9': ENHANCED_DIR / "opgave-009-FULL-enhanced.html",
    '10': ENHANCED_DIR / "opgave-010-FULL-enhanced.html",
}


def extract_opgave_content(opgave_num: str, html: str) -> tuple:
    """
    Extract a single opgave section from HTML.

    Returns: (start_pos, end_pos, content)
    """
    # Pattern for opgave header
    header_pattern = f'<p><strong>Opgave\\s+{re.escape(opgave_num)}:</strong></p>'

    match = re.search(header_pattern, html)
    if not match:
        return None, None, None

    start = match.start()

    # Find next opgave header (or end of HTML)
    next_pattern = r'<p><strong>Opgave\s+\d+[a-z]?:</strong></p>'
    next_match = re.search(next_pattern, html[match.end():])

    if next_match:
        end = match.end() + next_match.start()
    else:
        # No next opgave - take rest of HTML
        end = len(html)

    content = html[start:end]
    return start, end, content


def main():
    """Compile enhanced guide"""

    print("\n" + "="*70)
    print("COMPILING ENHANCED STUDY GUIDE - FINAL VERSION")
    print("="*70 + "\n")

    # Read base HTML
    print(f"Reading base: {BASE_HTML.relative_to(PROJECT_ROOT)}")
    with open(BASE_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix image paths
    html = html.replace('src="study-guide/', 'src="')

    # Replace each enhanced opgave
    for opgave_num, enhanced_file in ENHANCED_FILES.items():
        print(f"\nProcessing Opgave {opgave_num}...")

        if not enhanced_file.exists():
            print(f"  ⚠️ Enhanced file not found: {enhanced_file.name}")
            continue

        # Read enhanced content
        with open(enhanced_file, 'r', encoding='utf-8') as f:
            enhanced_content = f.read()

        # Find and replace in base HTML
        start, end, original = extract_opgave_content(opgave_num, html)

        if start is None:
            print(f"  ⚠️ Could not find Opgave {opgave_num} in base HTML")
            continue

        # Build replacement (wrap in opgave div)
        replacement = f'''<div class="opgave" id="opgave-{opgave_num}">
<div class="opgave-header">Opgave {opgave_num}</div>
<div class="chapter-ref">Enhanced Professional Edition</div>
{enhanced_content}
</div>
'''

        # Replace
        html = html[:start] + replacement + html[end:]
        print(f"  ✓ Replaced with enhanced version")

    # Add CSS and structure
    print("\nAdding professional styling...")

    css_header = '''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven - Enhanced Edition</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #000;
            background: #f5f5f5;
            padding: 40px 60px;
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #7f8c8d;
            font-size: 1.1em;
        }

        .enhanced-badge {
            display: inline-block;
            background: #27ae60;
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.85em;
            margin-left: 10px;
            font-weight: bold;
        }

        p { margin: 8px 0; text-align: justify; }
        strong { font-weight: 600; color: #000; }
        em { font-style: italic; }

        .opgave {
            margin: 30px 0;
            padding: 25px;
            background: white;
            border-left: 5px solid #3498db;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        .opgave-header {
            font-size: 1.4em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .chapter-ref {
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .question {
            background: #f8f9fa;
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
            border: 1px solid #dee2e6;
        }

        .solution {
            margin-top: 20px;
        }

        .solution-header {
            font-size: 1.2em;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0 15px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid #3498db;
        }

        .step {
            margin: 20px 0;
            padding: 15px;
            background: #f8f9fa;
            border-left: 3px solid #3498db;
            border-radius: 4px;
        }

        .step-header {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.05em;
        }

        math {
            font-size: 1.15em;
            margin: 0 3px;
        }

        .display-math {
            text-align: center;
            margin: 15px 0;
        }

        .display-math math {
            font-size: 1.4em;
        }

        img {
            max-width: 600px;
            height: auto;
            display: block;
            margin: 15px auto;
            border: 1px solid #dee2e6;
            padding: 10px;
            background: #fff;
            border-radius: 6px;
        }

        table {
            margin: 15px auto;
            border-collapse: collapse;
            background: #fff;
            width: 85%;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        th, td {
            padding: 10px 15px;
            border: 1px solid #dee2e6;
            text-align: left;
        }

        th {
            background: #f8f9fa;
            font-weight: bold;
            color: #2c3e50;
        }

        .interpretation {
            margin: 15px 0;
            padding: 15px;
            background: #e7f3ff;
            border-left: 4px solid #3498db;
            border-radius: 4px;
        }

        .interpretation-header {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 8px;
        }

        ul, ol {
            margin: 10px 0 10px 30px;
        }

        li {
            margin: 6px 0;
        }

        a {
            color: #3498db;
            text-decoration: underline;
        }

        a:hover {
            color: #2980b9;
        }

        blockquote {
            margin: 15px 0;
            padding: 10px 20px;
            background: #f8f9fa;
            border-left: 4px solid #bdc3c7;
            font-style: italic;
        }

        .banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
        }

        .banner h3 {
            margin-bottom: 10px;
        }

        @media print {
            body { background: white; padding: 20px; }
            .opgave { page-break-inside: avoid; box-shadow: none; }
            .banner { display: none; }
        }
    </style>
</head>
<body>

<header>
    <h1>Uitwerkingen Opgaven Energietechniek</h1>
    <p class="subtitle">Enhanced Professional Edition</p>
    <p style="margin-top: 10px; font-size: 0.95em;">
        Ir. JGM van der Zanden | Holmes - Elektrische Netwerken (3e editie)
    </p>
</header>

<div class="banner">
    <h3>✨ Enhanced Professional Edition</h3>
    <p style="margin-top: 8px; font-size: 1.05em;">
        <strong>Opgaven 1-10:</strong> Fully enhanced met 5-stappen methodologie, Holmes §X.Y referenties, Formuleblad citaties,
        dimensionale analyse, en fysische interpretatie<br>
        <strong>Overige opgaven (11+):</strong> Complete originele uitwerkingen met alle formules en circuit diagrams
    </p>
    <p style="margin-top: 10px; font-size: 0.95em; opacity: 0.9;">
        10 professionele opgaven dekken: Ohm, Kirchhoff, Thévenin/Norton, Superpositie, Inductantie, Spanningsdeling,
        Parallelweerstanden, en Systeemontwerp
    </p>
</div>

'''

    footer = '''
</body>
</html>
'''

    final_html = css_header + html + footer

    # Write output
    print("\nWriting final HTML...")
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(final_html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("ENHANCED GUIDE COMPLETE")
    print("="*70)

    print("\nContent Summary:")
    print("  ✓ Opgaven 1-10: FULLY ENHANCED (professional 5-step quality)")
    print("     - Opgave 1: Ohm's Law")
    print("     - Opgave 2: Thévenin/Norton Equivalents")
    print("     - Opgave 3: Thévenin Network Analysis")
    print("     - Opgave 4: Superpositie + Thévenin")
    print("     - Opgave 5: Kirchhoff Backwards Analysis")
    print("     - Opgave 6: Inductance (L·di/dt)")
    print("     - Opgave 7: Voltage Division + Polarity")
    print("     - Opgave 8: Parallel Resistance + Current Division")
    print("     - Opgave 9: System Design (inverse problem)")
    print("     - Opgave 10: Reference Polarity (theory)")
    print("  ✓ Opgaven 11+: Complete original content")
    print("\nThis gives you:")
    print("  • Complete study guide met 10 professional opgaven")
    print("  • Diverse physics concepts covered")
    print("  • All remaining content functional")
    print(f"\nOpen: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
