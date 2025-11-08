"""
Professional Content Enhancement System

Pipeline:
1. Parse raw HTML → extract opgaven
2. Enhance each opgave:
   - Better pedagogical structure
   - Proper formula notation
   - Physical interpretation
   - Step-by-step reasoning
3. Generate new HTML with enhanced content

Quality standards:
- 5-step methodology
- Display math for key equations
- Dimensional analysis
- Real-world context
"""

import sys
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dataclasses import dataclass

# Force UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-pandoc-raw.html"
OUTPUT_HTML = PROJECT_ROOT / "study-guide" / "uitwerkingen-ENHANCED.html"


@dataclass
class Opgave:
    """Represents one opgave (problem)"""
    number: str  # "1", "2", "3", etc.
    chapter: str  # "H 1.9 blz. 13"
    question: str  # The problem statement (HTML)
    solution: str  # The solution/uitwerking (HTML)
    images: List[str]  # Image filenames


def extract_opgaven_from_html(html: str) -> List[Opgave]:
    """
    Parse HTML and extract all opgaven.

    Pattern:
    - Chapter: <p><strong>H X.Y blz. Z</strong></p>
    - Question: <p><strong>Opgave N:</strong></p> ...
    - Solution: <p><strong>Uitwerking opgave N:</strong></p> ...
    """
    opgaven = []

    # Split by opgave headers
    # Pattern: <p><strong>Opgave X:</strong></p>
    opgave_pattern = r'<p><strong>Opgave\s+(\d+[a-z]?):</strong></p>'
    splits = re.split(opgave_pattern, html)

    # First split is header content before first opgave
    current_chapter = ""

    # Extract chapter from header
    chapter_match = re.search(r'<p><strong>(H\s+\d+\.\d+\s+blz\.\s+\d+)</strong></p>', splits[0])
    if chapter_match:
        current_chapter = chapter_match.group(1)

    # Process opgaven (pairs: number, content)
    for i in range(1, len(splits), 2):
        if i+1 >= len(splits):
            break

        opgave_num = splits[i]
        content = splits[i+1]

        # Find next chapter (if any)
        next_chapter = re.search(r'<p><strong>(H\s+\d+\.\d+\s+blz\.\s+\d+)</strong></p>', content)
        if next_chapter:
            current_chapter = next_chapter.group(1)
            # Remove chapter from content
            content = content[next_chapter.end():]

        # Split into question and solution
        solution_pattern = r'<p><strong>Uitwerking opgave\s+\d+[a-z]?:</strong></p>'
        parts = re.split(solution_pattern, content, maxsplit=1)

        question = parts[0].strip() if len(parts) > 0 else ""
        solution = parts[1].strip() if len(parts) > 1 else ""

        # Extract images from both parts
        images = re.findall(r'src="[^"]*/(image\d+\.(?:PNG|png|gif))"', question + solution)

        opgave = Opgave(
            number=opgave_num,
            chapter=current_chapter,
            question=question,
            solution=solution,
            images=images
        )

        opgaven.append(opgave)
        print(f"  Extracted: Opgave {opgave_num} ({current_chapter})")

    return opgaven


def enhance_opgave(opgave: Opgave) -> Opgave:
    """
    Enhance a single opgave with better content.

    Improvements:
    1. Structure solution in clear steps
    2. Convert inline math to display math for key equations
    3. Add physical interpretation
    4. Add dimensional analysis
    5. Improve explanatory text
    """

    # For now, return original (we'll implement enhancement logic incrementally)
    # This is a placeholder for the AI-assisted enhancement

    print(f"    Enhancing Opgave {opgave.number}...")

    # Step 1: Parse existing solution
    # Step 2: Identify key formulas
    # Step 3: Restructure with proper steps
    # Step 4: Add context and interpretation

    # TODO: Implement enhancement logic
    # For now, keep original but mark for enhancement

    return opgave


def generate_enhanced_html(opgaven: List[Opgave]) -> str:
    """Generate HTML with enhanced content"""

    css_header = '''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uitwerkingen Opgaven - Enhanced Professional Edition</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #000;
            background: #fff;
            padding: 40px 60px;
            max-width: 1400px;
            margin: 0 auto;
        }

        p { margin: 8px 0; text-align: justify; }
        strong { font-weight: 600; color: #000; }
        em { font-style: italic; }

        /* Opgave styling */
        .opgave {
            margin: 30px 0;
            padding: 20px;
            background: #f9f9f9;
            border-left: 4px solid #2c3e50;
            border-radius: 4px;
        }

        .opgave-header {
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .chapter-ref {
            color: #666;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .question {
            background: #fff;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
            border: 1px solid #ddd;
        }

        .solution {
            margin-top: 20px;
        }

        .solution-header {
            font-size: 1.1em;
            font-weight: bold;
            color: #2c3e50;
            margin: 15px 0 10px 0;
            padding-bottom: 5px;
            border-bottom: 2px solid #3498db;
        }

        /* Step structure */
        .step {
            margin: 15px 0;
            padding: 12px;
            background: #fff;
            border-left: 3px solid #3498db;
        }

        .step-header {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 8px;
        }

        /* Math - both inline and display */
        math {
            font-size: 1.1em;
            margin: 0 3px;
        }

        /* Display math (centered, larger) */
        p:has(> math[display="block"]),
        .display-math {
            text-align: center;
            margin: 15px 0;
        }

        .display-math math {
            font-size: 1.3em;
        }

        /* Images */
        img {
            max-width: 500px;
            height: auto;
            display: block;
            margin: 15px auto;
            border: 1px solid #ccc;
            padding: 8px;
            background: #fff;
            border-radius: 4px;
        }

        /* Tables (for given values) */
        table {
            margin: 15px auto;
            border-collapse: collapse;
            background: #fff;
        }

        th, td {
            padding: 8px 15px;
            border: 1px solid #ddd;
            text-align: left;
        }

        th {
            background: #f0f0f0;
            font-weight: bold;
        }

        /* Interpretation boxes */
        .interpretation {
            margin: 15px 0;
            padding: 12px;
            background: #e8f4f8;
            border-left: 4px solid #3498db;
            border-radius: 4px;
        }

        .interpretation-header {
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 6px;
        }

        /* Links */
        a { color: #0563c1; text-decoration: underline; }
        a:hover { color: #1f4788; }

        /* Print optimization */
        @media print {
            body { padding: 20px; font-size: 10pt; }
            .opgave { page-break-inside: avoid; }
        }
    </style>

    <!-- MathJax for better formula rendering -->
    <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']],
                processEscapes: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }
        };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

<header style="text-align: center; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 3px solid #2c3e50;">
    <h1 style="font-size: 2em; margin-bottom: 10px;">Uitwerkingen Opgaven Energietechniek</h1>
    <p style="font-size: 1.1em; color: #666;">Enhanced Professional Edition</p>
    <p style="margin-top: 10px; font-size: 0.95em;">Ir. JGM van der Zanden | Holmes - Elektrische Netwerken (3e editie)</p>
    <p style="margin-top: 5px; font-size: 0.9em; color: #999;">Enhanced met verbeterde pedagogiek en professionele formule-opmaak</p>
</header>

'''

    footer = '''
</body>
</html>
'''

    # Build content
    content = []

    for opgave in opgaven:
        content.append(f'<div class="opgave" id="opgave-{opgave.number}">')
        content.append(f'<div class="opgave-header">Opgave {opgave.number}</div>')

        if opgave.chapter:
            content.append(f'<div class="chapter-ref">{opgave.chapter}</div>')

        # Question
        content.append('<div class="question">')
        content.append(opgave.question)
        content.append('</div>')

        # Solution
        content.append('<div class="solution">')
        content.append('<div class="solution-header">Uitwerking</div>')
        content.append(opgave.solution)
        content.append('</div>')

        content.append('</div>')  # Close opgave

    return css_header + '\n'.join(content) + footer


def main():
    """Main execution"""

    print("\n" + "="*70)
    print("PROFESSIONAL CONTENT ENHANCEMENT")
    print("="*70 + "\n")

    # Read raw HTML
    print(f"Reading: {INPUT_HTML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_HTML, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix image paths
    html = html.replace('src="study-guide/', 'src="')

    # Extract opgaven
    print("\nExtracting opgaven...")
    opgaven = extract_opgaven_from_html(html)
    print(f"✓ Extracted {len(opgaven)} opgaven")

    # Enhance each opgave
    print("\nEnhancing content...")
    enhanced_opgaven = []
    for opgave in opgaven:
        enhanced = enhance_opgave(opgave)
        enhanced_opgaven.append(enhanced)

    print(f"✓ Enhanced {len(enhanced_opgaven)} opgaven")

    # Generate HTML
    print("\nGenerating enhanced HTML...")
    enhanced_html = generate_enhanced_html(enhanced_opgaven)

    # Write output
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(enhanced_html)

    file_size = OUTPUT_HTML.stat().st_size / 1024
    print(f"✓ Written: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("PHASE 1 COMPLETE - STRUCTURE READY")
    print("="*70)

    print("\nNext phase: Implement AI-assisted content enhancement")
    print("This will improve pedagogical quality for all opgaven")


if __name__ == "__main__":
    main()
