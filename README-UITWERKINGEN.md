# Uitwerkingen Opgaven - Extractie & Anki Kaarten

**Status:** ✓ Extractie compleet, Anki kaarten gegenereerd
**Datum:** 2025-11-08

---

## Overzicht

Dit document beschrijft de extractie en verwerking van het DOCX bestand **"Uitwerkingen Opgaven Energietechniek V0.8.docx"** naar Anki flashcards.

### Bron Materiaal

- **Bestand:** `source-materials/Uitwerkingen Opgaven Energietechniek V0.8.docx`
- **Auteur:** Ir. JGM van der Zanden
- **Versie:** V0.8 (Update december 2024/2025)
- **Inhoud:** Volledige uitwerkingen van opgaven uit Holmes textbook "Elektrische Netwerken"

---

## Extractie Resultaten

### Stap 1: DOCX → Markdown + Images

**Script:** [`scripts/extract_uitwerkingen_docx.py`](scripts/extract_uitwerkingen_docx.py)

**Output:**
- **Markdown:** [`analysis/uitwerkingen-extract.md`](analysis/uitwerkingen-extract.md) (8,628 regels)
- **Afbeeldingen:** [`images/uitwerkingen/`](images/uitwerkingen/) (1,037 bestanden)

**Afbeelding Types:**
- PNG: 959 bestanden (circuit diagrams, formules, grafieken)
- EMF: 61 bestanden (Windows metafiles, mogelijk conversie nodig)
- GIF: 17 bestanden (animaties/diagrammen)

**Details:** Zie [`analysis/UITWERKINGEN-EXTRACTION-REPORT.md`](analysis/UITWERKINGEN-EXTRACTION-REPORT.md)

---

### Stap 2: Markdown → Gestructureerde Data

**Script:** [`scripts/parse_uitwerkingen_to_structured.py`](scripts/parse_uitwerkingen_to_structured.py)

**Output:**
- **YAML:** [`analysis/uitwerkingen-structured.yaml`](analysis/uitwerkingen-structured.yaml) (33 opgaven)
- **Summary:** [`analysis/uitwerkingen-parsed-summary.md`](analysis/uitwerkingen-parsed-summary.md)

**Gestructureerde Data per Opgave:**
```yaml
- id: '3'
  chapter_ref:
    chapter: 1
    section: 9
    page: 13
  opgave: "Bij een knooppunt geldt: ..."
  opgave_images: [opgave_268.png, opgave_269.png, ...]
  uitwerking: "Stroomwet van Kirchhoff: ..."
  uitwerking_images: [opgave_356.png, ...]
  formulas_count: 14
  domains: [basiswetten, kirchhoff]
  difficulty: gemiddeld
```

**Automatische Classificatie:**
- Domeinen: Basiswetten, Kirchhoff, Thévenin/Norton, Transformatoren, etc.
- Moeilijkheid: basis (6%), gemiddeld (79%), gevorderd (15%)
- Hoofdstukken: H 1.9, H 3.11

---

### Stap 3: Gestructureerde Data → Anki Cards

**Script:** [`scripts/generate_anki_from_uitwerkingen.py`](scripts/generate_anki_from_uitwerkingen.py)

**Output:**
- **Anki CSV:** [`generated-cards/anki-deck-UITWERKINGEN-v1.csv`](generated-cards/anki-deck-UITWERKINGEN-v1.csv) (25 kaarten)
- **Metadata:** [`generated-cards/UITWERKINGEN-METADATA.md`](generated-cards/UITWERKINGEN-METADATA.md)

**Kaart Statistieken:**
- **Totaal kaarten:** 25 (van 33 opgaven, 8 overgeslagen wegens incomplete data)
- **Gemiddeld moeilijk:** 80%
- **Gevorderd:** 20%
- **Examen-kritisch:** 4 kaarten (Thévenin/Norton)

---

## Domein Verdeling

| Domein | Kaarten | Percentage |
|--------|---------|------------|
| Basiswetten (Ohm, spanning, stroom) | 25 | 100% |
| Netwerk-analyse (serie/parallel) | 21 | 84% |
| Berekeningen (formules) | 16 | 64% |
| Kirchhoff (knoop/maas) | 10 | 40% |
| Thévenin/Norton | 4 | 16% |
| Transformatoren | 2 | 8% |
| Inductie | 1 | 4% |

---

## Kaart Structuur

### Front (Vraag)

```
Hoofdstuk 1.9

Bij een knooppunt geldt:
I1 + I2 = I3

Bereken I1, I2 en I3.

[Circuit diagram image]
[Given values image]
```

### Back (Antwoord)

```
Uitwerking:

Stroomwet van Kirchhoff: De som van alle stromen naar een knooppunt
is gelijk aan de som van stromen vanaf dat knooppunt.

Stappenplan & Berekeningen:
[Step-by-step solution images]
[Formula images]
[Final answer image]

Bron: Holmes Hoofdstuk 1.9, blz. 13
```

### Tags

```
uitwerkingen;holmes;basiswetten;kirchhoff;netwerk-analyse;
niveau-gemiddeld;h1-9;berekening
```

---

## Anki Import Instructies

### 1. Kopieer Afbeeldingen naar Anki Media Folder

**Doel folder:**
```
%APPDATA%\Anki2\[Your Profile]\collection.media\
```

**Te kopiëren:**
```bash
# Kopieer ALLE bestanden uit:
images/uitwerkingen/*.png
images/uitwerkingen/*.gif

# EMF bestanden (optioneel - converteer eerst naar PNG):
images/uitwerkingen/*.emf
```

**Tip voor EMF conversie:**
```bash
# Met ImageMagick (als geïnstalleerd):
magick mogrify -format png images/uitwerkingen/*.emf
```

### 2. Importeer CSV in Anki

1. Open Anki
2. **File → Import**
3. Selecteer: `generated-cards/anki-deck-UITWERKINGEN-v1.csv`
4. **Instellingen:**
   - Type: **Basic**
   - **Allow HTML in fields: ✓ JA** (kritisch!)
   - Field mapping: `Front → Front`, `Back → Back`, `Tags → Tags`
5. Klik **Import**

### 3. Verifieer Rendering

- Open **Browse** (Ctrl+B)
- Filter op: `deck:"UITWERKINGEN"`
- Check of:
  - ✓ Afbeeldingen zichtbaar zijn
  - ✓ HTML formatting correct is
  - ✓ Tags aanwezig zijn

---

## Studie Aanbevelingen

### Dagelijkse Planning

**Conservatief (2 nieuwe kaarten/dag):**
- Totale tijd: ~12 dagen (1-2 weken)
- Studietijd: 15-20 min/dag

**Intensief (5 nieuwe kaarten/dag):**
- Totale tijd: ~5 dagen
- Studietijd: 30-45 min/dag

### Studie Volgorde

1. **Start:** `tag:niveau-gemiddeld` (20 kaarten)
2. **Daarna:** `tag:niveau-gevorderd` (5 kaarten)
3. **Focus:** `tag:examen-kritisch` (Thévenin/Norton)

### Tag Filtering in Anki

**Per domein oefenen:**
```
tag:kirchhoff           → 10 kaarten (knoop/maas wetten)
tag:thevenin-norton     → 4 kaarten (equivalent circuits)
tag:netwerk-analyse     → 21 kaarten (serie/parallel)
```

**Per hoofdstuk herhalen:**
```
tag:h1-9                → Basis elektrische netwerken
tag:h3-11               → Geavanceerde netwerk analyse
```

---

## Kwaliteit & Beperkingen

### Sterke Punten

✓ **Officieel Materiaal**
- Directe uitwerkingen van Holmes textbook opgaven
- Door docent (Ir. JGM van der Zanden) goedgekeurd
- Realistische examenniveau

✓ **Volledige Oplossingen**
- Elk stappenplan volledig uitgewerkt
- Fysische interpretatie aanwezig
- Nederlandse terminologie (NCOI exam conform)

✓ **Hoogwaardige Visualisaties**
- Professionele circuit diagrams
- Duidelijke formule afbeeldingen
- Multisim simulatie screenshots

### Beperkingen

⚠ **Afbeelding-intensief**
- 1037 afbeeldingen totaal (~500 MB)
- Sommige kaarten hebben 10+ afbeeldingen
- Kan laadtijd Anki beïnvloeden

⚠ **Formules als Afbeeldingen**
- Wiskundige vergelijkingen zijn PNG/EMF, niet LaTeX
- Niet doorzoekbaar als tekst
- Voor Anki gebruik is dit geen probleem (rendering goed)

⚠ **Incomplete Parsing**
- Van ~90 opgaven in DOCX zijn er 33 geparsed
- 25 kaarten gegenereerd (8 overgeslagen wegens incomplete data)
- **Potentieel:** Nog 60+ opgaven te extraheren met verbeterde parser

⚠ **EMF Bestanden**
- 61 Windows metafiles (EMF format)
- Mogelijk niet in alle Anki versies zichtbaar
- Aanbeveling: Converteer naar PNG

---

## Volgende Stappen (Optioneel)

### Parser Verbeteren (Meer Kaarten)

Het DOCX bevat ~90 opgaven, maar de huidige parser herkent er maar 33.

**Gemiste patronen:**
- Sub-opgaven: "Opgave 1a", "Opgave 1b", etc.
- Gegroepeerde opgaven: "Opgave 6, 7 en 8:"
- Variaties in "Uitwerking" formatting

**Script aanpassen:**
- `scripts/parse_uitwerkingen_to_structured.py`
- Regex patterns uitbreiden voor meer varianten
- Potentieel: 60+ extra kaarten

### EMF → PNG Conversie

**Met ImageMagick:**
```bash
cd images/uitwerkingen
magick mogrify -format png *.emf
```

**Met Python (Pillow + wand):**
```python
from wand.image import Image

for emf_file in Path('images/uitwerkingen').glob('*.emf'):
    with Image(filename=emf_file) as img:
        img.format = 'png'
        img.save(filename=emf_file.with_suffix('.png'))
```

### Kaarten Splitsen

Sommige kaarten hebben veel afbeeldingen (10+). Overwegen om te splitsen:
- Kaart 1: Opgave → Aanpak/Eerste stap
- Kaart 2: Volledige uitwerking → Eindantwoord

---

## Bestandsstructuur

```
ncoi-energietechniek-anki/
├── source-materials/
│   └── Uitwerkingen Opgaven Energietechniek V0.8.docx  ← Origineel
│
├── scripts/
│   ├── extract_uitwerkingen_docx.py       ← Stap 1: DOCX extractie
│   ├── parse_uitwerkingen_to_structured.py ← Stap 2: Structureren
│   └── generate_anki_from_uitwerkingen.py  ← Stap 3: Anki generatie
│
├── analysis/
│   ├── uitwerkingen-extract.md             ← Raw markdown (8628 lines)
│   ├── uitwerkingen-structured.yaml        ← 33 opgaven gestructureerd
│   ├── uitwerkingen-parsed-summary.md      ← Statistieken
│   └── UITWERKINGEN-EXTRACTION-REPORT.md   ← Technisch rapport
│
├── images/
│   └── uitwerkingen/                       ← 1037 afbeeldingen
│       ├── opgave_001.png
│       ├── opgave_002.png
│       └── ... (tot opgave_1037)
│
├── generated-cards/
│   ├── anki-deck-UITWERKINGEN-v1.csv       ← 25 Anki kaarten
│   └── UITWERKINGEN-METADATA.md            ← Import instructies
│
└── README-UITWERKINGEN.md                  ← Dit bestand
```

---

## Changelog

### v1.0 (2025-11-08) - Eerste Release

**Extractie:**
- ✓ 1037 afbeeldingen geëxtraheerd (PNG, EMF, GIF)
- ✓ 8628 regels markdown content
- ✓ Formules gedetecteerd en gemarkeerd

**Structurering:**
- ✓ 33 opgaven geparsed en geclassificeerd
- ✓ Automatische domein detectie (10 domeinen)
- ✓ Moeilijkheidsgraad geschat (basis/gemiddeld/gevorderd)

**Anki Kaarten:**
- ✓ 25 kaarten gegenereerd
- ✓ HTML formatting met afbeeldingen
- ✓ Tags per domein, niveau, hoofdstuk
- ✓ Metadata en import instructies

---

## Contact & Vragen

Voor vragen over:
- **Extractie scripts:** Zie comments in Python bestanden
- **Anki import:** Zie `UITWERKINGEN-METADATA.md`
- **Content kwaliteit:** Vergelijk met origineel DOCX

---

**Status:** ✓ Productie-klaar - Anki kaarten ready for import
