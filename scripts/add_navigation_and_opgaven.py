#!/usr/bin/env python3
"""
Script to add navigation sidebar and opgaven 11-16 to ENHANCED-FINAL.html
"""

import os

# File paths
FINAL_HTML = '/home/user/ncoi-energietechniek-anki/study-guide/uitwerkingen-ENHANCED-FINAL.html'
ENHANCED_DIR = '/home/user/ncoi-energietechniek-anki/enhanced-content'

# Navigation CSS to add before </style>
NAV_CSS = """
        /* Navigation Sidebar */
        .nav-sidebar {
            position: fixed;
            top: 80px;
            right: 20px;
            width: 250px;
            max-height: calc(100vh - 100px);
            overflow-y: auto;
            background: white;
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 1000;
        }

        .nav-sidebar h3 {
            color: #2c3e50;
            font-size: 1.1em;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #3498db;
        }

        .nav-sidebar ul {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .nav-sidebar li {
            margin: 8px 0;
        }

        .nav-sidebar a {
            display: block;
            padding: 8px 12px;
            color: #2c3e50;
            text-decoration: none;
            border-radius: 4px;
            transition: all 0.2s;
            font-size: 0.95em;
        }

        .nav-sidebar a:hover {
            background: #e8f4f8;
            color: #3498db;
            transform: translateX(-3px);
        }

        .nav-sidebar a.active {
            background: #3498db;
            color: white;
        }

        /* Adjust main content to make room for sidebar */
        body {
            margin-right: 290px;
        }

        /* Hide sidebar on small screens */
        @media (max-width: 1200px) {
            .nav-sidebar {
                display: none;
            }
            body {
                margin-right: 60px;
            }
        }

        @media print {
            .nav-sidebar { display: none; }
            body { margin-right: 0; }
        }

        /* Smooth scroll behavior */
        html {
            scroll-behavior: smooth;
        }

        /* Highlight target opgave */
        .opgave:target {
            animation: highlight 1.5s ease;
        }

        @keyframes highlight {
            0% { background-color: #fff3cd; }
            100% { background-color: white; }
        }
"""

# Navigation HTML to add after <body>
NAV_HTML = """
<nav class="nav-sidebar">
    <h3>📑 Navigatie</h3>
    <ul>
        <li><a href="#opgave-1">Opgave 1</a></li>
        <li><a href="#opgave-2">Opgave 2</a></li>
        <li><a href="#opgave-3">Opgave 3</a></li>
        <li><a href="#opgave-4">Opgave 4</a></li>
        <li><a href="#opgave-5">Opgave 5</a></li>
        <li><a href="#opgave-6">Opgave 6</a></li>
        <li><a href="#opgave-7">Opgave 7</a></li>
        <li><a href="#opgave-8">Opgave 8</a></li>
        <li><a href="#opgave-9">Opgave 9</a></li>
        <li><a href="#opgave-10">Opgave 10</a></li>
        <li><a href="#opgave-11">Opgave 11 <span class="enhanced-badge">NIEUW</span></a></li>
        <li><a href="#opgave-12">Opgave 12 <span class="enhanced-badge">NIEUW</span></a></li>
        <li><a href="#opgave-13">Opgave 13 <span class="enhanced-badge">NIEUW</span></a></li>
        <li><a href="#opgave-14">Opgave 14 <span class="enhanced-badge">NIEUW</span></a></li>
        <li><a href="#opgave-15">Opgave 15 <span class="enhanced-badge">NIEUW</span></a></li>
        <li><a href="#opgave-16">Opgave 16 <span class="enhanced-badge">NIEUW</span></a></li>
    </ul>
</nav>
"""

def main():
    print("📝 Adding navigation and opgaven 11-16 to ENHANCED-FINAL.html...")

    # Read the current FINAL HTML
    with open(FINAL_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add navigation CSS before </style>
    content = content.replace('    </style>', NAV_CSS + '\n    </style>', 1)
    print("✅ Added navigation CSS")

    # Add navigation HTML after <body>
    content = content.replace('<body>', '<body>\n' + NAV_HTML, 1)
    print("✅ Added navigation sidebar")

    # Add IDs to existing opgaven for navigation
    for i in range(1, 11):
        # Find "Opgave {i}" header and add ID to the .opgave div before it
        old_pattern = f'<div class="opgave-header">Opgave {i}</div>'
        new_pattern = f'<div class="opgave" id="opgave-{i}">\n<div class="opgave-header">Opgave {i}</div>'

        # First, wrap existing opgave headers with div if needed
        if f'<div class="opgave-header">Opgave {i}</div>' in content and f'id="opgave-{i}"' not in content:
            # Find the line before the header and add the ID there
            lines = content.split('\n')
            for idx, line in enumerate(lines):
                if f'<div class="opgave-header">Opgave {i}</div>' in line:
                    # Look backwards for the opening opgave div
                    for back_idx in range(idx-1, max(0, idx-10), -1):
                        if '<div class="opgave">' in lines[back_idx]:
                            lines[back_idx] = f'<div class="opgave" id="opgave-{i}">'
                            break
                    break
            content = '\n'.join(lines)

    print("✅ Added IDs to existing opgaven 1-10")

    # Read and add opgaven 11-16
    opgaven_content = "\n\n<!-- ========== NEWLY ADDED ENHANCED OPGAVEN 11-16 ========== -->\n\n"

    for i in range(11, 17):
        opgave_file = f"{ENHANCED_DIR}/opgave-{i:03d}-FULL-enhanced.html"
        if os.path.exists(opgave_file):
            with open(opgave_file, 'r', encoding='utf-8') as f:
                opgave_html = f.read()

            # Wrap in opgave div with ID and header
            wrapped_opgave = f"""
<div class="opgave" id="opgave-{i}">
<div class="opgave-header">Opgave {i}</div>
<div class="chapter-ref">H 1.9 blz. 13 (Holmes - Elektrische Netwerken)</div>

{opgave_html}

</div>
"""
            opgaven_content += wrapped_opgave
            print(f"✅ Added opgave {i}")
        else:
            print(f"⚠️  Warning: {opgave_file} not found")

    # Insert opgaven before </body>
    content = content.replace('</body>', opgaven_content + '\n</body>', 1)

    # Update banner text to reflect all 16 opgaven
    old_banner = '<strong>Opgaven 1-10:</strong> Fully enhanced'
    new_banner = '<strong>Opgaven 1-16:</strong> Fully enhanced'
    content = content.replace(old_banner, new_banner)

    old_banner2 = '<strong>Overige opgaven (11+):</strong> Complete originele uitwerkingen'
    new_banner2 = '<strong>Alle 16 opgaven:</strong> Volledig uitgewerkt met 5-stappen methodologie'
    content = content.replace(old_banner2, new_banner2)

    # Write back to file
    with open(FINAL_HTML, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✨ Successfully updated {FINAL_HTML}")
    print(f"📊 Added navigation sidebar with 16 opgaven")
    print(f"📝 Added opgaven 11-16 with FULL-enhanced format")
    print(f"\n💡 Open the file in a browser to see the navigation sidebar on the right!")

if __name__ == '__main__':
    main()
