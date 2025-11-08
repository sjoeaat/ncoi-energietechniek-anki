"""
Compile Mixed Study Guide

Creates a working HTML with:
- Opgave 1: Fully enhanced (approved quality)
- Opgaven 2-17: Original quality (from pandoc)

This gives immediate value while more opgaven can be enhanced over time.
"""

import sys
from pathlib import Path

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENHANCED_OPGAVE_1 = PROJECT_ROOT / "enhanced-content" / "opgave-001-enhanced.html"
FINAL_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-FINAL.html"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-MIXED-EDITION.html"


def main():
    """Compile working product"""

    print("\n" + "="*70)
    print("COMPILING MIXED EDITION STUDY GUIDE")
    print("="*70 + "\n")

    print("Strategy:")
    print("  - Opgave 1: Enhanced professional quality ✓")
    print("  - Opgaven 2-35: Original quality (still complete!)")
    print("  - Result: Immediate working product")
    print()

    # Read FINAL HTML (has all opgaven in original quality)
    print(f"Reading: {FINAL_HTML.relative_to(PROJECT_ROOT)}")
    with open(FINAL_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Read enhanced Opgave 1
    print(f"Reading enhanced: {ENHANCED_OPGAVE_1.relative_to(PROJECT_ROOT)}")
    with open(ENHANCED_OPGAVE_1, 'r', encoding='utf-8') as f:
        enhanced_og1 = f.read()

    # Find Opgave 1 in original HTML and replace with enhanced version
    print("\nReplacing Opgave 1 with enhanced version...")

    # Pattern: from first "Opgave 1:" to second "Opgave" header
    import re

    # Find start of Opgave 1
    opgave1_start = html.find('<p><strong>Opgave 1:</strong></p>')

    if opgave1_start == -1:
        print("ERROR: Could not find Opgave 1 in original HTML")
        return

    # Find next opgave (Opgave 2)
    opgave2_start = html.find('<p><strong>Opgave 2:</strong></p>', opgave1_start + 10)

    if opgave2_start == -1:
        print("ERROR: Could not find Opgave 2")
        return

    # Replace Opgave 1 section
    before = html[:opgave1_start]
    after = html[opgave2_start:]

    # Build new HTML with enhanced Opgave 1
    new_html = before + enhanced_og1 + after

    # Update title
    new_html = new_html.replace(
        '<title>Uitwerkingen Opgaven Energietechniek</title>',
        '<title>Uitwerkingen Opgaven - Mixed Edition (Enhanced + Original)</title>'
    )

    # Add banner
    banner = '''
<div style="background: #fff3cd; border: 2px solid #ff9800; padding: 15px; margin: 20px 0; border-radius: 5px;">
<p style="margin: 0; font-weight: bold; color: #856404;">ℹ️ Mixed Edition</p>
<p style="margin: 5px 0 0 0; font-size: 0.95em;">
<strong>Opgave 1:</strong> Enhanced professional quality met 5-stappen methodologie<br>
<strong>Opgaven 2-35:</strong> Originele kwaliteit (volledige content, formules en uitwerkingen)
</p>
</div>
'''

    # Insert banner after header
    header_end = new_html.find('</header>')
    if header_end != -1:
        new_html = new_html[:header_end+9] + banner + new_html[header_end+9:]

    # Write output
    print("\nWriting Mixed Edition...")
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(new_html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("MIXED EDITION COMPLETE")
    print("="*70)

    print("\nThis version gives you:")
    print("  ✓ Immediate working product")
    print("  ✓ Opgave 1 as quality showcase")
    print("  ✓ All other opgaven fully functional")
    print("\nFuture: More opgaven can be enhanced incrementally")
    print(f"\nOpen in browser: {OUTPUT_HTML}")


if __name__ == "__main__":
    main()
