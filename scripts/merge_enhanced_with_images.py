"""
Merge Enhanced Text with Old Images

This combines:
- Full text from enhanced extraction (uitwerkingen-enhanced.yaml)
- All 1335 images from old extraction (uitwerkingen-extract.md)

Creates complete structured data with inline images.
"""

import sys
import re
import yaml
from pathlib import Path
from typing import List, Dict, Any

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
OLD_EXTRACT = PROJECT_ROOT / "analysis" / "uitwerkingen-extract.md"
ENHANCED_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-enhanced.yaml"
OUTPUT_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-complete.yaml"


def parse_old_extract_images() -> Dict[str, List[str]]:
    """
    Parse old extraction to map images to opgaven.

    Returns: {opgave_id: [list of image filenames]}
    """
    print("Parsing old extraction for image mappings...")

    with open(OLD_EXTRACT, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by opgave headers
    opgave_sections = re.split(r'\nOpgave\s+(\d+[a-z]?):', content)

    image_map = {}

    # Process each opgave section
    for i in range(1, len(opgave_sections), 2):
        opgave_id = opgave_sections[i].strip()
        section_content = opgave_sections[i+1] if i+1 < len(opgave_sections) else ""

        # Find all images in this section
        images = re.findall(r'!\[.*?\]\((opgave_\d+\.(?:png|emf|gif))\)', section_content)

        if images:
            # Remove duplicates while preserving order
            unique_images = []
            seen = set()
            for img in images:
                if img not in seen:
                    unique_images.append(img)
                    seen.add(img)

            image_map[opgave_id] = unique_images
            print(f"  Opgave {opgave_id}: {len(unique_images)} images")

    total_images = sum(len(imgs) for imgs in image_map.values())
    print(f"\n✓ Mapped {total_images} images to {len(image_map)} opgaven")

    return image_map


def merge_enhanced_with_images(enhanced_data: List[Dict], image_map: Dict[str, List[str]]) -> List[Dict]:
    """
    Merge enhanced text data with old image mappings.
    """
    print("\nMerging enhanced data with images...")

    merged = []

    for problem in enhanced_data:
        opgave_id = problem['id']

        # Get images for this opgave
        images = image_map.get(str(opgave_id), [])

        # Split images between opgave and uitwerking sections
        # Heuristic: first 30% to opgave, rest to uitwerking
        split_point = max(1, len(images) // 3)

        opgave_images = images[:split_point]
        uitwerking_images = images[split_point:]

        # Add images to paragraph structure
        problem['opgave_images_list'] = opgave_images
        problem['uitwerking_images_list'] = uitwerking_images
        problem['all_images'] = images
        problem['image_count'] = len(images)

        merged.append(problem)

        if images:
            print(f"  Opgave {opgave_id}: {len(opgave_images)} opgave imgs, {len(uitwerking_images)} uitwerking imgs")

    total = sum(p['image_count'] for p in merged)
    print(f"\n✓ Merged {total} images into {len(merged)} problems")

    return merged


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("MERGING ENHANCED TEXT WITH OLD IMAGES")
    print("="*70 + "\n")

    # Load enhanced YAML
    print(f"Loading: {ENHANCED_YAML.relative_to(PROJECT_ROOT)}")
    with open(ENHANCED_YAML, 'r', encoding='utf-8') as f:
        enhanced_data = yaml.safe_load(f)

    print(f"✓ Loaded {len(enhanced_data)} problems with full text")

    # Parse old extraction for images
    image_map = parse_old_extract_images()

    # Merge
    complete_data = merge_enhanced_with_images(enhanced_data, image_map)

    # Save merged data
    print(f"\nSaving complete data...")
    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        yaml.dump(complete_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"✓ Saved to: {OUTPUT_YAML.relative_to(PROJECT_ROOT)}")

    # Statistics
    print("\n" + "="*70)
    print("MERGE COMPLETE")
    print("="*70)

    total_problems = len(complete_data)
    total_images = sum(p['image_count'] for p in complete_data)
    problems_with_images = sum(1 for p in complete_data if p['image_count'] > 0)

    print(f"\nStatistics:")
    print(f"  Total problems: {total_problems}")
    print(f"  Problems with images: {problems_with_images}")
    print(f"  Total images: {total_images}")
    print(f"  Average images per problem: {total_images/total_problems:.1f}")

    print(f"\nNext step:")
    print(f"  Generate HTML study guide from: {OUTPUT_YAML.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
