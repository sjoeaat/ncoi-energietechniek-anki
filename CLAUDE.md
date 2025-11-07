# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**NCOI Energietechniek - Anki Deck Generator**

This repository contains tools and materials for generating high-quality Anki flashcards for the NCOI Energietechniek exam. The project processes source materials (practice questions, formula sheets, exam-style questions) into structured CSV files ready for Anki import.

**Reference:** Elektrische Netwerken (3e editie, Paul Holmes)

---

## Repository Structure

```
ncoi-energietechniek-anki/
├── source-materials/          # PDF sources and HTML exam questions
│   ├── Formuleblad_Energietechniek_v3_2023.pdf
│   ├── Oefenvragen Energietechniek.pdf
│   ├── Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html
│   └── Energietechniek_Anki_Samenvatting.md
├── scripts/                   # Python extraction and processing tools
│   ├── extract_oefentoets.py
│   ├── extract_images_from_html.py
│   └── add_images_to_cards.py
├── analysis/                  # Extracted and analyzed content (markdown)
│   ├── formuleblad-extract.md
│   ├── oefenvragen-extract.md
│   ├── oefentoets-examenstijl.md
│   ├── FINAL-COVERAGE-REPORT.md
│   └── README.md
├── generated-cards/           # Output: Anki-ready CSV files
│   ├── anki-deck-KENNIS-v1.csv
│   ├── anki-deck-REKENEN-v1.csv
│   ├── anki-deck-KENNIS-v2-WITH-IMAGES.csv
│   ├── anki-deck-REKENEN-v2-WITH-IMAGES.csv
│   ├── DECK-METADATA.md
│   └── GENERATION-REPORT.md
└── images/                    # Circuit diagrams and schema's
    └── oefentoets/            # Extracted images from practice exam
        ├── vraag_01.png
        ├── vraag_02.png
        └── ...
```

---

## Key Concepts

### Card Types

1. **Formule begripsvragen** (31.3%) - Formula understanding with context
2. **Rekenvoorbeelden** (31.3%) - Complete calculation examples with steps
3. **Conceptuele vragen** (18.8%) - Physical interpretation questions
4. **Foutanalyse** (12.5%) - Common mistake analysis
5. **Examenstijl complex** (6.3%) - Multi-step integrated problems

### Exam Domains Covered (10 domains, 100% coverage)

1. Basiswetten & Netwerken (Ohm, Kirchhoff)
2. Thévenin & Norton equivalents
3. RLC-netwerken (serie/parallel)
4. Complexe impedantie & fasoren
5. Vermogensleer (P, Q, S, cos φ, compensatie)
6. Transformatoren & koppelfactor
7. Driefasensystemen (ster/delta)
8. Inductie & capaciteit
9. Energie, rendement, spanningsverlies
10. Resonantie & filters

### Deck Split Strategy

The deck is split into two separate CSV files for optimal learning:

- **KENNIS deck** (~40 cards): Conceptual understanding, definitions, physical meaning
- **REKENEN deck** (~40 cards): Calculation-intensive problems with full step-by-step solutions

This allows students to practice concepts separately from calculations.

---

## Working with Python Scripts

### Extract HTML Exam Questions

```bash
python scripts/extract_oefentoets.py
```

Extracts questions from HTML exam file into structured markdown.

### Extract Embedded Images

```bash
python scripts/extract_images_from_html.py
```

Extracts base64-encoded images from HTML and saves as PNG files.

### Add Images to Cards (Bulk Update)

```bash
python scripts/add_images_to_cards.py
```

Automatically inserts circuit diagrams and schema's into CSV cards based on intelligent pattern matching. Processes both KENNIS and REKENEN decks.

**Output:**
- `anki-deck-KENNIS-v2-WITH-IMAGES.csv`
- `anki-deck-REKENEN-v2-WITH-IMAGES.csv`

---

## CSV Format Specifications

### Field Structure

All CSV files use this format:

```csv
Front,Back,Tags
```

### Encoding & Formatting Rules

- **UTF-8 encoding** (required for LaTeX support)
- **LaTeX formulas:**
  - Inline: `\( U = I \cdot R \)`
  - Display: `\[ Z = \sqrt{R^2 + X^2} \]`
- **HTML formatting:**
  - Line breaks: `<br>` or `<br><br>` for spacing
  - Bold: `<b>Stap 1:</b>`
  - Images: `<img src="thevenin_equivalent.svg" style="max-width:600px;">`
- **Tags:** Semicolon-separated: `vermogen;examen-kritisch;niveau-gemiddeld`

### Example Card

```csv
Front,Back,Tags
"Een netwerk heeft <b>Uo = 6V</b> en <b>Ik = 0.5A</b>. Bereken de Thévenin weerstand en de stroom door Rload=10Ω","<b>Stap 1 - Thévenin weerstand:</b><br>Rth = Uo/Ik = 6/0.5 = <b>12Ω</b><br><br><b>Stap 2 - Stroom berekenen:</b><br>I = Uth/(Rth + Rload) = 6/(12+10) = <b>0.273A</b><br><br><i>Waarom:</i> Bij open klemmen meet je Uth, bij kortsluiting vloeit Ik. Thévenin equivalent gedraagt zich als spanningsbron Uth met serieweerstand Rth.","thevenin;netwerk-analyse;niveau-gemiddeld;examen-kritisch"
```

---

## Content Quality Standards

### Required Elements in Cards

1. **Complete step-by-step solutions** - Never skip intermediate steps
2. **Units throughout** - Include units in every calculation step
3. **Physical interpretation** - Explain "why" not just "what"
4. **Dutch terminology** - Use correct exam vocabulary
   - spanningsval (not voltage drop)
   - fasehoek (not phase angle)
   - schijnbaar vermogen (not apparent power)
   - wikkelverhouding (not turns ratio)
5. **Realistic rounding** - 2-3 significant figures
6. **Common pitfalls** - Explicitly warn about typical mistakes

### Validation Checklist for New Cards

- [ ] No trivial "what is formula X?" questions
- [ ] Dutch terminology consistent
- [ ] LaTeX syntax correct (`\(` not `$`)
- [ ] HTML properly escaped in CSV
- [ ] Tags include: onderwerp, niveau, and priority tags
- [ ] Calculation cards show all intermediate steps
- [ ] Physical meaning explained (not just math)
- [ ] Units present and correct
- [ ] Realistic values (230V/400V, standard component values)

---

## Important File References

### Analysis Documentation

- **`analysis/FINAL-COVERAGE-REPORT.md`** - Complete exam topic coverage verification
- **`analysis/oefentoets-examenstijl-summary.md`** - Exam style characteristics and recommendations
- **`analysis/formuleblad-extract.md`** - All 47 formulas from official formula sheet

### Generation Metadata

- **`generated-cards/DECK-METADATA.md`** - Statistics, import instructions, study recommendations
- **`generated-cards/GENERATION-REPORT.md`** - Generation process details
- **`generated-cards/DECK-SPLIT-OVERVIEW.md`** - Rationale for KENNIS/REKENEN split

### Image Integration

- **`KOPPELING-IMAGES-AAN-KAARTEN.md`** - Complete guide for linking circuit diagrams to cards
- **`images/oefentoets/image_mapping.txt`** - Maps extracted images to question numbers

---

## Anki Import Instructions

### Quick Import

1. Open Anki
2. File → Import
3. Select: `generated-cards/anki-deck-KENNIS-v2-WITH-IMAGES.csv`
4. Settings:
   - Type: **Basic**
   - Allow HTML in fields: **✓ YES** (critical!)
   - Field mapping: Front → Front, Back → Back, Tags → Tags
5. Import

Repeat for REKENEN deck.

### LaTeX Setup

LaTeX rendering requires:
- **Windows:** MiKTeX or TeX Live
- **Anki:** Tools → Preferences → LaTeX → Verify paths

Test with: `\( x^2 + y^2 = z^2 \)`

### Media Files (Images)

SVG/PNG files must be in Anki's media folder:
```
%APPDATA%\Anki2\[User]\collection.media\
```

Or use Anki's paperclip icon (📎) to attach images.

---

## Common Development Tasks

### Generate New Cards from Analysis Files

1. Read source material from `source-materials/`
2. Extract key concepts to `analysis/`
3. Create cards following quality standards above
4. Output to `generated-cards/` with appropriate filename
5. Update `DECK-METADATA.md` with statistics
6. Run validation checks

### Update Existing Cards

1. Read current CSV from `generated-cards/`
2. Make modifications (preserve UTF-8 encoding!)
3. Increment version number in filename
4. Document changes in `GENERATION-REPORT.md`

### Add Circuit Diagrams

Option 1: Manual (recommended for initial testing)
- Edit cards in Anki Browse mode
- Add `<img src="circuit.svg" style="max-width:600px;">`
- Test rendering

Option 2: Automated (for bulk updates)
- Update `IMAGE_RULES` in `scripts/add_images_to_cards.py`
- Run script to generate v2-WITH-IMAGES files
- Verify pattern matching worked correctly

---

## Image Placement Strategy

**Front (Question side):**
- Circuit is part of the problem statement
- Diagrams needed to understand the question
- Examples: Thévenin circuits, Kirchhoff networks, RLC schemas

**Back (Answer side):**
- Diagrams that explain the concept
- Power triangles (P, Q, S relationships)
- Phasor diagrams showing phase relationships
- Before/after comparisons (e.g., power factor compensation)

**Both:**
- Conversion problems (Norton ↔ Thévenin)
- Star-delta transformations

---

## Tag Taxonomy

### Primary Tags (Subject Matter)

- `vermogen`, `blindvermogen`, `schijnbaar-vermogen`, `cosphi`, `arbeidsfactor`
- `driefase`, `ster-configuratie`, `driehoek`, `ster-driehoek`, `lijnspanning`
- `impedantie`, `reactantie`, `capaciteit`, `inductie`, `complexe-rekening`
- `kirchhoff`, `knooppunt`, `maaswet`, `thevenin`, `norton`
- `transformator`, `koppelfactor`, `resonantie`
- `kabel`, `spanningsverlies`, `energie`, `rendement`

### Level Tags

- `niveau-basis` - Basic (22.5%)
- `niveau-gemiddeld` - Intermediate (52.5%)
- `niveau-gevorderd` - Advanced (25%)

### Priority Tags

- `examen-kritisch` - Most common on exams (35% of cards)

### Type Tags

- `formule`, `berekening`, `begrip`, `praktijk`, `foutanalyse`

---

## Special Considerations

### Dutch Language

All card content MUST be in Dutch. This is exam terminology and must match official NCOI materials.

### Formula Sheet References

Cards reference formulas from "Formuleblad Energietechniek v3 2023". Many cards include "Holmes-stijl" hints that simulate having the formula sheet available during the exam.

### Exam Preparation Strategy

The deck is designed for 20-40 days of daily practice:
- **Conservative:** 2 new cards/day, 15-20 min/day
- **Intensive:** 4 new cards/day, 30-45 min/day

Target retention: 90%+ on exam day

---

## Troubleshooting

### CSV Import Fails

- Verify UTF-8 encoding (not UTF-8 BOM or ANSI)
- Check for unescaped quotes in fields
- Ensure "Allow HTML in fields" is enabled

### LaTeX Not Rendering

- Install MiKTeX or TeX Live
- Restart Anki after installation
- Check: Tools → Preferences → LaTeX paths

### Images Not Showing

- Files must be in `collection.media` folder
- Use relative paths only (no `C:\...`)
- Check: Tools → Check Media → Fix

### Special Characters Broken

- Verify file is UTF-8 encoded
- Test characters: µ, φ, Ω, Δ, √
- Re-save with correct encoding if needed

---

## Development Workflow

When adding new content to this repository:

1. **Extract** - Use scripts to parse source materials
2. **Analyze** - Document findings in `analysis/`
3. **Generate** - Create cards following quality standards
4. **Validate** - Check against criteria above
5. **Document** - Update metadata files
6. **Version** - Increment version numbers appropriately

All generated cards should maintain the high quality bar established in v1.0:
- Complete explanations
- Physical interpretations
- Exam-realistic problems
- Dutch terminology
- Proper LaTeX/HTML formatting

---

## Version History

- **v1.0** (2025-11-06): Initial release - 80 cards (KENNIS + REKENEN split)
- **v2.0** (pending): WITH-IMAGES versions with automated circuit diagram insertion

---

**Status:** Production ready - Decks successfully cover all 10 exam domains with 90%+ expected retention
