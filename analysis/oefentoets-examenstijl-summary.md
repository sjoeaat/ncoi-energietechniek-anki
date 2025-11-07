# Oefentoets Examenstijl - Samenvatting & Analyse

**Bestand:** `Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html`
**Datum analyse:** 2025-11-06
**Output locatie:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\oefentoets-examenstijl.md`

---

## Executive Summary

### Algemeen
- **Aantal vragen:** 16
- **Formaat:** Examenstijl (NCOI Energietechniek)
- **Versie:** v6 (2025-10-21 17:56)
- **Bevat:** Gedetailleerde "Holmes-stijl" hints bij elke vraag

### Vraagformaten
- **Multiple choice:** 1 vraag (6%)
  - Vraag 1: Aderdikte
- **Open vragen / Berekeningen:** 15 vragen (94%)
  - Meeste vragen vereisen stapsgewijze berekeningen
  - Vraag 16 bevat Juist/Onjuist stellingen

---

## Onderwerpen Coverage

### 1. Basiselektrotechniek (5 vragen - 31%)
- **Kirchhoff wetten:**
  - Vraag 3: Knooppuntregel (KCL)
  - Vraag 8: Spanningslus / Maasregel (KVL)
- **Weerstandsberekeningen:**
  - Vraag 1: Aderdikte berekenen (ρ·L/A)
- **Netwerkvereenvoudiging:**
  - Vraag 5: Ster-Driehoek transformatie
  - Vraag 7: Thévenin equivalent

### 2. Wisselstroomleer (5 vragen - 31%)
- **Reactantie & Impedantie:**
  - Vraag 2: Condensatorbrug (serie/parallel C)
  - Vraag 4: LC-resonantie (f₀ = 1/(2π√LC))
  - Vraag 6: RL-serie met faseverschuiving
- **Vermogensleer:**
  - Vraag 9: Blindvermogen Q (S² = P² + Q²)
  - Vraag 12: cosφ-correctie met condensatorbank

### 3. Driefasensystemen (2 vragen - 13%)
- **Vraag 13:** Spanningsverlies 3-fase + 2%-norm
- **Vraag 14:** Lijnspanningen berekenen (√3 factor)

### 4. Transformatoren (2 vragen - 13%)
- **Vraag 10:** Wikkelverhouding (N₂/N₁ = U₂/U₁)
- **Vraag 15:** Voor- en nadelen magnetische kern (kennisvraag)

### 5. Energietoepassingen (2 vragen - 13%)
- **Vraag 11:** Zonnepanelen jaaropbrengst (PV-systeem)
- **Vraag 12:** cosφ-correctie (praktijk)

---

## Examenstijl Kenmerken

### 1. Vraagstelling
**Typische structuur:**
```
[Context/Gegeven] → [Opdracht] → [Formuleblad hint]
```

**Voorbeelden:**
- "Gegeven: ρ_Cu = 0,0178 Ω·mm²/m. Gebruik R = ρ·L/A."
- "Een transformator heeft U₁ = 6000 V en U₂ = 800 V. Bepaal N₂."
- "Toets of voldaan wordt aan de norm: maximaal 2% spanningsverlies"

### 2. "Holmes-stijl" Hints
**Elk vraag bevat gedetailleerde hints die:**
- Relevante formules opsommen
- Stapsgewijze aanpak suggereren
- Valkuilen signaleren

**Voorbeelden:**
- "Holmes-stijl hint (formuleblad): R = ρ·L/A (ρ(Cu) ≈ 0,0178 Ω·mm²/m). 1-fase: effectieve lengte = heen + terug."
- "Holmes-stijl hint (formuleblad): U_th = open-klemspanning. R_th: spanningsbronnen kort; stroombronnen open."
- "Holmes-stijl hint: E_jaar ≈ instraling (kWh/m²·jr) × oppervlak × η."

### 3. Formules & Notatie
**Consistent gebruik van:**
- Griekse letters: ρ, φ, ω, Δ, Σ
- Subscripts: U₁, I_fase, Z_C, f₀
- Eenheden: Ω, A, V, W, var, VA (met k/M prefixen)
- Complexe getallen: j (niet i)

### 4. Praktijkgerichtheid
**Vragen linken theorie aan praktijk:**
- Vraag 1: Aderdikte voor installatiewerk
- Vraag 11: PV-systeem energieneutraliteit
- Vraag 13: 2%-norm spanningsverlies (NEN normering)
- Vraag 12: cosφ-correctie driefasenmotor

---

## Moeilijkheidsgraad Inschatting

### Niveau 1: Basis (3 vragen - 19%)
**Direct formule toepassen:**
- Vraag 1: Aderdikte (R = ρ·L/A)
- Vraag 9: Blindvermogen (√(S² - P²))
- Vraag 10: Transformator wikkelverhouding

### Niveau 2: Gemiddeld (8 vragen - 50%)
**Meerdere stappen, formulemanipulatie:**
- Vraag 3: Kirchhoff knooppunt
- Vraag 4: LC-resonantie
- Vraag 6: RL-serie met faseverschuiving
- Vraag 8: Spanningslus
- Vraag 11: Zonnepanelen opbrengst
- Vraag 12: cosφ-correctie
- Vraag 13: Spanningsverlies 3-fase
- Vraag 14: Lijnspanningen

### Niveau 3: Gevorderd (5 vragen - 31%)
**Netwerkvereenvoudiging, vectorberekeningen:**
- Vraag 2: Condensatorbrug (balans principe)
- Vraag 5: Ster-Driehoek transformatie
- Vraag 7: Thévenin equivalent
- Vraag 15: Transformator kernmateriaal (conceptueel)
- Vraag 16: Juist/Onjuist (diverse onderwerpen)

---

## Typische Valkuilen & Aandachtspunten

### 1. Eenheden & Conversies
**Let op:**
- mm² ↔ m² conversie (vaak nodig bij ρ·L/A)
- kW vs MW (Vraag 11: 40 MWh verbruik!)
- mH, μF → standaard eenheden voor ω-berekeningen
- Fase vs lijn spanning/stroom (√3 factor)

### 2. Effectieve Lengtes
**Vraag 1 signaleert:**
- "25 m heen en 25 m terug = effectief 50 m"
- Vergeet niet: stroom gaat heen én terug!

### 3. Tekenkeuze & Polariteiten
**Kirchhoff vragen:**
- Vraag 3: "met jouw pijlen" → consistentie vereist
- Vraag 8: "noteer polariteiten consequent"
- Negatieve uitslag = tegengestelde richting

### 4. Standaardwaarden
**Vraag 1:**
- Berekende 3,56 mm² → kies "eerstvolgende standaard-mm²" (= 4 mm²)
- Niet exact berekende waarde!

### 5. Fase vs Lijn (3-fasensystemen)
**Vraag 13 & 14:**
- Check: is gegeven U_fase (230V) of U_lijn (400V)?
- |U_lijn| = √3·|U_fase|
- Spanningsverlies: bereken per fase, check norm

### 6. Resonantie (Serie vs Parallel)
**Vraag 4:**
- Serie LC: minimale Z bij f₀
- Parallel LC: maximale Z bij f₀

### 7. Vermogensdriehoek
**Vraag 9 & 12:**
- S² = P² + Q² (NIET S = P + Q!)
- tanφ voor Q_C berekening bij cosφ-correctie

---

## Benodigde Formules per Onderwerp

### Basiselektrotechniek
```
R = ρ·L/A                    [Weerstand]
ΣI = 0                       [KCL - Kirchhoff knooppunt]
ΣU = 0                       [KVL - Kirchhoff maas]
U_th, R_th                   [Thévenin]
Δ→Y: Y_tak = (Δ_a·Δ_b)/(Σ)  [Ster-Driehoek]
```

### Wisselstroomleer
```
Z = R + jX                   [Impedantie]
X_L = ωL = 2πfL             [Inductieve reactantie]
X_C = 1/(ωC) = 1/(2πfC)     [Capacitieve reactantie]
f₀ = 1/(2π√(LC))            [Resonantiefrequentie]
tanφ = X/R                   [Faseverschuiving]
```

### Vermogensleer
```
S² = P² + Q²                 [Schijnbaar vermogen]
cosφ = P/S                   [Arbeidsfactor]
Q_C = P(tanφ₁ - tanφ₂)      [cosφ-correctie]
```

### Driefasensystemen
```
U_lijn = √3·U_fase           [Ster-schakeling]
I_lijn = I_fase              [Ster-schakeling]
P_3fase = √3·U_lijn·I_lijn·cosφ
ΔU_fase ≈ I_fase·(ρ·L/A)    [Spanningsverlies]
```

### Transformatoren
```
U₂/U₁ = N₂/N₁               [Wikkelverhouding]
```

### Energietoepassingen
```
E_jaar = instraling × A × η  [PV-opbrengst]
```

---

## Aanbevelingen voor Anki Deck

### 1. Vraagtypen
**Creëer verschillende card types:**
- **Type A:** Directe formule toepassing (cloze)
- **Type B:** Meerkeuzevragen (multiple choice)
- **Type C:** Stapsgewijze berekeningen (basic front/back)
- **Type D:** Conceptuele vragen (image occlusion voor schema's)

### 2. Tagging Strategie
**Suggestie tags:**
```
#examenstijl
#niveau-1-basis / #niveau-2-gemiddeld / #niveau-3-gevorderd
#basiselektrotechniek / #wisselstroomleer / #driefasen / etc.
#formuleblad
#valkuil
#norm-2procent
#thevenin #kirchhoff #resonantie #cosphi-correctie
```

### 3. Focus Gebieden
**Op basis van deze analyse, prioriteit geven aan:**
1. **Kirchhoff wetten** (KCL/KVL) - fundamenteel, komt vaak voor
2. **Vermogensdriehoek** (P/Q/S relaties) - veel praktijkvragen
3. **3-fasensystemen** - complexer, vereist √3 factor begrip
4. **Thévenin/Norton** - belangrijk analysetool
5. **Resonantie** (LC circuits) - conceptueel én rekenkundig

### 4. Hints Integratie
**Gebruik "Holmes-stijl" hints als:**
- Extra tekst op achterkant kaart
- Formuleblad reminder
- "Show hint" button

### 5. Valkuilen Deck
**Apart sub-deck overwegen:**
- Alle "Let op" punten als aparte cards
- Typische fouten signaleren
- Eenheden conversie oefeningen

---

## Examenstijl Karakteristieken Samenvatting

### Wat maakt deze toets "examenstijl"?

1. **Realistische context:**
   - Praktijkwaarden (230/400V, standaard kabel mm², normeringen)
   - Installatietechnische vraagstelling

2. **Formuleblad hint systeem:**
   - Simuleert examen met formuleblad
   - Hints geven richting, geen complete oplossing

3. **Mix van niveaus:**
   - 19% basis (snel te scoren punten)
   - 50% gemiddeld (bulk van examen)
   - 31% gevorderd (onderscheidend vermogen)

4. **Stapsgewijze berekeningen:**
   - Geef tussenstappen aan
   - Niet alleen eindantwoord

5. **Normeringen & Standaarden:**
   - 2%-norm spanningsverlies (NEN 1010)
   - Standaard kabeldiameters
   - Praktijktoepassing transformatoren

6. **Vectorberekeningen:**
   - Complexe getallen (j-notatie)
   - Faseverschuivingen
   - 3-fasensystemen

---

## Conclusies

### Sterke Punten Oefentoets
✅ Brede onderwerpen coverage (alle hoofdstukken vertegenwoordigd)
✅ Realistische examenstijl vraagstelling
✅ Goede mix van niveaus (discriminerend vermogen)
✅ Gedetailleerde hints (leerdoel ondersteuning)
✅ Praktijkgerichtheid (installatietechniek)

### Aandachtspunten
⚠️ Vraag 16 (Juist/Onjuist) heeft geen vraagstelling in HTML
⚠️ Enkele vragen bevatten afbeeldingen (base64 encoded) - deze moeten apart geanalyseerd
⚠️ Holmes-hints zijn zeer uitgebreid - risico dat studenten te afhankelijk worden

### Geschiktheid voor Anki
**Zeer geschikt:**
- Alle 16 vragen kunnen omgezet worden naar Anki cards
- Hints systeem past perfect bij "show answer" mechanisme
- Mix van formules, concepten, en berekeningen
- Duidelijke onderwerp categorisatie mogelijk

**Aanpassingen nodig:**
- Afbeeldingen extraheren uit base64 naar aparte image files
- Vraag 16 stellingen apart analyseren (niet volledig in extraction)
- Lange berekeningen mogelijk opsplitsen in meerdere sub-cards

---

## Vervolgstappen

### 1. Afbeeldingen Extractie
**Actie:** Separate script om base64 images uit HTML te halen en op te slaan als PNG/JPG

### 2. Vraag 16 Detail Analyse
**Actie:** Handmatig HTML inspecteren voor Juist/Onjuist stellingen (niet goed geparsed)

### 3. Anki Deck Creatie
**Actie:**
- Template cards ontwerpen (zie aanbevelingen)
- Import script schrijven (MD → Anki format)
- Tags systeem implementeren

### 4. Formuleblad Integratie
**Actie:**
- Alle formules uit hints verzamelen
- Separaat formuleblad PDF/MD document maken
- Linken in Anki deck settings

### 5. Validatie
**Actie:**
- Cross-reference met studiehandleiding NCOI
- Check tegen eerder gemaakte cards (overlap?)
- Moeilijkheidsgraad kalibratie

---

**Einde Analyse**
