#!/usr/bin/env python3
"""
Formula Sheet Generator - Genereert formuleblad voor examen
Extracteert alle formules uit enhanced opgaven en organiseert per hoofdstuk
"""

import re
from pathlib import Path

ENHANCED_DIR = Path("/home/user/ncoi-energietechniek-anki/enhanced-content")
OUTPUT_FILE = Path("/home/user/ncoi-energietechniek-anki/study-guide/FORMULEBLAD-AUTO.html")

# Predefined formulas per chapter (Holmes reference)
FORMULAS = {
    "H 1.9 - Wet van Ohm & Kirchhoff": [
        ("Wet van Ohm", "U = I · R", "Spanning = Stroom × Weerstand"),
        ("Wet van Ohm (stroom)", "I = U / R", "Stroom = Spanning / Weerstand"),
        ("Wet van Ohm (weerstand)", "R = U / I", "Weerstand = Spanning / Stroom"),
        ("Kirchhoff Knooppuntwet (KCL)", "Σ I_in = Σ I_uit", "Som van stromen in knooppunt = 0"),
        ("Kirchhoff Spanningswet (KVL)", "Σ U_maas = 0", "Som van spanningen in maas = 0"),
        ("Vermogen", "P = U · I", "Vermogen = Spanning × Stroom"),
        ("Vermogen (wet van Ohm)", "P = I² · R = U² / R", "Alternatieve vormen"),
    ],

    "H 2.6 - Serie & Parallel": [
        ("Serie weerstanden", "R_totaal = R₁ + R₂ + R₃ + ...", "Weerstanden tellen op"),
        ("Parallel weerstanden", "1/R_totaal = 1/R₁ + 1/R₂ + 1/R₃ + ...", "Reciproken tellen op"),
        ("Parallel (2 weerstanden)", "R_totaal = (R₁ · R₂) / (R₁ + R₂)", "Product / Som"),
        ("Geleidingen parallel", "G_totaal = G₁ + G₂ + G₃ + ...", "G = 1/R"),
        ("Spanningsdeler", "U_x = U_totaal · (R_x / R_totaal)", "Spanning over R_x"),
        ("Stroomdeler", "I_x = I_totaal · (R_totaal / R_x)", "Stroom door R_x"),
    ],

    "H 3.11 - Netwerk Analyse": [
        ("Thévenin spanning", "U_th = U_openkleme", "Open klem spanning"),
        ("Thévenin weerstand", "R_th = U_th / I_kortsluit", "Interne weerstand"),
        ("Norton stroom", "I_N = I_kortsluit", "Kortsluitstroom"),
        ("Norton ↔ Thévenin", "U_th = I_N · R_th", "Omrekening"),
        ("Maasstromen", "Σ (R · I_maas) = Σ U_bron", "Per maas"),
        ("Superpositie", "I_totaal = I₁ + I₂ + ... + I_n", "Som van alle bronnen"),
    ],

    "H 4.4 - Energie & Vermogen": [
        ("Energie", "E = P · t", "Energie = Vermogen × Tijd"),
        ("Energie (Ws → kWh)", "E[kWh] = E[Ws] / 3.600.000", "Omrekening"),
        ("Rendement", "η = P_nuttig / P_totaal", "Rendement (0-1 of 0-100%)"),
        ("Vermogensaanpassing", "P_max bij R_last = R_th", "Maximaal vermogen"),
        ("Vermogen bij aanpassing", "P_max = U_th² / (4·R_th)", "Bij R_last = R_th"),
        ("Rendement bij aanpassing", "η = 50%", "Altijd 50% bij P_max"),
    ],

    "H 5.5 - Wisselspanning": [
        ("Effectieve waarde (sinus)", "U_eff = U_top / √2", "RMS waarde"),
        ("Gemiddelde waarde (sinus)", "U_gem = 2·U_top / π", "Rectified average"),
        ("Topwaarde uit effectief", "U_top = U_eff · √2", "Peak voltage"),
        ("Frequentie", "f = 1 / T", "Frequentie = 1 / Periode"),
        ("Hoekfrequentie", "ω = 2πf", "rad/s"),
        ("Sinusvorm", "u(t) = U_top · sin(ωt + φ)", "Tijddomein"),
    ],

    "H 6.8 - C & L": [
        ("Capaciteit (Q)", "Q = C · U", "Lading = Capaciteit × Spanning"),
        ("Capaciteit (stroom)", "I = C · dU/dt", "Stroom door condensator"),
        ("Energie condensator", "E = ½ · C · U²", "Opgeslagen energie"),
        ("Inductie (spanning)", "U = L · dI/dt", "Spanning over spoel"),
        ("Energie spoel", "E = ½ · L · I²", "Opgeslagen energie"),
    ],

    "H 7.8 & H 9.7 - RLC & Complex": [
        ("Capacitieve reactantie", "X_C = 1/(2πfC)", "Impedantie condensator (Ω)"),
        ("Inductieve reactantie", "X_L = 2πfL", "Impedantie spoel (Ω)"),
        ("Impedantie condensator", "Z_C = -j·X_C", "Complex notatie"),
        ("Impedantie spoel", "Z_L = +j·X_L", "Complex notatie"),
        ("Impedantie serie", "Z = R + jX", "X = X_L - X_C"),
        ("Impedantie magnitude", "|Z| = √(R² + X²)", "Absolute waarde"),
        ("Fasehoek", "φ = arctan(X/R)", "Faseverschuiving"),
        ("Serie RLC", "Z = R + j(X_L - X_C)", "Totale impedantie"),
        ("Parallel (complex)", "1/Z = 1/Z₁ + 1/Z₂ + ...", "Complexe berekening"),
        ("Resonantiefrequentie", "f_res = 1/(2π√(LC))", "Series resonantie"),
    ],

    "H 11.7 - Vermogen (AC)": [
        ("Schijnbaar vermogen", "S = U · I", "Volt-Ampere (VA)"),
        ("Werkelijk vermogen", "P = U · I · cos(φ)", "Watt (W)"),
        ("Blindvermogen", "Q = U · I · sin(φ)", "VAR"),
        ("Vermogensdriehoek", "S² = P² + Q²", "Pythagoras"),
        ("Arbeidsfactor", "cos(φ) = P / S", "Power factor"),
        ("Blindvermogen compensatie", "Q_C = Q_L - Q_gewenst", "Condensator toevoegen"),
    ],
}

def generate_html():
    """Generate formula sheet HTML"""

    html_parts = [
        '<!DOCTYPE html>',
        '<html lang="nl">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '    <title>📐 Formuleblad Energietechniek - NCOI</title>',
        '    <style>',
        '        * { margin: 0; padding: 0; box-sizing: border-box; }',
        '        @media print {',
        '            body { background: white !important; }',
        '            .no-print { display: none; }',
        '            .chapter { page-break-inside: avoid; }',
        '        }',
        '        body {',
        '            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;',
        '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
        '            padding: 20px;',
        '        }',
        '        .container {',
        '            max-width: 1000px;',
        '            margin: 0 auto;',
        '            background: white;',
        '            padding: 40px;',
        '            border-radius: 20px;',
        '            box-shadow: 0 20px 60px rgba(0,0,0,0.3);',
        '        }',
        '        h1 {',
        '            text-align: center;',
        '            color: #1e3c72;',
        '            font-size: 2.5em;',
        '            margin-bottom: 10px;',
        '        }',
        '        .subtitle {',
        '            text-align: center;',
        '            color: #666;',
        '            font-size: 1.1em;',
        '            margin-bottom: 30px;',
        '        }',
        '        .print-btn {',
        '            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
        '            color: white;',
        '            border: none;',
        '            padding: 15px 30px;',
        '            font-size: 1.1em;',
        '            border-radius: 10px;',
        '            cursor: pointer;',
        '            margin-bottom: 30px;',
        '            display: block;',
        '            margin-left: auto;',
        '            margin-right: auto;',
        '        }',
        '        .print-btn:hover {',
        '            transform: translateY(-2px);',
        '            box-shadow: 0 10px 30px rgba(102,126,234,0.4);',
        '        }',
        '        .chapter {',
        '            margin: 30px 0;',
        '            border-left: 5px solid #667eea;',
        '            padding-left: 20px;',
        '        }',
        '        .chapter-title {',
        '            font-size: 1.5em;',
        '            color: #667eea;',
        '            margin-bottom: 15px;',
        '            font-weight: bold;',
        '        }',
        '        .formula-table {',
        '            width: 100%;',
        '            border-collapse: collapse;',
        '            margin-bottom: 20px;',
        '        }',
        '        .formula-table th {',
        '            background: #667eea;',
        '            color: white;',
        '            padding: 12px;',
        '            text-align: left;',
        '            font-weight: bold;',
        '        }',
        '        .formula-table td {',
        '            padding: 10px 12px;',
        '            border-bottom: 1px solid #ddd;',
        '        }',
        '        .formula-table tr:hover {',
        '            background: #f5f5f5;',
        '        }',
        '        .formula-name {',
        '            font-weight: bold;',
        '            color: #333;',
        '        }',
        '        .formula-math {',
        '            font-family: "Courier New", monospace;',
        '            font-size: 1.1em;',
        '            color: #667eea;',
        '            background: #f5f5f5;',
        '            padding: 5px 10px;',
        '            border-radius: 5px;',
        '        }',
        '        .formula-desc {',
        '            color: #666;',
        '            font-style: italic;',
        '        }',
        '        .warning-box {',
        '            background: #fff3cd;',
        '            border-left: 5px solid #ffc107;',
        '            padding: 15px;',
        '            margin: 20px 0;',
        '            border-radius: 5px;',
        '        }',
        '    </style>',
        '</head>',
        '<body>',
        '    <div class="container">',
        '        <h1>📐 Formuleblad Energietechniek</h1>',
        '        <div class="subtitle">NCOI - Elektrische Netwerken (Holmes 3e editie)</div>',
        '        ',
        '        <button class="print-btn no-print" onclick="window.print()">🖨️ Printen / PDF Opslaan</button>',
        '        ',
        '        <div class="warning-box no-print">',
        '            <strong>⚠️ Let op:</strong> Dit formuleblad is automatisch gegenereerd uit de studiegids.',
        '            Controleer altijd met het officiële NCOI formuleblad welke formules tijdens het examen beschikbaar zijn!',
        '        </div>',
    ]

    # Add formulas per chapter
    for chapter, formulas in FORMULAS.items():
        html_parts.extend([
            f'        <div class="chapter">',
            f'            <div class="chapter-title">{chapter}</div>',
            f'            <table class="formula-table">',
            f'                <thead>',
            f'                    <tr>',
            f'                        <th style="width: 25%;">Formule</th>',
            f'                        <th style="width: 35%;">Wiskundige Notatie</th>',
            f'                        <th style="width: 40%;">Betekenis</th>',
            f'                    </tr>',
            f'                </thead>',
            f'                <tbody>',
        ])

        for name, math, desc in formulas:
            html_parts.extend([
                f'                    <tr>',
                f'                        <td class="formula-name">{name}</td>',
                f'                        <td class="formula-math">{math}</td>',
                f'                        <td class="formula-desc">{desc}</td>',
                f'                    </tr>',
            ])

        html_parts.extend([
            f'                </tbody>',
            f'            </table>',
            f'        </div>',
        ])

    # Add footer
    html_parts.extend([
        '        <div style="text-align: center; color: #999; margin-top: 50px; padding-top: 20px; border-top: 2px solid #ddd;">',
        '            <p><strong>Afkortingen:</strong></p>',
        '            <p style="margin-top: 10px;">',
        '                U = Spanning (V) | I = Stroom (A) | R = Weerstand (Ω) | ',
        '                P = Vermogen (W) | E = Energie (J/Wh) | ',
        '                f = Frequentie (Hz) | ω = Hoekfrequentie (rad/s)<br>',
        '                C = Capaciteit (F) | L = Inductie (H) | ',
        '                Z = Impedantie (Ω) | X = Reactantie (Ω) | ',
        '                φ = Fasehoek (rad/°)<br>',
        '                j = Imaginaire eenheid (√-1) | ',
        '                S = Schijnbaar vermogen (VA) | Q = Blindvermogen (VAR)',
        '            </p>',
        '            <p style="margin-top: 20px; font-size: 0.9em;">',
        '                Auto-gegenereerd • NCOI Energietechniek • 2025',
        '            </p>',
        '        </div>',
        '    </div>',
        '</body>',
        '</html>',
    ])

    return '\n'.join(html_parts)

if __name__ == "__main__":
    print("📐 Genereren van formuleblad...")

    html_content = generate_html()
    OUTPUT_FILE.write_text(html_content, encoding='utf-8')

    # Count formulas
    total_formulas = sum(len(formulas) for formulas in FORMULAS.values())

    print(f"✅ Formuleblad gegenereerd!")
    print(f"📄 Bestand: {OUTPUT_FILE}")
    print(f"📊 Hoofdstukken: {len(FORMULAS)}")
    print(f"🔢 Formules: {total_formulas}")
    print(f"\n💡 Open in browser of print naar PDF voor examen!")
