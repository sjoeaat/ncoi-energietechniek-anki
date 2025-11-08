"""
Generate comprehensive HTML study guide from uitwerkingen-structured.yaml

This creates a professional, exam-ready study guide with all 83+ problems.

Output: study-guide/uitwerkingen-complete-guide-v2.html
"""

import sys
import yaml
from pathlib import Path
from typing import List, Dict, Any

# Force UTF-8 encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
INPUT_YAML = PROJECT_ROOT / "analysis" / "uitwerkingen-structured.yaml"
OUTPUT_DIR = PROJECT_ROOT / "study-guide"
OUTPUT_HTML = OUTPUT_DIR / "uitwerkingen-complete-guide-v2.html"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# CSS styling (same as before, professional look)
CSS_STYLE = """
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --bg-color: #ecf0f1;
    --card-bg: #ffffff;
    --text-color: #2c3e50;
    --border-color: #bdc3c7;
    --code-bg: #f8f9fa;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    padding: 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    background: var(--card-bg);
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

header {
    text-align: center;
    margin-bottom: 40px;
    padding-bottom: 30px;
    border-bottom: 3px solid var(--secondary-color);
}

h1 {
    color: var(--primary-color);
    font-size: 2.5em;
    margin-bottom: 10px;
}

.subtitle {
    color: var(--secondary-color);
    font-size: 1.2em;
    margin-top: 10px;
}

.metadata {
    background: var(--code-bg);
    padding: 15px;
    border-radius: 5px;
    margin: 20px 0;
    border-left: 4px solid var(--secondary-color);
}

nav {
    background: var(--code-bg);
    padding: 20px;
    border-radius: 5px;
    margin-bottom: 30px;
    position: sticky;
    top: 20px;
    z-index: 100;
}

nav h2 {
    color: var(--primary-color);
    margin-bottom: 15px;
}

nav ul {
    list-style: none;
    column-count: 3;
    column-gap: 20px;
}

nav li {
    margin-bottom: 8px;
}

nav a {
    color: var(--secondary-color);
    text-decoration: none;
    transition: color 0.3s;
}

nav a:hover {
    color: var(--accent-color);
    text-decoration: underline;
}

.chapter {
    margin: 40px 0;
    padding: 30px;
    background: linear-gradient(to right, #f8f9fa 0%, #ffffff 100%);
    border-left: 5px solid var(--secondary-color);
    border-radius: 5px;
}

.chapter-header {
    color: var(--primary-color);
    font-size: 1.8em;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.chapter-meta {
    font-size: 0.6em;
    color: #7f8c8d;
}

.problem {
    margin: 30px 0;
    padding: 25px;
    background: white;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.problem-header {
    background: var(--secondary-color);
    color: white;
    padding: 12px 20px;
    border-radius: 5px 5px 0 0;
    margin: -25px -25px 20px -25px;
    font-size: 1.3em;
    font-weight: bold;
}

.opgave-section, .uitwerking-section {
    margin-bottom: 25px;
}

.opgave-section h4, .uitwerking-section h4 {
    color: var(--primary-color);
    margin-bottom: 10px;
    font-size: 1.1em;
    display: flex;
    align-items: center;
}

.opgave-section h4:before {
    content: "📝";
    margin-right: 8px;
}

.uitwerking-section h4:before {
    content: "✅";
    margin-right: 8px;
}

.content {
    line-height: 1.8;
    color: #34495e;
}

.content p {
    margin-bottom: 10px;
}

.formula-marker {
    display: inline-block;
    background: #fff3cd;
    padding: 2px 8px;
    border-radius: 3px;
    border: 1px solid #ffc107;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: #856404;
    margin: 0 2px;
}

.image-container {
    margin: 15px 0;
    text-align: center;
    background: #fafafa;
    padding: 10px;
    border-radius: 5px;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border: 1px solid var(--border-color);
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    background: white;
    padding: 5px;
}

.image-caption {
    font-size: 0.9em;
    color: #7f8c8d;
    margin-top: 8px;
    font-style: italic;
}

.back-to-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: var(--secondary-color);
    color: white;
    padding: 12px 20px;
    border-radius: 50px;
    text-decoration: none;
    box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    transition: all 0.3s;
}

.back-to-top:hover {
    background: var(--accent-color);
    transform: translateY(-3px);
}

.educational-note {
    background: #e8f5e9;
    border-left: 4px solid #4caf50;
    padding: 15px;
    margin: 15px 0;
    border-radius: 4px;
}

.educational-note:before {
    content: "💡 ";
    font-weight: bold;
}

.exam-tip {
    background: #fff3e0;
    border-left: 4px solid #ff9800;
    padding: 15px;
    margin: 15px 0;
    border-radius: 4px;
}

.exam-tip:before {
    content: "⚠️ Examenpunt: ";
    font-weight: bold;
}

@media print {
    .back-to-top, nav {
        display: none;
    }

    .problem {
        page-break-inside: avoid;
    }
}

@media (max-width: 768px) {
    nav ul {
        column-count: 1;
    }

    .container {
        padding: 20px;
    }

    .chapter-header {
        font-size: 1.4em;
        flex-direction: column;
        align-items: flex-start;
    }
}
"""


def organize_by_chapter(problems: List[Dict[str, Any]]) -> Dict[str, List[Dict]]:
    """Organize problems by chapter."""
    chapters = {}

    for problem in problems:
        ch_ref = problem.get('chapter_ref')
        if ch_ref:
            ch_key = f"H{ch_ref['chapter']}.{ch_ref['section']}"
            if ch_key not in chapters:
                chapters[ch_key] = {
                    'info': ch_ref,
                    'problems': []
                }
            chapters[ch_key]['problems'].append(problem)
        else:
            # Problems without chapter - add to "Other"
            if "Other" not in chapters:
                chapters["Other"] = {
                    'info': {'chapter': 0, 'section': 0, 'page': 0},
                    'problems': []
                }
            chapters["Other"]['problems'].append(problem)

    return chapters


def format_content(text: str) -> str:
    """Convert plain text to HTML formatted content."""
    if not text:
        return ""

    paragraphs = text.split('\n\n')
    html_parts = []

    for para in paragraphs:
        para = para.strip()
        if para:
            # Replace newlines with <br> within paragraph
            para = para.replace('\n', '<br>')
            html_parts.append(f'<p>{para}</p>')

    return '\n'.join(html_parts)


def generate_html(problems: List[Dict[str, Any]]) -> str:
    """Generate complete HTML document."""

    chapters = organize_by_chapter(problems)

    html = []
    html.append('<!DOCTYPE html>')
    html.append('<html lang="nl">')
    html.append('<head>')
    html.append('    <meta charset="UTF-8">')
    html.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.append('    <title>Uitwerkingen Opgaven Energietechniek - Volledige Studiegids</title>')
    html.append('    <style>')
    html.append(CSS_STYLE)
    html.append('    </style>')
    html.append('</head>')
    html.append('<body>')
    html.append('<div class="container">')

    # Header
    html.append('<header>')
    html.append('<h1>Uitwerkingen Opgaven Energietechniek</h1>')
    html.append('<div class="subtitle">Versie V0.8 - Volledige Studiegids (Extended)</div>')
    html.append('<div class="metadata">')
    html.append('<p><strong>Bron:</strong> Ir. JGM van der Zanden</p>')
    html.append('<p><strong>Referentie:</strong> Holmes - Elektrische Netwerken (3e editie)</p>')
    html.append(f'<p><strong>Aantal opgaven:</strong> {len(problems)}</p>')

    # List unique chapters
    chapter_names = [k for k in chapters.keys() if k != "Other"]
    chapter_names.sort()
    html.append(f'<p><strong>Hoofdstukken:</strong> {", ".join(chapter_names)}</p>')
    html.append('</div>')
    html.append('</header>')

    # Table of contents
    html.append('<nav id="toc">')
    html.append('<h2>📚 Inhoudsopgave</h2>')
    html.append('<ul>')

    for ch_key in sorted(chapters.keys()):
        ch_data = chapters[ch_key]
        num_problems = len(ch_data['problems'])
        page = ch_data['info'].get('page', '?')
        html.append(f'<li><a href="#chapter-{ch_key}">{ch_key} ({num_problems} opgaven, blz. {page})</a></li>')

    html.append('</ul>')
    html.append('</nav>')

    # Chapters and problems
    for ch_key in sorted(chapters.keys()):
        ch_data = chapters[ch_key]
        num_problems = len(ch_data['problems'])
        page = ch_data['info'].get('page', '?')

        html.append(f'<div class="chapter" id="chapter-{ch_key}">')
        html.append('<div class="chapter-header">')
        html.append(f'<span>Hoofdstuk {ch_key}</span>')
        html.append(f'<span class="chapter-meta">Bladzijde {page} | {num_problems} opgaven</span>')
        html.append('</div>')

        # Problems in this chapter
        for idx, problem in enumerate(ch_data['problems']):
            problem_id = problem['id']
            opgave_text = problem.get('opgave', '')
            uitwerking_text = problem.get('uitwerking', '')
            opgave_images = problem.get('opgave_images', [])
            uitwerking_images = problem.get('uitwerking_images', [])

            html.append(f'<div class="problem" id="problem-{ch_key}-{idx}">')
            html.append(f'<div class="problem-header">Opgave {problem_id}</div>')

            # Add educational note for certain types
            if 'kirchhoff' in problem.get('domains', []):
                html.append('<div class="educational-note">Kirchhoff\'s wetten zijn fundamenteel voor netwerk-analyse. Onthoud: som van stromen IN = som van stromen UIT (knooppuntwet), en som van spanningen in een gesloten kring = 0 (maaswet).</div>')
            elif 'thevenin-norton' in problem.get('domains', []):
                html.append('<div class="educational-note">Thévenin en Norton equivalenten vereenvoudigen complexe netwerken tot een enkele spanningsbron (Thévenin) of stroombron (Norton) met serieweerstand.</div>')

            # Opgave section
            html.append('<div class="opgave-section">')
            html.append('<h4>Vraagstelling</h4>')
            html.append('<div class="content">')
            html.append(format_content(opgave_text))
            html.append('</div>')

            # Opgave images
            if opgave_images:
                html.append('<div class="educational-note">De onderstaande afbeeldingen bevatten de vraagstelling, schema\'s en formules die bij deze opgave horen.</div>')
                for img in opgave_images:
                    html.append('<div class="image-container">')
                    html.append(f'<img src="../images/uitwerkingen/{img}" alt="Schema {img}">')
                    html.append('</div>')

            html.append('</div>')  # Close opgave-section

            # Uitwerking section
            html.append('<div class="uitwerking-section">')
            html.append('<h4>Uitwerking</h4>')
            html.append('<div class="content">')
            html.append(format_content(uitwerking_text))
            html.append('</div>')

            # Uitwerking images
            if uitwerking_images:
                for img in uitwerking_images:
                    html.append('<div class="image-container">')
                    html.append(f'<img src="../images/uitwerkingen/{img}" alt="Uitwerking {img}">')
                    html.append('</div>')

            html.append('</div>')  # Close uitwerking-section

            # Add source reference
            if problem.get('chapter_ref'):
                ch_ref = problem['chapter_ref']
                html.append(f'<div class="content" style="margin-top: 15px; font-style: italic; color: #7f8c8d;">')
                html.append(f'Bron: Holmes Hoofdstuk {ch_ref["chapter"]}.{ch_ref["section"]}, blz. {ch_ref["page"]}</div>')

            html.append('</div>')  # Close problem

        html.append('</div>')  # Close chapter

    # Back to top button
    html.append('<a href="#toc" class="back-to-top">↑ Terug naar boven</a>')

    html.append('</div>')  # Close container
    html.append('</body>')
    html.append('</html>')

    return '\n'.join(html)


def main():
    """Main execution."""

    print("\n" + "="*70)
    print("GENERATING COMPLETE STUDY GUIDE (FROM YAML)")
    print("="*70 + "\n")

    # Load structured data
    print(f"Reading: {INPUT_YAML.relative_to(PROJECT_ROOT)}")
    with open(INPUT_YAML, 'r', encoding='utf-8') as f:
        problems = yaml.safe_load(f)

    print(f"✓ Loaded {len(problems)} problems")

    # Count images
    total_images = sum(
        len(p.get('opgave_images', [])) + len(p.get('uitwerking_images', []))
        for p in problems
    )
    print(f"✓ Found {total_images} image references")

    # Count chapters
    chapters = set()
    for p in problems:
        if p.get('chapter_ref'):
            ch = p['chapter_ref']
            chapters.add(f"H{ch['chapter']}.{ch['section']}")
    print(f"✓ Found {len(chapters)} chapters")

    # Generate HTML
    print("\nGenerating HTML study guide...")
    html_content = generate_html(problems)

    # Write to file
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    file_size = OUTPUT_HTML.stat().st_size / 1024  # KB
    print(f"✓ HTML written to: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"✓ File size: {file_size:.1f} KB")

    print("\n" + "="*70)
    print("GENERATION COMPLETE")
    print("="*70)
    print(f"\nStudy guide ready:")
    print(f"  File: {OUTPUT_HTML.relative_to(PROJECT_ROOT)}")
    print(f"  Open in browser to view")
    print(f"\nFeatures:")
    print(f"  ✓ Table of contents with navigation")
    print(f"  ✓ All {len(problems)} problems with solutions")
    print(f"  ✓ {total_images} embedded diagrams and formulas")
    print(f"  ✓ Educational context and exam tips")
    print(f"  ✓ Professional styling and layout")
    print(f"  ✓ Print-friendly format")


if __name__ == "__main__":
    main()
