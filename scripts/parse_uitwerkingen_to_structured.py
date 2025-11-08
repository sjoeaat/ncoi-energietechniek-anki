"""
Parse uitwerkingen-extract.md into structured format for Anki card generation

This script:
1. Identifies problem boundaries (Opgave → Uitwerking → next Opgave)
2. Extracts chapter/topic metadata
3. Associates images with problems
4. Outputs structured YAML/JSON for each problem

Output: analysis/uitwerkingen-structured.yaml
"""

import re
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_MD = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
OUTPUT_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-structured.yaml"
OUTPUT_SUMMARY = PROJECT_ROOT / "analysis" / "uitwerkingen-parsed-summary.md"

# Regex patterns
CHAPTER_PATTERN = re.compile(r'H\s+(\d+)\.(\d+)\s+blz\.?\s+(\d+)', re.IGNORECASE)

# Multiple opgave patterns (in priority order - most specific first)
OPGAVE_GROUPED = re.compile(r'^Opgave\s+([\d,\s]+en\s+\d+):?\s*$', re.IGNORECASE)  # Opgave 6, 7 en 8: (group header, skip)
OPGAVE_WITH_DESC = re.compile(r'^Opgave\s+(\d+[a-z]?)[\.\s](.+)', re.IGNORECASE)   # Opgave 1. Description OR Opgave 1 Text
OPGAVE_DOT_ONLY = re.compile(r'^Opgave\s+(\d+[a-z]?)\.\s*$', re.IGNORECASE)       # Opgave 7. (only dot, no desc)
OPGAVE_LETTER = re.compile(r'^Opgave\s+(\d+)([a-z]):?\s*$', re.IGNORECASE)        # Opgave 1a:
OPGAVE_SIMPLE = re.compile(r'^Opgave\s+(\d+):?\s*$', re.IGNORECASE)               # Opgave 1:

# Uitwerking patterns
UITWERKING_PATTERN = re.compile(r'^Uitwerking\s+(?:opgave\s+|opdracht\s+)?(\d+[a-z]?):?\s*', re.IGNORECASE)

IMAGE_PATTERN = re.compile(r'!\[.*?\]\((opgave_\d+\.(?:png|emf|gif))\)')
FORMULA_PATTERN = re.compile(r'\*\*\[FORMULE\]:\*\*')


def expand_grouped_opgave(grouped_text: str) -> List[str]:
    """
    Expand grouped opgave numbers into individual numbers.

    Example: "6, 7 en 8" -> ["6", "7", "8"]
    Example: "10, 11, 12 en 13" -> ["10", "11", "12", "13"]
    """
    # Remove everything except numbers and commas
    numbers_only = re.sub(r'[^\d,]', ' ', grouped_text)
    # Split by comma or whitespace and filter empties
    numbers = [n.strip() for n in re.split(r'[,\s]+', numbers_only) if n.strip()]
    return numbers


def match_opgave_pattern(line: str) -> Optional[Dict[str, Any]]:
    """
    Try to match line against all opgave patterns.
    Returns dict with opgave info if matched, None otherwise.

    Returns 'skip' type for group headers that should be ignored.
    """
    # Check for grouped opgave header (these are just section headers, skip them)
    match = OPGAVE_GROUPED.match(line)
    if match:
        return {
            'type': 'skip',  # Don't create opgave for group headers
            'raw': line
        }

    # Try opgave with dot only (no description)
    match = OPGAVE_DOT_ONLY.match(line)
    if match:
        return {
            'type': 'dot_only',
            'number': match.group(1),
            'description': '',
            'raw': line,
            'direct_solution': True  # Solution follows directly without "Uitwerking" header
        }

    # Try opgave with description
    match = OPGAVE_WITH_DESC.match(line)
    if match:
        return {
            'type': 'with_description',
            'number': match.group(1),
            'description': match.group(2).strip(),
            'raw': line,
            'direct_solution': True  # Solution follows directly without "Uitwerking" header
        }

    # Try letter subopgave
    match = OPGAVE_LETTER.match(line)
    if match:
        return {
            'type': 'letter',
            'number': match.group(1) + match.group(2),
            'raw': line,
            'direct_solution': False
        }

    # Try simple opgave
    match = OPGAVE_SIMPLE.match(line)
    if match:
        return {
            'type': 'simple',
            'number': match.group(1),
            'raw': line,
            'direct_solution': False
        }

    return None


def classify_problem_domain(text: str) -> List[str]:
    """Classify problem by subject domain based on keywords."""
    domains = []

    text_lower = text.lower()

    # Domain keywords
    if any(kw in text_lower for kw in ['ohm', 'weerstand', 'spanning', 'stroom']):
        domains.append('basiswetten')

    if any(kw in text_lower for kw in ['kirchhoff', 'knooppunt', 'maas', 'mesh']):
        domains.append('kirchhoff')

    if any(kw in text_lower for kw in ['thévenin', 'thevenin', 'norton']):
        domains.append('thevenin-norton')

    if any(kw in text_lower for kw in ['serie', 'parallel', 'vervangings']):
        domains.append('netwerk-analyse')

    if any(kw in text_lower for kw in ['impedantie', 'reactantie', 'complexe', 'fasor']):
        domains.append('complexe-impedantie')

    if any(kw in text_lower for kw in ['vermogen', 'arbeidsvermogen', 'blindvermogen', 'schijnbaar']):
        domains.append('vermogensleer')

    if any(kw in text_lower for kw in ['cos phi', 'arbeidsfactor', 'compensatie']):
        domains.append('arbeidsfactor')

    if any(kw in text_lower for kw in ['transformator', 'wikkel', 'koppel', 'primair', 'secundair']):
        domains.append('transformatoren')

    if any(kw in text_lower for kw in ['driefase', '3-fase', 'ster', 'driehoek', 'delta']):
        domains.append('driefase')

    if any(kw in text_lower for kw in ['inductie', 'zelfinductie', 'spoel', 'l =']):
        domains.append('inductie')

    if any(kw in text_lower for kw in ['capaciteit', 'condensator', 'c =']):
        domains.append('capaciteit')

    if any(kw in text_lower for kw in ['resonantie', 'eigenfrequentie']):
        domains.append('resonantie')

    if any(kw in text_lower for kw in ['filter', 'hoogdoorlaat', 'laagdoorlaat']):
        domains.append('filters')

    if any(kw in text_lower for kw in ['rendement', 'verlies', 'efficiënt']):
        domains.append('rendement')

    if any(kw in text_lower for kw in ['energie', 'joule', 'watt']):
        domains.append('energie')

    if any(kw in text_lower for kw in ['kabel', 'lijn', 'spanningsverlies', 'leidingverlies']):
        domains.append('kabels')

    return domains if domains else ['algemeen']


def estimate_difficulty(text: str, has_multiple_steps: bool, has_complex_calc: bool) -> str:
    """Estimate difficulty level based on content analysis."""

    # Simple checks for basic problems
    if 'ohm' in text.lower() and len(text) < 200:
        return 'basis'

    # Complex indicators
    complex_keywords = [
        'thévenin', 'norton', 'superpos', 'complexe',
        'driefase', 'transformator', 'resonantie'
    ]

    if any(kw in text.lower() for kw in complex_keywords):
        return 'gevorderd'

    # Multiple steps or formulas = intermediate
    if has_multiple_steps or has_complex_calc:
        return 'gemiddeld'

    return 'gemiddeld'  # Default


def parse_uitwerkingen(input_file: Path) -> List[Dict[str, Any]]:
    """Parse markdown file into structured problem data."""

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    problems = []
    current_chapter = None
    current_problem = None
    current_section = None  # 'opgave' or 'uitwerking'
    content_buffer = []
    images_buffer = []

    for i, line in enumerate(lines):
        line = line.strip()

        # Detect chapter
        chapter_match = CHAPTER_PATTERN.search(line)
        if chapter_match:
            current_chapter = {
                'chapter': int(chapter_match.group(1)),
                'section': int(chapter_match.group(2)),
                'page': int(chapter_match.group(3))
            }
            continue

        # Detect new opgave (try all patterns)
        opgave_info = match_opgave_pattern(line)
        if opgave_info:
            # Skip group headers
            if opgave_info['type'] == 'skip':
                continue

            # Save previous problem if exists
            if current_problem:
                # For direct solutions OR if we're in uitwerking section
                if current_section == 'uitwerking' or (current_section == 'opgave' and current_problem.get('direct_solution')):
                    if not current_problem.get('uitwerking'):  # opgave section accumulated content
                        current_problem['opgave'] = '\n'.join(content_buffer).strip() if content_buffer else current_problem.get('opgave', '')
                        current_problem['opgave_images'] = images_buffer.copy()
                    else:  # uitwerking section accumulated content
                        current_problem['uitwerking'] = '\n'.join(content_buffer).strip()
                        current_problem['uitwerking_images'] = images_buffer.copy()

                    # Classify and estimate difficulty
                    full_text = current_problem.get('opgave', '') + ' ' + current_problem.get('uitwerking', '')
                    current_problem['domains'] = classify_problem_domain(full_text)
                    current_problem['difficulty'] = estimate_difficulty(
                        full_text,
                        has_multiple_steps=len(content_buffer) > 10,
                        has_complex_calc=current_problem.get('formulas_count', 0) > 3
                    )

                    problems.append(current_problem)

            # Determine opgave text and ID based on type
            if opgave_info['type'] in ['with_description', 'dot_only']:
                opgave_id = opgave_info['number']
                opgave_text = opgave_info.get('description', '')
            else:
                opgave_id = opgave_info['number']
                opgave_text = ''

            # Start new problem
            current_problem = {
                'id': opgave_id,
                'chapter_ref': current_chapter,
                'opgave': opgave_text,
                'opgave_images': [],
                'uitwerking': '',
                'uitwerking_images': [],
                'formulas_count': 0,
                'domains': [],
                'difficulty': 'gemiddeld',
                'opgave_type': opgave_info['type'],
                'raw_header': opgave_info['raw'],
                'direct_solution': opgave_info.get('direct_solution', False)
            }

            # For direct solutions, start in uitwerking mode immediately
            if opgave_info.get('direct_solution'):
                current_section = 'uitwerking'
            else:
                current_section = 'opgave'

            content_buffer = []
            images_buffer = []
            continue

        # Detect uitwerking
        uitwerking_match = UITWERKING_PATTERN.match(line)
        if uitwerking_match and current_problem:
            # Save opgave content
            current_problem['opgave'] = '\n'.join(content_buffer).strip()
            current_problem['opgave_images'] = images_buffer.copy()

            current_section = 'uitwerking'
            content_buffer = []
            images_buffer = []
            continue

        # Collect images
        image_matches = IMAGE_PATTERN.findall(line)
        if image_matches:
            images_buffer.extend(image_matches)

        # Count formulas
        if FORMULA_PATTERN.search(line) and current_problem:
            current_problem['formulas_count'] += 1

        # Accumulate content
        if current_section and line and not line.startswith('*Afbeelding:'):
            # Skip markdown image syntax and metadata
            if not line.startswith('!['):
                content_buffer.append(line)

    # Save last problem
    if current_problem:
        if current_section == 'uitwerking' or (current_section == 'opgave' and current_problem.get('direct_solution')):
            if not current_problem.get('uitwerking'):  # opgave section accumulated content
                current_problem['opgave'] = '\n'.join(content_buffer).strip() if content_buffer else current_problem.get('opgave', '')
                current_problem['opgave_images'] = images_buffer.copy()
            else:  # uitwerking section accumulated content
                current_problem['uitwerking'] = '\n'.join(content_buffer).strip()
                current_problem['uitwerking_images'] = images_buffer.copy()

            full_text = current_problem.get('opgave', '') + ' ' + current_problem.get('uitwerking', '')
            current_problem['domains'] = classify_problem_domain(full_text)
            current_problem['difficulty'] = estimate_difficulty(
                full_text,
                has_multiple_steps=len(content_buffer) > 10,
                has_complex_calc=current_problem.get('formulas_count', 0) > 3
            )

            problems.append(current_problem)

    return problems


def generate_summary(problems: List[Dict[str, Any]], output_file: Path):
    """Generate summary report of parsed problems."""

    summary = []
    summary.append("# Parsed Uitwerkingen Summary\n")
    summary.append(f"**Total Problems:** {len(problems)}\n")
    summary.append(f"**Parse Date:** 2025-11-08\n")
    summary.append("\n---\n\n")

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
    difficulty_counts = {}
    for problem in problems:
        diff = problem['difficulty']
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    summary.append("## Difficulty Distribution\n\n")
    summary.append("| Level | Count | Percentage |\n")
    summary.append("|-------|-------|------------|\n")
    for level in ['basis', 'gemiddeld', 'gevorderd']:
        count = difficulty_counts.get(level, 0)
        pct = (count / len(problems) * 100) if problems else 0
        summary.append(f"| {level} | {count} | {pct:.1f}% |\n")
    summary.append("\n")

    # Chapter distribution
    chapter_counts = {}
    for problem in problems:
        if problem['chapter_ref']:
            ch = f"H {problem['chapter_ref']['chapter']}.{problem['chapter_ref']['section']}"
            chapter_counts[ch] = chapter_counts.get(ch, 0) + 1

    summary.append("## Chapter Distribution (Top 20)\n\n")
    summary.append("| Chapter | Problems |\n")
    summary.append("|---------|----------|\n")
    for ch, count in sorted(chapter_counts.items(), key=lambda x: -x[1])[:20]:
        summary.append(f"| {ch} | {count} |\n")
    summary.append("\n")

    # Sample problems
    summary.append("## Sample Problems\n\n")
    for problem in problems[:5]:
        summary.append(f"### Opgave {problem['id']}\n\n")
        if problem['chapter_ref']:
            summary.append(f"**Chapter:** H {problem['chapter_ref']['chapter']}.{problem['chapter_ref']['section']}\n")
        summary.append(f"**Domains:** {', '.join(problem['domains'])}\n")
        summary.append(f"**Difficulty:** {problem['difficulty']}\n")
        summary.append(f"**Images:** {len(problem['opgave_images']) + len(problem['uitwerking_images'])}\n")
        summary.append(f"**Formulas:** {problem['formulas_count']}\n\n")
        summary.append(f"**Opgave Text (first 200 chars):**\n")
        summary.append(f"{problem['opgave'][:200]}...\n\n")
        summary.append("---\n\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(summary)

    print(f"\n✓ Summary written to: {output_file.relative_to(PROJECT_ROOT)}")


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("PARSING: uitwerkingen-extract.md")
    print("="*70 + "\n")

    # Parse
    problems = parse_uitwerkingen(INPUT_MD)

    print(f"✓ Parsed {len(problems)} problems")

    # Write YAML
    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        yaml.dump(problems, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"✓ Structured data written to: {OUTPUT_YAML.relative_to(PROJECT_ROOT)}")

    # Generate summary
    generate_summary(problems, OUTPUT_SUMMARY)

    print("\n" + "="*70)
    print("PARSING COMPLETE")
    print("="*70)
    print(f"\nNext steps:")
    print(f"1. Review: {OUTPUT_SUMMARY.relative_to(PROJECT_ROOT)}")
    print(f"2. Validate: {OUTPUT_YAML.relative_to(PROJECT_ROOT)}")
    print(f"3. Generate Anki cards from structured data")


if __name__ == "__main__":
    main()
