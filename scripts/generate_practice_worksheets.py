#!/usr/bin/env python3
"""
Practice Worksheets Generator - Genereert print-ready oefenbladen

Creëert opgaven worksheets per hoofdstuk waar studenten op kunnen schrijven.
Perfect voor offline studie en exam prep.
"""

from pathlib import Path

OUTPUT_DIR = Path("/home/user/ncoi-energietechniek-anki/study-guide/worksheets")

# Worksheet templates per hoofdstuk
WORKSHEETS = {
    "H 1.9 - Wet van Ohm & Kirchhoff": [
        {
            "q": "Een zaklantaarn heeft een totale weerstand van 15Ω en wordt gevoed door drie 1,5V batterijen in serie. Bereken de stroom door de lamp.",
            "given": "U_bat = 3 × 1,5V = 4,5V, R = 15Ω",
            "find": "I = ?",
            "space": 6
        },
        {
            "q": "In een knooppunt komen drie stromen samen: I₁ = 2A (binnen), I₂ = 0,5A (binnen), I₃ (buiten). Bereken I₃.",
            "given": "I₁ = 2A, I₂ = 0,5A, KCL geldig",
            "find": "I₃ = ?",
            "space": 5
        },
        {
            "q": "Een verwarmingselement trekt 4,51A uit het 230V net. Bereken de weerstand en het vermogen.",
            "given": "U = 230V, I = 4,51A",
            "find": "R = ?, P = ?",
            "space": 7
        },
    ],

    "H 2.6 - Serie & Parallel": [
        {
            "q": "Twee weerstanden van 10Ω en 40Ω staan parallel. Bereken de totale weerstand.",
            "given": "R₁ = 10Ω, R₂ = 40Ω, parallel",
            "find": "R_totaal = ?",
            "space": 6
        },
        {
            "q": "Een spanningsdeler heeft R₁ = 3kΩ en R₂ = 1kΩ in serie over 12V. Bereken de spanning over R₂.",
            "given": "U_totaal = 12V, R₁ = 3kΩ, R₂ = 1kΩ",
            "find": "U_R2 = ?",
            "space": 6
        },
        {
            "q": "Drie gelijke weerstanden van 60Ω staan parallel. Wat is de totale weerstand?",
            "given": "R = 60Ω (3×), parallel",
            "find": "R_totaal = ?",
            "space": 5
        },
    ],

    "H 3.11 - Netwerk Analyse": [
        {
            "q": "Een netwerk heeft een open-klem spanning van 10V en een kortsluitstroom van 2A. Bereken de Thévenin weerstand.",
            "given": "U_open = 10V, I_kort = 2A",
            "find": "R_th = ?",
            "space": 5
        },
        {
            "q": "Thévenin equivalent: U_th = 6V, R_th = 12Ω. Belasting R_load = 10Ω. Bereken de stroom door de belasting.",
            "given": "U_th = 6V, R_th = 12Ω, R_load = 10Ω",
            "find": "I_load = ?",
            "space": 6
        },
    ],

    "H 4.4 - Energie & Vermogen": [
        {
            "q": "Een apparaat van 1500W draait 3 uur per dag, 30 dagen per maand. Bereken het energieverbruik in kWh.",
            "given": "P = 1500W, t = 3h/dag × 30 dagen",
            "find": "E_maand = ? (kWh)",
            "space": 6
        },
        {
            "q": "Een motor trekt 2300W uit het net en levert 2000W mechanisch vermogen. Bereken het rendement.",
            "given": "P_in = 2300W, P_out = 2000W",
            "find": "η = ?",
            "space": 5
        },
    ],

    "H 7.8 - RLC Schakelingen": [
        {
            "q": "Serie RLC: R=10Ω, X_L=20Ω, X_C=15Ω. Bereken de impedantie (magnitude en fase).",
            "given": "R = 10Ω, X_L = 20Ω, X_C = 15Ω",
            "find": "|Z| = ?, φ = ?",
            "space": 7
        },
        {
            "q": "Een condensator van 10μF bij 50Hz. Bereken de capacitieve reactantie.",
            "given": "C = 10μF, f = 50Hz",
            "find": "X_C = ?",
            "space": 6
        },
    ],

    "H 9.7 - Complexe Impedantie": [
        {
            "q": "Complexe impedantie Z = 30 + j40 Ω. Bereken de magnitude en fasehoek.",
            "given": "Z = 30 + j40 Ω",
            "find": "|Z| = ?, φ = ?",
            "space": 6
        },
        {
            "q": "Vermenigvuldig 5∠30° × 4∠60° in polaire vorm.",
            "given": "Z₁ = 5∠30°, Z₂ = 4∠60°",
            "find": "Z₁ × Z₂ = ?",
            "space": 5
        },
    ],

    "H 11.7 - Vermogen AC": [
        {
            "q": "Motor: U=400V, I=10A, cos φ=0,8. Bereken P, Q en S.",
            "given": "U = 400V, I = 10A, cos φ = 0,8",
            "find": "P = ?, Q = ?, S = ?",
            "space": 8
        },
    ],
}

def generate_worksheet_html(chapter, questions):
    """Generate HTML for a single worksheet"""

    html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oefenblad - {chapter}</title>
    <style>
        @media print {{
            body {{
                background: white !important;
                padding: 0;
                margin: 0;
            }}
            .no-print {{
                display: none !important;
            }}
            .question {{
                page-break-inside: avoid;
            }}
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}

        body {{
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }}

        .worksheet {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        .header {{
            text-align: center;
            border-bottom: 3px solid #333;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}

        .header h1 {{
            font-size: 2em;
            color: #333;
            margin-bottom: 10px;
        }}

        .header .subtitle {{
            color: #666;
            font-size: 1.1em;
        }}

        .student-info {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 5px;
        }}

        .info-field {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .info-field label {{
            font-weight: bold;
            min-width: 60px;
        }}

        .info-field .line {{
            flex: 1;
            border-bottom: 1px solid #333;
            height: 25px;
        }}

        .question {{
            margin-bottom: 40px;
            padding: 20px;
            border: 2px solid #ddd;
            border-radius: 8px;
        }}

        .question-number {{
            background: #667eea;
            color: white;
            padding: 8px 15px;
            border-radius: 5px;
            display: inline-block;
            margin-bottom: 15px;
            font-weight: bold;
        }}

        .question-text {{
            font-size: 1.1em;
            margin-bottom: 15px;
            line-height: 1.6;
        }}

        .given-find {{
            background: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #667eea;
            margin-bottom: 15px;
        }}

        .given-find strong {{
            color: #667eea;
        }}

        .answer-space {{
            border: 2px dashed #ddd;
            min-height: 150px;
            padding: 15px;
            background: #fafafa;
        }}

        .answer-label {{
            font-weight: bold;
            color: #666;
            margin-bottom: 10px;
        }}

        .grid-lines {{
            background-image: linear-gradient(#ddd 1px, transparent 1px);
            background-size: 100% 25px;
        }}

        .footer {{
            text-align: center;
            color: #999;
            font-size: 0.9em;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #ddd;
        }}

        .print-btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.1em;
            display: block;
            margin: 20px auto;
        }}

        .print-btn:hover {{
            background: #5568d3;
        }}
    </style>
</head>
<body>
    <button class="print-btn no-print" onclick="window.print()">🖨️ Print Oefenblad</button>

    <div class="worksheet">
        <div class="header">
            <h1>📝 Oefenblad</h1>
            <div class="subtitle">{chapter}</div>
        </div>

        <div class="student-info">
            <div class="info-field">
                <label>Naam:</label>
                <div class="line"></div>
            </div>
            <div class="info-field">
                <label>Datum:</label>
                <div class="line"></div>
            </div>
        </div>

"""

    for i, q in enumerate(questions, 1):
        space_height = q.get('space', 6) * 25  # Lines × 25px

        html += f"""
        <div class="question">
            <div class="question-number">Vraag {i}</div>

            <div class="question-text">{q['q']}</div>

            <div class="given-find">
                <div><strong>Gegeven:</strong> {q['given']}</div>
                <div style="margin-top: 8px;"><strong>Gevraagd:</strong> {q['find']}</div>
            </div>

            <div class="answer-label">Uitwerking:</div>
            <div class="answer-space grid-lines" style="min-height: {space_height}px;"></div>
        </div>
"""

    html += f"""
        <div class="footer">
            NCOI Energietechniek Oefenblad | {chapter} | © 2025<br>
            <small>Voor antwoorden, zie de opgaven in de study guide</small>
        </div>
    </div>
</body>
</html>"""

    return html

def generate_all_worksheets():
    """Generate all worksheets"""

    print("📝 Genereren van practice worksheets...")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total_generated = 0

    for chapter, questions in WORKSHEETS.items():
        # Generate filename
        safe_name = chapter.replace(" ", "-").replace("/", "-")
        filename = OUTPUT_DIR / f"worksheet-{safe_name}.html"

        # Generate HTML
        html = generate_worksheet_html(chapter, questions)

        # Write file
        filename.write_text(html, encoding='utf-8')

        total_generated += 1
        print(f"✅ {chapter}: {len(questions)} vragen → {filename.name}")

    # Generate master index
    generate_worksheet_index(total_generated)

    print(f"\n🎉 Klaar!")
    print(f"📊 Totaal: {total_generated} worksheets gegenereerd")
    print(f"📁 Locatie: {OUTPUT_DIR}")
    print(f"\n💡 Open INDEX.html om alle worksheets te zien")

def generate_worksheet_index(total):
    """Generate index page for all worksheets"""

    html = """<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Practice Worksheets - Index</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        h1 {
            color: #1e3c72;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 40px;
            font-size: 1.1em;
        }

        .info-box {
            background: #e8f5e9;
            border-left: 5px solid #4caf50;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }

        .worksheet-grid {
            display: grid;
            gap: 15px;
        }

        .worksheet-card {
            background: #f5f5f5;
            border: 2px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            transition: all 0.3s;
        }

        .worksheet-card:hover {
            border-color: #667eea;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102,126,234,0.3);
        }

        .worksheet-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }

        .chapter-name {
            font-size: 1.3em;
            font-weight: bold;
            color: #667eea;
        }

        .question-count {
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }

        .worksheet-link {
            background: #667eea;
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            transition: all 0.3s;
        }

        .worksheet-link:hover {
            background: #5568d3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Practice Worksheets</h1>
        <div class="subtitle">Print-ready oefenbladen voor NCOI Energietechniek</div>

        <div class="info-box">
            <strong>📋 Hoe te gebruiken:</strong><br>
            1. Klik op een worksheet om te openen<br>
            2. Print het worksheet (Ctrl+P → Save as PDF)<br>
            3. Los de opgaven op papier op<br>
            4. Check antwoorden in de study guide<br><br>
            <strong>💡 Perfect voor:</strong> Offline studie, exam prep, handmatige oefening
        </div>

        <div class="worksheet-grid">
"""

    for chapter, questions in WORKSHEETS.items():
        safe_name = chapter.replace(" ", "-").replace("/", "-")
        filename = f"worksheet-{safe_name}.html"

        html += f"""
            <div class="worksheet-card">
                <div class="worksheet-header">
                    <div class="chapter-name">{chapter}</div>
                    <div class="question-count">{len(questions)} vragen</div>
                </div>
                <a href="{filename}" class="worksheet-link">📄 Open Worksheet</a>
            </div>
"""

    html += f"""
        </div>

        <div style="text-align: center; margin-top: 40px; color: #999;">
            <p>Totaal: {total} worksheets beschikbaar</p>
            <p style="margin-top: 10px; font-size: 0.9em;">NCOI Energietechniek © 2025</p>
        </div>
    </div>
</body>
</html>"""

    index_file = OUTPUT_DIR / "INDEX.html"
    index_file.write_text(html, encoding='utf-8')
    print(f"✅ Index gegenereerd: {index_file}")

if __name__ == "__main__":
    generate_all_worksheets()
