"""Take screenshots of v5"""
import sys
from playwright.sync_api import sync_playwright
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

html_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\study-guide\uitwerkingen-simple-v5.html")
output_dir = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1200, 'height': 1600})

    # Open the HTML
    page.goto(f'file:///{html_file.as_posix()}')
    page.wait_for_load_state('networkidle')

    # Screenshot top
    page.screenshot(path=output_dir / 'v5-screenshot-top.png', clip={'x': 0, 'y': 0, 'width': 1200, 'height': 1600})
    print("✓ Top screenshot saved")

    # Screenshot Opgave 1
    page.locator('strong:has-text("Opgave 1:")').first.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path=output_dir / 'v5-screenshot-opgave1.png', clip={'x': 0, 'y': 0, 'width': 1200, 'height': 1600})
    print("✓ Opgave 1 screenshot saved")

    # Screenshot Opgave 3 (has math)
    opgave3 = page.locator('strong:has-text("Opgave 3:")').first
    if opgave3.count() > 0:
        opgave3.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path=output_dir / 'v5-screenshot-opgave3.png', clip={'x': 0, 'y': 0, 'width': 1200, 'height': 1600})
        print("✓ Opgave 3 screenshot saved")

    browser.close()
    print("\n✓ All screenshots saved to analysis/")
