#!/usr/bin/env python3
"""
Integreer ALLE enhanced opgaven + hiërarchische navigatie in FINAL.html
"""

import os
import glob

# Paths
FINAL_HTML = '/home/user/ncoi-energietechniek-anki/study-guide/uitwerkingen-complete-guide.html'
ENHANCED_DIR = '/home/user/ncoi-energietechniek-anki/enhanced-content'

# Hiërarchische navigatie CSS
NAV_CSS = """
/* Hiërarchische Navigatie Sidebar */
.nav-sidebar {
    position: fixed;
    top: 80px;
    right: 20px;
    width: 300px;
    max-height: calc(100vh - 100px);
    overflow-y: auto;
    background: white;
    border: 2px solid #3498db;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    z-index: 1000;
    font-size: 0.9em;
}

.nav-sidebar h3 {
    color: #2c3e50;
    font-size: 1.1em;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 2px solid #3498db;
}

.nav-chapter {
    margin-bottom: 20px;
}

.nav-chapter-header {
    font-weight: bold;
    color: #2c3e50;
    background: #ecf0f1;
    padding: 8px 10px;
    border-radius: 4px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: all 0.2s;
}

.nav-chapter-header:hover {
    background: #d5dbdb;
}

.nav-opgaven {
    list-style: none;
    margin: 0;
    padding-left: 10px;
}

.nav-opgaven li {
    margin: 4px 0;
}

.nav-opgaven a {
    display: block;
    padding: 6px 10px;
    color: #34495e;
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.2s;
    font-size: 0.95em;
}

.nav-opgaven a:hover {
    background: #e8f4f8;
    color: #3498db;
    transform: translateX(-3px);
    padding-left: 15px;
}

.nav-footer {
    margin-top: 20px;
    padding-top: 15px;
    border-top: 1px solid #ecf0f1;
    text-align: center;
    color: #7f8c8d;
}

body {
    margin-right: 340px;
}

@media (max-width: 1400px) {
    .nav-sidebar { display: none; }
    body { margin-right: 60px; }
}

@media print {
    .nav-sidebar { display: none; }
    body { margin-right: 0; }
}

html {
    scroll-behavior: smooth;
}

.opgave:target {
    animation: highlight 1.5s ease;
}

@keyframes highlight {
    0% { background-color: #fff3cd; }
    100% { background-color: white; }
}

.nav-sidebar::-webkit-scrollbar {
    width: 6px;
}

.nav-sidebar::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 3px;
}

.nav-sidebar::-webkit-scrollbar-thumb {
    background: #3498db;
    border-radius: 3px;
}
"""

# Hiërarchische navigatie HTML (aangepast voor daadwerkelijke opgaven)
NAV_HTML = """
<nav class="nav-sidebar">
    <h3>📑 Enhanced Opgaven</h3>

    <!-- H 1.9: Basiswetten -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 1.9 - Kirchhoff (1)</div>
        <ul class="nav-opgaven">
            <li><a href="#h19-opgave-17">17. Spanningsbron stroom</a></li>
        </ul>
    </div>

    <!-- H 3.11: Thévenin & Norton -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 3.11 - Thévenin/Norton (12)</div>
        <ul class="nav-opgaven">
            <li><a href="#h311-opgave-1a">1a. Thévenin parameters</a></li>
            <li><a href="#h311-opgave-1b">1b. Thévenin parameters</a></li>
            <li><a href="#h311-opgave-1c">1c. Norton parameters</a></li>
            <li><a href="#h311-opgave-1d">1d. Superpositie</a></li>
            <li><a href="#h311-opgave-2a">2a. Netwerk vereenvoudigen</a></li>
            <li><a href="#h311-opgave-2b">2b. Netwerk vereenvoudigen</a></li>
            <li><a href="#h311-opgave-2c">2c. Netwerk vereenvoudigen</a></li>
            <li><a href="#h311-opgave-2d">2d. Netwerk vereenvoudigen</a></li>
            <li><a href="#h311-opgave-2e">2e. Netwerk vereenvoudigen</a></li>
            <li><a href="#h311-opgave-3">3. Stroom I<sub>x</sub> bepalen</a></li>
            <li><a href="#h311-opgave-4">4. Spanning U<sub>x</sub> bepalen</a></li>
            <li><a href="#h311-opgave-5">5. Bronspanning bepalen</a></li>
        </ul>
    </div>

    <!-- H 5.5: Wisselspanning -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 5.5 - Wisselspanning (3)</div>
        <ul class="nav-opgaven">
            <li><a href="#h55-opgave-1">1. Driehoekspanning</a></li>
            <li><a href="#h55-opgave-7-9">7-9. Vectoriële optelling</a></li>
            <li><a href="#h55-opgave-12-13">12-13. Gemiddelde & effectieve waarde</a></li>
        </ul>
    </div>

    <!-- H 6.8: Condensator & Spoel -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 6.8 - C & L Basisformules (2)</div>
        <ul class="nav-opgaven">
            <li><a href="#h68-opgave-1">1. Condensator u=kt</a></li>
            <li><a href="#h68-opgave-2-3">2-3. Spoel i=kt</a></li>
        </ul>
    </div>

    <div class="nav-footer">
        <small>18 Enhanced Opgaven | 4 Hoofdstukken</small>
    </div>
</nav>
"""

def create_complete_html():
    print("🚀 Creating Complete Enhanced Study Guide...")

    # Start HTML document
    html = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCOI Energietechniek - Complete Enhanced Study Guide</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #000;
            background: #f5f5f5;
            padding: 40px 60px;
            max-width: 1400px;
            margin: 0 auto;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .subtitle {
            color: #7f8c8d;
            font-size: 1.1em;
        }

        .status-banner {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            padding: 15px 20px;
            border-radius: 6px;
            margin: 20px 0;
            text-align: center;
        }

        .opgave {
            margin: 30px 0;
            padding: 25px;
            background: white;
            border-left: 5px solid #3498db;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        .opgave-header {
            font-size: 1.4em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }

        .chapter-ref {
            color: #7f8c8d;
            font-size: 0.9em;
            margin-bottom: 15px;
        }

        .question {
            background: #f8f9fa;
            padding: 15px;
            margin: 15px 0;
            border-radius: 6px;
            border: 1px solid #dee2e6;
        }

        .solution {
            margin-top: 20px;
        }

        .solution-header {
            font-size: 1.2em;
            font-weight: bold;
            color: #2c3e50;
            margin: 20px 0 15px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid #3498db;
        }

        .step {
            margin: 20px 0;
            padding: 15px;
            background: #f8f9fa;
            border-left: 4px solid #27ae60;
            border-radius: 4px;
        }

        .step-header {
            font-weight: bold;
            color: #27ae60;
            margin-bottom: 10px;
        }

        .display-math {
            margin: 15px 0;
            padding: 10px;
            background: white;
            border-radius: 4px;
            text-align: center;
        }

        .interpretation {
            background: #e8f4f8;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #3498db;
            border-radius: 4px;
        }

        .interpretation-header {
            font-weight: bold;
            color: #3498db;
            margin-bottom: 10px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }

        th {
            background: #3498db;
            color: white;
            font-weight: bold;
        }

        img {
            max-width: 100%;
            height: auto;
            margin: 15px 0;
        }

        """ + NAV_CSS + """
    </style>
</head>
<body>

<header>
    <h1>NCOI Energietechniek - Complete Enhanced Study Guide</h1>
    <p class="subtitle">Elektrische Netwerken (Holmes 3e editie)</p>
    <div class="status-banner">
        <strong>✨ 18 FULL-Enhanced Opgaven</strong> | 5-Stappen Methodologie | Volledige Uitwerkingen
    </div>
</header>

""" + NAV_HTML + """

<div id="content">
"""

    # Add opgaven per chapter
    opgaven_map = {
        'h19': [
            ('opgave-017', 'h19-opgave-17', 'H 1.9 - Opgave 17'),
        ],
        'h311': [
            ('h311-opgave-1a', 'h311-opgave-1a', 'H 3.11 - Opgave 1a'),
            ('h311-opgave-1b', 'h311-opgave-1b', 'H 3.11 - Opgave 1b'),
            ('h311-opgave-1c', 'h311-opgave-1c', 'H 3.11 - Opgave 1c'),
            ('h311-opgave-1d', 'h311-opgave-1d', 'H 3.11 - Opgave 1d'),
            ('h311-opgave-2a', 'h311-opgave-2a', 'H 3.11 - Opgave 2a'),
            ('h311-opgave-2b', 'h311-opgave-2b', 'H 3.11 - Opgave 2b'),
            ('h311-opgave-2c', 'h311-opgave-2c', 'H 3.11 - Opgave 2c'),
            ('h311-opgave-2d', 'h311-opgave-2d', 'H 3.11 - Opgave 2d'),
            ('h311-opgave-2e', 'h311-opgave-2e', 'H 3.11 - Opgave 2e'),
            ('h311-opgave-3', 'h311-opgave-3', 'H 3.11 - Opgave 3'),
            ('h311-opgave-4', 'h311-opgave-4', 'H 3.11 - Opgave 4'),
            ('h311-opgave-5', 'h311-opgave-5', 'H 3.11 - Opgave 5'),
        ],
        'h55': [
            ('h55-opgave-1', 'h55-opgave-1', 'H 5.5 - Opgave 1'),
            ('h55-opgave-7-9', 'h55-opgave-7-9', 'H 5.5 - Opgaven 7-9'),
            ('h55-opgave-12-13', 'h55-opgave-12-13', 'H 5.5 - Opgaven 12-13'),
        ],
        'h68': [
            ('h68-opgave-1', 'h68-opgave-1', 'H 6.8 - Opgave 1'),
            ('h68-opgave-2-3', 'h68-opgave-2-3', 'H 6.8 - Opgaven 2-3'),
        ],
    }

    for chapter, opgaven in opgaven_map.items():
        html += f'\n<!-- ========== {chapter.upper()} ========== -->\n\n'

        for filename, id_name, title in opgaven:
            filepath = f"{ENHANCED_DIR}/{filename}-FULL-enhanced.html"

            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Wrap in opgave div with ID
                html += f'''
<div class="opgave" id="{id_name}">
<div class="opgave-header">{title}</div>
<div class="chapter-ref">Holmes - Elektrische Netwerken (3e editie)</div>

{content}

</div>

'''
                print(f"✅ Added {filename}")
            else:
                print(f"⚠️  Warning: {filepath} not found")

    # Close HTML
    html += """
</div>

</body>
</html>
"""

    # Write file
    with open(FINAL_HTML, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\n✨ Successfully created {FINAL_HTML}")
    print(f"📊 Total opgaven integrated: 18")
    print(f"📁 File size: {len(html)} characters")
    print(f"\n💡 Open in browser to view the complete enhanced study guide!")

if __name__ == '__main__':
    create_complete_html()
