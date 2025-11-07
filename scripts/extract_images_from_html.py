#!/usr/bin/env python3
"""
Extract base64 encoded images from HTML oefentoets file.
Saves images as PNG files for use in Anki deck.
"""

import re
import base64
from pathlib import Path


def extract_images(html_content):
    """Extract all base64 encoded images from HTML."""
    # Pattern: src="data:image/png;base64,..."
    pattern = r'src="data:image/(png|jpg|jpeg|gif);base64,([A-Za-z0-9+/=]+)"'
    matches = re.finditer(pattern, html_content)

    images = []
    for idx, match in enumerate(matches, start=1):
        img_format = match.group(1)
        img_data = match.group(2)
        images.append({
            'number': idx,
            'format': img_format,
            'data': img_data
        })

    return images


def save_images(images, output_dir):
    """Save base64 images to files."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    saved_files = []
    for img in images:
        # Decode base64
        try:
            img_bytes = base64.b64decode(img['data'])

            # Save file
            filename = f"vraag_{img['number']:02d}.{img['format']}"
            filepath = output_dir / filename

            with open(filepath, 'wb') as f:
                f.write(img_bytes)

            saved_files.append(filepath)
            print(f"Saved: {filepath} ({len(img_bytes)} bytes)")

        except Exception as e:
            print(f"Error saving image {img['number']}: {e}")

    return saved_files


def find_question_for_image(html_content, image_index):
    """Find which question an image belongs to."""
    # Split on <h2>Vraag
    questions = re.split(r'<h2>Vraag (\d+)', html_content)

    # Count images in each section
    cumulative = 0
    for i in range(1, len(questions), 2):
        q_num = questions[i]
        q_content = questions[i+1] if i+1 < len(questions) else ""

        # Count images in this question
        img_count = len(re.findall(r'src="data:image/', q_content))

        if cumulative < image_index <= cumulative + img_count:
            return int(q_num)

        cumulative += img_count

    return None


def main():
    # Paths
    source_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\source-materials\Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html")
    output_dir = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\images\oefentoets")

    # Read HTML
    print(f"Reading {source_file}...")
    html_content = source_file.read_text(encoding='utf-8')

    # Extract images
    print("Extracting images...")
    images = extract_images(html_content)

    print(f"Found {len(images)} images")

    if not images:
        print("No images found!")
        return

    # Map images to questions
    print("\nMapping images to questions...")
    for img in images:
        q_num = find_question_for_image(html_content, img['number'])
        img['question'] = q_num
        print(f"Image {img['number']}: Vraag {q_num}")

    # Save images
    print("\nSaving images...")
    saved_files = save_images(images, output_dir)

    # Generate mapping file
    mapping_file = output_dir / "image_mapping.txt"
    with open(mapping_file, 'w', encoding='utf-8') as f:
        f.write("# Image to Question Mapping\n")
        f.write("# Generated automatically\n\n")
        for img in images:
            filename = f"vraag_{img['number']:02d}.{img['format']}"
            f.write(f"{filename} -> Vraag {img['question']}\n")

    print(f"\nMapping saved to: {mapping_file}")
    print(f"Total images saved: {len(saved_files)}")


if __name__ == '__main__':
    main()
