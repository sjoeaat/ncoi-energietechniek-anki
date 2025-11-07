# Koppeling Images aan Anki Kaarten - Praktische Handleiding

**Doel:** Schema's en diagrammen koppelen aan de juiste Anki kaarten voor NCOI Energietechniek

**Datum:** 2025-11-06

---

## 🎯 Overzicht: Welke Kaart → Welke Image?

### Snelle Referentie Tabel

| Kaart # | Onderwerp | Image(s) | Plaatsing |
|---------|-----------|----------|-----------|
| 1 | Driefase ster fasespanning | `driefase_120graden.svg` | Back |
| 2 | Vermogensdriehoek FOUT | `vermogensdriehoek_PQS.svg` | Back |
| 3, 4 | Capacitieve reactantie | - | - |
| 5 | Motor vermogen | `vermogensdriehoek_PQS.svg` | Back |
| 6 | RL-serie DC vs AC | `rl_series.svg` | Front |
| 7 | Effectieve waarde | `effectieve_waarde_RMS.svg` | Back |
| 8, 10 | Transformator wikkelverhouding | `transformer_basic.svg` | Front |
| 9, 11 | Parallel/Serie weerstanden | - | - |
| 10 | Kirchhoff knooppunt | `kirchhoff_node_3branches.svg` | Front |
| 12 | Inductieve reactantie | - | - |
| 13, 14 | Energie, rendement | - | - |
| 15 | Condensator faseverschuiving | `faseverschuiving_ijlen.svg` | Back |
| 16 | **Blindvermogen compensatie** | `vermogenscompensatie.svg` | Back |
| 17 | Kabelweerstand | - | - |
| 18 | Kirchhoff maaswet | `kirchhoff_mesh_2loops.svg` | Front |
| 19 | Zelfinductie | - | - |
| 20 | Complexe impedantie parallel | `complexe_impedantie.svg` | Back |
| 21 | **Spanningsverlies driefase** | `threephase_star_load.svg` | Front |
| 22 | Vermogensdriehoek PQS | `vermogensdriehoek_PQS.svg` | Front+Back |
| 25 | **Serie resonantie LC** | `series_resonance.svg` | Front |
| 27 | Driefase generator | `threephase_star.svg` | Front |
| 28 | Arbeidsfactor cos φ betekenis | `vermogensdriehoek_PQS.svg` | Back |
| 29 | Koppelfactor transformator | `transformer_with_load.svg` | Back |
| 35 | Vermogen P, Q, S definities | `vermogensdriehoek_PQS.svg` | Back |
| 36 | RC-serie impedantie | `rc_series.svg` | Front |
| 38 | **Thévenin equivalent** | `thevenin_equivalent.svg` | Front |
| 39 | Driefase motor driehoek | `threephase_delta.svg` | Front |
| 40 | Inductieve reactantie betekenis | `impedantie_driehoek.svg` | Back |
| 45 | LC-serie capacitief/inductief | `rlc_series.svg` | Front |
| 46 | Driefase ster resistief | `threephase_star_load.svg` | Front |
| 47 | Serie vs parallel resonantie | `series_resonance.svg` + `parallel_resonance.svg` | Back |
| 51 | Parallel RC-kring | `rc_series.svg` (aangepast) | Front |
| 53 | Spoel inschakelgedrag | - | Back (tijddomein grafiek) |
| 60 | Spoel uitschakelen spanningspiek | - | Back |
| 62 | **Norton ↔ Thévenin** | `thevenin_equivalent.svg` + `norton_equivalent.svg` | Back |
| 68 | Driefase motor ster→driehoek | `threephase_star.svg` + `threephase_delta.svg` | Front |
| 70, 75, 79 | Resonantie Q-factor | `series_resonance.svg` | Front |

**Totaal:** ~35-40 kaarten krijgen images (van 80)

---

## 📋 Methode 1: Handmatig Toevoegen (Aanbevolen voor Start)

### Stap-voor-Stap

**1. Open Anki en ga naar Browse (B)**

**2. Zoek de kaart** (gebruik zoekbalk):
```
tag:thevenin
```
of
```
front:*Thévenin*
```

**3. Selecteer de kaart en klik "Edit" (Enter)**

**4. Voeg image toe:**
- **Methode A:** Klik op paperclip icon (📎) → Selecteer SVG
- **Methode B:** Druk **Ctrl+Shift+A** → Browse naar image
- **Methode C:** Type direct HTML:
  ```html
  <img src="thevenin_equivalent.svg" style="max-width:600px;">
  ```

**5. Plaats image op juiste plek:**
- **Front (Vraag):** Als circuit onderdeel is van de opgave
- **Back (Antwoord):** Als diagram de uitleg ondersteunt

**6. Save en test** (preview met spacebar)

### Voorbeeld: Kaart 38 - Thévenin

**Voor (zonder image):**
```
Front: Een netwerk heeft Uo = 6V en Ik = 0.5A. Bereken Rth...
Back: Rth = Uo/Ik = 6/0.5 = 12Ω
```

**Na (met image):**
```
Front:
<img src="thevenin_equivalent.svg" style="max-width:600px;">
<br><br>
Een netwerk heeft Uo = 6V en Ik = 0.5A. Bereken Rth en stroom door Rload=10Ω

Back:
<b>Stap 1 - Thévenin weerstand:</b><br>
Rth = Uo/Ik = 6/0.5 = 12Ω
<br><br>
<b>Stap 2 - Stroom:</b><br>
I = Uth/(Rth + Rload) = 6/(12+10) = 0.273A
```

---

## 🤖 Methode 2: Automatisch met Script (Bulk Update)

### Python Script: `scripts/add_images_to_cards.py`

Ik maak een script dat automatisch de juiste images toevoegt aan de CSV:

```python
import csv

# Mapping: kaart onderwerp → image bestand
IMAGE_MAPPING = {
    # Thevenin/Norton
    'thevenin': 'thevenin_equivalent.svg',
    'norton': 'norton_equivalent.svg',

    # RLC circuits
    'rlc.*serie': 'rlc_series.svg',
    'rlc.*parallel': 'rlc_parallel.svg',
    'rc.*serie': 'rc_series.svg',
    'rl.*serie': 'rl_series.svg',

    # Kirchhoff
    'kirchhoff.*knoop': 'kirchhoff_node_3branches.svg',
    'kirchhoff.*maas': 'kirchhoff_mesh_2loops.svg',

    # Driefase
    'driefase.*ster': 'threephase_star.svg',
    'driefase.*driehoek': 'threephase_delta.svg',

    # Vermogen
    'vermogensdriehoek': 'vermogensdriehoek_PQS.svg',
    'compensatie': 'vermogenscompensatie.svg',

    # Resonantie
    'resonantie.*serie': 'series_resonance.svg',
    'resonantie.*parallel': 'parallel_resonance.svg',

    # Fasoren
    'eenheidscirkel': 'eenheidscirkel_sin_cos_tan.svg',
    'faseverschuiving': 'faseverschuiving_ijlen.svg',
}

def add_image_to_card(front, back, tags):
    """Voeg image toe op basis van tags en content"""

    # Check welke image past
    for pattern, image in IMAGE_MAPPING.items():
        if pattern in tags.lower() or pattern in front.lower():
            # Voeg image toe aan Front of Back
            if 'bereken' in front.lower():
                # Rekenvraag → image op Front
                front = f'<img src="{image}" style="max-width:600px;"><br><br>' + front
            else:
                # Kennisvraag → image op Back
                back = back + f'<br><br><img src="{image}" style="max-width:500px;">'

            break

    return front, back

# Verwerk CSV
with open('anki-deck-energietechniek-v1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    cards = list(reader)

for card in cards:
    card['Front'], card['Back'] = add_image_to_card(
        card['Front'], card['Back'], card['Tags']
    )

# Schrijf nieuwe CSV
with open('anki-deck-energietechniek-v2-WITH-IMAGES.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Front', 'Back', 'Tags'])
    writer.writeheader()
    writer.writerows(cards)
```

**Run:**
```bash
cd "C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\scripts"
python add_images_to_cards.py
```

---

## 📖 Methode 3: Selectief met Anki Browser (Efficiënt)

### Voor specifieke onderwerpen bulk updaten:

**1. Filter kaarten in Browser:**
```
tag:thevenin OR tag:norton
```
(Resultaat: ~7 kaarten)

**2. Selecteer alle gevonden kaarten** (Ctrl+A)

**3. Edit → Find and Replace** (Ctrl+F)

**4. Find:**
```
</b><br><br><b>
```

**5. Replace:**
```
</b><br><br><img src="thevenin_equivalent.svg" style="max-width:600px;"><br><br><b>
```

**6. Replace All in Selected**

**Herhaal voor andere onderwerpen!**

---

## 🎨 Styling Templates

### Basis Image Styling

```html
<!-- Standaard (600px breed) -->
<img src="circuit.svg" style="max-width:600px;">

<!-- Klein (400px) -->
<img src="diagram.svg" style="max-width:400px;">

<!-- Groot (800px voor complexe circuits) -->
<img src="complex.svg" style="max-width:800px;">

<!-- Centered -->
<div style="text-align:center;">
  <img src="circuit.svg" style="max-width:600px;">
</div>

<!-- Met caption -->
<figure>
  <img src="circuit.svg" style="max-width:600px;">
  <figcaption>Figuur 1: Thévenin equivalent circuit</figcaption>
</figure>
```

### Side-by-Side (Voor vergelijkingen)

```html
<!-- Ster vs Driehoek -->
<div style="display:flex; gap:20px;">
  <div>
    <img src="threephase_star.svg" style="width:300px;">
    <p><b>Ster</b></p>
  </div>
  <div>
    <img src="threephase_delta.svg" style="width:300px;">
    <p><b>Driehoek</b></p>
  </div>
</div>
```

---

## 🔍 Specifieke Koppeling per Onderwerp

### Thévenin & Norton (7 kaarten)

**Kaarten:** 38, 44, 58, 62

**Images:**
- `thevenin_equivalent.svg` - Basis Thévenin circuit
- `norton_equivalent.svg` - Norton stroombron

**Plaatsing:**
- Front: Bij berekeningsvragen
- Back: Bij conversie Norton↔Thévenin (toon beide!)

**Voorbeeld HTML:**
```html
<!-- Kaart 62: Norton ↔ Thévenin -->
Back:
<b>Norton:</b><br>
IN = 2A, RN = 8Ω<br><br>

<b>Thévenin equivalent:</b><br>
UTH = IN × RN = 2 × 8 = 16V<br>
RTH = RN = 8Ω<br><br>

<div style="display:flex; gap:20px;">
  <img src="norton_equivalent.svg" style="width:280px;">
  <img src="thevenin_equivalent.svg" style="width:280px;">
</div>
```

### Vermogensdriehoek (12 kaarten)

**Kaarten:** 2, 5, 16, 22, 28, 35, 49, 59, 68, 69

**Images:**
- `vermogensdriehoek_PQS.svg` - P, Q, S driehoek
- `vermogenscompensatie.svg` - Voor/na compensatie

**Plaatsing:**
- Bij begrip (wat is P/Q/S): Back
- Bij berekeningen: Front OF Back (afhankelijk van vraagstelling)

**Voorbeeld HTML:**
```html
<!-- Kaart 16: Blindvermogen compensatie -->
Back:
<b>Voor compensatie:</b><br>
cos φ₁ = 0.75 → Q₁ = 44.1 kvar<br><br>

<b>Na compensatie:</b><br>
cos φ₂ = 0.92 → Q₂ = 21.3 kvar<br><br>

<b>Condensatorbank:</b><br>
Qc = Q₁ - Q₂ = 22.8 kvar<br><br>

<img src="vermogenscompensatie.svg" style="max-width:700px;">
```

### Driefase Systemen (12 kaarten)

**Kaarten:** 1, 21, 27, 39, 46, 50, 68, 78

**Images:**
- `threephase_star.svg` - Ster Y schakeling
- `threephase_delta.svg` - Driehoek Δ schakeling
- `threephase_star_load.svg` - Ster met belasting
- `driefase_120graden.svg` - Fasoren 120° verschuiving
- `sterschakeling_fasoren.svg` - Ster fasoren met √3

**Plaatsing:**
- Front: Bij schakelingsvragen
- Back: Bij uitleg faseverschuiving

**Voorbeeld HTML:**
```html
<!-- Kaart 68: Motor ster→driehoek omschakeling -->
Front:
Een driefase motor schakelt van driehoek naar ster.
Wat gebeurt met het vermogen (zelfde lijnspanning)?<br><br>

<div style="display:flex; gap:10px;">
  <img src="threephase_delta.svg" style="width:250px;">
  <span style="font-size:30px;">→</span>
  <img src="threephase_star.svg" style="width:250px;">
</div>
```

### Resonantie (5 kaarten)

**Kaarten:** 25, 47, 70, 75, 79

**Images:**
- `series_resonance.svg` - Serie LC resonantie
- `parallel_resonance.svg` - Parallel LC tank

**Plaatsing:**
- Front: Circuit bij berekeningen
- Back: Resonantiecurve/Q-factor uitleg

**Voorbeeld HTML:**
```html
<!-- Kaart 70: RLC resonantie -->
Front:
<img src="series_resonance.svg" style="max-width:500px;">
<br><br>
Bereken resonantiefrequentie f₀ voor:<br>
R=10Ω, L=50mH, C=20µF<br>
Wat is Z bij resonantie?
```

### Kirchhoff Wetten (10 kaarten)

**Kaarten:** 10, 18, (+ meer in REKENEN deck)

**Images:**
- `kirchhoff_node_3branches.svg` - Knooppunt met stromen
- `kirchhoff_mesh_2loops.svg` - Maaslus met spanningen

**Plaatsing:**
- Altijd Front (circuit is de vraag!)

**Voorbeeld HTML:**
```html
<!-- Kaart 10: Kirchhoff knooppunt -->
Front:
<img src="kirchhoff_node_3branches.svg" style="max-width:500px;">
<br><br>
Stromen: I₁=4A (in), I₂=6A (uit), I₃=2A (uit), I₄=7A (uit), I₅=1A (in)<br>
Bereken Ix (horizontaal)
```

### Goniometrie & Fasoren (conceptueel)

**Kaarten:** 7, 15, 23, 28, 40, 53

**Images:**
- `eenheidscirkel_sin_cos_tan.svg` - **Belangrijkste!**
- `radialen_vs_graden.svg` - Conversie
- `faseverschuiving_ijlen.svg` - Voorijlen/achterijlen
- `effectieve_waarde_RMS.svg` - RMS vs piek
- `RLC_serie_fasoren.svg` - Impedantie vectoren

**Plaatsing:**
- Bijna altijd Back (uitleg)

**Voorbeeld HTML:**
```html
<!-- Kaart 15: Condensator faseverschuiving -->
Back:
Stroom ijlt 90° voor omdat i = C·du/dt<br><br>

<b>Visueel:</b><br>
<img src="faseverschuiving_ijlen.svg" style="max-width:600px;">
<br><br>
<b>In eenheidscirkel:</b><br>
<img src="eenheidscirkel_sin_cos_tan.svg" style="max-width:500px;">
```

---

## ✅ Checklist: Koppeling Compleet

Controleer of je deze kaarten hebt geüpdatet:

### Prioriteit 1 (MUST HAVE - 15 kaarten)
- [ ] Kaart 38: Thévenin equivalent
- [ ] Kaart 16: Blindvermogen compensatie
- [ ] Kaart 22: Vermogensdriehoek berekening
- [ ] Kaart 2: Foutanalyse vermogensoptelling
- [ ] Kaart 70/75/79: Resonantie Q-factor (3x)
- [ ] Kaart 10, 18: Kirchhoff (2x)
- [ ] Kaart 1, 27, 39, 46: Driefase (4x)
- [ ] Kaart 15: Eenheidscirkel sin/cos/tan
- [ ] Kaart 25: Serie resonantie

### Prioriteit 2 (SHOULD HAVE - 20 kaarten)
- [ ] Kaart 6: RL-serie
- [ ] Kaart 36: RC-serie
- [ ] Kaart 45: LC-serie
- [ ] Kaart 62: Norton↔Thévenin
- [ ] Kaart 8, 29: Transformatoren (2x)
- [ ] Kaart 47: Serie vs parallel resonantie
- [ ] Kaart 68: Ster-driehoek motor
- [ ] Kaart 28, 35, 40: Vermogen/impedantie begrip (3x)
- [ ] Kaart 5, 59: Vermogen berekeningen (2x)
- [ ] Overige driefase kaarten (5x)

### Prioriteit 3 (NICE TO HAVE - 10-15 kaarten)
- [ ] Alle overige RLC vragen
- [ ] Fasediagram kaarten
- [ ] Complexe impedantie kaarten

**Totaal minimaal:** 35 kaarten met images
**Optimaal:** 50-60 kaarten met images

---

## 🚀 Aanbevolen Workflow

### Week 1: Handmatig Starten (5-10 kaarten/dag)
1. Begin met Prioriteit 1 kaarten
2. Gebruik Methode 1 (handmatig in Anki)
3. Test rendering op desktop + mobiel
4. Pas styling aan indien nodig

### Week 2: Versnellen (15-20 kaarten/dag)
1. Gebruik Methode 3 (Find & Replace in Browser)
2. Verwerk hele onderwerpen tegelijk
3. Tag toegevoegde kaarten: `has-image`

### Week 3: Finaliseren
1. Run script (Methode 2) voor resterende kaarten
2. Quality check alle images
3. Sync naar AnkiWeb
4. Test op mobiele devices

---

## 💡 Tips & Tricks

### DO's ✅
- ✅ Test altijd eerst met 1 kaart
- ✅ Gebruik `max-width` voor responsive images
- ✅ Check rendering op mobiel (AnkiDroid/iOS)
- ✅ Backup voor bulk changes (File → Export)
- ✅ Gebruik `<br><br>` voor witruimte rond images

### DON'Ts ❌
- ❌ Te grote images (>1MB) gebruiken
- ❌ Absolute paths (`C:\...`) in HTML
- ❌ Image op Front EN Back (kies 1)
- ❌ Vergeten media sync aan te zetten

---

## 🔧 Troubleshooting

### "Image niet zichtbaar in Anki"
**Oorzaken:**
1. Bestand niet in `collection.media` folder
2. Verkeerde bestandsnaam (case-sensitive!)
3. Media sync uitgeschakeld

**Oplossing:**
```
Tools → Check Media → Fix
Tools → Preferences → Network → ✓ Sync media
```

### "Image te groot/klein"
**Oplossing:**
```html
<!-- Te groot -->
<img src="..." style="max-width:600px;">

<!-- Te klein -->
<img src="..." style="max-width:800px; min-width:400px;">
```

### "CSV import faalt bij bulk update"
**Oplossing:**
- UTF-8 encoding gebruiken
- Quotes escapen: `""` binnen velden
- Test met klein bestand eerst

---

## 📞 Support

**Documentatie:**
- `README-IMAGE-INTEGRATIE.md` - Quick start
- `ANKI-MEDIA-IMPORT-INSTRUCTIE.md` - Uitgebreide handleiding
- `IMAGE-MAPPING.md` - Image per onderwerp

**Scripts:**
- `scripts/add_images_to_cards.py` - Automatische koppeling
- `scripts/generate_circuit_diagrams.py` - Schema generatie

---

**Status:** Ready to use - Start met Prioriteit 1 kaarten (15 stuks)!

**Geschatte tijd:**
- Handmatig: 15 kaarten = 30-45 min
- Automatisch: 80 kaarten = 5-10 min

**Veel succes met de visuele upgrade van je Anki deck!** 🎨📚
