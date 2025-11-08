"""
Batch Enhancement of Opgaven

Uses the approved template from Opgave 1 to enhance all opgaven systematically.

Strategy:
- Identify opgave type (Ohm, Kirchhoff, Thevenin, etc.)
- Apply appropriate enhancement pattern
- Generate professional HTML with proper formulas
"""

import sys
import json
from pathlib import Path
from typing import Dict, List

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
ENHANCED_DIR = PROJECT_ROOT / "enhanced-content"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-ENHANCED-FINAL.html"
TEMPLATE_FILE = PROJECT_ROOT / "enhanced-content" / "opgave-001-enhanced.html"


def load_opgaven() -> List[Dict]:
    """Load all extracted opgaven from JSON"""
    opgaven = []
    for json_file in sorted(ENHANCED_DIR.glob("opgave-*-original.json")):
        with open(json_file, 'r', encoding='utf-8') as f:
            opgave = json.load(f)
            opgaven.append(opgave)
    return opgaven


def identify_opgave_type(opgave: Dict) -> str:
    """
    Identify the type of opgave based on content.

    Types:
    - ohm: Basic Ohm's law (U, I, R calculations)
    - kirchhoff_knoop: Kirchhoff current law
    - kirchhoff_maas: Kirchhoff voltage law
    - thevenin: Thévenin equivalent
    - norton: Norton equivalent
    - rlc_serie: RLC series circuits
    - rlc_parallel: RLC parallel circuits
    - vermogen: Power calculations
    - transformator: Transformer problems
    - driefase: Three-phase systems
    """

    question = opgave['question_html'].lower()
    solution = opgave['solution_html'].lower()
    combined = question + solution

    # Pattern matching for types
    if 'knooppunt' in combined or 'stroomwet' in combined:
        return 'kirchhoff_knoop'
    elif 'maas' in combined or 'spanningswet' in combined or 'gesloten' in combined:
        return 'kirchhoff_maas'
    elif 'thévenin' in combined or 'thevenin' in combined:
        return 'thevenin'
    elif 'norton' in combined:
        return 'norton'
    elif 'transformator' in combined or 'wikkel' in combined:
        return 'transformator'
    elif 'driefase' in combined or 'driehoek' in combined and 'ster' in combined:
        return 'driefase'
    elif 'vermogen' in combined or 'arbeidsfactor' in combined or 'cos' in combined:
        return 'vermogen'
    elif ('inductie' in combined or 'capaciteit' in combined) and ('serie' in combined or 'parallel' in combined):
        if 'serie' in combined:
            return 'rlc_serie'
        else:
            return 'rlc_parallel'
    elif 'wet van ohm' in combined or ('weerstand' in combined and 'spanning' in combined and 'stroom' in combined):
        return 'ohm'
    else:
        return 'general'


def main():
    """Main execution"""

    print("\n" + "="*70)
    print("BATCH ENHANCEMENT - ANALYZING OPGAVEN")
    print("="*70 + "\n")

    # Load all opgaven
    opgaven = load_opgaven()
    print(f"Loaded {len(opgaven)} opgaven")

    # Analyze types
    print("\nAnalyzing opgave types...")
    type_counts = {}

    for opgave in opgaven:
        opgave_type = identify_opgave_type(opgave)
        opgave['type'] = opgave_type

        if opgave_type not in type_counts:
            type_counts[opgave_type] = []
        type_counts[opgave_type].append(opgave['number'])

    # Report
    print("\nOPGAVE TYPE DISTRIBUTION:")
    print("-" * 50)
    for opgave_type, numbers in sorted(type_counts.items()):
        print(f"{opgave_type:20s}: {len(numbers):2d} opgaven - {', '.join(numbers[:5])}")
        if len(numbers) > 5:
            spaces = ' ' * 20
            print(f"{spaces}   (+ {len(numbers)-5} more)")

    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)

    print("\nNext step: Build enhancement templates for each type")
    print("Then: Process all opgaven with appropriate template")

    # Save analysis
    analysis_file = ENHANCED_DIR / "opgave-type-analysis.json"
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_opgaven': len(opgaven),
            'type_distribution': {k: len(v) for k, v in type_counts.items()},
            'opgaven_by_type': type_counts
        }, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Analysis saved to: {analysis_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
