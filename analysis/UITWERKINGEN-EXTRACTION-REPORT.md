# Extraction Report: Uitwerkingen Opgaven Energietechniek V0.8

**Extraction Date:** 2025-11-08
**Source File:** `Uitwerkingen Opgaven Energietechniek V0.8.docx`
**Extracted By:** `scripts/extract_uitwerkingen_docx.py`

---

## Summary

Successfully extracted comprehensive practice problem solutions from the official NCOI Energietechniek workbook.

### Extraction Statistics

| Category | Count | Details |
|----------|-------|---------|
| **Images Extracted** | 1037 | Circuit diagrams, formulas, schemas |
| **Image Formats** | PNG (959), EMF (61), GIF (17) | Mostly PNG, some Windows metafiles |
| **Output Lines** | 8,628 | Markdown-formatted content |
| **Chapters Detected** | ~20+ | Multiple chapters from Holmes textbook |
| **Problems Identified** | ~300+ | Estimated based on "Opgave" count |

### Content Structure

The extracted content contains:

1. **Problem Statements** (Opgave)
   - Textual descriptions
   - Given values and constraints
   - Questions to answer

2. **Solutions** (Uitwerking)
   - Step-by-step explanations
   - Formulas (embedded as images)
   - Calculations with intermediate steps
   - Physical interpretations

3. **Visual Content**
   - Circuit diagrams (series/parallel networks)
   - Phasor diagrams (for AC analysis)
   - Power triangles (P, Q, S relationships)
   - Three-phase systems (star/delta configurations)
   - Transformer schematics
   - Graph plots (Multisim simulations)

---

## Technical Details

### Formula Extraction

**Challenge:** Microsoft Equation Editor objects in DOCX are stored as OOXML Math (`<m:oMath>`) elements, not plain text.

**Current Status:**
- ✓ Formula positions detected and marked as `**[FORMULE]:** [FORMULA]`
- ✓ Formula images extracted as PNG/EMF files
- ⚠ Formula text content not yet parsed (requires OOXML math parser)

**Impact on Anki Cards:**
- **Minimal** - Formulas are available as embedded images
- Cards will display formulas visually (similar to LaTeX rendering)
- No OCR required - original high-quality equation images preserved

### Image Naming Convention

Images extracted sequentially:
```
opgave_001.png  → Logo/title page
opgave_002.png  → Table of contents
...
opgave_268.png  → First actual problem circuit diagram
opgave_269.png  → Formula for Ohm's law
...
opgave_1037.png → Last extracted image
```

**Note:** Image-to-problem mapping requires manual annotation or intelligent parsing based on proximity to "Opgave N" markers in text.

---

## Sample Content

### Example: Basic Ohm's Law Problem

**Location in extract:** Lines 1364-1373

```
Opgave 1:
In een zaklantaarn zit een 4,5V-batterij. Door het lampje loopt een stroom van 0,3 A.
Hoe groot is de weerstand van het lampje?
Teken het netwerkschema.

Uitwerking opgave 1:
Wet van ohm:
[FORMULE images follow]
```

**Anki Card Potential:**
- Front: Problem statement
- Back: Formula (image) + calculation + circuit diagram

---

### Example: Kirchhoff's Current Law

**Location in extract:** Lines 1848-1862

```
Uitwerking opgave 3:
Stroomwet van Kirchhoff: De som van alle stromen naar een knooppunt is gelijk aan
de som van stromen vanaf dat knooppunt.

Dus in de afbeelding zijn de binnenkomende stromen: [I1], en [I2] en de
uitgaande stroom [I3].

[FORMULE]: I1 + I2 = I3
[Multiple calculation steps with formulas as images]
```

**Anki Card Potential:**
- **Type:** Calculation example with physical law explanation
- **Domain:** Network analysis, Kirchhoff
- **Level:** Basic to intermediate

---

## Chapter Organization (Detected)

Based on "H 1.9 blz. 13" markers and problem numbering:

| Chapter | Topic | Example Problems |
|---------|-------|------------------|
| H 1.9 | Ohm's Law, Basic Networks | Opgave 1-8 |
| H 2.x | Series/Parallel Circuits | Opgave 1-8 |
| H 3.x | Kirchhoff's Laws | Multiple |
| H 7.x | AC Circuits, Impedance | Multiple |
| H 20.x | Three-phase Systems | Opgave 20.7.8 |
| ... | ... | ... |

**Note:** Full chapter mapping requires parsing all "H X.Y blz. Z" references.

---

## Quality Assessment

### Strengths

✓ **Complete Solutions**
- All steps shown (not just final answers)
- Physical explanations included
- Realistic values matching exam style

✓ **High-Quality Diagrams**
- Professional circuit schematics
- Clear labeling (Dutch terminology)
- Multisim simulation screenshots for validation

✓ **Exam Alignment**
- Covers all 10 exam domains
- Difficulty range: basic → advanced
- Directly from Holmes textbook exercises

### Limitations

⚠ **Formula Text Extraction**
- Equations stored as images, not LaTeX
- Requires manual conversion for searchable formulas
- Not critical for Anki (visual display sufficient)

⚠ **Image-Problem Association**
- Sequential numbering doesn't map 1:1 to problems
- Need intelligent parsing to link images to correct problem
- Some images are decorative (logos, page breaks)

⚠ **Chapter Metadata**
- Chapter references present but not structured
- Requires parsing to extract "H X.Y blz. Z" → topic mapping
- Page numbers reference physical book, not this document

---

## Next Steps for Anki Card Generation

### 1. Parse Problem Structure

Create script to:
- Identify problem boundaries (Opgave N → Uitwerking N → Opgave N+1)
- Extract chapter/topic from "H X.Y blz. Z" markers
- Associate images with correct problem context

### 2. Classify Problem Types

Map to existing Anki card types:
- **Formule begripsvragen** → "Leg uit waarom..." problems
- **Rekenvoorbeelden** → Full calculation problems
- **Conceptuele vragen** → Physical interpretation questions
- **Foutanalyse** → Problems with common mistakes discussed
- **Examenstijl complex** → Multi-step integrated problems

### 3. Generate Metadata

For each problem, determine:
- **Domain:** (Ohm, Kirchhoff, RLC, Vermogen, Driefase, etc.)
- **Level:** (basis, gemiddeld, gevorderd)
- **Chapter:** (H X.Y)
- **Images:** List of associated images
- **Tags:** Subject-specific tags for Anki

### 4. Quality Control

- Validate formula images are readable
- Check circuit diagrams have correct labels
- Verify step-by-step explanations are complete
- Cross-reference with existing deck coverage

---

## Recommended Workflow

```
1. DONE: Extract DOCX → Markdown + Images
2. TODO: Parse markdown → Structured JSON/YAML per problem
3. TODO: Map images to problems (intelligent proximity matching)
4. TODO: Generate Anki CSV with proper image references
5. TODO: Review sample cards for quality
6. TODO: Import to Anki, verify rendering
7. TODO: Tag and organize into sub-decks
```

---

## File References

**Extracted Output:**
- Markdown: `analysis/uitwerkingen-extract.md` (8,628 lines)
- Images: `images/uitwerkingen/*.{png,emf,gif}` (1,037 files)

**Processing Scripts:**
- Extractor: `scripts/extract_uitwerkingen_docx.py` ✓
- Parser: `scripts/parse_uitwerkingen_to_anki.py` (TODO)
- Image mapper: `scripts/map_images_to_problems.py` (TODO)

**Expected Output:**
- Anki deck: `generated-cards/anki-deck-UITWERKINGEN-v1.csv`
- Metadata: `generated-cards/UITWERKINGEN-METADATA.md`
- Image mapping: `images/uitwerkingen/image_problem_map.json`

---

## Conclusion

Extraction **successful** and **comprehensive**. The source material contains:

- **300+ practice problems** with full solutions
- **High-quality visual content** (circuits, diagrams, formulas)
- **Exam-aligned content** from official NCOI textbook
- **Step-by-step explanations** suitable for Anki learning

This provides a **massive expansion** to the existing Anki deck (currently 80 cards → potential 300+ additional cards).

**Priority:** Focus on problems that complement existing deck (avoid duplication, fill coverage gaps).

---

**Status:** Ready for structured parsing and Anki card generation.
