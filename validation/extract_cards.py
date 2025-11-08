#!/usr/bin/env python3
"""Extract specific cards from REKENEN deck for detailed analysis"""

import csv
from pathlib import Path

def extract_cards(csv_path, card_numbers):
    """Extract specific cards by number"""
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        cards = list(reader)

    for num in card_numbers:
        idx = num - 1  # 0-indexed
        if idx < len(cards):
            card = cards[idx]
            print(f"\n{'='*80}")
            print(f"KAART {num}")
            print('='*80)
            print(f"\n**FRONT:**\n{card['Front']}\n")
            print(f"**BACK:**\n{card['Back']}\n")
            print(f"**TAGS:** {card['Tags']}\n")

if __name__ == '__main__':
    csv_path = Path(__file__).parent.parent / 'generated-cards' / 'anki-deck-REKENEN-v1.csv'

    # Extract cards with minor issues + representative sample
    cards_to_check = [
        22, 27, 29, 54, 56,  # Minor issues (possible missing LaTeX)
        1,   # Driefase basic
        4,   # Vermogensberekening
        14,  # Blindvermogen compensatie
        20,  # Vermogensdriehoek
        32,  # Thévenin
        38,  # Driefase ster
        55,  # Resonantie
        62,  # Driefase vergelijking
    ]

    extract_cards(csv_path, cards_to_check)
