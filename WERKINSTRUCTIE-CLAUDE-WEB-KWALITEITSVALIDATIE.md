# WERKINSTRUCTIE: CLAUDE WEB - ABSOLUTE KWALITEITSVALIDATIE
## NCOI Energietechniek Anki Deck - Van Goed naar Excellent

**Voor:** Claude Web (claude.ai met Projects feature)
**Budget:** €500 aan tokens - **KWALITEIT BOVEN KOSTEN**
**Doel:** Alle vragen, antwoorden, afbeeldingen en context naar 100% examen-ready kwaliteit brengen

---

## 🎯 KRITISCHE SUCCESFACTOREN

1. **Absolute inhoudelijke correctheid** - Geen enkele fout in formules, berekeningen of fysische interpretaties
2. **Visuele perfectie** - Alle afbeeldingen professioneel, correct, en didactisch optimaal
3. **Anki best practices** - Optimale kaartstructuur volgens wetenschappelijk bewezen leermethodes
4. **Multi-stage validatie** - Elke kaart door minimaal 3 verschillende validatiefases
5. **Context & grouping** - Logische clustering voor optimaal leerpad
6. **Exam alignment** - 100% aansluiting bij NCOI exameneisen

---

## ⚠️ KRITISCH: BRONMATERIAAL VERANKERING

**ALLE validatie, verbeteringen en nieuwe content MOET verankerd blijven in:**

### 📚 Primaire Bronnen (HEILIG - niet van afwijken!)

1. **Formuleblad Energietechniek v3 2023**
   - ALLE formules MOETEN exact matchen met dit blad
   - Notatie MOET identiek zijn (φ voor fase, Uth voor Thévenin, etc.)
   - Geen alternatieve formules toevoegen die NIET op dit blad staan
   - `source-materials/Formuleblad_Energietechniek_v3_2023.pdf`

2. **Paul Holmes - Elektrische Netwerken (3e editie)**
   - Terminologie MOET matchen met boek
   - Voorbeelden bij voorkeur gebaseerd op boek
   - Uitlegmethode consistent met Holmes' aanpak
   - "Holmes-stijl hints" behouden waar aanwezig

3. **NCOI Oefenvragen Energietechniek**
   - Vraagstelling MOET lijken op NCOI stijl
   - Antwoordformaat consistent met officiële antwoorden
   - Moeilijkheidsgraad gekalibreerd op deze vragen
   - `source-materials/Oefenvragen Energietechniek.pdf`

4. **NCOI Oefentoets 16 Vragen (examenstijl v6)**
   - EXAMENSTIJL is leidend
   - Vraagformulering matchen
   - Multiple choice format waar relevant
   - `source-materials/Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html`

5. **Energietechniek Anki Samenvatting**
   - 10 examendomeinen coverage
   - Kernconcepten zoals gedefinieerd in samenvatting
   - `source-materials/Energietechniek_Anki_Samenvatting.md`

### 🚫 VERBODEN: Wat NIET mag

❌ **Formules toevoegen die NIET op formuleblad staan**
- Examen geeft formuleblad → student moet die formules kunnen gebruiken
- Geen "alternatieve afleidingen" die niet op examen beschikbaar zijn

❌ **Terminologie wijzigen "omdat het beter is"**
- NCOI/Holmes gebruikt "spanningsval" → gebruik dit, niet "voltage drop"
- NCOI gebruikt "fasehoek φ" → gebruik dit, niet "theta θ"
- Nederlands > Engels (tenzij Holmes Engels gebruikt)

❌ **Nieuwe concepten introduceren buiten syllabus**
- Focus op 10 examendomeinen
- Geen "nice to know" concepten die niet op examen komen

❌ **Afwijken van NCOI moeilijkheidsniveau**
- Niet moeilijker maken "om uitdagend te zijn"
- Niet makkelijker maken "voor toegankelijkheid"
- NCOI examenniveau is leidend

❌ **Vraagstijl veranderen naar "betere" pedagogische vorm**
- Als NCOI vraagt: "Bereken de stroom" → gebruik dit
- Niet wijzigen naar: "Wat is de waarde van de elektrische stroom door de weerstand?"
- NCOI stijl is leidend (voorbereiding op examen!)

### ✅ WEL Toegestaan: Verbeteringen binnen grenzen

✅ **Verduidelijking zonder inhoud te wijzigen**
- Tussenstappen toevoegen in berekeningen (als ze leiden tot formuleblad-formule)
- "Waarom"-uitleg toevoegen (zolang consistent met Holmes)
- Visuele hulp (diagrammen) toevoegen (als ze concept verduidelijken)

✅ **Correctie van fouten in v1.0**
- Typefouten, rekenpfouten, notatie-inconsistenties
- MITS je checkt dat correctie overeenkomt met bronmateriaal

✅ **Optimalisatie van kaartstructuur**
- Kaart splitsen in kleinere delen (zelfde content, betere structuur)
- Tags toevoegen voor filtering (niet content wijzigen)
- Templates verbeteren voor leesbaarheid

✅ **Toevoegen van afbeeldingen/diagrammen**
- MITS diagram klopt met formuleblad/boek
- Circuit symbolen volgens IEC/IEEE (zoals in Holmes boek)
- Waarden consistent met kaart tekst

### 🔍 Validatie Protocol per Wijziging

**VOOR elke wijziging aan een kaart, check:**

1. **Formule check:**
   - [ ] Staat deze formule op Formuleblad v3 2023?
   - [ ] Is notatie exact hetzelfde?
   - [ ] Zo nee: mag deze afleiding met formuleblad formules?

2. **Terminologie check:**
   - [ ] Gebruikt Holmes dit woord in hoofdstuk X?
   - [ ] Staat dit in NCOI materiaal?
   - [ ] Is dit standaard Nederlands elektrotechniek jargon?

3. **Examenstijl check:**
   - [ ] Zou deze vraag op NCOI examen kunnen staan?
   - [ ] Matcht moeilijkheid met oefentoets?
   - [ ] Is antwoordformaat consistent met officiële antwoorden?

4. **Bronverwijzing:**
   - [ ] Kan ik dit terugvinden in bronmateriaal?
   - [ ] Welke bron (formuleblad/Holmes/oefenvragen)?
   - [ ] Pagina/sectie nummer indien mogelijk

### 📖 Bronverwijzingen Verplicht

**Bij elke kaart validatie, documenteer:**

```markdown
## Kaart X: [beschrijving]

**Bronnen:**
- Formule: Formuleblad v3 2023, sectie [X]
- Concept: Holmes 3e editie, hoofdstuk [X], pagina [X]
- Examenstijl: Oefentoets vraag [X] / Oefenvragen [X]

**Validatie:**
- ✅ Formule exact zoals op formuleblad
- ✅ Terminologie consistent met Holmes
- ✅ Vraagstijl matcht NCOI oefentoets
```

### 🎓 Voorbeeld: Correcte vs Incorrecte Wijziging

**❌ INCORRECT (afwijken van bronnen):**

```csv
VOOR (v1.0):
"Bereken de effectieve waarde van een sinusvormige spanning met Upiek = 325V"

NA (v2.0 - FOUT!):
"Calculate the RMS voltage value for a sinusoidal waveform with peak voltage of 325V"
```
**Probleem:** Engels! NCOI examen is Nederlands.

---

**❌ INCORRECT (nieuwe formule):**

```csv
VOOR:
"Bereken arbeidsfactor: cos φ = P/S"

NA (FOUT!):
"Bereken arbeidsfactor: cos φ = P/√(P²+Q²)"
```
**Probleem:** Tweede formule niet op formuleblad! Student heeft op examen alleen P/S beschikbaar.

---

**✅ CORRECT (verduidelijking met bronverwijzing):**

```csv
VOOR:
"Bereken stroom bij resonantie in LC-kring"

NA (GOED!):
"Bereken de stroom bij resonantie in een LC-serie kring met L=50mH, C=20µF, R=10Ω, U=230V
<br><br>
<i>Hint (zoals op formuleblad): f₀ = 1/(2π√LC), bij resonantie: XL = XC → Z = R</i>"
```
**Goed omdat:**
- Formules van formuleblad
- NCOI stijl vraag
- Hint matcht "Holmes-stijl hints"

---

## 📋 VOORBEREIDING: VOORDAT JE BEGINT

### Stap 0.1: Repository Clone & Analyse

```bash
# Clone deze repository naar Claude Projects
# Upload alle bestanden naar een nieuw Claude Project
# Naam project: "NCOI Energietechniek - Quality Validation"
```

**Te uploaden bestanden (prioriteit):**
- Alle `generated-cards/*.csv` bestanden
- Alle `analysis/*.md` bestanden
- Alle `source-materials/*` (PDF's, HTML)
- `CLAUDE.md` (deze bevat project context)
- `README.md`
- Alle Python scripts uit `scripts/`

### Stap 0.2: Anki Software Analyse

**Analyseer het Anki ecosysteem:**

1. **Clone Anki repository:**
   ```bash
   git clone https://github.com/ankitects/anki.git
   ```

2. **Bestudeer (lees deze bestanden in Claude Project):**
   - `/docs/` - Officiële Anki documentatie
   - `/docs/media.md` - Media handling best practices
   - `/docs/templates.md` - Card template system
   - `/pylib/anki/` - Core library (vooral `cards.py`, `notes.py`)
   - `/qt/aqt/browser/` - Browser functionality
   - `/ts/` - Frontend TypeScript (rendering)

3. **Focus gebieden:**
   - ✅ Optimale card template structuur
   - ✅ Media embedding (SVG/PNG best practices)
   - ✅ LaTeX rendering pipeline
   - ✅ Tag hierarchies en filtering
   - ✅ Spaced repetition algoritme (SM-2/FSRS)
   - ✅ Mobile rendering compatibility (AnkiDroid/iOS)

4. **Output: Maak document:**
   ```
   analysis/ANKI-BEST-PRACTICES-VOOR-ENERGIETECHNIEK.md
   ```

   **Inhoud:**
   - Optimale kaartstructuur voor technische vakken
   - Image sizing en placement aanbevelingen
   - LaTeX formatting do's en don'ts
   - Tag strategie voor hiërarchische filtering
   - Mobile compatibility checklist
   - Cloze deletion vs Basic card types
   - Reverse cards waar nuttig

### Stap 0.3: Externe Expertise Verzamelen (Web Research)

**Zoek en analyseer:**

1. **Anki best practices voor STEM vakken:**
   - Reddit r/Anki top posts over physics/engineering
   - AnkiWeb shared decks voor electrical engineering
   - SuperMemo.com artikelen over formulation

2. **Nederlandse elektrotechniek normen:**
   - NEN 1010 (elektrische installaties)
   - Standaard symbolen en notaties
   - NCOI examen voorbeelden (indien publiek beschikbaar)

3. **Educatieve psychologie:**
   - Spacing effect research
   - Interleaving vs blocked practice
   - Visual learning voor technische concepten

**Output: Maak document:**
```
analysis/EXTERNAL-BEST-PRACTICES.md
```

---

## 🔍 FASE 1: DIEPGAANDE CONTENT ANALYSE

### Agent 1.1: Inhoudelijke Correctheid Validator

**Prompt voor nieuwe Claude chat (of agent):**

```
Je bent een expert elektrotechniek docent met 20 jaar ervaring in NCOI examens.

⚠️ KRITISCH: ALLE validatie moet verankerd zijn in bronmateriaal:
- Formuleblad Energietechniek v3 2023 (source-materials/)
- Paul Holmes - Elektrische Netwerken (3e editie)
- NCOI Oefenvragen + Oefentoets (source-materials/)

VERBODEN:
- ❌ Formules toevoegen die NIET op formuleblad staan
- ❌ Terminologie wijzigen (NCOI/Holmes is leidend)
- ❌ Engels gebruiken (Nederlands tenzij Holmes Engels gebruikt)
- ❌ Concepten toevoegen buiten 10 examendomeinen
- ❌ Afwijken van NCOI moeilijkheidsniveau

TAAK: Valideer ELKE kaart in generated-cards/anki-deck-KENNIS-v1.csv op:

1. FORMULES (met bronverwijzing!)
   - Staat formule op Formuleblad v3 2023? ✅/❌
   - Is notatie EXACT hetzelfde? ✅/❌
   - Kloppen eenheden in elke stap? ✅/❌
   - Afgeronde waarden realistisch? (2-3 sig. cijfers) ✅/❌
   - **DOCUMENTEER: Welke sectie van formuleblad**

2. FYSISCHE INTERPRETATIE (Holmes-consistent)
   - Is uitleg consistent met Holmes hoofdstuk X? ✅/❌
   - Worden valkuilen correct benoemd? ✅/❌
   - **DOCUMENTEER: Holmes pagina/hoofdstuk**

3. TERMINOLOGIE (NCOI/Holmes exact)
   - Nederlandse termen zoals in bronmateriaal? ✅/❌
   - Geen Anglicismen? ✅/❌
   - Match NCOI woordgebruik exact? ✅/❌
   - **LIJST inconsistenties met bron**

4. EXAM ALIGNMENT (NCOI examenstijl)
   - Zou deze vraag op NCOI examen kunnen? ✅/❌
   - Matcht vraagstijl met Oefentoets? ✅/❌
   - Moeilijkheid klopt met tag? ✅/❌
   - Waardes realistisch (230V/400V)? ✅/❌
   - **DOCUMENTEER: Vergelijkbare vraag in Oefentoets/Oefenvragen**

OUTPUT FORMAT:
```markdown
## Kaart [nummer]: [korte beschrijving]

**Status:** ✅ CORRECT / ⚠️ MINOR ISSUES / ❌ MAJOR ISSUES

**Bronverwijzingen:**
- Formule: Formuleblad v3 2023, sectie [X] ✅/❌
- Concept: Holmes 3e ed., hoofdstuk [X], pag [X] ✅/❌
- Examenstijl: Oefentoets vraag [X] / Oefenvragen [X] ✅/❌

**Bevindingen:**
- [Issue 1 + waarom dit afwijkt van bronmateriaal]
- [Issue 2 + welke bron dit tegenspreekt]

**Aanbevelingen:**
- [Fix 1 + hoe dit bron volgt]
- [Fix 2 + bronverwijzing voor correctie]

**Herziene versie (ALLEEN als binnen brongrenzen!):**
```csv
Front,Back,Tags
[Verbeterde versie - met bronverwijzing in comment]
```

**Rationale wijziging:**
- Waarom deze wijziging bronmateriaal volgt
- Welke sectie formuleblad/Holmes dit ondersteunt
```
```

**Herhaal voor anki-deck-REKENEN-v1.csv**

**Output bestanden:**
- `validation/phase1-KENNIS-content-validation.md`
- `validation/phase1-REKENEN-content-validation.md`

### Agent 1.2: Didactische Effectiviteit Validator

**Nieuwe chat/agent:**

```
Je bent een expert in educational psychology en spaced repetition learning.

TAAK: Analyseer elke kaart op LEERBAARHEID:

1. ATOMIC CONCEPT
   - Test kaart echt maar 1 concept? (niet 3-in-1)
   - Is de vraag duidelijk genoeg?
   - Kan je het in <30sec beantwoorden?

2. DIFFICULTY PROGRESSION
   - Zijn kaarten logisch opgebouwd (basis → gevorderd)?
   - Zijn er gaps in moeilijkheidsgraad?
   - Moeten sommige kaarten worden opgesplitst?

3. COGNITIVE LOAD
   - Is de hoeveelheid informatie per kaart optimaal?
   - Zijn er onnodige details die afleiden?
   - Is formatting (bold, linebreaks) consistent?

4. RETRIEVAL PRACTICE
   - Stimuleert de vraag actief nadenken?
   - Zijn hints niet te giveaway?
   - Is de kaart niet te triviaal ("wat is de formule voor X?")?

5. INTERLEAVING OPPORTUNITIES
   - Welke kaarten moeten worden gemixed (niet geblokkeerd per onderwerp)?
   - Zijn er cross-concept verbindingen gemist?

OUTPUT:
```markdown
## Didactische Analyse - Kaart [nummer]

**Atomic:** ✅/❌
**Difficulty:** [basis/gemiddeld/gevorderd] - CORRECT: ✅/❌
**Cognitive Load:** [low/medium/high] - OPTIMAL: ✅/❌
**Retrieval Strength:** [1-5 score]

**Aanbevelingen:**
- [Concrete verbeteringen]

**Herstructurering (indien nodig):**
[Splits kaart op in 2-3 kaarten, of merge met andere]
```
```

**Output:**
- `validation/phase1-didactic-analysis.md`

### Agent 1.3: Cross-Reference Validator

**Nieuwe chat:**

```
TAAK: Valideer consistentie TUSSEN kaarten

1. NOTATIE CONSISTENTIE
   - Wordt φ altijd voor fase gebruikt (niet soms θ)?
   - Is subscript consistent (Uth vs U_th vs Uthevenin)?
   - Zijn vector notaties uniform (U⃗ vs U_vec)?

2. CONCEPT OVERLAP
   - Welke kaarten behandelen hetzelfde concept anders?
   - Zijn er tegenstrijdigheden tussen kaarten?
   - Ontbreken er bruggen tussen gerelateerde concepten?

3. DIFFICULTY CALIBRATION
   - Zijn alle "niveau-basis" kaarten echt makkelijker dan "niveau-gemiddeld"?
   - Check: zijn er outliers (te moeilijk voor hun tag)?

4. TAG COMPLETENESS
   - Missen kaarten essentiële tags?
   - Zijn tags te breed (vermogen) of te specifiek (vermogen-driefase-ster-berekening)?

OUTPUT: Spreadsheet-achtige tabel met alle 80 kaarten en aanbevelingen
```

**Output:**
- `validation/phase1-cross-reference-matrix.md`

---

## 🎨 FASE 2: VISUELE CONTENT - AFBEELDINGEN 100% VALIDATIE

### Agent 2.1: Bestaande Afbeeldingen Audit

**Nieuwe chat:**

```
TAAK: Analyseer ALLE bestaande afbeeldingen in images/oefentoets/

Voor elke afbeelding (vraag_01.png t/m vraag_06.png):

1. TECHNISCHE KWALITEIT
   - Resolutie voldoende voor mobiel (min 800px breed)?
   - Leesbaarheid: zijn labels/waarden goed leesbaar?
   - Kleurcontrast: voldoende voor colorblind users?

2. INHOUDELIJKE CORRECTHEID
   - Zijn alle component symbolen correct (IEEE/IEC standaard)?
   - Kloppen de pijlen (stroomrichting)?
   - Zijn waarden in diagram consistent met kaart tekst?

3. DIDACTISCHE WAARDE
   - Helpt de afbeelding echt bij begrip?
   - Is er te veel of te weinig detail?
   - Zijn belangrijke elementen highlighted/labeled?

4. ANKI COMPATIBILITY
   - Formaat: SVG (vectorized) > PNG > JPG
   - Filesize: <500KB per afbeelding
   - Transparante achtergrond waar nuttig?

OUTPUT:
```markdown
## Afbeelding: vraag_01.png

**Gebruikt in kaarten:** [lijst kaart nummers]
**Huidige kwaliteit:** ✅/⚠️/❌
**Problemen:**
- [lijst issues]

**Actie:** KEEP / IMPROVE / REPLACE / REGENERATE
**Nieuwe spec (indien IMPROVE/REGENERATE):**
[Gedetailleerde beschrijving van gewenste afbeelding]
```
```

**Output:**
- `validation/phase2-image-audit.md`

### Agent 2.2: Missende Afbeeldingen Identificatie

**Nieuwe chat:**

```
TAAK: Identificeer ALLE kaarten die baat hebben bij afbeelding maar er geen hebben

Analyseer elke kaart en bepaal:

1. MOET HEBBEN (Priority 1)
   - Kaarten met "zie circuit", "zoals schema toont", maar geen image
   - Complexe netwerken (Thévenin, Norton, RLC)
   - Fasediagrammen (cos φ, complexe impedantie)
   - Driefase configuraties (ster/driehoek)

2. ZOU MOETEN HEBBEN (Priority 2)
   - Vermogensdriehoek kaarten zonder diagram
   - Golfvormen (sinus, blokgolf, resonantie curves)
   - Transformator wikkelingen
   - Kirchhoff circuits

3. NICE TO HAVE (Priority 3)
   - Conceptuele diagrammen
   - Geheugensteuntjes (mnemonics)
   - Vergelijkingstabellen

Voor elke missende afbeelding, schrijf een GEDETAILLEERDE SPEC:

```markdown
## Missende Afbeelding [ID]

**Voor kaart(en):** [nummers]
**Prioriteit:** 1/2/3
**Type:** circuit/diagram/graph/illustration

**Gedetailleerde specificatie:**

**Elementen:**
- [Exacte lijst van componenten met waarden]
- [Annotaties/labels die nodig zijn]

**Layout:**
- Afmetingen: [breedte x hoogte]
- Oriëntatie: horizontal/vertical
- Style: schematic/realistic/simplified

**Kleurenschema:**
- Achtergrond: [white/transparent]
- Primair: [bijv. black lines]
- Accenten: [bijv. red voor stroom, blue voor spanning]

**Referentie:**
- Gebaseerd op: [standaard symbolen IEC/IEEE]
- Voorbeeld: [link of beschrijving referentie]

**Tekst in afbeelding:**
- Labels: [lijst alle teksten]
- Font: [sans-serif, min 14pt]
- Taal: Nederlands

**SVG generatie prompt:**
[Exacte prompt die gebruikt kan worden voor code generation of DALL-E/Midjourney]
```
```

**Output:**
- `validation/phase2-missing-images-specs.md`

### Agent 2.3: Afbeelding Generator (SVG)

**Nieuwe chat met code execution:**

```
⚠️ KRITISCH: Afbeeldingen moeten consistent zijn met bronmateriaal!

VERPLICHT TE CHECKEN:
- Circuit symbolen zoals in Holmes boek (IEC/IEEE standaard)
- Component waarden zoals in oefenvragen (realistische waardes)
- Nederlandse labels (geen Engels!)
- Notatie zoals op formuleblad (φ voor fase, Uth voor Thévenin, etc.)

TAAK: Genereer ALLE afbeeldingen volgens specs uit phase2-missing-images-specs.md

Gebruik Python + schemdraw library voor circuits:

```python
import schemdraw
import schemdraw.elements as elm

# Voorbeeld: Thévenin equivalent
with schemdraw.Drawing() as d:
    d.config(fontsize=14, font='sans-serif')

    # Thévenin bron
    d += (Vth := elm.SourceV().label('Uth\n6V'))
    d += elm.ResistorIEC().right().label('Rth\n12Ω')
    d += elm.Line().right().at(...)
    # etc...

    d.save('thevenin_equivalent.svg')
```

Voor fasediagrammen/grafieken gebruik matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np

# Voorbeeld: Vermogensdriehoek
fig, ax = plt.subplots(figsize=(8, 6))

# Driehoek tekenen
P = [0, 50]  # kW
Q = [0, 30]  # kvar
S = np.sqrt(P[1]**2 + Q[1]**2)

# Plot
ax.arrow(0, 0, P[1], 0, head_width=2, head_length=3, fc='blue', ec='blue')
ax.arrow(0, 0, 0, Q[1], head_width=2, head_length=3, fc='red', ec='red')
ax.arrow(0, 0, P[1], Q[1], head_width=2, head_length=3, fc='green', ec='green')

ax.text(P[1]/2, -3, 'P (kW)', ha='center', fontsize=14)
ax.text(-5, Q[1]/2, 'Q (kvar)', va='center', fontsize=14)
ax.text(P[1]/2, Q[1]/2+3, 'S (kVA)', ha='center', fontsize=14)

# Hoek cos φ
angle = np.arctan(Q[1]/P[1])
ax.text(15, 3, f'cos φ = {P[1]/S:.2f}', fontsize=12)

plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.savefig('vermogensdriehoek_PQS.svg', bbox_inches='tight', dpi=300)
```

INSTALLEER INDIEN NODIG:
```bash
pip install schemdraw matplotlib numpy
```

KWALITEITSCHECKS per afbeelding:
- ✅ Alle labels leesbaar (min 12pt)
- ✅ Nederlandse teksten
- ✅ Kleuren consistent
- ✅ SVG format (scalable!)
- ✅ Transparante achtergrond waar zinvol
- ✅ Filesize check (<500KB)

OUTPUT:
- `images/circuits/` - Alle circuit diagrams
- `images/diagrams/` - Fasoren, vermogensdriehoeken, etc.
- `images/graphs/` - Resonantie curves, Bode plots
- `validation/phase2-generated-images-log.md` - Metadata per afbeelding
```

**Output directory:**
```
images/
├── circuits/           # Schemdraw SVG bestanden
├── diagrams/          # Matplotlib fasoren/driehoeken
├── graphs/            # Frequency responses, curves
└── validation/
    └── phase2-generated-images-log.md
```

### Agent 2.4: Afbeelding Kwaliteitscontrole

**Nieuwe chat:**

```
TAAK: Valideer ALLE gegenereerde afbeeldingen

Voor elke afbeelding:

1. VISUAL INSPECTION
   - Open afbeelding
   - Check: alle elementen zichtbaar?
   - Check: labels correct gespeld?
   - Check: waarden kloppen met kaart?

2. TECHNICAL VALIDATION
   - Circuit topologie correct?
   - Component symbolen volgens standaard?
   - Pijlen/polariteiten correct?

3. MOBILE TEST
   - Simuleer weergave op 375px breed scherm
   - Blijft alles leesbaar?

4. ACCESSIBILITY
   - Kleurenblind safe? (test met colorblind simulator)
   - Voldoende contrast?

GENEREER RAPPORT:

```markdown
## Afbeelding QC: [filename]

**✅ APPROVED** / **⚠️ MINOR FIXES** / **❌ REGENERATE**

**Checklist:**
- [ ] Technisch correct
- [ ] Labels compleet en correct
- [ ] Leesbaar op mobiel
- [ ] Colorblind safe
- [ ] Filesize OK

**Issues (indien van toepassing):**
1. [Probleem + voorgestelde fix]

**Fixes toegepast:**
[Beschrijf wat je hebt aangepast]
```

**Output:**
- `validation/phase2-image-QC-report.md`
```

---

## 🏗️ FASE 3: KAARTSTRUCTUUR OPTIMALISATIE

### Agent 3.1: Anki Card Type Designer

**Nieuwe chat:**

```
TAAK: Ontwerp OPTIMALE card templates voor Energietechniek deck

Gebaseerd op Anki best practices + analyse uit Stap 0.2

CREËER CARD TYPES:

1. **Basic-Energietechniek**
   - Front template
   - Back template
   - Styling CSS
   - JavaScript (indien nodig voor interactie)

2. **Calculation-Stepwise**
   - Front: Vraag + gegeven waardes
   - Back: Uitklapbare stappen (accordion?)
   - Styling: Duidelijke step numbering

3. **Concept-Visual**
   - Front: Vraag
   - Back: Uitleg + diagram
   - Image placement optimized

4. **Cloze-Formula** (voor formule memorization)
   - Template voor {{c1::deletion}} syntax
   - Math rendering

5. **Comparison-Card** (voor ster vs driehoek, etc.)
   - Side-by-side layout
   - Tabel support

OUTPUT: Voor elk card type:

```html
<!-- FRONT TEMPLATE -->
<div class="card front">
  <div class="question">
    {{Front}}
  </div>
  {{#Image}}
  <div class="image-container">
    {{Image}}
  </div>
  {{/Image}}
</div>

<!-- BACK TEMPLATE -->
<div class="card back">
  <div class="question">
    {{FrontSide}}
  </div>
  <hr>
  <div class="answer">
    {{Back}}
  </div>
  {{#Explanation}}
  <div class="explanation">
    <strong>Waarom:</strong> {{Explanation}}
  </div>
  {{/Explanation}}
</div>

<!-- STYLING -->
<style>
.card {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 18px;
  line-height: 1.6;
  color: #333;
  background: white;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.question {
  font-size: 20px;
  margin-bottom: 15px;
}

.image-container {
  text-align: center;
  margin: 20px 0;
}

.image-container img {
  max-width: 100%;
  height: auto;
  max-height: 500px;
}

/* LaTeX formules */
.latex {
  font-size: 1.2em;
  margin: 10px 0;
}

/* Stap-voor-stap berekeningen */
.step {
  margin: 10px 0;
  padding-left: 20px;
  border-left: 3px solid #0066cc;
}

.step-number {
  font-weight: bold;
  color: #0066cc;
}

/* Mobile responsive */
@media (max-width: 600px) {
  .card {
    font-size: 16px;
    padding: 15px;
  }

  .question {
    font-size: 18px;
  }
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  .card {
    background: #1e1e1e;
    color: #e0e0e0;
  }
}
</style>
```

TEST deze templates in echte Anki instance!

**Output:**
- `anki-templates/card-type-basic.html`
- `anki-templates/card-type-calculation.html`
- `anki-templates/card-type-visual.html`
- `anki-templates/card-type-cloze.html`
- `anki-templates/card-type-comparison.html`
- `anki-templates/README-IMPORT-INSTRUCTIONS.md`
```

### Agent 3.2: Card Grouping & Tagging Architect

**Nieuwe chat:**

```
TAAK: Ontwerp OPTIMALE tag hiërarchie en card grouping strategie

1. ANALYSEER HUIDIGE TAGS
   - Welke tags zijn te breed?
   - Welke tags zijn redundant?
   - Welke tags ontbreken?

2. ONTWERP HIËRARCHIE

```
Voorbeeld hiërarchische tag structuur:

energie::vermogen::werkelijk (P)
energie::vermogen::blind (Q)
energie::vermogen::schijnbaar (S)
energie::vermogen::driehoek::berekening
energie::vermogen::driehoek::concept

componenten::passief::weerstand
componenten::passief::condensator
componenten::passief::spoel
componenten::actief::transformator

netwerken::analyse::kirchhoff::knoop
netwerken::analyse::kirchhoff::maas
netwerken::analyse::thevenin
netwerken::analyse::norton

driefase::configuratie::ster
driefase::configuratie::driehoek
driefase::configuratie::conversie
driefase::berekening::vermogen
driefase::berekening::spanningsverlies

formules::basis::[formule naam]
formules::afgeleid::[formule naam]

niveau::1-basis
niveau::2-gemiddeld
niveau::3-gevorderd

prioriteit::examen-kritisch
prioriteit::veelvoorkomend
prioriteit::randgebied

type::begrip
type::berekening
type::toepassing
type::foutanalyse
```

3. MAPPING
   - Map elke bestaande kaart naar nieuwe tag structuur
   - Identificeer kaarten die in meerdere groepen thuishoren

4. STUDY PATHS
   - Definieer 5-7 study paths (filtered decks)
   - Bijv: "Week 1 - Fundamentals", "Pre-exam - Critical Only"

OUTPUT:
```markdown
# Tag Hiërarchie v2.0

## Volledige tag tree
[Complete hierarchical list]

## Mapping oude → nieuwe tags
| Oude tag | Nieuwe tag(s) | Aantal kaarten |
|----------|---------------|----------------|
| vermogen | energie::vermogen::werkelijk, type::berekening | 15 |
| ...      | ...           | ... |

## Study Path Definitions

### Path 1: Fundamentals (Week 1-2)
**Filter:** `tag:niveau::1-basis OR (tag:niveau::2-gemiddeld AND tag:prioriteit::examen-kritisch)`
**Kaarten:** ~25
**Volgorde:** [Aanbevolen volgorde]

### Path 2: Intermediate (Week 3-4)
[etc...]

## Implementation Script
```python
# Script om alle CSVs te updaten met nieuwe tags
import csv
import re

TAG_MAPPING = {
    'vermogen': ['energie::vermogen::werkelijk', 'type::berekening'],
    # ... etc
}

def update_tags(old_tags):
    new_tags = []
    for old in old_tags.split(';'):
        if old in TAG_MAPPING:
            new_tags.extend(TAG_MAPPING[old])
        else:
            new_tags.append(old)  # Keep unmapped tags
    return ';'.join(sorted(set(new_tags)))

# Process CSVs...
```
```
```

**Output:**
- `validation/phase3-tag-hierarchy-v2.md`
- `scripts/update_tags_to_v2.py`

### Agent 3.3: Card Splitting & Merging Optimizer

**Nieuwe chat:**

```
TAAK: Identificeer kaarten die moeten worden opgesplitst of samengevoegd

CRITERIA VOOR SPLITTING:
- Kaart test >1 onafhankelijk concept
- Antwoord >200 woorden (cognitive overload)
- Multi-step berekening die beter in 2-3 kaarten past

CRITERIA VOOR MERGING:
- 2 kaarten testen exact hetzelfde (alleen andere waarden)
- Triviaal gerelateerde concepten die beter samen passen

ANALYSEER ELKE KAART:

```markdown
## Kaart 42: [beschrijving]

**Actie:** KEEP / SPLIT / MERGE / REWRITE

**Rationale:**
[Waarom deze actie]

**Nieuwe structuur (indien SPLIT):**

### Kaart 42A
```csv
Front,Back,Tags
[Eerste deel]
```

### Kaart 42B
```csv
Front,Back,Tags
[Tweede deel]
```

**Merge met (indien MERGE):**
Kaart 42 + Kaart 67 → Nieuwe kaart 42
```

GENEREER COMPLETE NIEUWE CSV:
- `generated-cards/anki-deck-KENNIS-v3-OPTIMIZED.csv`
- `generated-cards/anki-deck-REKENEN-v3-OPTIMIZED.csv`

Met change log:
- `validation/phase3-card-restructuring-changelog.md`
```

**Output:**
- `generated-cards/anki-deck-KENNIS-v3-OPTIMIZED.csv`
- `generated-cards/anki-deck-REKENEN-v3-OPTIMIZED.csv`
- `validation/phase3-restructuring-log.md`

---

## ✅ FASE 4: MULTI-STAGE VALIDATIE & QUALITY ASSURANCE

### Agent 4.1: Technical Review Agent

**Nieuwe chat - Expert elektrotechniek:**

```
Je bent een NCOI examinator met PhD in elektrotechniek.

TAAK: Final technical review van ALLE v3-OPTIMIZED kaarten

VOOR ELKE KAART:

1. FORMULE VERIFICATIE
   - Wiskundig correct? ✅/❌
   - Afleiding klopt? ✅/❌
   - Eenheden dimensioneel consistent? ✅/❌
   - Numerieke waardes realistisch? ✅/❌

2. FYSISCHE INTERPRETATIE
   - Fysisch principe correct uitgelegd? ✅/❌
   - Valkuilen accuraat benoemd? ✅/❌
   - Praktische context klopt? ✅/❌

3. EXAM RELEVANCE
   - Zou deze vraag op NCOI examen kunnen? ✅/❌
   - Moeilijkheidsgraad past bij tag? ✅/❌
   - Vocabulaire professioneel Nederlands? ✅/❌

GEEF SCORE per kaart: A+ / A / B / C / F
- A+: Perfect, geen aanpassingen
- A: Excellent, minor polishing
- B: Goed, enkele verbeteringen nodig
- C: Matig, significante herziening nodig
- F: Fail, complete herschrijving nodig

OUTPUT:
```markdown
## Technical Review Summary

**Totaal kaarten:** [aantal]
**Scores:**
- A+: [aantal] ([%])
- A: [aantal] ([%])
- B: [aantal] ([%])
- C: [aantal] ([%])
- F: [aantal] ([%])

**Gemiddelde score:** [X.X/5.0]

## Per-Card Review

### Kaart 1: [beschrijving]
**Score:** A
**Issues:**
- Minor: Subscript notation niet consistent (Uth vs U_th)

**Fix:**
[Concrete suggestie]

---

[Repeat voor alle kaarten]
```

**Output:**
- `validation/phase4-technical-review.md`
- `generated-cards/anki-deck-KENNIS-v4-TECHNICAL-APPROVED.csv` (alleen A/A+ kaarten)
- `validation/phase4-cards-requiring-fixes.md` (B/C/F kaarten)
```

### Agent 4.2: Pedagogical Review Agent

**Nieuwe chat - Expert learning science:**

```
Je bent een expert in educational psychology en evidence-based learning.

TAAK: Review alle kaarten op LEERBAARHEID en RETENTIE-EFFECTIVITEIT

CRITERIA:

1. DESIRABLE DIFFICULTY
   - Is difficulty "just right" (niet te makkelijk, niet frustrerend)?
   - Stimuleert de kaart diep nadenken?
   - Score: 1-5

2. RETRIEVAL STRENGTH
   - Moeten studenten info ophalen uit geheugen (niet herkennen)?
   - Is de vraag niet te obvious?
   - Score: 1-5

3. ELABORATIVE INTERROGATION
   - Wordt "waarom" uitgelegd (niet alleen "wat")?
   - Zijn er connecties naar andere concepten?
   - Score: 1-5

4. DUAL CODING
   - Voor visuele kaarten: complementeren tekst + beeld elkaar?
   - Is er redundantie vermeden?
   - Score: 1-5 (N/A voor text-only)

5. SPACING-FRIENDLY
   - Is de kaart atomic genoeg voor SRS?
   - Geen context-dependencies?
   - Score: 1-5

OUTPUT:

```markdown
## Pedagogical Review - Kaart [nummer]

**Scores:**
- Desirable Difficulty: [1-5]
- Retrieval Strength: [1-5]
- Elaborative Interrogation: [1-5]
- Dual Coding: [1-5] / N/A
- Spacing-Friendly: [1-5]

**OVERALL: [average]/5.0**

**Strengths:**
- [Wat gaat goed]

**Improvements:**
- [Concrete voorstellen]

**Revised version (indien <4.0):**
```csv
[Verbeterde kaart]
```
```

SUMMARY STATISTICS:
- Gemiddelde score per dimensie
- Distribution plot van overall scores
- Top 10 beste kaarten (role models)
- Bottom 10 kaarten (need most work)

**Output:**
- `validation/phase4-pedagogical-review.md`
- `validation/phase4-pedagogy-statistics.md`
```

### Agent 4.3: Cross-Validation Agent (Consistency Check)

**Nieuwe chat:**

```
TAAK: Valideer CONSISTENTIE over alle kaarten heen

1. NOTATIONAL CONSISTENCY
   Check dat OVERAL hetzelfde wordt gebruikt:
   - φ voor fasehoek (niet θ, niet alpha)
   - Subscripts: U_th, I_N, Z_tot (consistent format)
   - Vectornotatie: overal hetzelfde (U⃗ of **U** of \vec{U})
   - Eenheden: kVA vs kva, kWh vs kW·h

   OUTPUT: Master notation guide + lijst inconsistenties

2. CONCEPT PROGRESSION
   - Zijn basis concepten geïntroduceerd VOOR complexe?
   - Check dependency graph: kaart X verwijst naar concept Y → is kaart Y eerdere in deck?

   OUTPUT: Dependency graph + aanbevolen volgorde

3. DIFFICULTY CALIBRATION
   - Zijn alle "niveau-1-basis" echt makkelijker dan "niveau-2-gemiddeld"?
   - Statistical check: zijn er outliers?

   OUTPUT: Difficulty distribution plot + hercategorisatie voorstellen

4. TAG COMPLETENESS
   - Heeft elke kaart minimaal:
     * 1 onderwerp tag (energie::*, componenten::*, etc.)
     * 1 niveau tag
     * 1 type tag
   - Ontbreken nuttige tags?

   OUTPUT: Tag coverage matrix

5. INFORMATION OVERLAP
   - Zijn er kaarten die 90%+ dezelfde info testen?
   - Merge candidates?

   OUTPUT: Similarity matrix + merge aanbevelingen

GENEREER:
```markdown
# Cross-Validation Report

## 1. Notational Inconsistencies Found: [aantal]

| Concept | Kaarten met notatie A | Kaarten met notatie B | Aanbeveling |
|---------|----------------------|----------------------|-------------|
| Fasehoek | 1,5,7 (φ) | 23,45 (θ) | Unify to φ |
| ... | ... | ... | ... |

## 2. Concept Dependency Issues: [aantal]

- Kaart 67 verwijst naar "Thévenin equivalent" maar kaart 38 (die Thévenin uitlegt) komt later in deck
  → **Fix:** Herorder kaarten of voeg mini-uitleg toe

## 3. Difficulty Miscalibrations: [aantal]

- Kaart 23 (tagged niveau-1) heeft moeilijkheid score 4.5/5 (te hoog voor basis)
  → **Fix:** Hertag naar niveau-2 OF vereenvoudig vraag

## 4. Tag Coverage Gaps: [aantal kaarten]

- Kaarten zonder type tag: [lijst]
- Kaarten zonder onderwerp tag: [lijst]

## 5. Duplicate Content: [aantal pairs]

- Kaart 12 & 34: 87% overlap → Merge voorstel
- ...

---

## Master Notation Guide (FINAL STANDAARD)

### Elektrische grootheden
- Spanning: U (hoofdletter)
- Stroom: I (hoofdletter)
- Impedantie: Z
- Fasehoek: φ (phi, niet theta)
- Frequentie: f
- Hoekfrequentie: ω (omega)

### Subscripts
- Thévenin: U_th, R_th (underscore, lowercase th)
- Norton: I_N, R_N (underscore, uppercase N)
- Fasoren: U_eff, I_eff (effectieve waarde)
- Lijn/fase: U_lijn, U_fase

### Vectoren
- Gebruik: \vec{U} in LaTeX
- Magnitude: |U| of U (zonder vector arrow)

### Eenheden
- Vermogen: kW, kvar, kVA (spatie voor getal)
- Energie: kWh, MWh
- Weerstand: Ω, kΩ, MΩ
- Capaciteit: µF, nF, pF
- Inductie: mH, µH

[Etc. voor ALLE notaties in deck]
```

**Output:**
- `validation/phase4-cross-validation-report.md`
- `validation/MASTER-NOTATION-GUIDE.md`
- `scripts/enforce_notation_consistency.py`
```

---

## 🎯 FASE 5: FINAL INTEGRATION & PACKAGE

### Agent 5.1: Final Assembly

**Nieuwe chat:**

```
TAAK: Assembleer de DEFINITIEVE, PRODUCTION-READY decks

INPUTS:
- Alle validated kaarten uit fase 4
- Alle gegenereerde afbeeldingen (phase 2)
- Nieuwe tag structuur (phase 3)
- Card templates (phase 3)
- Notation guide (phase 4)

PROCESS:

1. APPLY ALL FIXES
   - Implement alle aanbevelingen uit technical review
   - Implement alle aanbevelingen uit pedagogical review
   - Enforce master notation guide

2. INSERT ALL IMAGES
   - Update CSV met image references
   - Verify alle images bestaan
   - Check path correctness

3. APPLY NEW TAGS
   - Replace oude tags met hiërarchische v2 tags
   - Ensure completeness (every card has niveau, type, onderwerp)

4. OPTIMIZE CARD ORDER
   - Sort op basis van dependency graph
   - Binnen onderwerpen: basis → gemiddeld → gevorderd
   - Interleave gerelateerde concepten (niet block)

5. QUALITY CHECKS
   - UTF-8 encoding ✓
   - LaTeX syntax check ✓
   - HTML validation ✓
   - CSV escaping correct ✓
   - No broken image references ✓
   - Tag syntax valid ✓

6. GENERATE OUTPUTS

OUTPUT BESTANDEN:

```
generated-cards/FINAL/
├── NCOI-Energietechniek-MASTER-v5.0.csv          # Alles in 1 deck
├── NCOI-Energietechniek-KENNIS-v5.0.csv          # Kennis split
├── NCOI-Energietechniek-REKENEN-v5.0.csv         # Rekenen split
├── NCOI-Energietechniek-FUNDAMENTALS-v5.0.csv    # Alleen basis
├── NCOI-Energietechniek-EXAM-CRITICAL-v5.0.csv   # Alleen kritische kaarten
└── README-IMPORT-INSTRUCTIONS.md

images/FINAL/
├── circuits/       # Alle circuit SVGs
├── diagrams/       # Alle fasoren/vermogensdriehoeken
├── graphs/         # Alle curves
└── README-IMAGE-MANIFEST.md

anki-templates/FINAL/
├── card-types/
│   ├── Basic-Energietechniek.html
│   ├── Calculation-Stepwise.html
│   ├── Concept-Visual.html
│   ├── Cloze-Formula.html
│   └── Comparison-Card.html
├── shared-styling.css
└── README-TEMPLATE-INSTALLATION.md

documentation/FINAL/
├── COMPLETE-VALIDATION-REPORT.md      # Samenvatting alle fases
├── QUALITY-METRICS.md                 # Scores & statistics
├── STUDY-GUIDE.md                     # Hoe deck te gebruiken
├── TROUBLESHOOTING.md                 # Common issues
└── CHANGELOG.md                       # Alle wijzigingen vs v1.0
```

METADATA:
```markdown
# FINAL DECK METADATA

**Versie:** 5.0 (Quality Validated)
**Datum:** [datum]
**Totaal kaarten:** [aantal]
**Totaal afbeeldingen:** [aantal]
**Validation phases:** 4
**AI agents gebruikt:** 15+
**Quality score:** [X.X/5.0]

**Coverage:**
- Examendomeinen: 10/10 (100%)
- Formuleblad coverage: [X/47 formules]
- Oefenvragen coverage: [X/16 vragen]

**Quality metrics:**
- Technical accuracy: [score]
- Pedagogical effectiveness: [score]
- Visual quality: [score]
- Consistency: [score]

**Wijzigingen vs v1.0:**
- [aantal] kaarten toegevoegd
- [aantal] kaarten samengevoegd
- [aantal] kaarten opgesplitst
- [aantal] kaarten herschreven
- [aantal] afbeeldingen toegevoegd
- [aantal] tags herstructureerd
```
```

**Output:** Alles in `generated-cards/FINAL/`, `images/FINAL/`, etc.

### Agent 5.2: Documentation Generator

**Nieuwe chat:**

```
TAAK: Genereer COMPLETE gebruikersdocumentatie

1. STUDY GUIDE
```markdown
# NCOI Energietechniek - Complete Study Guide

## Hoe dit deck te gebruiken

### Installatie (step-by-step met screenshots)
[Gedetailleerde instructies]

### Aanbevolen studiepad (6 weken)

#### Week 1: Fundamentals
**Kaarten:** Filter `tag:niveau::1-basis`
**Nieuwe kaarten per dag:** 5
**Tijd:** 20-30 min/dag
**Onderwerpen:**
- Wet van Ohm
- Kirchhoff wetten
- Serie/parallel schakelingen

**Succesindicatoren:**
- [ ] 90%+ correct op eerste poging
- [ ] Kan formules uit hoofd
- [ ] Kan basis circuits analyseren

#### Week 2: Wisselstroom Basis
[etc...]

### Card types uitgelegd
[Visual guide per card type]

### Tag filtering
[Alle nuttige filters]

### Mobile study tips
[AnkiDroid/iOS specifieke tips]

### Troubleshooting
[Common problems + fixes]
```

2. QUALITY REPORT
```markdown
# Validation Report - NCOI Energietechniek Deck v5.0

## Executive Summary

Dit deck is door 15+ AI agents gevalideerd over 4 fases:
1. Content accuracy (3 agents)
2. Visual quality (4 agents)
3. Structure optimization (3 agents)
4. Multi-stage QA (3 agents)
5. Final integration (2 agents)

**Final scores:**
- Technical accuracy: 4.8/5.0
- Pedagogical effectiveness: 4.7/5.0
- Visual quality: 4.9/5.0
- Consistency: 4.9/5.0

**OVERALL: 4.83/5.0 (96.6%)**

## Detailed Metrics

### Per onderwerp

| Onderwerp | Kaarten | Avg Score | Images | Kritisch |
|-----------|---------|-----------|--------|----------|
| Vermogensleer | 15 | 4.9/5 | 8 | Ja |
| Driefase | 12 | 4.7/5 | 12 | Ja |
| ... | ... | ... | ... | ... |

### Difficulty distribution
[Chart/tabel]

### Tag coverage
[Matrix]

## Validation proces details
[Gedetailleerde beschrijving elke fase]

## Comparison vs v1.0

| Metric | v1.0 | v5.0 | Verbetering |
|--------|------|------|-------------|
| Kaarten met images | 0 | 67 | +67 |
| Avg technical score | 4.2 | 4.8 | +14% |
| Tag completeness | 78% | 100% | +22% |
| ... | ... | ... | ... |
```

3. CHANGELOG
```markdown
# Changelog v1.0 → v5.0

## Phase 1: Content Validation
- [datum] - 3 technical errors fixed in formulas
- [datum] - 7 kaarten herschreven voor clarity
- [datum] - 12 kaarten opgesplitst (te complex)

## Phase 2: Visual Content
- [datum] - 67 afbeeldingen gegenereerd
- [datum] - Alle afbeeldingen QC approved
- [datum] - Image placement optimized

## Phase 3: Structure
- [datum] - Tag hiërarchie v2.0 implemented
- [datum] - 5 card templates designed
- [datum] - Card order optimized (dependency graph)

## Phase 4: QA
- [datum] - Technical review: 4.8/5.0
- [datum] - Pedagogical review: 4.7/5.0
- [datum] - Consistency check: 23 notational fixes

## Phase 5: Integration
- [datum] - Final assembly completed
- [datum] - All QA approved
- [datum] - Documentation complete
```

**Output:**
- `documentation/FINAL/STUDY-GUIDE.md`
- `documentation/FINAL/VALIDATION-REPORT.md`
- `documentation/FINAL/CHANGELOG.md`
```

### Agent 5.3: Testing & Validation Agent

**Nieuwe chat:**

```
TAAK: Test ALLES in echte Anki environment

SETUP:
1. Installeer Anki desktop
2. Maak test profiel
3. Importeer FINAL decks

TESTS:

1. IMPORT TEST
   - [ ] CSV imports zonder errors
   - [ ] Alle kaarten tellen correct ([verwacht aantal])
   - [ ] Geen missing fields
   - [ ] Tags correct geparsed

2. RENDERING TEST
   - [ ] LaTeX formules renderen correct
   - [ ] HTML formatting werkt
   - [ ] Afbeeldingen tonen
   - [ ] Geen broken image links
   - [ ] Mobile view OK (resize window naar 375px)

3. FUNCTIONALITY TEST
   - [ ] Filtering werkt (`tag:niveau::1-basis`)
   - [ ] Search werkt
   - [ ] Kaarten kunnen worden beoordeeld (Again/Hard/Good/Easy)
   - [ ] Statistics genereren

4. TEMPLATE TEST
   - [ ] Importeer custom templates
   - [ ] Assign templates aan kaarten
   - [ ] Verify rendering met templates

5. SYNC TEST
   - [ ] Upload naar AnkiWeb
   - [ ] Sync naar AnkiDroid/iOS
   - [ ] Verify images synced
   - [ ] Test op mobiel device

GENEREER TEST RAPPORT:

```markdown
# Anki Integration Test Report

**Datum:** [datum]
**Anki versie:** [versie]
**OS:** Windows/Mac/Linux

## Import Results

**KENNIS deck:**
- ✅ Imported successfully
- Kaarten: [aantal]
- Warnings: [lijst indien van toepassing]

**REKENEN deck:**
- ✅ Imported successfully
- Kaarten: [aantal]
- Warnings: [lijst]

## Rendering Test

**LaTeX:**
- ✅ All formulas render correctly
- Tested: \( x^2 \), \[ \frac{1}{2} \], \( \vec{U} \)

**Images:**
- ✅ All [aantal] images display
- ✅ No broken links
- ⚠️ Issue: [indien problemen]

**Mobile:**
- ✅ Responsive layout works
- ✅ Text readable at 375px width
- ✅ Images scale appropriately

## Functionality

**Filtering:**
- ✅ `tag:niveau::1-basis` returns [aantal] cards
- ✅ `tag:prioriteit::examen-kritisch` returns [aantal] cards
- ✅ Combined filters work

**Search:**
- ✅ Search "Thévenin" finds [aantal] cards
- ✅ Search works in Front and Back fields

## Issues Found

1. [Issue description]
   - **Severity:** Critical/Major/Minor
   - **Fix:** [Wat gedaan]

2. [etc...]

## FINAL VERDICT

✅ **APPROVED FOR RELEASE** / ⚠️ **APPROVED WITH MINOR ISSUES** / ❌ **REQUIRES FIXES**

**Confidence level:** [percentage]%

**Recommendation:**
[Ready to use / Needs fixes / Requires retesting]
```

**Output:**
- `validation/FINAL-ANKI-INTEGRATION-TEST-REPORT.md`
- Screenshots van test results
```

---

## 📊 FASE 6: DELIVERABLES & HANDOFF

### Final Package Structure

```
NCOI-ENERGIETECHNIEK-ANKI-FINAL-v5.0/
│
├── 📁 DECKS/                          # Ready to import
│   ├── NCOI-Energietechniek-MASTER-v5.0.csv
│   ├── NCOI-Energietechniek-KENNIS-v5.0.csv
│   ├── NCOI-Energietechniek-REKENEN-v5.0.csv
│   ├── NCOI-Energietechniek-FUNDAMENTALS-v5.0.csv
│   ├── NCOI-Energietechniek-EXAM-CRITICAL-v5.0.csv
│   └── README-IMPORT.md
│
├── 📁 MEDIA/                          # All images
│   ├── circuits/                      # 40+ circuit diagrams
│   ├── diagrams/                      # 20+ phasor/power diagrams
│   ├── graphs/                        # 10+ frequency responses
│   └── IMAGE-MANIFEST.md
│
├── 📁 TEMPLATES/                      # Anki card templates
│   ├── Basic-Energietechniek.html
│   ├── Calculation-Stepwise.html
│   ├── Concept-Visual.html
│   ├── Cloze-Formula.html
│   ├── Comparison-Card.html
│   └── INSTALLATION-GUIDE.md
│
├── 📁 DOCUMENTATION/
│   ├── STUDY-GUIDE.md                 # How to use the deck
│   ├── VALIDATION-REPORT.md           # Quality metrics
│   ├── CHANGELOG.md                   # v1→v5 changes
│   ├── TROUBLESHOOTING.md             # Common issues
│   ├── TAG-REFERENCE.md               # All tags explained
│   ├── NOTATION-GUIDE.md              # Consistent notation
│   └── ANKI-BEST-PRACTICES.md         # Tips & tricks
│
├── 📁 VALIDATION/                     # Audit trail
│   ├── phase1-content-validation/
│   ├── phase2-visual-validation/
│   ├── phase3-structure-optimization/
│   ├── phase4-multi-stage-qa/
│   ├── phase5-integration-testing/
│   └── VALIDATION-SUMMARY.md
│
├── 📁 TOOLS/                          # Scripts used
│   ├── generate_images.py
│   ├── update_tags.py
│   ├── enforce_notation.py
│   ├── validate_csv.py
│   └── TOOLS-README.md
│
├── 📄 README.md                       # Main entry point
├── 📄 QUICK-START.md                  # TL;DR version
└── 📄 QUALITY-CERTIFICATE.md          # Validation seal

```

### Quality Certificate

```markdown
# NCOI Energietechniek Anki Deck - Quality Certificate

**Versie:** 5.0
**Validatie datum:** [datum]
**Validatie budget:** €[bedrag] (van €500 budget)

---

## ✅ CERTIFICATION

Dit Anki deck is gevalideerd door 15+ gespecialiseerde AI agents over een periode van [X dagen].

**Kwaliteitsnormen:**
- ✅ Technische correctheid: 4.8/5.0 (96%)
- ✅ Pedagogische effectiviteit: 4.7/5.0 (94%)
- ✅ Visuele kwaliteit: 4.9/5.0 (98%)
- ✅ Consistentie: 4.9/5.0 (98%)

**OVERALL SCORE: 4.83/5.0 (96.6%)**

---

## Validatie proces

### Phase 1: Content Accuracy (3 agents, [X tokens])
- Formule verificatie
- Fysische interpretatie check
- Terminologie validatie

### Phase 2: Visual Quality (4 agents, [X tokens])
- Bestaande afbeeldingen audit
- Missende afbeeldingen geïdentificeerd
- [aantal] nieuwe afbeeldingen gegenereerd
- Kwaliteitscontrole visuele content

### Phase 3: Structure Optimization (3 agents, [X tokens])
- Card templates ontworpen
- Tag hiërarchie v2.0 geïmplementeerd
- Card splitting/merging geoptimaliseerd

### Phase 4: Multi-Stage QA (3 agents, [X tokens])
- Technical review (expert level)
- Pedagogical review (learning science)
- Cross-validation (consistency)

### Phase 5: Integration (2 agents, [X tokens])
- Final assembly
- Documentation generation
- Anki integration testing

---

## Statistieken

**Kaarten:**
- Totaal: [aantal]
- Met afbeeldingen: [aantal] ([%]%)
- Difficulty levels: Basis ([aantal]), Gemiddeld ([aantal]), Gevorderd ([aantal])

**Afbeeldingen:**
- Totaal: [aantal]
- Circuits: [aantal]
- Diagrammen: [aantal]
- Grafieken: [aantal]

**Tags:**
- Unieke tags: [aantal]
- Hiërarchische niveaus: 3-4
- Tag completeness: 100%

**Coverage:**
- Examendomeinen: 10/10 (100%)
- Formuleblad: [X]/47 formules ([%]%)
- Oefenvragen: 16/16 (100%)

---

## Aanbevolen gebruik

**Studieduur:** 6-8 weken
**Nieuwe kaarten/dag:** 4-6
**Review tijd:** 30-45 min/dag
**Verwachte retentie:** 90%+ op examendag

**Studie paden:**
1. Complete deck (80 kaarten) - 20 dagen
2. Fundamentals first (40 kaarten) - 10 dagen → Rest (40 kaarten) - 10 dagen
3. KENNIS + REKENEN interleaved - 20 dagen
4. Exam-critical only (28 kaarten) - 7 dagen (pre-exam review)

---

## Garantie

Dit deck is gevalideerd volgens de hoogste kwaliteitsnormen.

**Indien je een fout vindt:**
1. Documenteer de fout (screenshot, kaart nummer)
2. Rapporteer via [contactmethode]
3. We committeren aan fix binnen 48 uur

**Verwachte exam performance:**
Bij dagelijks gebruik (30+ min) gedurende 4+ weken:
- 90%+ kans op voldoende
- 70%+ kans op goed of hoger

---

**Certified by:** Claude Code AI Validation Pipeline
**Signature:** [Digital signature / hash van final package]
**Date:** [datum]

```

---

## 🎓 BONUS: ADVANCED OPTIMIZATIONS (Optioneel, indien tijd/budget)

### Bonus Agent 1: Spaced Repetition Optimizer

```
TAAK: Optimaliseer kaart moeilijkheid voor Anki's algoritme

- Analyseer welke kaarten historisch moeilijk zijn (als je access hebt tot user data)
- Predict welke kaarten studenten zullen strugglen
- Stel custom "ease factors" voor per kaart
- Genereer pre-seeded scheduler data

OUTPUT: Anki collection.anki2 met optimale scheduling
```

### Bonus Agent 2: Interactive Elements Generator

```
TAAK: Maak interactive kaarten (JavaScript)

- Hover tooltips voor formule onderdelen
- Draggable phasor diagram animation
- Interactive circuit simulator (basic)
- Formula builder (drag-and-drop)

REQUIRES: Advanced Anki templating + JavaScript
```

### Bonus Agent 3: Audio Pronunciation Generator

```
TAAK: Genereer audio voor terminologie

- Text-to-speech voor moeilijke termen
- Nederlandse uitspraak
- Embed in kaarten

OUTPUT: MP3 bestanden + updated CSVs
```

### Bonus Agent 4: Adaptive Difficulty Recommender

```
TAAK: Machine learning model voor personalisatie

- Train model op user performance (indien data beschikbaar)
- Recommend focus areas per student
- Generate custom filtered decks

OUTPUT: Python script + model
```

---

## 🚀 EXECUTION PLAN

### Recommended Agent Deployment Order

**Week 1: Foundation (Stap 0 + Fase 1)**
1. Stap 0.1-0.3: Setup & research (1 dag)
2. Agent 1.1: Content validation (1 dag)
3. Agent 1.2: Didactic validation (1 dag)
4. Agent 1.3: Cross-reference (1 dag)

**Week 2: Visuals (Fase 2)**
5. Agent 2.1: Image audit (0.5 dag)
6. Agent 2.2: Missing images specs (0.5 dag)
7. Agent 2.3: Image generation (2 dagen - iteratief)
8. Agent 2.4: Image QC (0.5 dag)

**Week 3: Structure (Fase 3)**
9. Agent 3.1: Card templates (1 dag)
10. Agent 3.2: Tag architecture (1 dag)
11. Agent 3.3: Card optimization (1 dag)

**Week 4: QA (Fase 4)**
12. Agent 4.1: Technical review (1 dag)
13. Agent 4.2: Pedagogical review (1 dag)
14. Agent 4.3: Cross-validation (1 dag)

**Week 5: Integration (Fase 5)**
15. Agent 5.1: Final assembly (1 dag)
16. Agent 5.2: Documentation (1 dag)
17. Agent 5.3: Testing (1 dag)

**Week 6: Delivery (Fase 6)**
18. Package final deliverables (0.5 dag)
19. Quality certificate (0.5 dag)
20. Handoff & gebruikerstraining (optioneel)

**BONUS (Week 7-8, indien budget/tijd):**
21-24. Advanced optimizations

---

## 💰 BUDGET MANAGEMENT

**Estimated token usage:**
- Fase 0 (Research): ~500K tokens
- Fase 1 (Content): ~1M tokens
- Fase 2 (Visuals): ~800K tokens (image generation intensief)
- Fase 3 (Structure): ~600K tokens
- Fase 4 (QA): ~1.2M tokens
- Fase 5 (Integration): ~400K tokens
- Documentatie: ~300K tokens

**Total estimate: ~4.8M tokens**

Met Claude Opus pricing (~$15 per 1M tokens input, ~$75 per 1M tokens output):
- Geschat: €250-400 (ruim binnen €500 budget)

**Reserve voor:**
- Iteraties (fixes na QA)
- Bonus features
- Onverwachte complexiteit

---

## 📝 SELF-MODIFICATION INSTRUCTIONS

**Claude Web: Je mag en MOET dit plan aanvullen waar nodig!**

✅ **Toegestaan:**
- Extra validatiestappen toevoegen die je belangrijk vindt
- Meer agents deployen voor edge cases
- Diepere analyse waar je onzekerheden ziet
- Additional tools maken/downloaden
- Externe expertise raadplegen (web research)
- Anki community best practices integreren

✅ **Aangemoedigd:**
- Wees EXTRA kritisch op formules (liever 2x checken)
- Genereer MORE afbeeldingen dan gevraagd (if didactically useful)
- Maak tools voor automation waar mogelijk
- Documenteer je reasoning bij belangrijke beslissingen

✅ **Vereist:**
- Track je token usage (blijf binnen €500 budget)
- Documenteer ALLE wijzigingen vs originele plan
- Als je iets nieuws toevoegt: leg uit waarom in validation docs

❌ **Niet toegestaan:**
- Stappen overslaan om tijd/geld te besparen (KWALITEIT > KOSTEN)
- Aannames maken zonder verificatie
- Afbeeldingen/content genereren zonder QC
- Shortcuts nemen op validatie

---

## ✅ SUCCESS CRITERIA

Dit project is geslaagd als:

1. ✅ **Zero technical errors** - Geen enkele fout in formules/berekeningen
2. ✅ **100% visual coverage** - Alle kaarten die image nodig hebben, hebben een goede image
3. ✅ **4.5+ quality score** - Op alle dimensies (technical, pedagogical, visual, consistency)
4. ✅ **Anki import werkt** - Flawless import in Anki, alle features werken
5. ✅ **Complete documentatie** - User kan zonder hulp aan de slag
6. ✅ **Reproduceerbaar** - Alle scripts/tools gedocumenteerd en werkend
7. ✅ **Within budget** - <€500 aan tokens gebruikt
8. ✅ **100% bronmateriaal alignment** - ALLE kaarten traceerbaar naar formuleblad/Holmes/NCOI

**Bonus success:**
9. ✅ **90%+ student satisfaction** - Bij echte gebruikers (indien te meten)
10. ✅ **Reusable framework** - Proces kan worden hergebruikt voor andere vakken

---

## 🔒 FINAL VERIFICATION CHECKLIST (voor release v5.0)

**VOOR je v5.0 als "KLAAR" markeert, MOET je deze checklist doorlopen:**

### A. Bronmateriaal Verificatie (KRITISCH!)

- [ ] **Random sample test (20 kaarten):**
  - [ ] Trek willekeurig 20 kaarten
  - [ ] Check ELKE formule tegen Formuleblad v3 2023
  - [ ] Check ELKE term tegen Holmes boek
  - [ ] Check vraagstijl tegen Oefentoets
  - [ ] **Target: 20/20 kaarten traceerbaar naar bronnen**

- [ ] **Formuleblad coverage:**
  - [ ] Lijst alle formules gebruikt in deck
  - [ ] Verify ELKE formule staat op Formuleblad v3 2023
  - [ ] Check notatie 100% identiek (φ niet θ, Uth niet Uthevenin, etc.)
  - [ ] **Target: 100% formules van formuleblad**

- [ ] **Terminologie scan:**
  - [ ] Scan alle kaarten op Engelse termen
  - [ ] Verify elke Nederlandse term in Holmes/NCOI
  - [ ] Check geen nieuwe jargon geïntroduceerd
  - [ ] **Target: 0 Engelse termen (tenzij Holmes gebruikt), 100% NCOI-compatibel**

- [ ] **Examenstijl matching:**
  - [ ] Vergelijk 10 random kaarten met Oefentoets vragen
  - [ ] Check vraagformulering (niet te academisch/formeel)
  - [ ] Verify multiple choice waar relevant
  - [ ] **Target: Ononderscheidbaar van echte NCOI vragen**

- [ ] **Moeilijkheidsgraad kalibratie:**
  - [ ] Check 5 "niveau-basis" kaarten → makkelijker dan Oefenvragen
  - [ ] Check 5 "niveau-gevorderd" kaarten → vergelijkbaar met moeilijkste Oefentoets
  - [ ] **Target: Alle niveau tags accuraat vs. NCOI materiaal**

### B. Content Kwaliteit

- [ ] **Technical accuracy: 4.5+/5.0**
  - [ ] Technical review report shows avg 4.5+
  - [ ] Max 5% kaarten met minor issues
  - [ ] 0% kaarten met major issues
  - [ ] Alle formules dimensioneel correct

- [ ] **Pedagogical effectiveness: 4.5+/5.0**
  - [ ] Pedagogical review shows avg 4.5+
  - [ ] Retrieval strength sufficient
  - [ ] Cognitive load optimized

- [ ] **Consistency: 4.9+/5.0**
  - [ ] Master notation guide implemented
  - [ ] Zero notatie inconsistenties
  - [ ] Tag structure 100% complete

### C. Visual Content

- [ ] **Image coverage:**
  - [ ] Alle Priority 1 kaarten hebben images
  - [ ] Min 80% Priority 2 kaarten hebben images
  - [ ] Alle images QC approved

- [ ] **Image quality:**
  - [ ] Alle labels leesbaar (min 12pt)
  - [ ] Nederlandse tekst (geen Engels)
  - [ ] **Component waarden matchen kaart tekst EXACT**
  - [ ] **Circuit symbolen zoals in Holmes boek**
  - [ ] Colorblind safe
  - [ ] Mobile compatible (test op 375px)

### D. Anki Integration

- [ ] **Import test:**
  - [ ] CSV import zonder errors
  - [ ] Alle kaarten present
  - [ ] Tags correct geparsed
  - [ ] LaTeX rendert correct
  - [ ] Images tonen (0 broken links)

- [ ] **Functionality test:**
  - [ ] Filtering werkt (test 5 filters)
  - [ ] Search werkt
  - [ ] Templates applied correct
  - [ ] Mobile sync succesvol

### E. Documentation

- [ ] **Study Guide:**
  - [ ] 6-week studieplan compleet
  - [ ] Alle tags uitgelegd
  - [ ] Import instructies stap-voor-stap
  - [ ] Troubleshooting sectie

- [ ] **Validation Report:**
  - [ ] Alle 6 fases gedocumenteerd
  - [ ] Quality scores per dimensie
  - [ ] Changelog v1→v5
  - [ ] Bronverwijzingen per wijziging

- [ ] **Quality Certificate:**
  - [ ] Overall score 4.5+
  - [ ] Token usage gedocumenteerd
  - [ ] Bronmateriaal alignment verified
  - [ ] Test results included

### F. Budget & Timeline

- [ ] **Budget:**
  - [ ] Total spend <€500
  - [ ] Budget breakdown per fase
  - [ ] Reserve niet volledig gebruikt (flexibiliteit)

- [ ] **Timeline:**
  - [ ] Alle fases compleet
  - [ ] Progress tracker up to date
  - [ ] Learnings gedocumenteerd

---

## 🎯 BRONMATERIAAL SIGN-OFF (VERPLICHT!)

**VOORDAT v5.0 als KLAAR wordt gemarkeerd:**

```markdown
# BRONMATERIAAL ALIGNMENT CERTIFICAAT

Ik (Claude Web) certificeer dat:

✅ ALLE formules traceerbaar zijn naar Formuleblad Energietechniek v3 2023
✅ ALLE terminologie consistent is met Holmes 3e editie en NCOI materiaal
✅ ALLE vraagstellingen matchen NCOI examenstijl (Oefentoets/Oefenvragen)
✅ GEEN concepten toegevoegd buiten 10 NCOI examendomeinen
✅ GEEN afwijkingen van NCOI moeilijkheidsniveau
✅ ALLE afbeeldingen gebruiken symbolen/notatie zoals in bronmateriaal

**Random sample test resultaat:** [X/20 kaarten verified]
**Formuleblad coverage:** [X formules, 100% van formuleblad]
**Terminologie scan:** [0 Engelse termen, 100% NCOI-compatibel]
**Examenstijl matching:** [Ononderscheidbaar van NCOI vragen]

**Datum:** [datum]
**Agent:** Claude Web v[versie]
**Validation phases:** 6/6 compleet
**Quality score:** [X.X/5.0]

Deze deck is KLAAR voor gebruik en sluit 100% aan bij NCOI Energietechniek examen.
```

**Dit certificaat MOET aanwezig zijn in `documentation/FINAL/BRONMATERIAAL-ALIGNMENT-CERTIFICATE.md`**

---

## 🎯 FINAL NOTES

**Voor Claude Web die dit uitvoert:**

Je hebt €500 budget en carte blanche om dit deck perfect te maken.

**Prioriteiten (in volgorde):**
1. **Correctheid** - Geen fouten, punt.
2. **Leerbaarheid** - Studenten moeten hiermee ECHT beter worden
3. **Volledigheid** - Alles wat genoemd is, moet er zijn
4. **Professionaliteit** - Output is publicatie-ready
5. **Documentatie** - Iemand anders moet ermee kunnen werken

**Werkwijze:**
- Wees grondig, niet snel
- Validate, dan validate again
- Bij twijfel: extra check doen
- Documenteer je proces
- Maak het awesome

**Eindresultaat:**
Een Anki deck waar ik (en toekomstige NCOI studenten) met 100% vertrouwen mee het examen in kunnen, wetende dat ALLES klopt.

---

**Good luck, en maak er iets moois van! 🚀**

---

*Document versie: 1.0*
*Laatst bijgewerkt: [datum]*
*Auteur: Sjoerd van der Heide + Claude Code*
