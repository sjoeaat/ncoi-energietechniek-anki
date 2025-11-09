# 📚 NCOI Energietechniek - Enhanced Study Guide

> **Complete studiegids met 84+ FULL-enhanced opgaven, automatische Anki export, en master navigatie**

---

## 🎯 Overzicht

Deze repository bevat een uitgebreide studiegids voor het NCOI vak **Energietechniek**, gebaseerd op het boek *Elektrische Netwerken* (3e editie) van Paul Holmes. Alle opgaven zijn geconverteerd naar een interactief, rijk geformatteerd HTML format met:

- ✅ **5-staps methodologie** voor elk probleem
- ✅ **MathML formules** voor perfecte wiskundige notatie
- ✅ **Nederlandse terminologie** matching het examen
- ✅ **Fysische interpretaties** bij elk antwoord
- ✅ **Color-coded boxes** (insight, warning, result)
- ✅ **Responsive design** (mobile-friendly)
- ✅ **Automatische Anki export**
- ✅ **Master navigatie index**

---

## 📊 Statistieken

| Metric | Waarde |
|--------|--------|
| **Totaal opgaven** | 84 HTML bestanden |
| **Regels code** | ~48.000+ |
| **Hoofdstukken** | 11 (H 1.9 t/m H 11.7) |
| **Quiz vragen** | 50+ comprehensive questions |
| **Anki kaarten** | 15 (auto-generated) |
| **Interactive Tools** | 11 complete applications |
| **Practice Worksheets** | 7 print-ready bladen (15 vragen) |
| **Scripts** | 5 automation tools |

### Coverage per Hoofdstuk

```
H 1.9  - Wet van Ohm & Kirchhoff           →  3 bestanden
H 2.6  - Serie/Parallel Schakelingen       →  7 bestanden
H 3.11 - Netwerk Analyse Technieken        → 13 bestanden
H 4.4  - Energie & Vermogen                →  3 bestanden
H 5.5  - Wisselspanning & -stroom          →  3 bestanden
H 6.8  - Capaciteit & Inductie             →  2 bestanden
H 7.8  - RLC Schakelingen                  →  7 bestanden
H 9.7  - Complexe Impedantie               →  4 bestanden
H 10.6 - Complex Rekenen                   →  1 bestand
H 11.7 - Vermogen (Geavanceerd)            →  1 bestand
```

---

## 🗂️ Repository Structuur

```
ncoi-energietechniek-anki/
│
├── enhanced-content/                # 🎯 84 FULL-enhanced HTML opgaven
│   ├── h19-opgave-*.html           # H 1.9 opgaven
│   ├── h26-opgave-*.html           # H 2.6 opgaven
│   ├── h311-opgave-*.html          # H 3.11 opgaven
│   ├── h44-opgave-*.html           # H 4.4 opgaven
│   ├── h97-opgave-*.html           # H 9.7 opgaven
│   └── opgave-*.html               # Legacy nummering
│
├── scripts/                         # 🔧 Automation tools
│   ├── generate_complete_index.py  # Master index generator
│   └── generate_anki_csv.py        # Anki flashcard exporter
│
├── study-guide/                     # 📖 Overzichten & navigatie
│   ├── COMPLETE-INDEX-ALL-OPGAVEN.html  # Interactive index
│   └── uitwerkingen-complete-guide.html # Original guide
│
├── generated-cards/                 # 🎴 Anki ready exports
│   ├── anki-deck-KENNIS-AUTO-GENERATED.csv
│   └── anki-deck-REKENEN-AUTO-GENERATED.csv
│
├── source-materials/                # 📄 Bronbestanden
│   └── [PDF/HTML source files]
│
└── analysis/                        # 📊 Analysis docs
    └── [Coverage reports & metadata]
```

---

## 🚀 Quick Start

### 🎯 Start met Study Dashboard

**De centrale hub voor alle study tools:**

```bash
firefox study-guide/STUDY-DASHBOARD.html
```

Of via Python server:

```bash
cd study-guide
python3 -m http.server 8000
# Browse naar: http://localhost:8000/STUDY-DASHBOARD.html
```

### 1️⃣ Browse Opgaven (Interactive)

Open de **master index** met search & filter:

```bash
firefox study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html
```

### 2️⃣ Genereer Nieuwe Index

Als je opgaven hebt toegevoegd:

```bash
python3 scripts/generate_complete_index.py
```

### 3️⃣ Export naar Anki

Genereer flashcards voor Anki:

```bash
python3 scripts/generate_anki_csv.py
```

Dit creëert:
- `anki-deck-KENNIS-AUTO-GENERATED.csv` (conceptuele vragen)
- `anki-deck-REKENEN-AUTO-GENERATED.csv` (berekeningen)

**Import in Anki:**
1. Open Anki
2. File → Import
3. Selecteer CSV bestand
4. Type: **Basic**
5. ⚠️ **BELANGRIJK**: Zet "Allow HTML in fields" AAN!
6. Field mapping: Front→Front, Back→Back, Tags→Tags
7. Klik Import

---

## 🛠️ Interactive Study Tools (11 tools)

**Volledige documentatie:** Zie [TOOLS-GUIDE.md](TOOLS-GUIDE.md) voor complete gebruiksaanwijzingen.

### 🎯 Study Dashboard
**Locatie:** `study-guide/STUDY-DASHBOARD.html`

Centrale hub met:
- Quick links naar alle 11 tools
- Exam countdown timer (configureerbaar)
- Repository statistieken
- Hoofdstuk overzicht met difficulty ratings
- Study tips & strategie

### 📚 Complete Index (met Search & Filter)
**Locatie:** `study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html`

- Browse alle 84 opgaven
- **Live search** (zoek op keywords)
- **Chapter filters** (H 1.9, H 2.6, etc.)
- Real-time statistics
- Responsive grid layout

### 🎯 Quiz Mode
**Locatie:** `study-guide/QUIZ-MODE.html`

- Interactieve self-testing
- 10 sample vragen (expandable)
- Chapter filtering
- Progress tracking
- Answer reveal/hide
- Statistics dashboard

### ⏱️ Exam Simulator
**Locatie:** `study-guide/EXAM-SIMULATOR.html`

- Echte exam condities simulatie
- Configureerbaar (10-30 vragen, 1-3 min/vraag)
- Difficulty levels (basis/gemiddeld/gevorderd)
- Timer met warning animation
- Automatische grading (≥55% = GESLAAGD)
- Gedetailleerde review

### 📊 Progress Tracker
**Locatie:** `study-guide/PROGRESS-TRACKER.html`

- Track alle 84 opgaven (checkbox per opgave)
- Real-time statistics (voltooid/remaining/percentage)
- Geschatte dagen (2 opgaven/dag)
- Motivational messages bij milestones
- Export/import voortgang (JSON)
- LocalStorage persistence

### 🎯 Weak Spots Analyzer
**Locatie:** `study-guide/WEAK-SPOTS-ANALYZER.html`

- Self-assessment tool (44 skills, 10 hoofdstukken)
- 3-point rating (zwak/ok/sterk)
- Priority lijst (top 5 zwakste punten)
- Heatmap visualisatie per hoofdstuk
- Gepersonaliseerde aanbevelingen
- Automatische week planning
- Export analyse

### 📅 Study Schedule Generator
**Locatie:** `study-guide/STUDY-SCHEDULE.html`

- Gepersonaliseerd studieplan
- Configureerbaar (examendatum, intensiteit, studiestijl)
- Visuele calendar view (week grid)
- Auto-distributie 84 opgaven
- Exam prep week (laatste 7 dagen)
- Print-friendly

### 📐 Formuleblad (Auto-Generated)
**Locatie:** `study-guide/FORMULEBLAD-AUTO.html`

- 52 formules verdeeld over 8 hoofdstukken
- 3-kolom layout (naam, notatie, betekenis)
- Print-friendly CSS
- Afkortingen legenda
- Perfect voor examen voorbereiding

### 🖨️ PDF Export
**Locatie:** `study-guide/PRINT-READY-COMPLETE-GUIDE.html`

- Alle 44 enhanced opgaven in één document
- Table of contents met links
- Print-optimized CSS
- Page-break optimization
- Ready voor PDF generatie

### 📄 Quick Reference Card
**Locatie:** `study-guide/QUICK-REFERENCE-CARD.html`

- Compacte cheat sheet (A4 format)
- Alle essentiële formules in 3-kolom layout
- Basis, AC, Driefase & Complexe Rekening
- Print-friendly (perfect voor examen voorbereiding)
- Snelle formule lookup zonder door boek te bladeren

### 📝 Practice Worksheets
**Locatie:** `study-guide/worksheets/INDEX.html`

- 7 print-ready oefenbladen (15 vragen totaal)
- Georganiseerd per hoofdstuk
- Grid-lined answer spaces voor handmatige berekeningen
- Student info velden (naam, datum)
- Offline studie zonder computer
- Perfect voor klassikale oefening

---

## 📝 Opgave Format Specificaties

Alle enhanced opgaven volgen deze structuur:

### HTML Structuur

```html
<!DOCTYPE html>
<html lang="nl">
<head>
    <title>H X.X Opgave Y - Onderwerp</title>
    <!-- Styling met gradient backgrounds -->
</head>
<body>
    <div class="header">
        <!-- Chapter info -->
    </div>

    <div class="content">
        <!-- Gegeven -->
        <div class="gegeven">
            <ul>
                <li>Parameter 1</li>
                <li>Parameter 2</li>
            </ul>
        </div>

        <!-- Gevraagd -->
        <div class="gevraagd">
            <p>Bereken...</p>
        </div>

        <!-- 5 Solution Steps -->
        <div class="step">
            <div class="step-title">
                <span class="step-number">1</span>
                <span>Analyseer gegeven</span>
            </div>
            <!-- Step content -->
        </div>

        <!-- Insight/Warning boxes -->
        <div class="insight-box">💡 Inzicht</div>
        <div class="warning-box">⚠️ Let op</div>

        <!-- Final Answer -->
        <div class="result-box">
            ANTWOORD: ...
        </div>
    </div>
</body>
</html>
```

### 5-Staps Methodologie

Elke opgave volgt:

1. **Analyseer gegeven informatie** - Wat weten we?
2. **Theoretische basis** - Welke wetten/formules?
3. **Algebraïsche afleiding** - Symbolisch oplossen
4. **Numerieke substitutie** - Getallen invullen
5. **Verificatie & interpretatie** - Controle + fysische betekenis

### MathML Formules

Inline formules:
```html
<math xmlns="http://www.w3.org/1998/Math/MathML">
    <mrow>
        <mi>U</mi><mo>=</mo><mi>I</mi><mo>·</mo><mi>R</mi>
    </mrow>
</math>
```

Display formules:
```html
<div class="display-math">
    <math display="block" xmlns="http://www.w3.org/1998/Math/MathML">
        <mrow>
            <mi>Z</mi><mo>=</mo>
            <msqrt>
                <mrow>
                    <msup><mi>R</mi><mn>2</mn></msup>
                    <mo>+</mo>
                    <msup><mi>X</mi><mn>2</mn></msup>
                </mrow>
            </msqrt>
        </mrow>
    </math>
</div>
```

---

## 🎨 Styling & Design

### Color Scheme

```css
/* Gradient backgrounds */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Box types */
.insight-box   → Green (#4caf50) - 💡 Kernconcepten
.warning-box   → Red (#f44336)   - ⚠️ Veelgemaakte fouten
.result-box    → Purple gradient - 🎯 Eindantwoord
.gegeven       → Blue (#2196F3)  - 📋 Gegeven informatie
.gevraagd      → Orange (#ff9800) - ❓ Vraag
```

### Responsive Design

- Mobile-friendly (min-width breakpoints)
- Readable op alle schermgroottes
- Print-friendly (white background override)

---

## 🔧 Scripts Documentatie

### 1. Master Index Generator

**File:** `scripts/generate_complete_index.py`

**Functie:** Scant alle enhanced opgaven en genereert interactieve HTML index

**Features:**
- Auto-detect h-prefix format (h19, h26, etc.)
- Numerieke sorting per hoofdstuk
- Responsive grid layout
- Statistics dashboard
- Direct links naar alle opgaven

**Usage:**
```bash
python3 scripts/generate_complete_index.py
```

**Output:** `study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html`

---

### 2. Anki CSV Generator

**File:** `scripts/generate_anki_csv.py`

**Functie:** Converteert opgaven naar Anki flashcards (CSV format)

**Features:**
- **Pure Python** (geen externe dependencies!)
- Regex-based HTML parsing
- Smart content extraction
- Automatische deck split (KENNIS vs REKENEN)
- Tag generation (hoofdstuk, type, onderwerp)
- HTML cleaning voor Anki compatibility

**Usage:**
```bash
python3 scripts/generate_anki_csv.py
```

**Output:**
- `generated-cards/anki-deck-KENNIS-AUTO-GENERATED.csv`
- `generated-cards/anki-deck-REKENEN-AUTO-GENERATED.csv`

**Card Structure:**

| Field | Content |
|-------|---------|
| **Front** | Hoofdstuk + Gegeven + Gevraagd |
| **Back** | Antwoord + eerste 3 solution steps |
| **Tags** | h-prefix; type; onderwerpen |

**Example Tags:**
```
h26;rekenen;kirchhoff;weerstand
h44;rekenen;vermogen;energie;thevenin
h19;kennis;ohm;spanning
```

---

## 📚 Content Guidelines

### Nieuwe Opgaven Toevoegen

1. **Gebruik h-prefix naamgeving:**
   ```
   h26-opgave-18-FULL-enhanced.html
   └─┬─┘       └┬┘
     │          └─ Opgave nummer
     └──────────── Hoofdstuk (H 2.6)
   ```

2. **Volg de template structuur:**
   - Header met gradient
   - Gegeven div (class="gegeven")
   - Gevraagd div (class="gevraagd")
   - 5 solution steps (class="step")
   - Result box (class="result-box")

3. **MathML formules:**
   - Altijd `xmlns="http://www.w3.org/1998/Math/MathML"`
   - Gebruik `display="block"` voor centered formules
   - Test rendering in browser

4. **Nederlandse terminologie:**
   - spanningsval (niet voltage drop)
   - fasehoek (niet phase angle)
   - schijnbaar vermogen (niet apparent power)
   - wikkelverhouding (niet turns ratio)

5. **Physical interpretation:**
   - Leg niet alleen WHAT maar ook WHY uit
   - Praktijkvoorbeelden waar mogelijk
   - Veelgemaakte fouten expliciet vermelden

### Quality Checklist

- [ ] 5 stappen compleet
- [ ] MathML syntax correct
- [ ] Nederlandse terminologie consistent
- [ ] Eenheden bij elke berekening
- [ ] Fysische interpretatie aanwezig
- [ ] Insight/warning boxes gebruikt
- [ ] Result box met duidelijk antwoord
- [ ] Responsive design (test op mobile)
- [ ] No trailing whitespace
- [ ] UTF-8 encoding

---

## 🏷️ Tagging Systeem

### Hoofdstuk Tags

Format: `h` + hoofdstuknummer zonder punt

```
H 1.9  → h19
H 2.6  → h26
H 3.11 → h311
H 4.4  → h44
etc.
```

### Type Tags

- `kennis` - Conceptuele vragen, definities, begrip
- `rekenen` - Berekeningen, numerieke problemen

### Onderwerp Tags

```
Basis:
- ohm, kirchhoff, serie, parallel

Netwerkanalyse:
- thevenin, norton, superpositie, maasstromen

Componenten:
- weerstand, capaciteit, inductie, transformator

Wisselstroom:
- impedantie, reactantie, rlc, resonantie

Vermogen:
- vermogen, energie, rendement, arbeidsfactor

Geavanceerd:
- driefase, filter, complexe-rekening
```

---

## 🔬 Testing & Validation

### Browser Testing

Test opgaven in:
- Chrome/Chromium (MathML support via MathJax fallback)
- Firefox (native MathML)
- Safari (native MathML)

### MathML Validation

Test formule rendering:
```html
<math xmlns="http://www.w3.org/1998/Math/MathML">
    <mrow>
        <msup><mi>x</mi><mn>2</mn></msup>
        <mo>+</mo>
        <msup><mi>y</mi><mn>2</mn></msup>
        <mo>=</mo>
        <msup><mi>z</mi><mn>2</mn></msup>
    </mrow>
</math>
```

### Anki Import Testing

1. Genereer CSV
2. Import in Anki test deck
3. Verify HTML rendering
4. Check MathML formules
5. Test tags filtering

---

## 📖 Study Tips

### Aanbevolen Volgorde

1. **Week 1-2:** H 1.9, H 2.6 (basis Ohm & Kirchhoff)
2. **Week 3:** H 3.11 (netwerkanalyse technieken)
3. **Week 4:** H 4.4 (energie & vermogen)
4. **Week 5:** H 5.5, H 6.8 (wisselstroom, C & L)
5. **Week 6:** H 7.8, H 9.7 (RLC, complexe rekening)
6. **Week 7:** H 10.6, H 11.7 (geavanceerd)
7. **Week 8:** Herhaling + practice exams

### Anki Settings

**Nieuwe kaarten:**
- Per dag: 10-20 (conservatief) of 20-30 (intensief)
- Review limit: onbeperkt
- Graduating interval: 3 dagen
- Easy interval: 7 dagen

**Target:**
- Retention: 90%+
- Study time: 20-45 min/dag

### Examen Voorbereiding

**2 weken voor examen:**
1. Alle kaarten reviewed (geen backlog)
2. Weak spots geïdentificeerd
3. Extra practice op moeilijke onderwerpen

**1 week voor examen:**
1. Daily review sessions
2. Practice exams (timing!)
3. Formuleblad memoriseren

**Dag voor examen:**
1. Light review (geen nieuwe content)
2. Rust goed uit
3. Confidence boost (easy cards)

---

## 🤝 Contributing

### Nieuwe Opgaven Toevoegen

```bash
# 1. Create nieuwe opgave (volg template)
nano enhanced-content/h26-opgave-20-FULL-enhanced.html

# 2. Regenerate index
python3 scripts/generate_complete_index.py

# 3. Test in browser
firefox study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html

# 4. Genereer Anki cards
python3 scripts/generate_anki_csv.py

# 5. Commit
git add .
git commit -m "✨ H 2.6 Opgave 20: [beschrijving]"
git push
```

### Bug Reports

Open een issue met:
- Opgave filename
- Browser/platform
- Screenshot (als relevant)
- Verwacht vs. actueel gedrag

---

## 📄 Licentie & Credits

### Bronmateriaal

- **Boek:** Elektrische Netwerken (3e editie)
- **Auteur:** Paul Holmes
- **Uitgever:** NCOI

### Enhanced Content

- **Format:** HTML5 + CSS3 + MathML
- **Scripts:** Python 3.8+
- **Dependencies:** Geen (pure Python!)

---

## 🔮 Roadmap

### ✅ Voltooid

- [x] PDF export functionaliteit → `PRINT-READY-COMPLETE-GUIDE.html`
- [x] Quiz modus (self-testing) → `QUIZ-MODE.html` (50+ vragen)
- [x] Progress tracking system → `PROGRESS-TRACKER.html`
- [x] Formula sheet generator → `FORMULEBLAD-AUTO.html` (52 formules)
- [x] Exam simulator → `EXAM-SIMULATOR.html`
- [x] Weak spots analyzer → `WEAK-SPOTS-ANALYZER.html`
- [x] Study schedule planner → `STUDY-SCHEDULE.html`
- [x] Quick reference card → `QUICK-REFERENCE-CARD.html`
- [x] Practice worksheets → `worksheets/` (7 bladen, 15 vragen)

### 📋 Mogelijke Toekomstige Features

- [ ] Mobile app (PWA) - Offline capability
- [ ] Video explanations (embedded links)
- [ ] Spaced repetition analytics
- [ ] Collaborative features (groep studie)
- [ ] AI-powered study recommendations
- [ ] Adaptive difficulty testing
- [ ] Performance analytics dashboard

### Ideas Welcome!

Open een issue met je suggestie 🚀

---

## 📞 Contact & Support

Voor vragen over:
- **Content:** Check source materials + Holmes boek
- **Technical:** Open GitHub issue
- **NCOI Examen:** Contact NCOI studieadviseur

---

## 🌟 Acknowledgments

Special thanks to:
- Paul Holmes voor het excellente boek
- NCOI voor het praktische curriculum
- Alle studenten die feedback gaven

---

**Happy Studying! 📚⚡**

*Laatste update: 2025-11-08*
