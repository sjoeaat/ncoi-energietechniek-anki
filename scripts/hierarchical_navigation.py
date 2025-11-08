#!/usr/bin/env python3
"""
Enhanced Navigation - Hiërarchische structuur met hoofdstukken en onderwerpen
"""

# Navigatie structuur met alle 52+ opgaven georganiseerd per hoofdstuk

NAV_HTML_HIERARCHICAL = """
<nav class="nav-sidebar">
    <h3>📑 Opgaven per Hoofdstuk</h3>

    <!-- H 1.9: Basiswetten (Ohm, Kirchhoff) -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 1.9 - Basiswetten (17)</div>
        <ul class="nav-opgaven">
            <li><a href="#h19-opgave-1">1. Wet van Ohm</a></li>
            <li><a href="#h19-opgave-2">2. Wet van Ohm</a></li>
            <li><a href="#h19-opgave-3">3. Kirchhoff knooppunt</a></li>
            <li><a href="#h19-opgave-4">4. Kirchhoff maas</a></li>
            <li><a href="#h19-opgave-5">5. Spanning/polariteit</a></li>
            <li><a href="#h19-opgave-6">6. Spanningsdeling</a></li>
            <li><a href="#h19-opgave-7">7. Stroomdeling</a></li>
            <li><a href="#h19-opgave-8">8. Mixed circuit</a></li>
            <li><a href="#h19-opgave-9">9. Kirchhoff backwards</a></li>
            <li><a href="#h19-opgave-10">10. Polariteit MC</a></li>
            <li><a href="#h19-opgave-11">11. Stroomverdeling</a></li>
            <li><a href="#h19-opgave-12">12. Spanning spanningsbron</a></li>
            <li><a href="#h19-opgave-13">13. KCL direct</a></li>
            <li><a href="#h19-opgave-14">14. Spanning stroombron</a></li>
            <li><a href="#h19-opgave-15">15. Stroom // spanningsbron</a></li>
            <li><a href="#h19-opgave-16">16. Kirchhoff complex</a></li>
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
            <li><a href="#h311-opgave-2a">2a. Vereenvoudig netwerk</a></li>
            <li><a href="#h311-opgave-2b">2b. Vereenvoudig netwerk</a></li>
            <li><a href="#h311-opgave-2c">2c. Vereenvoudig netwerk</a></li>
            <li><a href="#h311-opgave-2d">2d. Vereenvoudig netwerk</a></li>
            <li><a href="#h311-opgave-2e">2e. Vereenvoudig netwerk</a></li>
            <li><a href="#h311-opgave-3">3. Stroom bepalen</a></li>
            <li><a href="#h311-opgave-4">4. Spanning bepalen</a></li>
            <li><a href="#h311-opgave-5">5. Spanningsbron bepalen</a></li>
        </ul>
    </div>

    <!-- H 5.5: Wisselspanning -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 5.5 - Wisselspanning (6)</div>
        <ul class="nav-opgaven">
            <li><a href="#h55-opgave-1">1. Driehoek</a></li>
            <li><a href="#h55-opgave-7">7-9. Effectieve waarden</a></li>
            <li><a href="#h55-opgave-12">12-13. Gemiddelde waarde</a></li>
        </ul>
    </div>

    <!-- H 6.8: Condensator & Spoel -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 6.8 - C & L Basisformules (3)</div>
        <ul class="nav-opgaven">
            <li><a href="#h68-opgave-1">1. Condensator u=kt</a></li>
            <li><a href="#h68-opgave-2">2. Spoel i=kt</a></li>
            <li><a href="#h68-opgave-3">3. Spoel variatie</a></li>
        </ul>
    </div>

    <!-- H 7.8: RLC Schakelingen -->
    <div class="nav-chapter">
        <div class="nav-chapter-header">H 7.8 - RLC Netwerken (14)</div>
        <ul class="nav-opgaven">
            <li><a href="#h78-opgave-1">1. Basis RLC</a></li>
            <li><a href="#h78-opgave-2">2. Wienbrug</a></li>
            <li><a href="#h78-opgave-3">3. L + C||R</a></li>
            <li><a href="#h78-opgave-5">5. C + (C||(L+R))</a></li>
            <li><a href="#h78-opgave-6">6. Impedantie</a></li>
            <li><a href="#h78-opgave-7">7. R + C||L</a></li>
            <li><a href="#h78-opgave-8">8. Gelijke warmte</a></li>
            <li><a href="#h78-opgave-9">9. RC stroombronnen</a></li>
            <li><a href="#h78-opgave-10">10. Onbekende L</a></li>
            <li><a href="#h78-opgave-12">12. Fasor</a></li>
            <li><a href="#h78-opgave-13">13. Scope capaciteit</a></li>
            <li><a href="#h78-opgave-20">20. Extra opgave</a></li>
        </ul>
    </div>

    <div class="nav-footer">
        <small>Totaal: 52+ opgaven | 5 hoofdstukken</small>
    </div>
</nav>
"""

# Enhanced CSS voor hiërarchische navigatie
NAV_CSS_HIERARCHICAL = """
        /* Hiërarchische Navigatie Sidebar */
        .nav-sidebar {
            position: fixed;
            top: 80px;
            right: 20px;
            width: 280px;
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

        /* Hoofdstuk styling */
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

        /* Opgaven lijst */
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

        .nav-opgaven a.active {
            background: #3498db;
            color: white;
        }

        .nav-footer {
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #ecf0f1;
            text-align: center;
            color: #7f8c8d;
        }

        /* Adjust main content to make room for sidebar */
        body {
            margin-right: 320px;
        }

        /* Hide sidebar on small screens */
        @media (max-width: 1400px) {
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

        /* Scrollbar styling voor navigatie */
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

        .nav-sidebar::-webkit-scrollbar-thumb:hover {
            background: #2980b9;
        }
"""

if __name__ == "__main__":
    print("📐 Hiërarchische navigatie HTML en CSS klaar")
    print(f"   - {len([l for l in NAV_HTML_HIERARCHICAL.split('href=') if 'opgave' in l])} navigatielinks")
    print(f"   - 5 hoofdstukken met onderverdeling")
    print(f"   - Responsive design met collapsible chapters")
