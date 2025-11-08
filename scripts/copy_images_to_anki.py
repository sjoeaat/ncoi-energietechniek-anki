#!/usr/bin/env python3
"""
Kopieer alle SVG afbeeldingen naar Anki media folder
NCOI Energietechniek - Image Deployment Script

Author: Claude Code
Date: 2025-11-08
"""

import os
import sys
import shutil
from pathlib import Path
from collections import defaultdict

def find_anki_media_folder():
    """Zoek Anki media folder op Windows"""
    appdata = os.getenv('APPDATA')
    if not appdata:
        return None

    anki_base = Path(appdata) / 'Anki2'
    if not anki_base.exists():
        return None

    # Zoek alle user profiles
    profiles = []
    for item in anki_base.iterdir():
        if item.is_dir() and item.name != 'addons21':
            media_folder = item / 'collection.media'
            if media_folder.exists():
                profiles.append(media_folder)

    return profiles


def collect_svg_files(base_dir):
    """Verzamel alle SVG bestanden uit circuits/ en phasors/"""
    circuits_dir = base_dir / 'images' / 'circuits'
    phasors_dir = base_dir / 'images' / 'phasors'

    svg_files = []

    # Verzamel uit circuits/
    if circuits_dir.exists():
        for file in circuits_dir.glob('*.svg'):
            svg_files.append(('circuits', file))

    # Verzamel uit phasors/
    if phasors_dir.exists():
        for file in phasors_dir.glob('*.svg'):
            svg_files.append(('phasors', file))

    return svg_files


def check_duplicates(svg_files):
    """Check voor naam-conflicten tussen circuits en phasors"""
    names = defaultdict(list)

    for source_dir, file_path in svg_files:
        names[file_path.name].append(source_dir)

    duplicates = {name: dirs for name, dirs in names.items() if len(dirs) > 1}
    return duplicates


def copy_to_anki(svg_files, target_folder, dry_run=False):
    """Kopieer SVG bestanden naar Anki media folder"""
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Kopiëren naar: {target_folder}")
    print("="*70)

    copied = 0
    skipped = 0

    for source_dir, file_path in svg_files:
        target_path = target_folder / file_path.name

        # Check of bestand al bestaat
        if target_path.exists():
            # Vergelijk file sizes
            if target_path.stat().st_size == file_path.stat().st_size:
                print(f"  [SKIP] {file_path.name} (al aanwezig, zelfde grootte)")
                skipped += 1
                continue
            else:
                print(f"  [REPLACE] {file_path.name} (nieuwe versie)")
        else:
            print(f"  [COPY] {file_path.name} (vanuit {source_dir}/)")

        if not dry_run:
            shutil.copy2(file_path, target_path)

        copied += 1

    print("="*70)
    print(f"\nResultaat:")
    print(f"  Gekopieerd: {copied}")
    print(f"  Overgeslagen: {skipped}")
    print(f"  Totaal: {copied + skipped}")

    return copied, skipped


def main():
    """Main entry point"""
    # Check for auto-confirm flag
    auto_confirm = '--yes' in sys.argv or '-y' in sys.argv

    print("="*70)
    print("ANKI ENERGIETECHNIEK - SVG DEPLOYMENT TOOL")
    print("="*70)
    print()

    # 1. Find base directory
    base_dir = Path(__file__).parent.parent
    print(f"Project directory: {base_dir}")

    # 2. Collect SVG files
    print("\nVerzamelen SVG bestanden...")
    svg_files = collect_svg_files(base_dir)

    if not svg_files:
        print("[ERROR] Geen SVG bestanden gevonden!")
        return

    print(f"  [OK] {len(svg_files)} SVG bestanden gevonden")

    # Groepeer per source directory
    circuits_count = sum(1 for src, _ in svg_files if src == 'circuits')
    phasors_count = sum(1 for src, _ in svg_files if src == 'phasors')
    print(f"    - circuits/: {circuits_count}")
    print(f"    - phasors/:  {phasors_count}")

    # 3. Check for duplicates
    print("\nControleren op naam-conflicten...")
    duplicates = check_duplicates(svg_files)

    if duplicates:
        print("  [WARNING] Duplicate bestandsnamen gevonden:")
        for name, dirs in duplicates.items():
            print(f"    - {name} in: {', '.join(dirs)}")
        print("\n  Deze bestanden zullen elkaar overschrijven!")
        if not auto_confirm:
            response = input("\n  Doorgaan? (y/n): ")
            if response.lower() != 'y':
                print("  Afgebroken.")
                return
        else:
            print("\n  [AUTO-CONFIRM] Doorgaan...")
    else:
        print("  [OK] Geen conflicten")

    # 4. Find Anki media folders
    print("\nZoeken naar Anki media folder...")
    media_folders = find_anki_media_folder()

    if not media_folders:
        print("  [ERROR] Anki media folder niet gevonden!")
        print("\n  Verwachte locatie: %APPDATA%\\Anki2\\[User]\\collection.media\\")
        print("\n  Mogelijke oorzaken:")
        print("    - Anki is nog niet geïnstalleerd")
        print("    - Anki is nog nooit geopend")
        print("    - Anki staat op een andere locatie")
        return

    if len(media_folders) == 1:
        target_folder = media_folders[0]
        print(f"  [OK] Gevonden: {target_folder}")
    else:
        print(f"  [OK] {len(media_folders)} profielen gevonden:")
        for i, folder in enumerate(media_folders, 1):
            print(f"    [{i}] {folder}")

        if not auto_confirm:
            choice = input(f"\n  Selecteer profiel (1-{len(media_folders)}): ")
            try:
                idx = int(choice) - 1
                target_folder = media_folders[idx]
            except (ValueError, IndexError):
                print("  [ERROR] Ongeldige keuze")
                return
        else:
            # Auto-select eerste profiel
            target_folder = media_folders[0]
            print(f"\n  [AUTO-CONFIRM] Selecteer profiel 1: {target_folder}")

    # 5. Preview
    print("\n" + "="*70)
    print("PREVIEW - Wat wordt er gekopieerd?")
    print("="*70)

    for source_dir, file_path in svg_files[:5]:
        print(f"  • {file_path.name} (vanuit {source_dir}/)")

    if len(svg_files) > 5:
        print(f"  ... en nog {len(svg_files) - 5} bestanden")

    print(f"\nNaar: {target_folder}")

    if not auto_confirm:
        response = input("\nDoorgaan met kopiëren? (y/n): ")
        if response.lower() != 'y':
            print("\nAfgebroken.")
            return
    else:
        print("\n[AUTO-CONFIRM] Kopiëren gestart...")

    # 6. Copy files
    copied, skipped = copy_to_anki(svg_files, target_folder, dry_run=False)

    # 7. Summary
    print("\n" + "="*70)
    print("KLAAR!")
    print("="*70)
    print(f"\n[OK] {copied} bestanden gekopieerd naar Anki")
    print(f"[OK] {skipped} bestanden waren al up-to-date")
    print(f"\nAnki kan nu de afbeeldingen vinden in de CSV bestanden!")
    print("\nVolgende stappen:")
    print("  1. Open Anki")
    print("  2. File -> Import")
    print("  3. Selecteer: generated-cards/anki-deck-KENNIS-v3-WITH-IMAGES.csv")
    print("  4. Check: 'Allow HTML in fields' = YES")
    print("  5. Import en test een kaart met afbeelding")


if __name__ == '__main__':
    main()
