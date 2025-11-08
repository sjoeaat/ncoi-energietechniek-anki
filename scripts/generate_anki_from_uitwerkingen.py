"""
Generate Anki flashcards from structured uitwerkingen data

Reads: analysis/uitwerkingen-structured.yaml
Outputs:
- generated-cards/anki-deck-UITWERKINGEN-v1.csv
- generated-cards/UITWERKINGEN-METADATA.md
"""

import sys
import yaml
import csv
from pathlib import Path
from typing import List, Dict, Any

# Force UTF-8 encoding for console output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-structured.yaml"
OUTPUT_CSV = PROJECT_ROOT / "generated-cards" / "anki-deck-UITWERKINGEN-v1.csv"
OUTPUT_METADATA = PROJECT_ROOT / "generated-cards" / "UITWERKINGEN-METADATA.md"

# Create output directory
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)


def format_opgave_front(problem: Dict[str, Any]) -> str:
    """Format the front (question) side of the card."""

    front_parts = []

    # Add chapter reference
    if problem.get('chapter_ref'):
        ch = problem['chapter_ref']
        front_parts.append(f"<b>Hoofdstuk {ch['chapter']}.{ch['section']}</b><br><br>")

    # Add opgave text (clean formula markers)
    opgave_text = problem['opgave']
    # Remove **[FORMULE]:** markers (formulas are in images)
    opgave_text = opgave_text.replace('**[FORMULE]:** `[FORMULA]`', '[zie formule]')

    front_parts.append(opgave_text)

    # Add images to front (if they're part of the problem statement)
    if problem['opgave_images']:
        front_parts.append("<br><br>")
        # Only add first few images to front (circuit diagrams, problem setup)
        for img in problem['opgave_images'][:3]:  # Max 3 images on front
            front_parts.append(f'<img src=\'{img}\' style=\'max-width:600px;\'><br>')

    return ''.join(front_parts)


def format_uitwerking_back(problem: Dict[str, Any]) -> str:
    """Format the back (answer/solution) side of the card."""

    back_parts = []

    # Add uitwerking text
    uitwerking_text = problem.get('uitwerking', '')
    # Clean formula markers
    uitwerking_text = uitwerking_text.replace('**[FORMULE]:** `[FORMULA]`', '[formule]')

    back_parts.append(f"<b>Uitwerking:</b><br><br>")
    back_parts.append(uitwerking_text)

    # Add images to back (solution diagrams, calculations)
    if problem['uitwerking_images']:
        back_parts.append("<br><br>")
        back_parts.append("<b>Stappenplan & Berekeningen:</b><br><br>")
        # Add all solution images
        for img in problem['uitwerking_images'][:10]:  # Max 10 images on back
            back_parts.append(f'<img src=\'{img}\' style=\'max-width:600px;\'><br>')

    # Add chapter reference at bottom
    if problem.get('chapter_ref'):
        ch = problem['chapter_ref']
        back_parts.append(f"<br><i>Bron: Holmes Hoofdstuk {ch['chapter']}.{ch['section']}, blz. {ch['page']}</i>")

    return ''.join(back_parts)


def generate_tags(problem: Dict[str, Any]) -> str:
    """Generate Anki tags for the problem."""

    tags = []

    # Add source tag
    tags.append('uitwerkingen')
    tags.append('holmes')

    # Add domain tags
    for domain in problem.get('domains', []):
        tags.append(domain)

    # Add difficulty tag
    difficulty = problem.get('difficulty', 'gemiddeld')
    tags.append(f'niveau-{difficulty}')

    # Add chapter tag
    if problem.get('chapter_ref'):
        ch = problem['chapter_ref']
        tags.append(f"h{ch['chapter']}-{ch['section']}")

    # Add type tags based on content
    if problem.get('formulas_count', 0) > 3:
        tags.append('berekening')

    if 'kirchhoff' in problem.get('domains', []):
        tags.append('netwerk-analyse')

    if 'thevenin-norton' in problem.get('domains', []):
        tags.append('examen-kritisch')  # Thévenin/Norton is critical for exam

    return ';'.join(tags)


def should_include_problem(problem: Dict[str, Any]) -> bool:
    """Determine if problem should be included in Anki deck."""

    # Skip if no uitwerking
    if not problem.get('uitwerking') or len(problem['uitwerking']) < 20:
        return False

    # Skip if no opgave text
    if not problem.get('opgave') or len(problem['opgave']) < 10:
        return False

    return True


def generate_anki_cards(problems: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Convert structured problems to Anki cards."""

    cards = []
    skipped = 0

    for problem in problems:
        # Check if we should include this problem
        if not should_include_problem(problem):
            skipped += 1
            continue

        # Generate card
        card = {
            'Front': format_opgave_front(problem),
            'Back': format_uitwerking_back(problem),
            'Tags': generate_tags(problem)
        }

        cards.append(card)
        print(f"  ✓ Generated card for Opgave {problem['id']}")

    if skipped > 0:
        print(f"\n  ⚠ Skipped {skipped} problems (incomplete data)")

    return cards


def write_csv(cards: List[Dict[str, str]], output_file: Path):
    """Write cards to Anki CSV format."""

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Front', 'Back', 'Tags'])
        writer.writeheader()
        writer.writerows(cards)

    print(f"\n✓ CSV written to: {output_file.relative_to(PROJECT_ROOT)}")


def generate_metadata(cards: List[Dict[str, str]], problems: List[Dict[str, Any]], output_file: Path):
    """Generate metadata documentation."""

    metadata = []
    metadata.append("# Uitwerkingen Anki Deck - Metadata\n\n")
    metadata.append(f"**Generated:** 2025-11-08\n")
    metadata.append(f"**Source:** Uitwerkingen Opgaven Energietechniek V0.8.docx\n")
    metadata.append(f"**Total Cards:** {len(cards)}\n")
    metadata.append(f"**Total Problems Processed:** {len(problems)}\n\n")
    metadata.append("---\n\n")

    # Statistics
    metadata.append("## Deck Statistics\n\n")

    # Domain distribution
    domain_counts = {}
    for card in cards:
        tags = card['Tags'].split(';')
        for tag in tags:
            if tag not in ['uitwerkingen', 'holmes'] and not tag.startswith('niveau-') and not tag.startswith('h'):
                domain_counts[tag] = domain_counts.get(tag, 0) + 1

    metadata.append("### Domain Coverage\n\n")
    metadata.append("| Domain | Cards |\n")
    metadata.append("|--------|-------|\n")
    for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1])[:15]:
        metadata.append(f"| {domain} | {count} |\n")
    metadata.append("\n")

    # Difficulty distribution
    difficulty_counts = {'basis': 0, 'gemiddeld': 0, 'gevorderd': 0}
    for card in cards:
        tags = card['Tags'].split(';')
        for tag in tags:
            if tag.startswith('niveau-'):
                level = tag.replace('niveau-', '')
                difficulty_counts[level] = difficulty_counts.get(level, 0) + 1

    metadata.append("### Difficulty Distribution\n\n")
    metadata.append("| Level | Cards | Percentage |\n")
    metadata.append("|-------|-------|------------|\n")
    total = len(cards)
    for level in ['basis', 'gemiddeld', 'gevorderd']:
        count = difficulty_counts[level]
        pct = (count / total * 100) if total > 0 else 0
        metadata.append(f"| {level} | {count} | {pct:.1f}% |\n")
    metadata.append("\n")

    # Import instructions
    metadata.append("## Anki Import Instructions\n\n")
    metadata.append("1. Open Anki\n")
    metadata.append("2. File → Import\n")
    metadata.append(f"3. Select: `{OUTPUT_CSV.name}`\n")
    metadata.append("4. Settings:\n")
    metadata.append("   - Type: **Basic**\n")
    metadata.append("   - Allow HTML in fields: **✓ YES**\n")
    metadata.append("   - Field mapping: Front → Front, Back → Back, Tags → Tags\n")
    metadata.append("5. Import\n\n")

    metadata.append("### Media Files (Images)\n\n")
    metadata.append("Images must be copied to Anki's media folder:\n")
    metadata.append("```\n")
    metadata.append("%APPDATA%\\Anki2\\[User]\\collection.media\\\n")
    metadata.append("```\n\n")
    metadata.append("Copy all files from:\n")
    metadata.append("```\n")
    metadata.append(f"{PROJECT_ROOT / 'images' / 'uitwerkingen'}\\*.png\n")
    metadata.append(f"{PROJECT_ROOT / 'images' / 'uitwerkingen'}\\*.emf\n")
    metadata.append(f"{PROJECT_ROOT / 'images' / 'uitwerkingen'}\\*.gif\n")
    metadata.append("```\n\n")

    metadata.append("**Note:** EMF files (Windows metafiles) may not display in Anki. ")
    metadata.append("Consider converting to PNG using ImageMagick or similar tool.\n\n")

    # Study recommendations
    metadata.append("## Study Recommendations\n\n")
    metadata.append("**Daily Study Plan:**\n")
    metadata.append(f"- Total cards: {len(cards)}\n")
    metadata.append(f"- Conservative: 2 new/day = {len(cards)//2} days (~{len(cards)//2//7} weeks)\n")
    metadata.append(f"- Intensive: 5 new/day = {len(cards)//5} days (~{len(cards)//5//7} weeks)\n\n")

    metadata.append("**Recommended Study Order:**\n")
    metadata.append("1. Start with `niveau-basis` cards\n")
    metadata.append("2. Progress to `niveau-gemiddeld`\n")
    metadata.append("3. Finish with `niveau-gevorderd`\n\n")

    metadata.append("**Tag Filtering:**\n")
    metadata.append("- Practice specific domains: `tag:kirchhoff`, `tag:thevenin-norton`\n")
    metadata.append("- Focus on exam-critical: `tag:examen-kritisch`\n")
    metadata.append("- Chapter-specific review: `tag:h1-9`, `tag:h3-11`\n\n")

    # Quality notes
    metadata.append("## Quality Notes\n\n")
    metadata.append("**Strengths:**\n")
    metadata.append("- ✓ Complete step-by-step solutions from official workbook\n")
    metadata.append("- ✓ High-quality circuit diagrams and formulas\n")
    metadata.append("- ✓ Realistic exam-style problems\n")
    metadata.append("- ✓ Dutch terminology matching NCOI exam\n\n")

    metadata.append("**Known Limitations:**\n")
    metadata.append("- ⚠ Some formulas displayed as images (not LaTeX text)\n")
    metadata.append("- ⚠ EMF images may need conversion to PNG\n")
    metadata.append("- ⚠ Very image-heavy (1000+ images total)\n")
    metadata.append("- ⚠ Some cards have many images (may need splitting)\n\n")

    # Version history
    metadata.append("## Version History\n\n")
    metadata.append("**v1.0** (2025-11-08):\n")
    metadata.append(f"- Initial release with {len(cards)} cards\n")
    metadata.append("- Covers chapters H 1.9 and H 3.11\n")
    metadata.append("- Domains: Basiswetten, Kirchhoff, Thévenin/Norton, Transformatoren\n")
    metadata.append("- Source: First 33 problems from uitwerkingen document\n\n")

    metadata.append("---\n\n")
    metadata.append("**Status:** Production ready - Ready for Anki import\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(metadata)

    print(f"✓ Metadata written to: {output_file.relative_to(PROJECT_ROOT)}")


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("GENERATING ANKI CARDS FROM UITWERKINGEN")
    print("="*70 + "\n")

    # Load structured data
    print(f"Reading: {INPUT_YAML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_YAML, 'r', encoding='utf-8') as f:
        problems = yaml.safe_load(f)

    print(f"✓ Loaded {len(problems)} problems\n")

    # Generate cards
    print("Generating cards...")
    cards = generate_anki_cards(problems)

    print(f"\n✓ Generated {len(cards)} Anki cards")

    # Write CSV
    write_csv(cards, OUTPUT_CSV)

    # Generate metadata
    generate_metadata(cards, problems, OUTPUT_METADATA)

    print("\n" + "="*70)
    print("GENERATION COMPLETE")
    print("="*70)
    print(f"\nFiles created:")
    print(f"  1. {OUTPUT_CSV.relative_to(PROJECT_ROOT)}")
    print(f"  2. {OUTPUT_METADATA.relative_to(PROJECT_ROOT)}")
    print(f"\nNext steps:")
    print(f"  1. Review sample cards in CSV file")
    print(f"  2. Copy images to Anki media folder")
    print(f"  3. Import CSV to Anki")
    print(f"  4. Test rendering in Anki")


if __name__ == "__main__":
    main()
