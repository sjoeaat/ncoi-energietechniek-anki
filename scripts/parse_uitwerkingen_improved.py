"""
IMPROVED Parser for uitwerkingen-extract.md

This parser handles ALL variations:
- Standard: "Opgave 1:"
- Sub-tasks: "Opgave 1a:", "Opgave 1b:"
- Grouped: "Opgave 6, 7 en 8:" (followed by individual tasks)
- Without colon: "Opgave 7.", "Opgave 8. Description"
- Inline: "Opgave 9. The question is in this line"
- Uitwerking variations: "Uitwerking 5.", "Uitwerking opdracht 6:"

Output: analysis/uitwerkingen-structured-FULL.yaml
"""

import re
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_MD = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
OUTPUT_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-structured-FULL.yaml"
OUTPUT_SUMMARY = PROJECT_ROOT / "analysis" / "uitwerkingen-parsed-FULL-summary.md"

# Improved regex patterns
# Match: "Opgave 1:", "Opgave 1a:", "Opgave 7.", "Opgave 9. Question text"
OPGAVE_PATTERN = re.compile(
    r'^Opgave\s+(\d+)([a-z]?)[\.:]\s*(.*?)$',
    re.IGNORECASE
)

# Match: "Opgave 6, 7 en 8:" (group header, skip)
OPGAVE_GROUP_PATTERN = re.compile(
    r'^Opgave\s+\d+(?:,\s*\d+)*(?:\s+en\s+\d+)?:?\s*$',
    re.IGNORECASE
)

# Match: "Uitwerking opgave 1:", "Uitwerking 5.", "Uitwerking opdracht 6:"
UITWERKING_PATTERN = re.compile(
    r'^Uitwerking\s+(?:opgave\s+|opdracht\s+)?(\d+)([a-z]?)[\.:]\s*(.*?)$',
    re.IGNORECASE
)

# Chapter reference
CHAPTER_PATTERN = re.compile(r'H\s+(\d+)\.(\d+)\s+blz\.?\s+(\d+)', re.IGNORECASE)

# Image reference
IMAGE_PATTERN = re.compile(r'!\[.*?\]\((opgave_\d+\.(?:png|emf|gif))\)')

# Formula marker
FORMULA_PATTERN = re.compile(r'\*\*\[FORMULE\]:\*\*')


def classify_problem_domain(text: str) -> List[str]:
    """Classify problem by subject domain based on keywords."""
    domains = []
    text_lower = text.lower()

    # Domain keywords mapping
    domain_keywords = {
        'basiswetten': ['ohm', 'weerstand', 'spanning', 'stroom', 'wet van'],
        'kirchhoff': ['kirchhoff', 'knooppunt', 'maas', 'mesh', 'stroomwet', 'spanningswet'],
        'thevenin-norton': ['thévenin', 'thevenin', 'norton', 'equivalent'],
        'netwerk-analyse': ['serie', 'parallel', 'vervangings', 'netwerk'],
        'complexe-impedantie': ['impedantie', 'reactantie', 'complexe', 'fasor', 'phasor'],
        'vermogensleer': ['vermogen', 'arbeidsvermogen', 'blindvermogen', 'schijnbaar'],
        'arbeidsfactor': ['cos phi', 'arbeidsfactor', 'compensatie', 'cosphi'],
        'transformatoren': ['transformator', 'wikkel', 'koppel', 'primair', 'secundair'],
        'driefase': ['driefase', '3-fase', 'ster', 'driehoek', 'delta'],
        'inductie': ['inductie', 'zelfinductie', 'spoel', 'inductor'],
        'capaciteit': ['capaciteit', 'condensator', 'capacitor'],
        'resonantie': ['resonantie', 'eigenfrequentie', 'resoneren'],
        'filters': ['filter', 'hoogdoorlaat', 'laagdoorlaat', 'banddoorlaat'],
        'rendement': ['rendement', 'verlies', 'efficiënt', 'efficiency'],
        'energie': ['energie', 'joule', 'watt', 'vermogen'],
        'kabels': ['kabel', 'lijn', 'spanningsverlies', 'leidingverlies']
    }

    for domain, keywords in domain_keywords.items():
        if any(kw in text_lower for kw in keywords):
            domains.append(domain)

    return domains if domains else ['algemeen']


def estimate_difficulty(text: str, has_multiple_steps: bool, formula_count: int) -> str:
    """Estimate difficulty level."""

    # Simple Ohm's law problems = basic
    if 'ohm' in text.lower() and len(text) < 200 and formula_count < 2:
        return 'basis'

    # Complex topics = advanced
    complex_keywords = [
        'thévenin', 'norton', 'superpos', 'complexe',
        'driefase', 'resonantie', 'wien', 'fasor'
    ]

    if any(kw in text.lower() for kw in complex_keywords):
        return 'gevorderd'

    # Multiple steps or many formulas = intermediate
    if has_multiple_steps or formula_count > 3:
        return 'gemiddeld'

    return 'gemiddeld'  # Default


def parse_uitwerkingen_improved(input_file: Path) -> List[Dict[str, Any]]:
    """Enhanced parser that catches all opgave variations."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    problems = []
    current_chapter = None
    current_problem = None
    current_section = None  # 'opgave' or 'uitwerking'
    content_buffer = []
    images_buffer = []

    skipped_lines = []

    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Detect chapter
        chapter_match = CHAPTER_PATTERN.search(line_stripped)
        if chapter_match:
            current_chapter = {
                'chapter': int(chapter_match.group(1)),
                'section': int(chapter_match.group(2)),
                'page': int(chapter_match.group(3))
            }
            continue

        # Skip group headers like "Opgave 6, 7 en 8:"
        if OPGAVE_GROUP_PATTERN.match(line_stripped):
            continue

        # Detect new opgave
        opgave_match = OPGAVE_PATTERN.match(line_stripped)
        if opgave_match:
            # Save previous problem if exists
            if current_problem and current_section == 'uitwerking':
                current_problem['uitwerking'] = '\n'.join(content_buffer).strip()
                current_problem['uitwerking_images'] = images_buffer.copy()

                # Classify
                full_text = current_problem['opgave'] + ' ' + current_problem.get('uitwerking', '')
                current_problem['domains'] = classify_problem_domain(full_text)
                current_problem['difficulty'] = estimate_difficulty(
                    full_text,
                    has_multiple_steps=len(content_buffer) > 10,
                    formula_count=current_problem.get('formulas_count', 0)
                )

                problems.append(current_problem)

            # Start new problem
            opgave_id = opgave_match.group(1) + (opgave_match.group(2) or '')
            inline_text = opgave_match.group(3).strip()

            current_problem = {
                'id': opgave_id,
                'chapter_ref': current_chapter,
                'opgave': inline_text,  # May have inline question
                'opgave_images': [],
                'uitwerking': '',
                'uitwerking_images': [],
                'formulas_count': 0,
                'domains': [],
                'difficulty': 'gemiddeld'
            }
            current_section = 'opgave'
            content_buffer = [inline_text] if inline_text else []
            images_buffer = []
            continue

        # Detect uitwerking
        uitwerking_match = UITWERKING_PATTERN.match(line_stripped)
        if uitwerking_match and current_problem:
            uitwerking_id = uitwerking_match.group(1) + (uitwerking_match.group(2) or '')
            inline_text = uitwerking_match.group(3).strip()

            # Only accept if IDs match
            if uitwerking_id == current_problem['id']:
                # Save opgave content
                current_problem['opgave'] = '\n'.join(content_buffer).strip()
                current_problem['opgave_images'] = images_buffer.copy()

                current_section = 'uitwerking'
                content_buffer = [inline_text] if inline_text else []
                images_buffer = []
                continue

        # Collect images
        image_matches = IMAGE_PATTERN.findall(line_stripped)
        if image_matches:
            images_buffer.extend(image_matches)

        # Count formulas
        if FORMULA_PATTERN.search(line_stripped) and current_problem:
            current_problem['formulas_count'] += 1

        # Accumulate content
        if current_section and line_stripped and not line_stripped.startswith('*Afbeelding:'):
            # Skip markdown image syntax
            if not line_stripped.startswith('!['):
                content_buffer.append(line_stripped)

    # Save last problem
    if current_problem and current_section == 'uitwerking':
        current_problem['uitwerking'] = '\n'.join(content_buffer).strip()
        current_problem['uitwerking_images'] = images_buffer.copy()

        full_text = current_problem['opgave'] + ' ' + current_problem.get('uitwerking', '')
        current_problem['domains'] = classify_problem_domain(full_text)
        current_problem['difficulty'] = estimate_difficulty(
            full_text,
            has_multiple_steps=len(content_buffer) > 10,
            formula_count=current_problem.get('formulas_count', 0)
        )

        problems.append(current_problem)

    return problems


def generate_summary(problems: List[Dict[str, Any]], output_file: Path):
    """Generate comprehensive summary report."""

    summary = []
    summary.append("# FULL Parsed Uitwerkingen Summary\n\n")
    summary.append(f"**Total Problems:** {len(problems)}\n")
    summary.append(f"**Parse Date:** 2025-11-08\n")
    summary.append(f"**Parser Version:** Improved (catches all variations)\n\n")
    summary.append("---\n\n")

    # Domain distribution
    domain_counts = {}
    for problem in problems:
        for domain in problem['domains']:
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    summary.append("## Domain Distribution\n\n")
    summary.append("| Domain | Count |\n")
    summary.append("|--------|-------|\n")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
        summary.append(f"| {domain} | {count} |\n")
    summary.append("\n")

    # Difficulty distribution
    difficulty_counts = {'basis': 0, 'gemiddeld': 0, 'gevorderd': 0}
    for problem in problems:
        diff = problem['difficulty']
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    summary.append("## Difficulty Distribution\n\n")
    summary.append("| Level | Count | Percentage |\n")
    summary.append("|-------|-------|------------|\n")
    for level in ['basis', 'gemiddeld', 'gevorderd']:
        count = difficulty_counts[level]
        pct = (count / len(problems) * 100) if problems else 0
        summary.append(f"| {level} | {count} | {pct:.1f}% |\n")
    summary.append("\n")

    # Chapter distribution
    chapter_counts = {}
    for problem in problems:
        if problem['chapter_ref']:
            ch = f"H {problem['chapter_ref']['chapter']}.{problem['chapter_ref']['section']}"
            chapter_counts[ch] = chapter_counts.get(ch, 0) + 1

    summary.append("## Chapter Distribution\n\n")
    summary.append("| Chapter | Problems |\n")
    summary.append("|---------|----------|\n")
    for ch, count in sorted(chapter_counts.items(), key=lambda x: -x[1]):
        summary.append(f"| {ch} | {count} |\n")
    summary.append("\n")

    # Problems with most images
    image_heavy = sorted(
        [(p['id'], len(p['opgave_images']) + len(p['uitwerking_images'])) for p in problems],
        key=lambda x: -x[1]
    )[:10]

    summary.append("## Most Image-Heavy Problems (Top 10)\n\n")
    summary.append("| Opgave ID | Total Images |\n")
    summary.append("|-----------|-------------|\n")
    for opgave_id, img_count in image_heavy:
        summary.append(f"| {opgave_id} | {img_count} |\n")
    summary.append("\n")

    # Sample problems
    summary.append("## Sample Problems (First 5)\n\n")
    for problem in problems[:5]:
        summary.append(f"### Opgave {problem['id']}\n\n")
        if problem['chapter_ref']:
            summary.append(f"**Chapter:** H {problem['chapter_ref']['chapter']}.{problem['chapter_ref']['section']}\n")
        summary.append(f"**Domains:** {', '.join(problem['domains'])}\n")
        summary.append(f"**Difficulty:** {problem['difficulty']}\n")
        summary.append(f"**Images:** {len(problem['opgave_images']) + len(problem['uitwerking_images'])}\n")
        summary.append(f"**Formulas:** {problem['formulas_count']}\n\n")
        summary.append(f"**Opgave (first 150 chars):**\n")
        summary.append(f"{problem['opgave'][:150]}...\n\n")
        summary.append("---\n\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(summary)

    print(f"\n✓ Summary written to: {output_file.relative_to(PROJECT_ROOT)}")


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("IMPROVED PARSING: uitwerkingen-extract.md")
    print("="*70 + "\n")

    # Parse
    problems = parse_uitwerkingen_improved(INPUT_MD)

    print(f"✓ Parsed {len(problems)} problems (improved parser)")

    # Write YAML
    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        yaml.dump(problems, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"✓ Structured data written to: {OUTPUT_YAML.relative_to(PROJECT_ROOT)}")

    # Generate summary
    generate_summary(problems, OUTPUT_SUMMARY)

    print("\n" + "="*70)
    print("PARSING COMPLETE")
    print("="*70)
    print(f"\nComparison:")
    print(f"  Previous parser: 33 problems")
    print(f"  Improved parser: {len(problems)} problems")
    print(f"  Improvement: +{len(problems) - 33} problems ({((len(problems) - 33) / 33 * 100):.1f}% increase)")
    print(f"\nNext steps:")
    print(f"1. Review: {OUTPUT_SUMMARY.relative_to(PROJECT_ROOT)}")
    print(f"2. Generate Anki cards from FULL dataset")


if __name__ == "__main__":
    main()
