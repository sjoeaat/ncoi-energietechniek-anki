"""
Inspect study guide HTML to see what's actually wrong
"""
from playwright.sync_api import sync_playwright
from pathlib import Path

html_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\study-guide\uitwerkingen-complete-guide-v4.html")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Show browser so I can see
    page = browser.new_page()

    # Open the HTML file
    page.goto(f'file:///{html_file.as_posix()}')
    page.wait_for_load_state('networkidle')

    # Take full page screenshot
    page.screenshot(path='analysis/v4-screenshot-full.png', full_page=True)

    # Take screenshot of first opgave
    page.screenshot(path='analysis/v4-screenshot-top.png')

    # Check what's visible
    print("=== PAGE INSPECTION ===")
    print(f"Title: {page.title()}")

    # Check for images
    images = page.locator('img').all()
    print(f"\nImages found: {len(images)}")
    for i, img in enumerate(images[:5]):
        src = img.get_attribute('src')
        print(f"  Image {i+1}: {src}")

    # Check for math
    math_elements = page.locator('math').all()
    print(f"\nMath elements: {len(math_elements)}")

    # Check for navigation
    nav = page.locator('nav').count()
    print(f"Navigation elements: {nav}")

    # Check for opgave headers
    opgaven = page.locator('strong:has-text("Opgave")').all()
    print(f"\nOpgave headers found: {len(opgaven)}")
    for i, opgave in enumerate(opgaven[:5]):
        print(f"  {i+1}. {opgave.inner_text()}")

    # Check for console errors
    errors = []
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)

    # Wait a bit to see if errors appear
    page.wait_for_timeout(2000)

    if errors:
        print("\n=== CONSOLE ERRORS ===")
        for error in errors:
            print(f"  {error}")

    print("\n=== KEEPING BROWSER OPEN ===")
    print("Check the browser window to see what's wrong!")
    print("Press Enter to close...")
    input()

    browser.close()
