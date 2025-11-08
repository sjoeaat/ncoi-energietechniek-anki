"""
Full Enhancement Pipeline

Strategy:
1. Parse all opgaven from raw HTML
2. For each opgave, enhance content using AI-assisted approach
3. Generate final ENHANCED HTML with all improvements

This will take ~2-4 hours to process all 90 opgaven.
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass, asdict

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-pandoc-raw.html"
OUTPUT_DIR = PROJECT_ROOT / "enhanced-content"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-ENHANCED-FINAL.html"

# Create output directory
OUTPUT_DIR.mkdir(exist_ok=True)


@dataclass
class Opgave:
    """Represents one opgave"""
    number: str
    chapter: str
    question_html: str
    solution_html: str
    images: List[str]


def extract_opgaven(html: str) -> List[Opgave]:
    """Extract all opgaven from HTML"""

    print("Parsing HTML to extract opgaven...")

    # Fix image paths first
    html = html.replace('src="study-guide/', 'src="')

    opgaven = []

    # Split by opgave headers
    opgave_pattern = r'<p><strong>Opgave\s+(\d+[a-z]?):</strong></p>'
    splits = re.split(opgave_pattern, html)

    current_chapter = ""

    # Extract initial chapter
    chapter_match = re.search(r'<p><strong>(H\s+\d+\.\d+\s+blz\.\s+\d+)</strong></p>', splits[0])
    if chapter_match:
        current_chapter = chapter_match.group(1)

    # Process opgaven
    for i in range(1, len(splits), 2):
        if i+1 >= len(splits):
            break

        opgave_num = splits[i]
        content = splits[i+1]

        # Update chapter if found
        next_chapter = re.search(r'<p><strong>(H\s+\d+\.\d+\s+blz\.\s+\d+)</strong></p>', content)
        if next_chapter:
            current_chapter = next_chapter.group(1)
            content = content[next_chapter.end():]

        # Split question and solution
        solution_pattern = r'<p><strong>Uitwerking opgave\s+\d+[a-z]?:</strong></p>'
        parts = re.split(solution_pattern, content, maxsplit=1)

        question = parts[0].strip() if len(parts) > 0 else ""
        solution = parts[1].strip() if len(parts) > 1 else ""

        # Extract images
        images = re.findall(r'src="[^"]*/(image\d+\.(?:PNG|png|gif))"', question + solution)

        opgave = Opgave(
            number=opgave_num,
            chapter=current_chapter,
            question_html=question,
            solution_html=solution,
            images=images
        )

        opgaven.append(opgave)

    print(f"✓ Extracted {len(opgaven)} opgaven")
    return opgaven


def save_opgave_to_json(opgave: Opgave, output_file: Path):
    """Save opgave to JSON for processing"""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(asdict(opgave), f, ensure_ascii=False, indent=2)


def main():
    """Main execution"""

    print("\n" + "="*70)
    print("FULL ENHANCEMENT PIPELINE - STARTING")
    print("="*70 + "\n")

    # Read raw HTML
    print(f"Reading: {INPUT_HTML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all opgaven
    opgaven = extract_opgaven(html)

    # Save each opgave to JSON for AI processing
    print("\nSaving opgaven to JSON files for AI processing...")
    for opgave in opgaven:
        json_file = OUTPUT_DIR / f"opgave-{opgave.number}-original.json"
        save_opgave_to_json(opgave, json_file)

    print(f"✓ Saved {len(opgaven)} opgaven to {OUTPUT_DIR}")

    print("\n" + "="*70)
    print("PHASE 1 COMPLETE - EXTRACTION DONE")
    print("="*70)

    print("\nNext: Use AI agent to enhance each opgave")
    print(f"Files ready in: {OUTPUT_DIR}")
    print("\nTo process all opgaven, run:")
    print("  python scripts/enhance_with_ai.py")


if __name__ == "__main__":
    main()
