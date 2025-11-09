#!/usr/bin/env python3
"""
PDF Export Generator - Genereert print-ready HTML voor PDF export
Combineert alle opgaven in één document voor simpel printen/archiveren
"""

import re
from pathlib import Path

ENHANCED_DIR = Path("/home/user/ncoi-energietechniek-anki/enhanced-content")
OUTPUT_FILE = Path("/home/user/ncoi-energietechniek-anki/study-guide/PRINT-READY-COMPLETE-GUIDE.html")

def extract_opgave_content(filepath):
    """Extract main content from opgave HTML"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1) if title_match else filepath.stem

    # Extract chapter from filename
    filename = filepath.name
    h_match = re.match(r'h(\d+)-opgave-(.+)\.html', filename)
    if h_match:
        chapter_num = h_match.group(1)
        chapter = f"H {chapter_num[0]}.{chapter_num[1:]}"
    else:
        chapter = "Algemeen"

    # Extract body content (everything in .content div or similar)
    # For simplicity, extract everything between <body> tags
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    body_content = body_match.group(1) if body_match else ""

    return {
        'title': title,
        'chapter': chapter,
        'content': body_content,
        'filename': filepath.name
    }

def generate_print_html():
    """Generate single HTML file with all opgaven for printing"""

    print("📄 Genereren van print-ready PDF export...")

    # Collect all opgaven
    all_files = sorted(ENHANCED_DIR.glob("h*.html"))  # Only h-prefix files (enhanced)
    print(f"📊 Gevonden: {len(all_files)} enhanced opgaven")

    opgaven_data = []
    for filepath in all_files:
        try:
            data = extract_opgave_content(filepath)
            opgaven_data.append(data)
        except Exception as e:
            print(f"⚠️  Error processing {filepath.name}: {e}")

    # Generate HTML
    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="nl">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '    <title>NCOI Energietechniek - Complete Studiegids (Print Ready)</title>',
        '    <style>',
        '        @media print {',
        '            body {',
        '                background: white !important;',
        '                padding: 0;',
        '            }',
        '            .opgave-container {',
        '                page-break-after: always;',
        '                page-break-inside: avoid;',
        '            }',
        '            .opgave-container:last-child {',
        '                page-break-after: auto;',
        '            }',
        '            .no-print {',
        '                display: none !important;',
        '            }',
        '            .toc {',
        '                page-break-after: always;',
        '            }',
        '        }',
        '        * { margin: 0; padding: 0; box-sizing: border-box; }',
        '        body {',
        '            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;',
        '            background: #f5f5f5;',
        '            padding: 20px;',
        '            line-height: 1.6;',
        '        }',
        '        .print-header {',
        '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
        '            color: white;',
        '            padding: 40px;',
        '            text-align: center;',
        '            border-radius: 10px;',
        '            margin-bottom: 30px;',
        '        }',
        '        .print-header h1 { font-size: 2.5em; margin-bottom: 10px; }',
        '        .print-header p { font-size: 1.2em; }',
        '        .print-btn {',
        '            background: #4caf50;',
        '            color: white;',
        '            border: none;',
        '            padding: 15px 30px;',
        '            font-size: 1.1em;',
        '            border-radius: 8px;',
        '            cursor: pointer;',
        '            margin: 20px auto;',
        '            display: block;',
        '        }',
        '        .print-btn:hover {',
        '            background: #45a049;',
        '            transform: translateY(-2px);',
        '        }',
        '        .toc {',
        '            background: white;',
        '            padding: 30px;',
        '            border-radius: 10px;',
        '            margin-bottom: 30px;',
        '        }',
        '        .toc h2 {',
        '            color: #667eea;',
        '            margin-bottom: 20px;',
        '            font-size: 2em;',
        '        }',
        '        .toc-item {',
        '            padding: 10px;',
        '            border-bottom: 1px solid #ddd;',
        '        }',
        '        .toc-item a {',
        '            color: #333;',
        '            text-decoration: none;',
        '        }',
        '        .toc-item a:hover {',
        '            color: #667eea;',
        '        }',
        '        .opgave-container {',
        '            background: white;',
        '            padding: 30px;',
        '            margin-bottom: 30px;',
        '            border-radius: 10px;',
        '            border-left: 5px solid #667eea;',
        '        }',
        '        .opgave-header {',
        '            border-bottom: 3px solid #667eea;',
        '            padding-bottom: 15px;',
        '            margin-bottom: 20px;',
        '        }',
        '        .opgave-chapter {',
        '            color: #667eea;',
        '            font-weight: bold;',
        '            font-size: 1.1em;',
        '        }',
        '        .opgave-title {',
        '            color: #333;',
        '            font-size: 1.5em;',
        '            margin-top: 5px;',
        '        }',
        '    </style>',
        '</head>',
        '<body>',
        '    <div class="print-header">',
        '        <h1>📚 NCOI Energietechniek</h1>',
        '        <p>Complete Studiegids - Print Ready Export</p>',
        '        <p style="margin-top: 10px; font-size: 0.9em;">Elektrische Netwerken (3e editie) - Paul Holmes</p>',
        '    </div>',
        '',
        '    <button class="print-btn no-print" onclick="window.print()">🖨️ Printen / PDF Opslaan</button>',
        '',
        '    <div class="toc">',
        '        <h2>📑 Inhoudsopgave</h2>',
        f'        <p style="color: #666; margin-bottom: 20px;"><strong>{len(opgaven_data)} opgaven</strong> - Georganiseerd per hoofdstuk</p>',
    ]

    # Generate table of contents
    current_chapter = None
    for i, opgave in enumerate(opgaven_data, 1):
        if opgave['chapter'] != current_chapter:
            if current_chapter is not None:
                html_parts.append('        </div>')
            html_parts.append(f'        <div style="margin: 20px 0;">')
            html_parts.append(f'            <h3 style="color: #667eea; margin-bottom: 10px;">{opgave["chapter"]}</h3>')
            current_chapter = opgave['chapter']

        html_parts.append(f'            <div class="toc-item">')
        html_parts.append(f'                <a href="#opgave-{i}">{i}. {opgave["title"][:80]}...</a>')
        html_parts.append(f'            </div>')

    html_parts.append('        </div>')
    html_parts.append('    </div>')

    # Add all opgaven content
    for i, opgave in enumerate(opgaven_data, 1):
        html_parts.extend([
            f'    <div class="opgave-container" id="opgave-{i}">',
            f'        <div class="opgave-header">',
            f'            <div class="opgave-chapter">{opgave["chapter"]} - Opgave {i}/{len(opgaven_data)}</div>',
            f'            <div class="opgave-title">{opgave["title"]}</div>',
            f'        </div>',
            f'        {opgave["content"]}',
            f'    </div>',
        ])

    # Footer
    html_parts.extend([
        '    <div style="text-align: center; color: #999; margin-top: 50px; padding: 20px;">',
        '        <p><strong>NCOI Energietechniek - Complete Studiegids</strong></p>',
        f'        <p style="margin-top: 10px;">Auto-gegenereerd • {len(opgaven_data)} opgaven • 2025</p>',
        '        <p style="margin-top: 5px; font-size: 0.9em;">Voor beste resultaten: print naar PDF (Ctrl+P) met "Background graphics" aan</p>',
        '    </div>',
        '</body>',
        '</html>',
    ])

    return '\n'.join(html_parts)

if __name__ == "__main__":
    print("📄 Genereren van PDF export...")

    html_content = generate_print_html()
    OUTPUT_FILE.write_text(html_content, encoding='utf-8')

    print(f"✅ PDF export gegenereerd!")
    print(f"📄 Bestand: {OUTPUT_FILE}")
    print(f"📏 Grootte: {len(html_content):,} characters")
    print(f"\n💡 Gebruik tips:")
    print(f"   1. Open in browser: firefox {OUTPUT_FILE}")
    print(f"   2. Print naar PDF (Ctrl+P)")
    print(f"   3. Kies: 'Save as PDF' of 'Microsoft Print to PDF'")
    print(f"   4. Zet 'Background graphics' AAN voor kleuren")
    print(f"   5. Resultaat: Complete studiegids in één PDF!")
