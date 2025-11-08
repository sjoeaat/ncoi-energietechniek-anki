#!/usr/bin/env python3
"""
Automatisch Images Toevoegen aan Anki Kaarten
NCOI Energietechniek - Circuit Schema's en Fasor Diagrammen

Gebruikt: Intelligent pattern matching op kaart content en tags
Output: Nieuwe CSV met embedded images

Author: Claude Code
Date: 2025-11-06
"""

import csv
import re
from pathlib import Path

# ============================================================
# IMAGE MAPPING: Welke kaart krijgt welke image?
# ============================================================

# Pattern -> (image_file, placement, priority)
# placement: 'front', 'back', or 'both'
# priority: 1=must, 2=should, 3=nice

IMAGE_RULES = [
    # Thévenin & Norton
    {
        'patterns': ['thévenin', 'thevenin'],
        'image': 'thevenin_equivalent.svg',
        'placement': 'front',  # Circuit is de vraag
        'priority': 1,
        'condition': 'bereken|gegeven',  # Rekenvraag
    },
    {
        'patterns': ['norton'],
        'image': 'norton_equivalent.svg',
        'placement': 'both',  # Conversie vraag
        'priority': 1,
        'condition': 'bepaal|bereken',
    },

    # Vermogensdriehoek (ZEER BELANGRIJK!)
    {
        'patterns': ['vermogensdriehoek', 'p.*q.*s', 'schijnbaar.*vermogen'],
        'image': 'vermogensdriehoek_PQS.svg',
        'placement': 'back',  # Uitleg diagram
        'priority': 1,
    },
    {
        'patterns': ['blindvermogen.*compensatie', 'compensatie.*cos'],
        'image': 'vermogenscompensatie.svg',
        'placement': 'back',
        'priority': 1,
    },

    # Driefase systemen
    {
        'patterns': ['driefase.*ster', 'ster.*configuratie', 'ster-schakeling'],
        'image': 'threephase_star.svg',
        'placement': 'front',
        'priority': 1,
        'exclude': ['driehoek'],  # Niet als driehoek ook genoemd wordt
    },
    {
        'patterns': ['driefase.*driehoek', 'delta.*schakeling'],
        'image': 'threephase_delta.svg',
        'placement': 'front',
        'priority': 1,
    },
    {
        'patterns': ['ster.*driehoek.*omschakeling', 'driehoek.*ster'],
        'image': 'threephase_star.svg',  # Toon beide in template
        'placement': 'front',
        'priority': 1,
        'extra_image': 'threephase_delta.svg',  # Side-by-side
    },
    {
        'patterns': ['driefase.*120.*graden', 'fasevolgorde', 'l1.*l2.*l3'],
        'image': 'driefase_120graden.svg',
        'placement': 'back',
        'priority': 2,
    },

    # RLC Circuits
    {
        'patterns': ['rlc.*serie', 'serie.*rlc'],
        'image': 'rlc_series.svg',
        'placement': 'front',
        'priority': 2,
        'condition': 'bereken|gegeven',
    },
    {
        'patterns': ['rlc.*parallel', 'parallel.*rlc'],
        'image': 'rlc_parallel.svg',
        'placement': 'front',
        'priority': 2,
    },
    {
        'patterns': ['rc.*serie', 'serie.*rc'],
        'image': 'rc_series.svg',
        'placement': 'front',
        'priority': 2,
    },
    {
        'patterns': ['rl.*serie', 'serie.*rl'],
        'image': 'rl_series.svg',
        'placement': 'front',
        'priority': 2,
    },

    # Kirchhoff
    {
        'patterns': ['kirchhoff.*knoop', 'knooppunt.*wet', 'kcl'],
        'image': 'kirchhoff_node_3branches.svg',
        'placement': 'front',
        'priority': 1,
    },
    {
        'patterns': ['kirchhoff.*maas', 'maaswet', 'kvl'],
        'image': 'kirchhoff_mesh_2loops.svg',
        'placement': 'front',
        'priority': 1,
    },

    # Resonantie
    {
        'patterns': ['resonantie.*serie', 'serie.*resonantie', 'lc.*serie'],
        'image': 'series_resonance.svg',
        'placement': 'front',
        'priority': 1,
        'condition': 'bereken|f.*=',
    },
    {
        'patterns': ['resonantie.*parallel', 'parallel.*resonantie'],
        'image': 'parallel_resonance.svg',
        'placement': 'front',
        'priority': 2,
    },
    {
        'patterns': ['q-factor', 'kwaliteitsfactor', 'bandbreedte'],
        'image': 'series_resonance.svg',
        'placement': 'back',
        'priority': 2,
    },

    # Transformatoren
    {
        'patterns': ['transformator.*wikkelverhoud', 'wikkel.*verhouding'],
        'image': 'transformer_basic.svg',
        'placement': 'front',
        'priority': 2,
    },
    {
        'patterns': ['koppelfactor', 'wederzijdse.*inductie'],
        'image': 'transformer_with_load.svg',
        'placement': 'back',
        'priority': 2,
    },

    # Goniometrie & Fasoren
    {
        'patterns': ['eenheidscirkel', 'sin.*cos.*tan'],
        'image': 'eenheidscirkel_sin_cos_tan.svg',
        'placement': 'back',
        'priority': 1,
    },
    {
        'patterns': ['faseverschuiving', 'ijlen.*voorijlen', 'achterijlen'],
        'image': 'faseverschuiving_ijlen.svg',
        'placement': 'back',
        'priority': 2,
    },
    {
        'patterns': ['effectieve.*waarde', 'rms.*piek'],
        'image': 'effectieve_waarde_RMS.svg',
        'placement': 'back',
        'priority': 2,
    },
    {
        'patterns': ['impedantie.*driehoek', 'r.*xl.*xc'],
        'image': 'impedantie_driehoek.svg',
        'placement': 'back',
        'priority': 2,
    },
]


def match_pattern(text, patterns, exclude=None):
    """Check of text een van de patterns bevat (regex, case-insensitive)"""
    text_lower = text.lower()

    # Check exclude patterns first
    if exclude:
        for excl in exclude:
            if re.search(excl, text_lower):
                return False

    # Check main patterns
    for pattern in patterns:
        if re.search(pattern, text_lower):
            return True
    return False


def get_image_for_card(front, back, tags):
    """
    Bepaal welke image(s) bij een kaart horen

    Returns: (image_file, placement, extra_image) or (None, None, None)
    """
    combined_text = f"{front} {back} {tags}"

    best_match = None
    best_priority = 999

    for rule in IMAGE_RULES:
        # Check patterns
        if not match_pattern(combined_text, rule['patterns'],
                           rule.get('exclude')):
            continue

        # Check condition (extra filter)
        condition = rule.get('condition')
        if condition and not re.search(condition, combined_text, re.IGNORECASE):
            continue

        # Check priority (lagere nummer = hogere prioriteit)
        if rule['priority'] < best_priority:
            best_priority = rule['priority']
            best_match = rule

    if best_match:
        return (
            best_match['image'],
            best_match['placement'],
            best_match.get('extra_image')
        )

    return None, None, None


def insert_image(content, image_file, placement_type='front', extra_image=None):
    """
    Voeg image HTML toe aan content

    Args:
        content: Front of Back text
        image_file: Naam van SVG bestand
        placement_type: 'front' of 'back'
        extra_image: Optionele tweede image (side-by-side)
    """
    if not image_file:
        return content

    # Template voor image
    if extra_image:
        # Side-by-side voor vergelijkingen (bijv. ster + driehoek)
        img_html = f'''
<div style="display:flex; gap:15px; justify-content:center; margin:15px 0;">
  <div style="text-align:center;">
    <img src="{image_file}" style="max-width:280px;">
  </div>
  <div style="text-align:center;">
    <img src="{extra_image}" style="max-width:280px;">
  </div>
</div>
'''
    else:
        # Enkele image
        img_html = f'<img src="{image_file}" style="max-width:600px;">'

    # Placement strategie
    if placement_type == 'front':
        # Image bovenaan (circuit eerst, dan vraag)
        if '<img' not in content:  # Voorkom dubbele images
            return img_html + '<br><br>' + content
    else:  # back
        # Image onderaan (uitleg eerst, dan diagram)
        if '<img' not in content:
            return content + '<br><br>' + img_html

    return content


def process_csv(input_file, output_file):
    """
    Lees CSV, voeg images toe, schrijf nieuwe CSV
    """
    print(f"[LEES] {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        cards = list(reader)

    print(f"[INFO] {len(cards)} kaarten gevonden")

    # Statistieken
    stats = {
        'processed': 0,
        'with_images': 0,
        'front_images': 0,
        'back_images': 0,
        'both_images': 0,
    }

    # Verwerk elke kaart
    for i, card in enumerate(cards, 1):
        front = card['Front']
        back = card['Back']
        tags = card['Tags']

        # Zoek passende image
        image, placement, extra = get_image_for_card(front, back, tags)

        if image:
            stats['with_images'] += 1

            # Voeg image toe
            if placement == 'front':
                card['Front'] = insert_image(front, image, 'front', extra)
                stats['front_images'] += 1
            elif placement == 'back':
                card['Back'] = insert_image(back, image, 'back', extra)
                stats['back_images'] += 1
            elif placement == 'both':
                card['Front'] = insert_image(front, image, 'front', extra)
                card['Back'] = insert_image(back, image, 'back', extra)
                stats['both_images'] += 1

            # Voeg tag toe
            if 'has-image' not in tags:
                card['Tags'] = tags + ';has-image'

            print(f"  [OK] Kaart {i}: {image} -> {placement}")

        stats['processed'] += 1

    # Schrijf output
    print(f"\n[SCHRIJF] {output_file}")

    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Front', 'Back', 'Tags'])
        writer.writeheader()
        writer.writerows(cards)

    # Rapportage
    print("\n" + "="*60)
    print("RESULTATEN")
    print("="*60)
    print(f"Totaal kaarten verwerkt: {stats['processed']}")
    print(f"Kaarten met images:      {stats['with_images']} ({stats['with_images']/stats['processed']*100:.1f}%)")
    print(f"  - Image op Front:       {stats['front_images']}")
    print(f"  - Image op Back:        {stats['back_images']}")
    print(f"  - Images op beide:      {stats['both_images']}")
    print(f"\n[KLAAR] Output: {output_file}")
    print("\nImporteer in Anki: File -> Import -> Kies dit CSV bestand")


def main():
    """Main entry point"""
    print("="*60)
    print("ANKI ENERGIETECHNIEK - AUTOMATIC IMAGE INSERTION")
    print("="*60)
    print()

    # Pad naar bestanden
    base_dir = Path(__file__).parent.parent
    input_kennis = base_dir / 'generated-cards' / 'anki-deck-KENNIS-v3-FINAL.csv'
    input_rekenen = base_dir / 'generated-cards' / 'anki-deck-REKENEN-v3-FINAL.csv'

    output_kennis = base_dir / 'generated-cards' / 'anki-deck-KENNIS-v3-WITH-IMAGES.csv'
    output_rekenen = base_dir / 'generated-cards' / 'anki-deck-REKENEN-v3-WITH-IMAGES.csv'

    # Check of bestanden bestaan
    if not input_kennis.exists():
        print(f"[ERROR] Niet gevonden: {input_kennis}")
        return

    if not input_rekenen.exists():
        print(f"[ERROR] Niet gevonden: {input_rekenen}")
        return

    # Verwerk beide decks
    print("\n### KENNIS DECK ###\n")
    process_csv(input_kennis, output_kennis)

    print("\n\n### REKENEN DECK ###\n")
    process_csv(input_rekenen, output_rekenen)

    print("\n" + "="*60)
    print("SUCCES! Beide decks zijn bijgewerkt met images.")
    print("="*60)
    print("\nOUTPUT BESTANDEN:")
    print(f"  - {output_kennis}")
    print(f"  - {output_rekenen}")
    print("\nVOLGENDE STAPPEN:")
    print("  1. Open Anki")
    print("  2. File -> Import")
    print("  3. Selecteer een van de v2-WITH-IMAGES.csv bestanden")
    print("  4. Check: 'Allow HTML in fields' = YES")
    print("  5. Import en verifieer in browse mode")
    print("\nMEDIA FOLDER:")
    print("  Zorg dat SVG bestanden in Anki media folder staan:")
    print("  Windows: %APPDATA%\\Anki2\\[User]\\collection.media\\")
    print("  Of kopieer vanuit: images/circuits/ en images/phasors/")


if __name__ == '__main__':
    main()
