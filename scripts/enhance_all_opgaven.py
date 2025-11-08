"""
Enhanced Opgaven Generator
Processes all opgave-*-original.json files and creates enhanced HTML versions
following the approved opgave-001-enhanced.html template methodology.

Author: Claude Code
Date: 2025-11-08
Project: NCOI Energietechniek Study Guide
"""

import json
import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki")
ENHANCED_DIR = BASE_DIR / "enhanced-content"

# Formula reference mapping (from formuleblad-extract.md)
FORMULA_REFERENCES = {
    "ohm": {"holmes": "§1.8", "formuleblad": "1.1"},
    "kirchhoff_maas": {"holmes": "§1.8", "formuleblad": "1.2"},
    "kirchhoff_knoop": {"holmes": "§1.8", "formuleblad": "1.3"},
    "thevenin": {"holmes": "§3.10", "formuleblad": "9.1"},
    "norton": {"holmes": "§3.10", "formuleblad": "9.2"},
    "serie_weerstanden": {"holmes": "§2.5", "formuleblad": "2.1"},
    "parallel_weerstanden": {"holmes": "§2.5", "formuleblad": "2.2"},
    "spanningsdeling": {"holmes": "§2.5", "formuleblad": "2.3"},
    "vermogen": {"holmes": "§4.3", "formuleblad": "6.1"},
    "energie": {"holmes": "§4.3", "formuleblad": "10.1"},
    "rendement": {"holmes": "§4.3", "formuleblad": "10.2"},
    "capacitieve_reactantie": {"holmes": "§6.7", "formuleblad": "3.3"},
    "inductieve_reactantie": {"holmes": "§6.7", "formuleblad": "3.4"},
    "complex_vermogen": {"holmes": "§11.6", "formuleblad": "6.7"},
}

def identify_opgave_type(question_html, solution_html, number):
    """Identify the physics topic/type of the opgave."""
    combined_text = (question_html + solution_html).lower()

    if "thévenin" in combined_text or "norton" in combined_text:
        return "thevenin_norton"
    elif "kirchhoff" in combined_text or "maas" in combined_text or "knoop" in combined_text:
        return "kirchhoff"
    elif "vermogen" in combined_text or "rendement" in combined_text:
        return "power_energy"
    elif "reactantie" in combined_text or "impedantie" in combined_text:
        return "rlc_impedance"
    elif "spanning" in combined_text and "stroom" in combined_text:
        return "ohm_basic"
    else:
        return "general_network"

def clean_html_content(html):
    """Clean up HTML content from the original JSON."""
    # Remove excessive whitespace
    html = re.sub(r'\s+', ' ', html)
    # Remove style attributes (we'll use our own CSS)
    html = re.sub(r'style="[^"]*"', '', html)
    return html.strip()

def convert_math_to_mathml(text):
    """
    Convert LaTeX math notation to proper MathML.
    This is a simplified version - complex cases might need manual review.
    """
    # This function will be enhanced as we process more opgaven
    # For now, it returns the text as-is since original already has MathML
    return text

def generate_enhanced_html(opgave_data):
    """
    Generate enhanced HTML following the approved template.

    Args:
        opgave_data: Dictionary with opgave JSON data

    Returns:
        Enhanced HTML string
    """
    number = opgave_data["number"]
    chapter = opgave_data.get("chapter", "")
    question_html = clean_html_content(opgave_data["question_html"])
    solution_html = clean_html_content(opgave_data["solution_html"])
    images = opgave_data.get("images", [])

    opgave_type = identify_opgave_type(question_html, solution_html, number)

    # Start building HTML
    html = f"""<!-- OPGAVE {number} - ENHANCED VERSION -->
<!-- Chapter: {chapter} -->
<!-- Type: {opgave_type} -->

<div class="question">
{question_html}
</div>

<div class="solution">
<div class="solution-header">Uitwerking</div>

"""

    # Note: For now, we'll preserve the original solution structure
    # but mark sections for future enhancement
    html += f"""
<div class="enhancement-note" style="background: #fff3cd; padding: 10px; margin: 10px 0; border-left: 4px solid #ffc107;">
<strong>⚠️ Enhancement in progress</strong><br>
Deze opgave is geëxtraheerd uit het bronmateriaal en bevat de originele uitwerking.<br>
Volgende stappen voor volledige enhancement:
<ul>
<li>Stap 1: Analyseer gegeven informatie (tabel format)</li>
<li>Stap 2: Identificeer relevante natuurkundige wet (Holmes {opgave_type.upper()} formules)</li>
<li>Stap 3: Algebraïsche afleiding (stap-voor-stap met pijlen)</li>
<li>Stap 4: Numerieke substitutie (met eenheden)</li>
<li>Stap 5: Verificatie & fysische interpretatie</li>
</ul>
</div>

<div class="original-solution">
<div class="step-header">Originele Uitwerking</div>
{solution_html}
</div>

"""

    html += """
</div>
"""

    return html

def process_all_opgaven():
    """Process all opgave JSON files and generate enhanced HTML versions."""

    # Find all original JSON files
    json_files = sorted(ENHANCED_DIR.glob("opgave-*-original.json"))

    stats = {
        "total": len(json_files),
        "processed": 0,
        "errors": [],
        "types": {}
    }

    print(f"Found {stats['total']} opgaven to process")
    print("=" * 60)

    for json_file in json_files:
        try:
            # Read JSON
            with open(json_file, 'r', encoding='utf-8') as f:
                opgave_data = json.load(f)

            number = opgave_data["number"]
            print(f"\nProcessing Opgave {number}...")

            # Generate enhanced HTML
            enhanced_html = generate_enhanced_html(opgave_data)

            # Determine output filename
            output_file = ENHANCED_DIR / f"opgave-{number}-enhanced.html"

            # Write enhanced HTML
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(enhanced_html)

            # Update stats
            opgave_type = identify_opgave_type(
                opgave_data["question_html"],
                opgave_data["solution_html"],
                number
            )
            stats["types"][opgave_type] = stats["types"].get(opgave_type, 0) + 1
            stats["processed"] += 1

            print(f"  [OK] Created {output_file.name} (Type: {opgave_type})")

        except Exception as e:
            error_msg = f"Opgave {json_file.stem}: {str(e)}"
            stats["errors"].append(error_msg)
            print(f"  [ERROR] {error_msg}")

    # Print summary
    print("\n" + "=" * 60)
    print("PROCESSING SUMMARY")
    print("=" * 60)
    print(f"Total opgaven found: {stats['total']}")
    print(f"Successfully processed: {stats['processed']}")
    print(f"Errors: {len(stats['errors'])}")

    if stats["types"]:
        print("\nOpgave Types Distribution:")
        for opgave_type, count in sorted(stats["types"].items()):
            print(f"  - {opgave_type}: {count}")

    if stats["errors"]:
        print("\nErrors encountered:")
        for error in stats["errors"]:
            print(f"  - {error}")

    return stats

if __name__ == "__main__":
    print("Enhanced Opgaven Generator")
    print("=" * 60)
    print("Following approved template: opgave-001-enhanced.html")
    print("Target: Process all opgave-*-original.json files")
    print("=" * 60)

    stats = process_all_opgaven()

    print("\n" + "=" * 60)
    print("COMPLETED")
    print("=" * 60)
    print(f"\n{stats['processed']}/{stats['total']} opgaven have been processed.")
    print("Next steps:")
    print("1. Review generated HTML files")
    print("2. Manually enhance each opgave following the 5-step template")
    print("3. Add proper MathML notation")
    print("4. Include Holmes/Formuleblad references")
    print("5. Add physical interpretation sections")
