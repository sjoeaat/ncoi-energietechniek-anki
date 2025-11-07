# Oefentoets Examenstijl - Analyse Overzicht

**Datum:** 2025-11-06
**Bron:** `Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html`

---

## Gegenereerde Bestanden

### 1. Hoofdanalyse
**Locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\oefentoets-examenstijl.md`

**Bevat:**
- Alle 16 examenvragen volledig uitgeschreven
- Vraagstelling, opties, hints per vraag
- Onderwerp categorisatie

**Gebruik:** Gedetailleerde referentie voor Anki deck creatie

---

### 2. Samenvatting & Aanbevelingen
**Locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\oefentoets-examenstijl-summary.md`

**Bevat:**
- Executive summary (16 vragen, onderwerpen coverage)
- Examenstijl karakteristieken analyse
- Moeilijkheidsgraad inschatting (niveau 1/2/3)
- Typische valkuilen & aandachtspunten
- Benodigde formules per onderwerp
- Aanbevelingen voor Anki deck structuur
- Tagging strategie suggesties

**Gebruik:** Strategisch overzicht voor deck ontwerp

---

### 3. Geëxtraheerde Afbeeldingen
**Locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\images\oefentoets\`

**Bestanden:**
```
vraag_01.png  -> Vraag 1  (Aderdikte schema)           [24 KB]
vraag_02.png  -> Vraag 2  (Condensatorbrug netwerk)     [21 KB]
vraag_03.png  -> Vraag 4  (LC-resonantie circuit)       [132 KB]
vraag_04.png  -> Vraag 5  (Ster-Driehoek netwerk)       [84 KB]
vraag_05.png  -> Vraag 6  (RL-serie toongenerator)      [138 KB]
vraag_06.png  -> Vraag 14 (3-fasen generator schema)    [70 KB]
```

**Totaal:** 6 afbeeldingen (470 KB)

**Mapping:** `image_mapping.txt` bevat vraag nummers

**Gebruik:** Integreer in Anki cards met afbeeldingen

---

## Scripts

### 1. Vraag Extractie Script
**Locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\scripts\extract_oefentoets.py`

**Functionaliteit:**
- Parse HTML oefentoets
- Extraheer alle vragen met metadata
- Genereer gestructureerde markdown output
- Identificeer onderwerpen en formaat

**Gebruik:**
```bash
python scripts/extract_oefentoets.py
```

---

### 2. Image Extractie Script
**Locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\scripts\extract_images_from_html.py`

**Functionaliteit:**
- Extraheer base64 encoded images uit HTML
- Decode en sla op als PNG bestanden
- Map images naar vraag nummers
- Genereer image mapping file

**Gebruik:**
```bash
python scripts/extract_images_from_html.py
```

---

## Belangrijkste Bevindingen

### Onderwerpen Verdeling (16 vragen)
1. **Basiselektrotechniek:** 5 vragen (31%)
   - Kirchhoff, Thévenin, Ster-Driehoek, Aderdikte
2. **Wisselstroomleer:** 5 vragen (31%)
   - Reactantie, Resonantie, Vermogen, cosφ-correctie
3. **Driefasensystemen:** 2 vragen (13%)
   - Spanningsverlies, Lijnspanningen
4. **Transformatoren:** 2 vragen (13%)
   - Wikkelverhouding, Kernmateriaal
5. **Energietoepassingen:** 2 vragen (13%)
   - Zonnepanelen, cosφ-correctie praktijk

### Moeilijkheidsgraad
- **Niveau 1 (Basis):** 3 vragen (19%)
- **Niveau 2 (Gemiddeld):** 8 vragen (50%)
- **Niveau 3 (Gevorderd):** 5 vragen (31%)

### Examenstijl Kenmerken
✅ "Holmes-stijl" hints bij elke vraag (formuleblad simulatie)
✅ Realistische praktijkwaarden (230/400V, NEN normen)
✅ Mix van multiple choice en open vragen
✅ Stapsgewijze berekeningen vereist
✅ Valkuilen expliciet gesignaleerd in hints

---

## Vervolgstappen

### Volgende Fase: Anki Deck Creatie

1. **Card Templates Ontwerpen**
   - Type A: Formule cloze cards
   - Type B: Multiple choice cards
   - Type C: Berekening cards (met stappen)
   - Type D: Image occlusion cards (schema's)

2. **Tags Implementeren**
   ```
   #examenstijl
   #niveau-1 / #niveau-2 / #niveau-3
   #basiselektrotechniek / #wisselstroomleer / etc.
   #formuleblad
   #valkuil
   #kirchhoff / #thevenin / #resonantie / etc.
   ```

3. **Import Script**
   - Converteer markdown naar Anki import format
   - Link afbeeldingen
   - Genereer hints velden
   - Automatisch tagging

4. **Validatie**
   - Cross-check met studiehandleiding
   - Moeilijkheidsgraad kalibratie
   - Peer review

---

## Aandachtspunten

⚠️ **Vraag 16 (Juist/Onjuist):**
- Heeft geen volledige vraagstelling in extractie
- Handmatig HTML inspecteren nodig
- Stellingen apart analyseren

⚠️ **Afbeeldingen:**
- 6 vragen hebben schema's/circuits
- Moeten goed leesbaar zijn in Anki
- Mogelijk vergroten of annoteren

⚠️ **Holmes Hints:**
- Zeer uitgebreid (leerzaam maar lang)
- Mogelijk inkorten voor Anki cards
- Of als "toon hint" extra veld

---

## Contact & Documentatie

**Project:** NCOI Energietechniek Anki Deck
**Repository:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\`

**Gerelateerde Documenten:**
- `source-materials/` - Originele HTML oefentoets
- `analysis/` - Deze analyse bestanden
- `images/oefentoets/` - Geëxtraheerde afbeeldingen
- `scripts/` - Python extractie scripts

---

**Laatste update:** 2025-11-06
