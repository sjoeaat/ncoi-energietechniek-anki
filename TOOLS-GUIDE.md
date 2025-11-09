# 🛠️ Study Tools Guide - NCOI Energietechniek

> **Complete documentatie van alle 14 interactieve study tools**

---

## 📖 Overzicht

Deze studiegids bevat een **complete ecosysteem van 14 interactieve tools** om je optimaal voor te bereiden op het NCOI Energietechniek examen.

### Quick Navigation

| Tool | Gebruik | Tijdsinvestering |
|------|---------|------------------|
| [Study Dashboard](#-study-dashboard) | Start hier - central hub | 1 minuut |
| [Complete Index](#-complete-index) | Zoek specifieke opgaven | 5-10 minuten |
| [Quiz Mode](#-quiz-mode) | Test jezelf | 10-20 minuten |
| [Exam Simulator](#%EF%B8%8F-exam-simulator) | Practice onder druk | 20-60 minuten |
| [Progress Tracker](#-progress-tracker) | Track voortgang | Dagelijks 2 minuten |
| [Weak Spots Analyzer](#-weak-spots-analyzer) | Identificeer zwaktes | 20-30 minuten (1x/week) |
| [Study Schedule](#-study-schedule) | Plan je studie | 10 minuten (1x setup) |
| [Formuleblad](#-formuleblad) | Reference & memorisatie | Dagelijks 5-10 minuten |
| [PDF Export](#-pdf-export) | Print studiegids | 1x printen |
| [Quick Reference](#-quick-reference-card) | Formule cheat sheet | 5 minuten (exam prep) |
| [Practice Worksheets](#-practice-worksheets) | Offline oefenen | 30-45 minuten per blad |
| [Formula Quiz](#-formula-quiz) | Formule memorisatie | 10-20 minuten |
| [Study Timer](#%EF%B8%8F-study-timer-pomodoro) | Pomodoro sessies | 25-55 minuten/sessie |
| [Flashcard Generator](#-flashcard-generator) | Fysieke flashcards | 1x printen |

---

## 🎯 Study Dashboard

**Locatie:** `study-guide/STUDY-DASHBOARD.html`

### Wat is het?

De **centrale hub** voor toegang tot alle tools. Dit is je startpunt elke studiesessie.

### Features

✅ **Quick Links** naar alle 14 tools
✅ **Exam Countdown Timer** (configureerbaar)
✅ **Repository Statistieken** (84 opgaven, 11 hoofdstukken, 52 formules)
✅ **Hoofdstuk Overzicht** met difficulty ratings
✅ **Study Tips & Strategie**
✅ **Mobile-friendly design**

### Gebruik

```bash
# Open in browser
firefox study-guide/STUDY-DASHBOARD.html

# Of via HTTP server
cd study-guide
python3 -m http.server 8000
# Navigeer naar: http://localhost:8000/STUDY-DASHBOARD.html
```

### Exam Countdown Setup

1. Klik op **"Stel Examendatum In"**
2. Voer datum in (formaat: `YYYY-MM-DD`, bijv. `2025-12-15`)
3. Dashboard toont nu countdown in dagen
4. Countdown verandert kleur bij < 14 dagen (geel) en < 7 dagen (rood)

---

## 📚 Complete Index

**Locatie:** `study-guide/COMPLETE-INDEX-ALL-OPGAVEN.html`

### Wat is het?

Interactieve index met **84 opgaven** georganiseerd per hoofdstuk, met **live search & filter** functionaliteit.

### Features

✅ **Live Search** (zoek op trefwoorden: "Ohm", "Kirchhoff", "vermogen")
✅ **Chapter Filters** (H 1.9, H 2.6, H 3.11, etc.)
✅ **Real-time Statistics** (X van Y gevonden)
✅ **Auto-hide** empty chapters
✅ **Responsive grid layout**
✅ **Direct links** naar alle opgaven

### Gebruik

**Basis navigatie:**
```
1. Open Complete Index
2. Klik op hoofdstuk filter (bijv. "H 2.6")
3. Of: typ in zoekbalk (bijv. "thevenin")
4. Klik op opgave om te openen
```

**Search Voorbeelden:**
- Zoek "ohm" → Vindt alle Ohm gerelateerde opgaven
- Zoek "multiple choice" → Vindt alle MC vragen
- Zoek "H 3.11" → Vindt hoofdstuk 3.11 opgaven
- Filter op H 2.6 + zoek "parallel" → Specifieke opgaven

---

## 🎯 Quiz Mode

**Locatie:** `study-guide/QUIZ-MODE.html`

### Wat is het?

Interactieve **self-testing tool** met 10 sample vragen, chapter filtering, en progress tracking.

### Features

✅ **10 Sample Vragen** (expandable)
✅ **Chapter Filtering** (H 1.9, H 2.6, H 3.11, H 4.4, H 7.8, H 9.7)
✅ **Answer Reveal/Hide** functionaliteit
✅ **Progress Tracking** (X/Y correct, accuracy %)
✅ **Statistieken Dashboard**
✅ **End Screen** met final score

### Gebruik

**Study Workflow:**
```
1. Open Quiz Mode
2. Selecteer hoofdstuk (of "Alle Hoofdstukken")
3. Lees vraag ZONDER antwoord te kijken
4. Probeer zelf te beantwoorden
5. Klik "Juist" of "Fout" (eerlijk zijn!)
6. Lees antwoord voor begrip
7. Klik "Volgende Vraag"
8. Herhaal tot einde → bekijk statistieken
```

**Tips:**
- Gebruik ZONDER antwoorden eerst (active recall)
- Track welke vragen je fout hebt
- Herhaal moeilijke vragen later
- Doel: 90%+ accuracy voordat je door gaat

---

## ⏱️ Exam Simulator

**Locatie:** `study-guide/EXAM-SIMULATOR.html`

### Wat is het?

**Exam condities simulator** met timing, multiple choice, en automatische grading.

### Features

✅ **Configureerbaar:**
  - 10-30 vragen
  - 1-3 minuten per vraag
  - Moeilijkheid: basis/gemiddeld/gevorderd/all

✅ **Exam Condities:**
  - Timer met countdown
  - Warning animation (< 2 min)
  - Geen antwoorden tijdens exam
  - Navigation (vorige/volgende)

✅ **Resultaten:**
  - Score (X/Y)
  - Percentage
  - GESLAAGD/NIET GESLAAGD (≥55%)
  - Tijd gebruikt
  - Gedetailleerde review

### Gebruik

**Exam Voorbereiding (aanbevolen 2 weken voor examen):**

```
Week -2:
  - 16 vragen, 2 min/vraag, gemiddeld
  - Doel: ≥70%

Week -1:
  - 20 vragen, 2 min/vraag, gevorderd
  - Doel: ≥75%

Dag -3:
  - 30 vragen, 2 min/vraag, all levels
  - Doel: ≥80%

Dag -1:
  - RUST! Geen exams meer
```

**Tips:**
- Simuleer echte condities (stil, geen hulpmiddelen)
- Treat it like real exam (stress training)
- Review ALLE foute antwoorden na afloop
- Track je scores over tijd

---

## 📊 Progress Tracker

**Locatie:** `study-guide/PROGRESS-TRACKER.html`

### Wat is het?

Track voltooiing van **alle 84 opgaven** met statistieken, motivational feedback, en export/import.

### Features

✅ **Track alle 84 opgaven** (checkbox per opgave)
✅ **Real-time Statistics:**
  - Voltooid / Nog Te Doen / Percentage
  - Geschatte dagen (2 opgaven/dag)

✅ **Progress Bar** met percentage
✅ **Motivational Messages** bij milestones (25%, 50%, 75%, 90%, 100%)
✅ **LocalStorage Persistence** (auto-save)
✅ **Export/Import** voortgang (JSON backup)
✅ **Per-Chapter Progress** tracking

### Gebruik

**Dagelijkse Workflow:**
```
1. Open Progress Tracker
2. Vink voltooide opgaven af
3. Check statistieken:
   - Hoeveel nog te doen?
   - Geschatte dagen tot klaar
4. Export backup (1x per week)
```

**Export/Import:**
```
Export:
  - Klik "Exporteer Voortgang"
  - Bewaar JSON bestand veilig
  - Gebruik als backup

Import:
  - Klik "Importeer Voortgang"
  - Selecteer JSON bestand
  - Voortgang wordt hersteld
```

---

## 🎯 Weak Spots Analyzer

**Locatie:** `study-guide/WEAK-SPOTS-ANALYZER.html`

### Wat is het?

**Self-assessment tool** die je zwakke punten identificeert en gepersonaliseerde study aanbevelingen geeft.

### Features

✅ **44 Skills Assessment** (10 hoofdstukken)
✅ **3-Point Rating Scale:**
  - ❌ Zwak - Begrijp het niet goed
  - ⚠️ OK - Basis begrip, onzeker
  - ✅ Sterk - Goed begrip, vertrouwen

✅ **Analyse:**
  - Priority list (top 5 zwakste punten)
  - Heatmap per hoofdstuk
  - Gepersonaliseerde aanbevelingen
  - Automatische week planning

✅ **Export/Import** analyse (JSON)
✅ **LocalStorage** persistence

### Gebruik

**Weekly Assessment (aanbevolen elke zondag):**

```
1. Open Weak Spots Analyzer
2. Beoordeel alle skills eerlijk:
   - Zwak = moeite mee, niet begrepen
   - OK = kan het, maar onzeker
   - Sterk = vertrouwen, snap het goed
3. Klik "Analyseer Resultaten"
4. Review:
   - Priority list → focus hier deze week
   - Heatmap → welke hoofdstukken zijn zwak?
   - Recommendations → follow deze adviezen
   - Week Plan → volg dit schema
5. Export analyse voor tracking
```

**Interpretation:**

| Heatmap Kleur | Betekenis | Actie |
|---------------|-----------|-------|
| 🔴 Rood (< 1.7) | Zwak hoofdstuk | **PRIORITEIT!** Extra tijd hier |
| 🟠 Oranje (1.7-2.3) | Gemiddeld | Review + practice |
| 🟢 Groen (> 2.3) | Sterk | Maintain met Anki |

---

## 📅 Study Schedule

**Locatie:** `study-guide/STUDY-SCHEDULE.html`

### Wat is het?

**Gepersonaliseerd studieplan generator** die een week-voor-week schema maakt tot je examen.

### Features

✅ **Configuratie:**
  - Examendatum
  - Intensiteit (licht/gemiddeld/intensief: 1-5 opgaven/dag)
  - Studiestijl (sequentieel/mixed/difficulty)
  - Weekenden (studeren/review/rust)
  - Huidige voortgang
  - Dagelijkse studietijd

✅ **Output:**
  - Visuele calendar view (week grid)
  - Auto-distributie 84 opgaven
  - Exam prep week (laatste 7 dagen)
  - Rest day (dag voor examen)
  - Summary statistics

✅ **Export:**
  - Print schema (PDF via browser)
  - iCal export (toekomstig)
  - Save to browser

### Gebruik

**Initial Setup:**

```
1. Open Study Schedule Generator
2. Configureer:
   - Examendatum: bijv. 2025-12-15
   - Intensiteit: "Gemiddeld" (2-3 opgaven/dag)
   - Studiestijl: "Mixed" (afwisseling)
   - Weekenden: "Studeren"
   - Voortgang: 0 (of je huidige aantal)
   - Studietijd: "1 uur"
3. Klik "Genereer Studieplan"
4. Review calendar view
5. Print of screenshot voor referentie
```

**Week Grid Interpretatie:**

| Kleur | Type | Betekenis |
|-------|------|-----------|
| 🟢 Groen | Study Day | Normale studie opgaven |
| 🟠 Oranje | Review Day | Herhaling (weekenden) |
| 🔴 Rood | Exam Prep/Dag | Laatste week voorbereiding |
| ⚪ Wit | Rest | Vrije dag |

**Suggested Intensiteit:**

| Beschikbare Tijd | Intensiteit | Opgaven/Dag | Totaal Dagen |
|------------------|-------------|-------------|--------------|
| > 60 dagen | Licht | 1-2 | ~42-84 |
| 30-60 dagen | Gemiddeld | 2-3 | ~28-42 |
| < 30 dagen | Intensief | 4-5 | ~17-21 |

---

## 📐 Formuleblad

**Locatie:** `study-guide/FORMULEBLAD-AUTO.html`

### Wat is het?

Auto-gegenereerd **formuleblad met 52 formules** georganiseerd per hoofdstuk, print-ready voor examen.

### Features

✅ **52 Formules** verdeeld over 8 hoofdstukken:
  - H 1.9 - Wet van Ohm & Kirchhoff (7 formules)
  - H 2.6 - Serie & Parallel (6 formules)
  - H 3.11 - Netwerk Analyse (6 formules)
  - H 4.4 - Energie & Vermogen (6 formules)
  - H 5.5 - Wisselspanning (6 formules)
  - H 6.8 - C & L (5 formules)
  - H 7.8 & H 9.7 - RLC & Complex (10 formules)
  - H 11.7 - Vermogen (AC) (6 formules)

✅ **3-kolom layout:**
  - Formule naam
  - Wiskundige notatie
  - Betekenis/beschrijving

✅ **Print-Friendly:**
  - @media print CSS
  - Page-break optimization
  - Afkortingen legenda

### Gebruik

**Examen Voorbereiding:**

```
Week -4:
  - Print formuleblad
  - Lees 1x volledig door
  - Markeer onbekende formules

Week -3 tot -2:
  - Dagelijks: 5-10 formules memoriseren
  - Practice schrijven zonder kijken
  - Test jezelf met Quiz Mode

Week -1:
  - Volledige formuleblad uit hoofd
  - Random formula recall practice
  - Gebruik tijdens practice exams

Examen dag:
  - Neem formuleblad mee (check NCOI regels!)
  - Bekijk 10 min voor examen
```

**Memorisatie Technieken:**

1. **Spaced Repetition:** Anki decks met formules
2. **Write It Out:** Schrijf elke formule 10x
3. **Teach Someone:** Leg formules uit aan ander
4. **Application:** Gebruik in opgaven (begrijp context)
5. **Mnemonics:** Maak ezelsbruggetjes (bijv. "U Is Raar" → U = I × R)

---

## 🖨️ PDF Export

**Locatie:** `study-guide/PRINT-READY-COMPLETE-GUIDE.html`

### Wat is het?

**Print-ready HTML** met alle 44 enhanced opgaven in één document voor PDF export/archivering.

### Features

✅ **44 Enhanced Opgaven** (h-prefix bestanden)
✅ **Table of Contents** met links
✅ **Week-by-week organisatie**
✅ **Print-Optimized CSS:**
  - Page-break-after per opgave
  - White background override
  - Optimized margins

✅ **Print Button** voor easy PDF generatie

### Gebruik

**PDF Generatie:**

```
1. Open PRINT-READY-COMPLETE-GUIDE.html
2. Methode A - Direct print:
   - Klik "Printen / PDF Opslaan" button
   - Of: Ctrl+P

3. Print Settings:
   - Destination: "Save as PDF"
   - Paper size: A4
   - Margins: Normal
   - Background graphics: ON (belangrijk!)
   - Headers/Footers: OFF

4. Klik "Save" → PDF ready!
```

**Use Cases:**

- **Offline Studie:** Print PDF voor studie zonder internet
- **Backup:** Bewaar PDF als archief
- **E-reader:** Upload naar tablet/e-reader
- **Annotatie:** Print en annoteer met pen
- **Delen:** Deel PDF met medestudenten (check copyright)

---

## 📄 Quick Reference Card

**Locatie:** `study-guide/QUICK-REFERENCE-CARD.html`

### Wat is het?

**Compacte cheat sheet (A4)** met alle essentiële formules in 3-kolom layout, perfect voor last-minute exam prep.

### Features

✅ **Alle Essentiële Formules:**
  - Basis (Ohm, Kirchhoff, Serie/Parallel)
  - AC (RLC, Impedantie, Resonantie)
  - Driefase (Ster/Delta, Lijnspanning)
  - Complex Rekenen (Fasoren, Vermogen)

✅ **3-Kolom Layout:**
  - Kolom 1: Basis & DC
  - Kolom 2: AC & RLC
  - Kolom 3: Driefase & Complex

✅ **Print-Optimized:**
  - A4 formaat (perfect voor exam)
  - Compacte presentatie
  - Geen verspilde ruimte
  - Clear formule notatie

### Gebruik

**Exam Prep (laatste week):**

```
Week -1:
  - Print Quick Reference Card
  - Review 2x per dag (morning + evening)
  - Highlight moeilijke formules
  - Practice schrijven zonder kijken

Dag -1:
  - Final review (15 min)
  - Neem mee naar examen (check NCOI regels!)

Exam Dag:
  - Review 10 min voor examen
  - Gebruik als reference tijdens exam (indien toegestaan)
```

**Tips:**

- **Compact:** Alle formules op 1 pagina
- **Quick Lookup:** Sneller dan door boek bladeren
- **Exam-Safe:** Print op wit papier, geen annotations (check NCOI regels)
- **Memorization:** Use als checklist (welke formules ken je uit hoofd?)

---

## 📝 Practice Worksheets

**Locatie:** `study-guide/worksheets/INDEX.html`

### Wat is het?

**7 print-ready oefenbladen** (15 practice vragen totaal) voor offline studie en handmatige berekeningen.

### Features

✅ **7 Worksheets:**
  - H 1.9 - Wet van Ohm & Kirchhoff (3 vragen)
  - H 2.6 - Serie & Parallel (2 vragen)
  - H 3.11 - Thévenin & Norton (2 vragen)
  - H 4.4 - Energie & Vermogen (2 vragen)
  - H 7.8 - RLC Schakelingen (2 vragen)
  - H 9.7 - Complexe Impedantie (2 vragen)
  - H 11.7 - Vermogensleer (2 vragen)

✅ **Per Worksheet:**
  - Student info velden (naam, datum, klas)
  - Gegeven + Gevraagd voor elke vraag
  - Grid-lined answer spaces
  - Adequate ruimte voor berekeningen
  - Print-friendly formatting

✅ **Offline Study:**
  - Geen computer nodig
  - Practice handmatig rekenen
  - Exam-realistic (pen & papier)
  - Perfect voor klassikale oefening

### Gebruik

**Study Workflow:**

```
1. Open worksheets/INDEX.html
2. Print gewenste hoofdstuk worksheet(s)
3. Vul student info in
4. Los vragen op (zonder computer!)
5. Check antwoorden in opgaven bestanden
6. Noteer fouten & weak spots
```

**Best Practices:**

- **Handmatig:** Schrijf alle stappen uit (zoals op examen)
- **No Calculator First:** Try without rekenmachine eerst
- **Time Yourself:** 10-15 min per vraag
- **Review:** Check antwoorden in enhanced opgaven
- **Archive:** Bewaar voltooide worksheets (track improvement)

**Use Cases:**

| Scenario | Waarom Worksheets? |
|----------|-------------------|
| **Klassikaal** | Print voor hele klas, gezamenlijk oefenen |
| **Examen Practice** | Simuleer echte exam condities (pen & papier) |
| **Groepsstudie** | Elk persoon lost op, vergelijk antwoorden |
| **Offline Studie** | Geen internet/computer nodig |
| **Handmatig Rekenen** | Practice zonder calculator dependency |

**Example Usage (Study Group):**

```
1. Print worksheet voor iedereen
2. 30 min: Iedereen lost individueel op
3. 15 min: Vergelijk antwoorden
4. 10 min: Bespreek fouten & begrip
5. 5 min: Note weak spots voor iedereen
```

---

## 🎯 Formula Quiz

**Locatie:** `study-guide/FORMULA-QUIZ.html`

### Wat is het?

**Interactieve formule memorisatie tool** met 52 formules en 3 quiz modi voor effectief leren.

### Features

✅ **52 Formules Database** (alle hoofdstukken)
✅ **3 Quiz Modi:**
  - Naam → Formule (gegeven naam, type formule)
  - Formule → Naam (gegeven formule, herken naam)
  - Mixed (afwisselend beide)

✅ **Chapter Filtering** (per hoofdstuk oefenen)
✅ **Real-time Feedback** (juist/fout direct)
✅ **Hint Systeem** (optionele hints per formule)
✅ **Progress Tracking** (X/Y correct, percentage)
✅ **Configureerbaar** (10-52 vragen)

### Gebruik

**Daily Practice (10-15 min):**

```
1. Open Formula Quiz
2. Selecteer hoofdstuk (of "Alle")
3. Kies modus: "Naam → Formule" (moeilijkst)
4. Start met 10-20 vragen
5. Type antwoord ZONDER hint eerst
6. Review fouten en herhaal
```

**Recommended Workflow:**

```
Week 1-2: Naam → Formule (20 vragen/dag)
Week 3-4: Formule → Naam (20 vragen/dag)
Week 5-6: Mixed Mode (30 vragen/dag)
Week 7-8: Alle 52 formules (daily drill)
```

**Tips:**

- **No Hints:** Probeer eerst zonder hints (active recall)
- **Spaced Repetition:** Focus op foute formules de volgende dag
- **Type Completely:** Type hele formule, niet alleen delen
- **Speed:** Build up snelheid (< 30 sec per formule)
- **Target:** 90%+ accuracy before exam

**Example Session:**

```
1. Select: H 7.8 & H 9.7 (RLC & Complex)
2. Mode: Naam → Formule
3. Count: 10 vragen
4. Goal: 8/10 correct (80%)
5. Review: Note foute formules
6. Repeat: Same questions next day
```

---

## ⏱️ Study Timer (Pomodoro)

**Locatie:** `study-guide/STUDY-TIMER.html`

### Wat is het?

**Pomodoro Technique timer** voor gestructureerde studie met focus sessies en pauzes.

### Features

✅ **Pomodoro Technique:**
  - Werk sessies (default 25 min, configureerbaar)
  - Korte pauzes (default 5 min)
  - Lange pauze (default 15 min na 4 sessies)

✅ **Configureerbaar:**
  - Werk duur (1-60 min)
  - Pauze duur (1-30 min)
  - Lange pauze duur (1-60 min)
  - Sessies tot lange pauze (2-10)

✅ **Task Tracking:**
  - Noteer huidige opgave
  - Blijft zichtbaar tijdens timer

✅ **Statistics (Daily):**
  - Completed pomodoros (aantal)
  - Total minuten studied
  - Sessies vandaag

✅ **Notifications:**
  - Visual notifications (on-screen)
  - Sound alerts (optioneel, 🔔 toggle)
  - Browser title updates (zie tijd in tab)

✅ **Keyboard Shortcuts:**
  - Space: Start/Pause
  - Ctrl+R: Reset

✅ **LocalStorage** (auto-save daily stats)

### Gebruik

**Setup (eenmalig):**

```
1. Open Study Timer
2. Configureer durations (default = 25/5/15)
3. Enable sound (optioneel)
4. Test 1 sessie
```

**Daily Study Session:**

```
1. Open timer
2. Type huidige taak: "H 2.6 Opgave 18"
3. Klik "Start"
4. Werk FOCUS (geen telefoon, geen tabs)
5. Timer loopt af → PAUZE (mandatory!)
6. Herhaal voor volgende opgave
```

**Recommended Schedule:**

```
Morning Session (2 pomodoros = 1 uur):
- 25 min: Opgave 1
- 5 min: Pauze (stretch, water)
- 25 min: Opgave 2
- 15 min: Lange pauze

Evening Session (2 pomodoros = 1 uur):
- 25 min: Review + Anki
- 5 min: Pauze
- 25 min: Practice quiz
- Done for the day!
```

**Tips:**

- **Strict Breaks:** ALWAYS neem pauze (geen "ik ga door")
- **Single Task:** 1 opgave per pomodoro (focus)
- **Track Daily:** Aim for 4-6 pomodoros/dag (2-3 uur)
- **Statistics:** Review stats weekly (ben je consistent?)
- **Long Breaks:** Use voor walk, meal, refresh

**Common Patterns:**

| Study Style | Pomodoros/Day | Total Time | Results |
|-------------|---------------|------------|---------|
| **Licht** | 2-3 | 50-75 min | Steady progress |
| **Gemiddeld** | 4-6 | 100-150 min | Good coverage |
| **Intensief** | 8-10 | 200-250 min | Fast completion |

---

## 🃏 Flashcard Generator

**Locatie:** `study-guide/FLASHCARD-GENERATOR.html`

### Wat is het?

**Print-ready fysieke flashcard generator** voor 52 formules in traditioneel flashcard formaat.

### Features

✅ **52 Formules** (complete database)
✅ **Chapter Selection:**
  - Alle hoofdstukken (52 cards)
  - Of specifiek hoofdstuk (5-10 cards)

✅ **2-Sided Design:**
  - Voorkant: Formula naam + hint
  - Achterkant: Formula zelf

✅ **Print Optimized:**
  - 4 cards per A4 pagina
  - Dashed cutout guides
  - Color-coded (blauw voorkant, geel achterkant)
  - Perfect alignment front/back

✅ **Easy Printing:**
  - Print voorkant eerste
  - Draai papier
  - Print achterkant (auto-reversed voor correcte alignment)

### Gebruik

**Generate & Print:**

```
1. Open Flashcard Generator
2. Select Chapter (of "Alle Hoofdstukken")
3. Klik "Genereer Flashcards"
4. Review preview
5. Klik "Print / PDF"
6. Print Settings:
   - A4 paper
   - Marges: Normaal
   - Background graphics: ON (belangrijk!)
   - Print BEIDE pagina's
7. Snij langs stippellijnen
8. Optioneel: Lamineer voor duurzaamheid
```

**Print Instructions (Duplex):**

```
Page 1 (VOORKANT):
- Print normaal
- Laat drogen (inkjet)

Page 2 (ACHTERKANT):
- Draai papier 180° (short edge flip)
- Print op achterkant
- Formules staan nu correct aligned

Knip:
- Langs stippellijnen
- 4 flashcards per vel
```

**Study with Flashcards:**

```
Daily Routine (15 min):
1. Shuffle deck (52 cards)
2. Read voorkant (naam + hint)
3. Try to recall formule
4. Flip to check achterkant
5. Correct → "Ja" stapel
6. Fout → "Nee" stapel (herhaal deze)
7. Repeat "Nee" stapel until 100%
```

**Leitner System (spaced repetition):**

```
Box 1 (daily): Nieuwe + foute cards
Box 2 (om de dag): 1x correct
Box 3 (weekly): 2x correct achter elkaar
Box 4 (monthly): 3x+ correct
Box 5 (archived): Mastered (100%)

Move cards based on performance!
```

**Tips:**

- **Laminate:** Flashcards gaan langer mee
- **Color Code:** Use gekleurde markers voor moeilijke formules
- **Mobile:** Neem mee in tas voor "dead time" studie
- **Study Partner:** Quiz elkaar met flashcards
- **Mix:** Combine met digital Formula Quiz voor variatie

**Use Cases:**

| Scenario | Waarom Flashcards? |
|----------|-------------------|
| **Pendelen** | Studie in bus/trein (geen screen needed) |
| **Groepsstudie** | Fysiek delen met groep |
| **No Screen Time** | Avoid screen fatigue |
| **Tactile Learning** | Hands-on memory boost |
| **Exam Day** | Last-minute review (geen laptop nodig) |

---

## 🎴 Anki Decks

**Locatie:** `generated-cards/`

### Wat is het?

Auto-gegenereerde **Anki flashcards** (CSV format) voor spaced repetition learning.

### Files

```
generated-cards/
├── anki-deck-KENNIS-AUTO-GENERATED.csv     (6 kaarten - conceptueel)
└── anki-deck-REKENEN-AUTO-GENERATED.csv    (9 kaarten - berekeningen)
```

### Features

✅ **Deck Split:**
  - KENNIS: Conceptuele vragen, definities, begrip
  - REKENEN: Berekeningen, numerieke problemen

✅ **Card Structure:**
  - Front: Hoofdstuk + Gegeven + Gevraagd
  - Back: Antwoord + eerste 3 solution steps
  - Tags: h-prefix, type, onderwerpen

✅ **15 Cards Total** (auto-generated from opgaven)

### Gebruik

**Anki Import:**

```
1. Download & Install Anki (gratis)
   https://apps.ankiweb.net/

2. Open Anki

3. File → Import

4. Select: anki-deck-KENNIS-AUTO-GENERATED.csv

5. Settings:
   - Type: Basic
   - Allow HTML in fields: ✓ YES (BELANGRIJK!)
   - Field mapping:
     * Field 1: Front
     * Field 2: Back
     * Field 3: Tags

6. Click "Import"

7. Repeat voor REKENEN deck
```

**Daily Anki Routine:**

```
Nieuwe kaarten: 2-4 per dag
Review kaarten: ALLE daily reviews

Consistency > Quantity
→ Liever 15 min/dag dan 2 uur 1x/week
```

**Settings (recommended):**

```
New Cards:
  - Per day: 2-4
  - Learning steps: 10m 1d 3d
  - Graduating interval: 7 days
  - Easy interval: 14 days

Reviews:
  - Maximum per day: Unlimited
  - Easy bonus: 130%
  - Interval modifier: 100%

Lapses:
  - Relearning steps: 10m 1d
  - New interval: 50%
```

---

## 🔄 Recommended Workflow

### Daily Routine (30-45 minuten)

```
Morning (15 min):
  ✅ Anki reviews (all due cards)
  ✅ Formula sheet review (5 formules)

Study Session (20-30 min):
  ✅ Check Progress Tracker → pick opgave
  ✅ Complete opgave (full 5-step method)
  ✅ Update Progress Tracker (check off)
  ✅ If stuck → mark as weak spot

Evening (5-10 min):
  ✅ Quiz Mode (5-10 vragen)
  ✅ Review day's learnings
```

### Weekly Routine

```
Sunday:
  ✅ Weak Spots Analyzer (re-assess all skills)
  ✅ Review week plan
  ✅ Export progress backup

Mid-Week (Wednesday):
  ✅ Mini exam (10-15 vragen, Exam Simulator)
  ✅ Check if on track with schedule
  ✅ Adjust study plan if needed
```

### Pre-Exam Routine (last 2 weeks)

```
Week -2:
  - Monday-Friday: Complete any remaining opgaven
  - Daily: Exam Simulator (16 vragen)
  - Focus: Weak spots

Week -1:
  - Monday-Thursday: Practice exams only
  - Friday: Light review + formuleblad
  - Saturday: Rest day
  - Sunday: Formula review only

Exam Day:
  - Morning: Formuleblad review (10 min)
  - 30 min before: Deep breaths, confidence
  - During: Trust your preparation
```

---

## 📊 Tool Comparison Matrix

| Tool | Purpose | Frequency | Time | Priority |
|------|---------|-----------|------|----------|
| Dashboard | Navigation | Daily start | 1 min | 🟢 |
| Index | Find opgaven | As needed | 5-10 min | 🟢 |
| Quiz Mode | Quick testing | Daily | 10-20 min | 🟢 |
| Exam Simulator | Exam prep | 2x/week | 30-60 min | 🟡 |
| Progress Tracker | Track completion | Daily | 2 min | 🟢 |
| Weak Spots | Identify gaps | Weekly | 20-30 min | 🟢 |
| Study Schedule | Plan study | 1x setup | 10 min | 🟡 |
| Formuleblad | Memorization | Daily | 5-10 min | 🟢 |
| PDF Export | Archive/print | 1x | 5 min | 🟡 |
| Quick Reference | Cheat sheet | Exam week | 5 min | 🟡 |
| Worksheets | Offline practice | 2x/week | 30-45 min | 🟡 |
| Formula Quiz | Formula drill | Daily | 10-20 min | 🟢 |
| Study Timer | Pomodoro focus | Daily | 25-55 min | 🟢 |
| Flashcards | Physical cards | 1x print | 5 min setup | 🟡 |
| Anki | Spaced repetition | Daily | 15-20 min | 🟢 |

**Legend:**
- 🟢 High Priority (use daily/weekly)
- 🟡 Medium Priority (setup once or use periodically)

---

## 🚀 Quick Start Guide

**Absolute beginner? Start hier:**

```
Day 1:
  1. Open Study Dashboard
  2. Set exam date
  3. Generate Study Schedule
  4. Complete Weak Spots Analyzer
  5. Start first opgave from schedule

Day 2-7:
  - Follow daily routine (zie boven)
  - Track progress daily
  - Use tools as needed

Week 2:
  - Re-assess weak spots (Sunday)
  - Adjust study plan if behind
  - Start using Exam Simulator

Continue until exam! 🎓
```

---

## 💡 Tips & Best Practices

### General

✅ **Consistency > Intensity:** 30 min/dag > 4 uur 1x/week
✅ **Active Recall:** Test zonder antwoorden eerst
✅ **Spaced Repetition:** Herhaal in toenemende intervals
✅ **Physical Meaning:** Begrijp WHY, niet alleen WHAT
✅ **Track Everything:** Use Progress Tracker religiously

### Tool-Specific

**Quiz Mode:**
- Cover antwoorden met hand
- Probeer eerst zelf te beantwoorden
- Alleen "Juist" als je 100% zeker bent

**Exam Simulator:**
- Simuleer echte condities (geen telefoon!)
- Time yourself strikt
- Review ALLE foute antwoorden

**Weak Spots:**
- Wees eerlijk met jezelf
- Update weekly
- Focus op fundament eerst (H 1.9, H 2.6)

**Study Schedule:**
- Build in buffer days (life happens!)
- Adjust if you fall behind (don't panic)
- Exam prep week is sacred (laatste 7 dagen)

---

## 🆘 Troubleshooting

### "Tools niet werkend in browser"

**Probleem:** HTML tools openen niet correct

**Oplossing:**
```bash
# Gebruik HTTP server in plaats van direct file opening
cd study-guide
python3 -m http.server 8000

# Navigeer naar:
http://localhost:8000/STUDY-DASHBOARD.html
```

### "LocalStorage data kwijt"

**Probleem:** Progress/ratings verloren na browser clear

**Preventie:**
- Export regelmatig (Weekly!)
- Backup JSON bestanden
- Use dezelfde browser consistent

### "Ik loop achter op schema"

**Probleem:** Niet op track met Study Schedule

**Oplossing:**
1. Re-assess realistische tempo (Weak Spots)
2. Genereer nieuwe schedule met huidige progress
3. Verhoog intensiteit (4-5 opgaven/dag kort term)
4. Focus op exam-kritisch (H 3.11, H 7.8, H 9.7)
5. Skip legacy opgaven (focus op h-prefix)

### "Te veel tools, overwhelming"

**Probleem:** Niet weten waar te beginnen

**Minimale Setup (3 tools):**
1. Complete Index (browse opgaven)
2. Progress Tracker (track completion)
3. Formuleblad (formulas)

**Later toevoegen:**
- Weak Spots (na ~20 opgaven)
- Exam Simulator (2 weken voor examen)

---

## 📞 Support & Feedback

**Issues/Bugs:**
- Check CLAUDE.md voor project documentatie
- Review README-ENHANCED-CONTENT.md

**Feature Requests:**
- Tools zijn open source
- Modify HTML files directly
- Share improvements

---

## 🎓 Final Checklist (Week voor Examen)

```
□ Alle 84 opgaven voltooid (Progress Tracker)
□ Weak Spots < 5 items (Weak Spots Analyzer)
□ Practice exam score ≥80% (Exam Simulator)
□ Formuleblad uit hoofd (Formuleblad)
□ Anki reviews up-to-date (0 due)
□ Geprobeerd alle MC questions (Quiz Mode)
□ Last review notes made (Print PDF)
□ Exam materials ready (rekenmachine, pen, ID)
□ Good night sleep (8+ uur)
□ CONFIDENCE HOOG! 🚀
```

---

**Succes met je studie! 📚⚡**

*Laatste update: 2025-11-08*
