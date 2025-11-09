#!/usr/bin/env python3
"""
Integration Script: Combineert alle enhanced opgaven tot complete studiegids
Genereert een master index met alle 84+ opgaven georganiseerd per hoofdstuk
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Directories
ENHANCED_DIR = Path("/home/user/ncoi-energietechniek-anki/enhanced-content")
OUTPUT_FILE = Path("/home/user/ncoi-energietechniek-anki/study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html")

def extract_metadata(filepath):
    """Extract titel en hoofdstuk info uit HTML bestand"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else filepath.stem

    # Extract chapter from filename or content
    filename = filepath.name

    # Try h-prefix format first (h19, h26, etc.)
    h_match = re.match(r'h(\d+)-opgave-(.+)\.html', filename)
    if h_match:
        chapter_num = h_match.group(1)
        opgave_info = h_match.group(2).replace('-FULL-enhanced', '')
        return {
            'file': filename,
            'title': title,
            'chapter': f"H {chapter_num[0]}.{chapter_num[1:]}",
            'opgave': opgave_info,
            'sort_key': (int(chapter_num), opgave_info)
        }

    # Try opgave-XXX format
    opgave_match = re.match(r'opgave-(\d+)', filename)
    if opgave_match:
        num = opgave_match.group(1)
        return {
            'file': filename,
            'title': title,
            'chapter': "Algemeen",
            'opgave': num,
            'sort_key': (999, int(num))  # Sort at end
        }

    return None

def generate_index():
    """Genereer complete index van alle opgaven"""

    # Collect all files
    all_files = list(ENHANCED_DIR.glob("*.html"))
    print(f"📊 Gevonden: {len(all_files)} HTML bestanden")

    # Extract metadata
    opgaven_data = []
    for filepath in all_files:
        metadata = extract_metadata(filepath)
        if metadata:
            opgaven_data.append(metadata)

    # Group by chapter
    chapters = defaultdict(list)
    for data in opgaven_data:
        chapters[data['chapter']].append(data)

    # Sort within chapters
    for chapter in chapters:
        chapters[chapter].sort(key=lambda x: x['sort_key'])

    # Generate HTML
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="nl">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '    <title>Complete Index - Alle Energietechniek Opgaven</title>',
        '    <style>',
        '        * { margin: 0; padding: 0; box-sizing: border-box; }',
        '        body {',
        '            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;',
        '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
        '            padding: 20px;',
        '        }',
        '        .container {',
        '            max-width: 1200px;',
        '            margin: 0 auto;',
        '            background: white;',
        '            border-radius: 20px;',
        '            padding: 40px;',
        '            box-shadow: 0 20px 60px rgba(0,0,0,0.3);',
        '        }',
        '        h1 {',
        '            color: #1e3c72;',
        '            text-align: center;',
        '            margin-bottom: 10px;',
        '            font-size: 2.5em;',
        '        }',
        '        .subtitle {',
        '            text-align: center;',
        '            color: #666;',
        '            margin-bottom: 40px;',
        '            font-size: 1.2em;',
        '        }',
        '        .stats {',
        '            background: #e8f5e9;',
        '            padding: 20px;',
        '            border-radius: 10px;',
        '            margin-bottom: 30px;',
        '            border-left: 5px solid #4caf50;',
        '        }',
        '        .stats h2 { color: #2e7d32; margin-bottom: 10px; }',
        '        .chapter {',
        '            margin: 30px 0;',
        '            border-left: 4px solid #667eea;',
        '            padding-left: 20px;',
        '        }',
        '        .chapter-title {',
        '            font-size: 1.8em;',
        '            color: #667eea;',
        '            margin-bottom: 15px;',
        '        }',
        '        .opgave-list {',
        '            display: grid;',
        '            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));',
        '            gap: 15px;',
        '        }',
        '        .opgave-card {',
        '            background: #f5f5f5;',
        '            padding: 15px;',
        '            border-radius: 8px;',
        '            border: 2px solid #ddd;',
        '            transition: all 0.3s;',
        '        }',
        '        .opgave-card:hover {',
        '            border-color: #667eea;',
        '            transform: translateY(-2px);',
        '            box-shadow: 0 4px 12px rgba(102,126,234,0.3);',
        '        }',
        '        .opgave-card a {',
        '            text-decoration: none;',
        '            color: #333;',
        '            display: block;',
        '        }',
        '        .opgave-number {',
        '            font-weight: bold;',
        '            color: #667eea;',
        '            margin-bottom: 5px;',
        '        }',
        '        .opgave-title {',
        '            font-size: 0.9em;',
        '            color: #666;',
        '        }',
        '    </style>',
        '</head>',
        '<body>',
        '    <div class="container">',
        '        <h1>📚 Complete Index</h1>',
        '        <div class="subtitle">Alle Energietechniek Opgaven - NCOI Studiegids</div>',
        '',
        '        <div class="stats">',
        f'            <h2>📊 Statistieken</h2>',
        f'            <p><strong>Totaal opgaven:</strong> {len(opgaven_data)}</p>',
        f'            <p><strong>Hoofdstukken:</strong> {len([c for c in chapters.keys() if c != "Algemeen"])}</p>',
        f'            <p><strong>Format:</strong> FULL-enhanced met 5-staps methodologie</p>',
        f'            <p><strong>Features:</strong> MathML formules, Nederlandse terminologie, fysische interpretaties</p>',
        '        </div>',
    ]

    # Sort chapters numerically
    sorted_chapters = sorted(chapters.keys(), key=lambda x: (
        999 if x == "Algemeen" else float(x.replace("H ", "").replace(".", ""))
    ))

    # Add chapters
    for chapter in sorted_chapters:
        opgaven = chapters[chapter]
        html_parts.extend([
            f'        <div class="chapter">',
            f'            <div class="chapter-title">{chapter} ({len(opgaven)} opgaven)</div>',
            f'            <div class="opgave-list">',
        ])

        for opgave in opgaven:
            html_parts.extend([
                f'                <div class="opgave-card">',
                f'                    <a href="../enhanced-content/{opgave["file"]}">',
                f'                        <div class="opgave-number">Opgave {opgave["opgave"]}</div>',
                f'                        <div class="opgave-title">{opgave["title"][:60]}...</div>',
                f'                    </a>',
                f'                </div>',
            ])

        html_parts.extend([
            f'            </div>',
            f'        </div>',
        ])

    html_parts.extend([
        '    </div>',
        '</body>',
        '</html>',
    ])

    # Write to file
    output_html = '\n'.join(html_parts)
    OUTPUT_FILE.write_text(output_html, encoding='utf-8')

    print(f"✅ Index gegenereerd: {OUTPUT_FILE}")
    print(f"📄 {len(opgaven_data)} opgaven geïndexeerd")
    print(f"📁 {len(sorted_chapters)} hoofdstukken")

if __name__ == "__main__":
    print("🚀 Genereren van complete index...")
    generate_index()
    print("✅ Klaar!")
