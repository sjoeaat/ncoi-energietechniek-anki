"""Validate FINAL study guide"""
import sys
from playwright.sync_api import sync_playwright
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

html_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\study-guide\uitwerkingen-FINAL.html")
output_dir = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1400, 'height': 2000})

    # Open
    page.goto(f'file:///{html_file.as_posix()}')
    page.wait_for_load_state('networkidle')

    print("=== FINAL VERSION VALIDATION ===\n")

    # Check page height
    height = page.evaluate("document.body.scrollHeight")
    print(f"Page height: {height:,} pixels")

    # Content stats
    images = page.locator('img').all()
    math_elements = page.locator('math').all()
    opgaven = page.locator('strong:has-text("Opgave")').all()

    print(f"\nContent:")
    print(f"  Images: {len(images)}")
    print(f"  Math formulas: {len(math_elements)}")
    print(f"  Opgave headers: {len(opgaven)}")

    # Screenshot top
    page.screenshot(path=output_dir / 'FINAL-screenshot-top.png',
                    clip={'x': 0, 'y': 0, 'width': 1400, 'height': 2000})
    print(f"\n✓ Top screenshot saved")

    # Scroll to Opgave 1 with circuit diagram
    opgave1 = page.locator('strong:has-text("Opgave 1:")').first
    if opgave1.count() > 0:
        opgave1.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path=output_dir / 'FINAL-screenshot-opgave1.png',
                        clip={'x': 0, 'y': 0, 'width': 1400, 'height': 2000})
        print(f"✓ Opgave 1 screenshot saved")

    # Scroll to Opgave 3 with math
    opgave3 = page.locator('strong:has-text("Opgave 3:")').first
    if opgave3.count() > 0:
        opgave3.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path=output_dir / 'FINAL-screenshot-opgave3.png',
                        clip={'x': 0, 'y': 0, 'width': 1400, 'height': 2000})
        print(f"✓ Opgave 3 screenshot saved")

    browser.close()

    print("\n=== VALIDATION COMPLETE ===")
    print("Screenshots saved to analysis/")
