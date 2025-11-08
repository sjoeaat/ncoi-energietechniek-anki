"""
Validate the generated study guide using Playwright

This script:
1. Opens the HTML study guide in a real browser
2. Takes screenshots of sample problems
3. Validates that images are loading
4. Checks for broken image links
5. Reports issues found
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
import time

# Force UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
HTML_FILE = PROJECT_ROOT / "study-guide" / "uitwerkingen-complete-guide.html"
SCREENSHOT_DIR = PROJECT_ROOT / "analysis" / "validation-screenshots"

# Create screenshot directory
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


def validate_study_guide():
    """Validate the study guide with Playwright."""

    print("\n" + "="*70)
    print("VALIDATING STUDY GUIDE WITH PLAYWRIGHT")
    print("="*70 + "\n")

    if not HTML_FILE.exists():
        print(f"❌ HTML file not found: {HTML_FILE}")
        return

    print(f"✓ HTML file found: {HTML_FILE.relative_to(PROJECT_ROOT)}")
    print(f"  File size: {HTML_FILE.stat().st_size / 1024:.1f} KB")

    with sync_playwright() as p:
        print("\n🌐 Launching browser...")
        browser = p.chromium.launch(headless=False)  # Visible browser
        page = browser.new_page(viewport={'width': 1400, 'height': 900})

        # Navigate to the HTML file
        file_url = f"file:///{HTML_FILE.as_posix()}"
        print(f"📄 Opening: {file_url}")

        try:
            page.goto(file_url, timeout=30000)
            print("✓ Page loaded")

            # Wait for page to fully render
            page.wait_for_load_state('networkidle', timeout=10000)
            time.sleep(2)  # Extra wait for images

            # Take full page screenshot
            print("\n📸 Taking screenshots...")
            screenshot_path = SCREENSHOT_DIR / "full-page.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            print(f"✓ Full page screenshot: {screenshot_path.relative_to(PROJECT_ROOT)}")

            # Get page title
            title = page.title()
            print(f"\n📋 Page title: {title}")

            # Check for images
            print("\n🖼️  Checking images...")
            all_images = page.locator('img').all()
            total_images = len(all_images)
            print(f"  Found {total_images} <img> tags in HTML")

            # Check how many images actually loaded
            loaded_images = 0
            broken_images = []

            for i, img in enumerate(all_images[:10]):  # Check first 10
                src = img.get_attribute('src')
                natural_width = img.evaluate('el => el.naturalWidth')

                if natural_width > 0:
                    loaded_images += 1
                else:
                    broken_images.append(src)

                if i < 5:  # Show details for first 5
                    status = "✓" if natural_width > 0 else "❌"
                    print(f"  {status} Image {i+1}: {src[:60]}... (width: {natural_width})")

            print(f"\n  Summary: {loaded_images}/10 images loaded successfully")

            if broken_images:
                print(f"\n  ⚠️  Broken images found:")
                for broken in broken_images[:5]:
                    print(f"     - {broken}")

            # Scroll to first problem
            print("\n📍 Scrolling to first problem...")
            first_problem = page.locator('.problem').first
            if first_problem.count() > 0:
                first_problem.scroll_into_view_if_needed()
                time.sleep(1)

                # Screenshot of first problem
                screenshot_path = SCREENSHOT_DIR / "problem-1.png"
                first_problem.screenshot(path=str(screenshot_path))
                print(f"✓ First problem screenshot: {screenshot_path.relative_to(PROJECT_ROOT)}")

                # Get problem text
                problem_text = first_problem.inner_text()
                print(f"\n📝 First problem preview:")
                print(f"   {problem_text[:200]}...")

            # Check for formula markers
            formula_markers = page.locator('.formula-marker').all()
            print(f"\n🔢 Found {len(formula_markers)} formula markers")

            # Check for educational notes
            edu_notes = page.locator('.educational-note').all()
            print(f"💡 Found {len(edu_notes)} educational notes")

            # Scroll to a problem with images
            print("\n🖼️  Looking for problem with images...")
            problems_with_images = page.locator('.problem:has(.image-container)').all()
            print(f"  Found {len(problems_with_images)} problems with images")

            if len(problems_with_images) > 0:
                # Scroll to second problem (likely has more images)
                target_problem = problems_with_images[min(1, len(problems_with_images)-1)]
                target_problem.scroll_into_view_if_needed()
                time.sleep(1)

                # Screenshot
                screenshot_path = SCREENSHOT_DIR / "problem-with-images.png"
                target_problem.screenshot(path=str(screenshot_path))
                print(f"✓ Problem with images screenshot: {screenshot_path.relative_to(PROJECT_ROOT)}")

                # Count images in this problem
                images_in_problem = target_problem.locator('img').all()
                print(f"  This problem has {len(images_in_problem)} images")

            # Validation summary
            print("\n" + "="*70)
            print("VALIDATION SUMMARY")
            print("="*70)
            print(f"✓ Total <img> tags: {total_images}")
            print(f"✓ Images checked: 10")
            print(f"✓ Loaded successfully: {loaded_images}/10")
            print(f"✓ Formula markers: {len(formula_markers)}")
            print(f"✓ Educational notes: {len(edu_notes)}")
            print(f"✓ Problems with images: {len(problems_with_images)}")
            print(f"✓ Screenshots saved to: {SCREENSHOT_DIR.relative_to(PROJECT_ROOT)}")

            if loaded_images < 5:
                print(f"\n⚠️  WARNING: Most images failed to load!")
                print(f"   This indicates broken image paths.")
                print(f"   Expected path structure:")
                print(f"     study-guide/uitwerkingen-complete-guide.html")
                print(f"     images/uitwerkingen/*.png")
                print(f"\n   Checking image paths...")

                # Get actual image directory structure
                images_dir = PROJECT_ROOT / "images" / "uitwerkingen"
                if images_dir.exists():
                    image_files = list(images_dir.glob("*.png"))
                    print(f"   ✓ Found {len(image_files)} PNG files in images/uitwerkingen/")
                    if len(image_files) > 0:
                        print(f"   First image: {image_files[0].name}")
                else:
                    print(f"   ❌ Directory not found: {images_dir}")

            print("\n✓ Browser will stay open for 10 seconds for manual inspection...")
            time.sleep(10)

        except Exception as e:
            print(f"\n❌ Error during validation: {e}")
            import traceback
            traceback.print_exc()

        finally:
            print("\n🔒 Closing browser...")
            browser.close()

    print("\n" + "="*70)
    print("VALIDATION COMPLETE")
    print("="*70)
    print(f"\nScreenshots available in: {SCREENSHOT_DIR.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    validate_study_guide()
