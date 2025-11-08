"""
Validate ENHANCED-FINAL HTML
- Check it renders without errors
- Verify enhanced opgaven are present
- Check page height is reasonable
- Take screenshots for verification
"""

import sys
from playwright.sync_api import sync_playwright
from pathlib import Path

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path(__file__).parent
HTML_FILE = PROJECT_ROOT / "study-guide" / "uitwerkingen-ENHANCED-FINAL.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Load the HTML file
    file_url = f"file:///{HTML_FILE.as_posix()}"
    print(f"\nOpening: {file_url}")

    page.goto(file_url)
    page.wait_for_load_state('networkidle')

    # Check page dimensions
    page_height = page.evaluate("document.documentElement.scrollHeight")
    page_width = page.evaluate("document.documentElement.scrollWidth")
    print(f"\nPage dimensions: {page_width}px × {page_height}px")

    # Check for enhanced opgaven
    print("\nChecking for enhanced opgaven...")
    for i in range(1, 11):
        opgave_header = page.locator(f"#opgave-{i} .opgave-header").first
        if opgave_header.is_visible():
            text = opgave_header.text_content()
            print(f"  ✓ Opgave {i}: {text}")
        else:
            print(f"  ✗ Opgave {i}: NOT FOUND")

    # Check for 5-step structure in Opgave 1
    print("\nChecking 5-step structure in Opgave 1...")
    steps = page.locator("#opgave-1 .step-header").all()
    print(f"  Found {len(steps)} steps:")
    for step in steps[:5]:  # Show first 5
        print(f"    - {step.text_content()}")

    # Check for formulas
    math_elements = page.locator("math").all()
    print(f"\n✓ Found {len(math_elements)} math formulas")

    # Check for images
    images = page.locator("img").all()
    print(f"✓ Found {len(images)} images")

    # Check banner
    banner = page.locator(".banner h3").first
    if banner.is_visible():
        print(f"✓ Banner present: {banner.text_content()}")

    # Take screenshot of top
    screenshot_dir = PROJECT_ROOT / "analysis" / "validation-screenshots"
    screenshot_dir.mkdir(exist_ok=True)

    print(f"\nSaving screenshots to {screenshot_dir}...")
    page.screenshot(path=str(screenshot_dir / "enhanced-final-top.png"))

    # Scroll to Opgave 1 and screenshot
    opgave1 = page.locator("#opgave-1").first
    opgave1.scroll_into_view_if_needed()
    page.screenshot(path=str(screenshot_dir / "enhanced-final-opgave1.png"))

    print("\n" + "="*70)
    print("VALIDATION COMPLETE")
    print("="*70)

    if page_height < 100000:
        print("✓ Page height is reasonable (no nested div bug)")
    else:
        print(f"⚠️  WARNING: Page height is {page_height}px (very tall!)")

    print(f"\nScreenshots saved:")
    print(f"  - enhanced-final-top.png")
    print(f"  - enhanced-final-opgave1.png")

    browser.close()
