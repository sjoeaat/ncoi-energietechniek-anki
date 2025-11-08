#!/usr/bin/env python3
"""
Anki CSV Generator - Converteert enhanced opgaven naar Anki flashcards
Genereert twee decks: KENNIS (conceptueel) en REKENEN (berekeningen)
GEEN externe dependencies - pure Python met regex
"""

import re
from pathlib import Path
import csv

# Directories
ENHANCED_DIR = Path("/home/user/ncoi-energietechniek-anki/enhanced-content")
OUTPUT_DIR = Path("/home/user/ncoi-energietechniek-anki/generated-cards")
OUTPUT_DIR.mkdir(exist_ok=True)

# Output files
KENNIS_CSV = OUTPUT_DIR / "anki-deck-KENNIS-AUTO-GENERATED.csv"
REKENEN_CSV = OUTPUT_DIR / "anki-deck-REKENEN-AUTO-GENERATED.csv"

def extract_div_content(html, class_name):
    """Extract content from div with specific class"""
    pattern = rf'<div class="{class_name}">(.*?)</div>'
    match = re.search(pattern, html, re.DOTALL)
    return match.group(1) if match else ""

def extract_list_items(html):
    """Extract <li> items from HTML"""
    items = re.findall(r'<li[^>]*>(.*?)</li>', html, re.DOTALL)
    return [re.sub(r'<[^>]+>', ' ', item).strip() for item in items]

def clean_html_for_anki(text):
    """Clean HTML maar behoud essentiële tags"""
    if not text:
        return ""

    # Remove div wrappers maar behoud inhoud
    text = re.sub(r'<div[^>]*class="display-math"[^>]*>\s*', '', text)
    text = re.sub(r'<div[^>]*class="step"[^>]*>.*?</div>', '', text, flags=re.DOTALL)

    # Remove step numbers
    text = re.sub(r'<span class="step-number">.*?</span>', '', text, flags=re.DOTALL)

    # Clean excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'<br>\s*<br>\s*<br>', '<br><br>', text)

    # Remove problematic style attributes
    text = re.sub(r'\s*style="[^"]*"', '', text)
    text = re.sub(r'\s*class="[^"]*"', '', text)

    return text.strip()

def extract_question_answer(filepath):
    """Extraheer vraag en antwoord uit opgave HTML - PURE REGEX"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else filepath.stem

    # Bepaal type (KENNIS vs REKENEN)
    is_rekenen = any(keyword in title.lower() for keyword in [
        'bereken', 'berekening', 'reken', 'vermogen', 'stroom', 'spanning',
        'weerstand', 'impedantie', 'energie', 'norton', 'thevenin'
    ])

    # Extract gegeven
    gegeven_match = re.search(r'<div class="gegeven"[^>]*>(.*?)</div>', content, re.DOTALL)
    gegeven_text = ""
    if gegeven_match:
        gegeven_html = gegeven_match.group(1)
        items = extract_list_items(gegeven_html)
        if items:
            gegeven_text = '<br>'.join([f"• {item}" for item in items[:5]])  # Max 5 items

    # Extract gevraagd
    gevraagd_match = re.search(r'<div class="gevraagd"[^>]*>(.*?)</div>', content, re.DOTALL)
    gevraagd_text = ""
    if gevraagd_match:
        gevraagd_html = gevraagd_match.group(1)
        # Get first <p> tag
        p_match = re.search(r'<p[^>]*>(.*?)</p>', gevraagd_html, re.DOTALL)
        if p_match:
            gevraagd_text = clean_html_for_anki(p_match.group(1))

    # Build FRONT of card
    front_parts = []

    # Add chapter reference
    chapter_match = re.search(r'H\s*(\d+\.\d+)', title)
    if chapter_match:
        front_parts.append(f"<b>Hoofdstuk {chapter_match.group(1)}</b><br>")

    if gegeven_text:
        front_parts.append(f"<b>Gegeven:</b><br>{gegeven_text}<br><br>")

    if gevraagd_text:
        front_parts.append(f"<b>Gevraagd:</b><br>{gevraagd_text}")
    else:
        # Fallback: extract opgave title
        opgave_title_match = re.search(r'<div class="opgave-title"[^>]*>(.*?)</div>', content)
        if opgave_title_match:
            opgave_title = re.sub(r'<[^>]+>', '', opgave_title_match.group(1)).strip()
            front_parts.append(opgave_title)

    front = ''.join(front_parts)

    # Extract BACK (solution - simplified approach)
    back_parts = []

    # Find result box (final answer)
    result_match = re.search(r'<div class="result-box"[^>]*>(.*?)</div>', content, re.DOTALL)
    if result_match:
        result_text = re.sub(r'<[^>]+>', ' ', result_match.group(1)).strip()
        back_parts.append(f"<b>🎯 ANTWOORD:</b><br>{result_text}<br><br>")

    # Extract first few steps (simplified)
    step_matches = re.findall(r'<div class="step"[^>]*>.*?<div class="step-title"[^>]*>.*?<span[^>]*>.*?</span>(.*?)</div>(.*?)</div>',
                              content, re.DOTALL)

    for i, (step_title, step_content) in enumerate(step_matches[:3], 1):  # Max 3 steps
        title_clean = re.sub(r'<[^>]+>', '', step_title).strip()
        if title_clean:
            back_parts.append(f"<b>Stap {i}: {title_clean}</b><br>")

            # Extract first paragraph of step
            p_matches = re.findall(r'<p[^>]*>(.*?)</p>', step_content, re.DOTALL)
            if p_matches:
                first_p = clean_html_for_anki(p_matches[0])
                if len(first_p) > 10:
                    back_parts.append(first_p[:500] + '<br><br>')  # Max 500 chars per step

    # If no steps found, extract insight boxes
    if not back_parts or len(back_parts) < 2:
        insight_match = re.search(r'<div class="insight-box"[^>]*>(.*?)</div>', content, re.DOTALL)
        if insight_match:
            insight = re.sub(r'<[^>]+>', ' ', insight_match.group(1)).strip()
            back_parts.append(f"💡 <b>Inzicht:</b> {insight[:300]}<br>")

    back = ''.join(back_parts) if back_parts else "Zie opgave voor volledige uitwerking"

    # Generate tags
    tags = []

    # Add chapter tag
    if chapter_match:
        chapter_num = chapter_match.group(1).replace('.', '')
        tags.append(f"h{chapter_num}")

    # Add type tag
    tags.append("rekenen" if is_rekenen else "kennis")

    # Add topic tags based on title keywords
    topic_keywords = {
        'ohm': 'ohm',
        'kirchhoff': 'kirchhoff',
        'thevenin': 'thevenin',
        'norton': 'norton',
        'vermogen': 'vermogen',
        'energie': 'energie',
        'spanning': 'spanning',
        'stroom': 'stroom',
        'weerstand': 'weerstand',
        'impedantie': 'impedantie',
        'capaciteit': 'capaciteit',
        'inductie': 'inductie',
        'rlc': 'rlc',
        'superpositie': 'superpositie',
        'multiple choice': 'multiple-choice',
    }

    title_lower = title.lower()
    for keyword, tag in topic_keywords.items():
        if keyword in title_lower:
            tags.append(tag)

    return {
        'front': front,
        'back': back,
        'tags': ';'.join(tags),
        'type': 'REKENEN' if is_rekenen else 'KENNIS',
        'filename': filepath.name
    }

def generate_anki_csvs():
    """Genereer Anki CSV bestanden"""

    print("🚀 Start Anki CSV generatie...")

    # Collect all opgaven
    all_files = sorted(ENHANCED_DIR.glob("*.html"))
    print(f"📊 Gevonden: {len(all_files)} HTML bestanden")

    kennis_cards = []
    rekenen_cards = []
    errors = []
    skipped = 0

    for filepath in all_files:
        try:
            card_data = extract_question_answer(filepath)

            # Skip if no meaningful content
            if not card_data['front'] or len(card_data['front']) < 20:
                skipped += 1
                continue

            if not card_data['back'] or len(card_data['back']) < 10:
                skipped += 1
                continue

            if card_data['type'] == 'REKENEN':
                rekenen_cards.append(card_data)
            else:
                kennis_cards.append(card_data)

        except Exception as e:
            error_msg = f"Error in {filepath.name}: {str(e)}"
            errors.append(error_msg)

    # Write KENNIS deck
    with open(KENNIS_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['Front', 'Back', 'Tags'])

        for card in kennis_cards:
            writer.writerow([card['front'], card['back'], card['tags']])

    # Write REKENEN deck
    with open(REKENEN_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['Front', 'Back', 'Tags'])

        for card in rekenen_cards:
            writer.writerow([card['front'], card['back'], card['tags']])

    # Print summary
    print("\n" + "="*70)
    print("✅ ANKI CSV GENERATIE COMPLEET")
    print("="*70)
    print(f"📚 KENNIS deck: {len(kennis_cards)} kaarten → {KENNIS_CSV.name}")
    print(f"🔢 REKENEN deck: {len(rekenen_cards)} kaarten → {REKENEN_CSV.name}")
    print(f"⏭️  Skipped: {skipped} (geen content)")
    print(f"📊 Totaal: {len(kennis_cards) + len(rekenen_cards)} kaarten")

    if errors:
        print(f"\n⚠️  Errors: {len(errors)}")
        for error in errors[:5]:
            print(f"   {error}")

    print("\n📥 IMPORT INSTRUCTIES:")
    print("   1. Open Anki")
    print("   2. File → Import")
    print("   3. Selecteer CSV bestand (KENNIS of REKENEN)")
    print("   4. Type: Basic")
    print("   5. ⚠️  BELANGRIJK: 'Allow HTML in fields' AAN ZETTEN!")
    print("   6. Field mapping: Front→Front, Back→Back, Tags→Tags")
    print("   7. Import")
    print(f"\n📂 Bestanden:")
    print(f"   {KENNIS_CSV}")
    print(f"   {REKENEN_CSV}")

if __name__ == "__main__":
    generate_anki_csvs()
