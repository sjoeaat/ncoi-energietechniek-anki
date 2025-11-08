"""Check v5 study guide"""
import sys
from playwright.sync_api import sync_playwright
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

html_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\study-guide\uitwerkingen-simple-v5.html")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open the HTML
    page.goto(f'file:///{html_file.as_posix()}')
    page.wait_for_load_state('networkidle')

    print("=== V5 VALIDATION ===")
    print(f"Title: {page.title()}")

    # Check page dimensions
    viewport = page.viewport_size
    print(f"\nViewport: {viewport['width']}x{viewport['height']}")

    # Scroll to bottom to get actual height
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    height = page.evaluate("document.body.scrollHeight")
    print(f"Page height: {height} pixels")

    if height > 100000:
        print(f"❌ STILL TOO TALL! ({height} pixels)")
    else:
        print(f"✓ Reasonable height")

    # Check content
    images = page.locator('img').all()
    print(f"\nImages: {len(images)}")

    math_elements = page.locator('math').all()
    print(f"Math elements: {len(math_elements)}")

    opgaven = page.locator('strong:has-text("Opgave")').all()
    print(f"Opgave headers: {len(opgaven)}")

    # Take top screenshot
    page.goto(f'file:///{html_file.as_posix()}')
    page.wait_for_load_state('networkidle')
    page.screenshot(path='analysis/v5-screenshot-top.png', clip={'x': 0, 'y': 0, 'width': 1200, 'height': 800})
    print("\n✓ Screenshot saved: analysis/v5-screenshot-top.png")

    # Scroll to middle opgave
    page.locator('strong:has-text("Opgave 5")').first.scroll_into_view_if_needed()
    page.screenshot(path='analysis/v5-screenshot-opgave5.png', clip={'x': 0, 'y': 0, 'width': 1200, 'height': 1000})
    print("✓ Screenshot saved: analysis/v5-screenshot-opgave5.png")

    print("\n✓ VALIDATION COMPLETE")
    print("Check browser window and screenshots!")

    input("Press Enter to close...")
    browser.close()
