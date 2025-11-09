# EXAM PERFECTIONALISATIE STRATEGIE
**NCOI Elektrische Netwerken Examen - Image Quality Improvement**

*Aangemaakt: 2025-11-09*

---

## 🎯 DOEL

Verbeteren van alle circuit diagrams en afbeeldingen in het examen zonder verlies van context, zodat studenten perfecte, professionele visualisaties krijgen die exact aansluiten bij de examenvragen.

---

## 📊 HUIDIGE STATUS ANALYSE

### ✅ **Bestaande Draw.io SVG Circuits (7 stuks)**

| Opdracht | Bestand | Status | Kwaliteit | Verbetering Nodig |
|----------|---------|--------|-----------|-------------------|
| 2 | opdracht2.drawio.svg | ✅ Bestaat | Basis OK | ✨ Componentlabels, nettere layout |
| 4 | opdracht4.drawio.svg | ✅ Bestaat | Basis OK | ✨ LC waardes toevoegen |
| 5 | opdracht5.drawio.svg | ✅ Bestaat | Basis OK | ✨ Delta/ster labels duidelijker |
| 6 | opdracht6.drawio.svg | ✅ Bestaat | Basis OK | ✨ R en L waardes aangeven |
| 9 | opdracht9.drawio.svg | ✅ Bestaat | Basis OK | ✨ Admittantie notatie verbeteren |
| 15 | opdracht15.drawio.svg | ✅ Bestaat | Basis OK | ✨ Holmes p.119 referentie checken |
| 16 | Opdrach16.drawio.svg | ✅ Bestaat | Basis OK | ✨ Knooppunten labelen (V1, V2) |

**Problemen:**
- Filename typo: "Opdrach16" → moet "Opdracht16"
- Missen componentwaardes (R, L, C in Ω, H, F)
- Geen knooppunt/stroomlabels
- Basis draw.io symbolen (kunnen professioneler)

### ✅ **Bestaande Support SVG's (5 stuks)**

| Bestand | Gebruikt in | Status | Kwaliteit |
|---------|-------------|--------|-----------|
| condensator_i_u_verloop.svg | Opgave 7 | ✅ Goed | 🟢 Professional |
| thevenin_norton_equivalent.svg | Opgave 13 | ✅ Goed | 🟢 Professional |
| trapezium_spanning_ueff.svg | Opgave 14 | ✅ Goed | 🟢 Professional |
| vermogensdriehoek_compensatie.svg | Opgave 8 | ✅ Goed | 🟢 Professional |
| ui_karakteristiek_werkpunt.svg | Opgave 3 | ✅ Goed | 🟢 Professional |

**Deze zijn EXCELLENT - behouden!**

### ❌ **Missing: Placeholder PNG's (12 stuks)**

| Placeholder | Opgave | Type Diagram Nodig | Prioriteit |
|-------------|--------|-------------------|------------|
| accu_werkpunt.png | 3 | U-I karakteristiek | 🔴 HIGH - maar SVG bestaat al! |
| blz119_complex_netwerk.png | 15 | Circuit diagram | 🟡 MEDIUM - opdracht15.svg bestaat |
| complex_netwerk_boek.png | ? | Circuit diagram | 🟢 LOW - niet gebruikt in HTML |
| cos_phi_correctie.png | 8 | Vermogensdriehoek | 🔴 HIGH - maar SVG bestaat al! |
| delta_naar_ster.png | 5 | Transformatie schema | 🟡 MEDIUM |
| knooppuntanalyse_schema.png | 16 | Labeled circuit | 🟡 MEDIUM |
| motor_modulatie.png | 12 | PWM/Freq diagram | 🟢 LOW - theorievraag |
| rl_fasediagram.png | 6 | Phasor diagram | 🟡 MEDIUM |
| ster_driehoek_motor.png | 11 | Y-Δ comparison | 🟡 MEDIUM |
| thevenin_norton.png | 13 | Equivalenten | 🔴 HIGH - maar SVG bestaat al! |
| u_t_i_t_verband.png | 7 | Tijd-grafiek | 🔴 HIGH - maar SVG bestaat al! |
| ueff_grafiek.png | 14 | Trapezium grafiek | 🔴 HIGH - maar SVG bestaat al! |

**Belangrijke bevinding:** De meeste "missing" PNGs hebben al een SVG equivalent! Het HTML gebruikt inconsistent .png vs .svg paden.

---

## 🔧 STRATEGIE: 3-STAPPEN PLAN

### **STAP 1: Fix HTML References (Quick Win)**

**Probleem:** HTML refereert naar .png files die niet bestaan, terwijl .svg files WEL bestaan.

**Oplossing:** Update HTML om correcte SVG paths te gebruiken:

```html
<!-- VOOR (niet werkend): -->
<img src="examen_afbeeldingen/cos_phi_correctie.png">

<!-- NA (werkend): -->
<img src="vermogensdriehoek_compensatie.svg">
```

**Benodigde aanpassingen:**
| HTML Referentie | → | Correcte Bestand |
|-----------------|---|------------------|
| examen_afbeeldingen/cos_phi_correctie.png | → | vermogensdriehoek_compensatie.svg |
| examen_afbeeldingen/thevenin_norton.png | → | thevenin_norton_equivalent.svg |
| examen_afbeeldingen/u_t_i_t_verband.png | → | condensator_i_u_verloop.svg |
| examen_afbeeldingen/ueff_grafiek.png | → | trapezium_spanning_ueff.svg |
| examen_afbeeldingen/accu_werkpunt.png | → | ui_karakteristiek_werkpunt.svg |

---

### **STAP 2: Improve Existing Draw.io SVG Circuits**

**Voor elk circuit diagram:**

#### **2.1 Opdracht 2 - Wheatstone Brug**
- ✨ Add component labels: "C = 10 μF" bij elke condensator
- ✨ Add voltage source label: "U = 10 V, f = 50 Hz"
- ✨ Duidelijkere brug-structuur (balans zichtbaar maken)
- ✨ Node labels waar stroom splittingen zijn

#### **2.2 Opdracht 4 - LC Resonantie**
- ✨ Add values: "L = 10 mH", "C = 10 μF"
- ✨ Maak TWEE duidelijke schemas:
  - Links: Serie-resonantie
  - Rechts: Parallel-resonantie
- ✨ Add "f = ?" indicator

#### **2.3 Opdracht 5 - Ster/Driehoek Transformatie**
- ✨ Add labels: Ra = 20Ω, Rb = 20Ω, Rc = 2Ω
- ✨ Klem-aanwijzingen: A, B, C
- ✨ Transformatie-pijl: Δ → Y

#### **2.4 Opdracht 6 - RL Serieschakeling**
- ✨ Add values: "L = 10 mH", "R = ?"
- ✨ Meetgegevens: "U = 10 V, I = 125 mA, φ = 45°"
- ✨ Fasehoek indicator

#### **2.5 Opdracht 9 - Complex Parallel Netwerk**
- ✨ Label alle takken met impedanties
- ✨ Current directions
- ✨ "U = 230 V" bronspanning

#### **2.6 Opdracht 15 - Holmes p.119 Network**
- ✨ Verify tegen boek p.119
- ✨ Component waardes toevoegen
- ✨ Node voltage labels (voor admittantie berekening)

#### **2.7 Opdracht 16 - Knooppuntanalyse**
- ✨ **RENAME**: "Opdrach16.drawio.svg" → "Opdracht16.drawio.svg"
- ✨ Nodes labelen: V1, V2, V3, GND
- ✨ Current labels: I1, I2, I3, Ix
- ✨ Component values

---

### **STAP 3: Create Missing Diagram SVG's**

#### **3.1 RL Fasediagram (Opgave 6)**
**Bestand:** `rl_fasediagram.svg`
- Vector diagram met:
  - UR (horizontaal)
  - UL (verticaal omhoog)
  - Utot (hypotenusa)
  - Hoek φ = 45°
- Clean, professioneel axes
- Labels met eenheden

#### **3.2 Delta ↔ Ster Transformatie Schema (Opgave 5)**
**Bestand:** `delta_naar_ster_transformatie.svg`
- Links: Δ-configuratie (Ra, Rb, Rc)
- Rechts: Y-configuratie (R1, R2, R3)
- Transformatie pijl met formules
- Klemmen A-B-C alignment

#### **3.3 Ster-Driehoek Motor Comparison (Opgave 11)**
**Bestand:** `ster_driehoek_motor_vergelijking.svg`
- Side-by-side:
  - Links: Y-schakeling → P = 1 kW
  - Rechts: Δ-schakeling → P = ?
- Vermogensvergelijking P_Δ = 3 × P_Y
- Fasespanning vs lijnspanning indicator

#### **3.4 Knooppuntanalyse Schema (Opgave 16)**
**Bestand:** `knooppuntanalyse_labeled.svg`
- Enhanced versie van opdracht16
- Explicit node labels
- KCL vergelijkingen bij nodes
- Reference (ground) node

---

## 🎨 KWALITEITSSTANDAARDEN

### **Visual Requirements:**
1. **Clean white background** (#FFFFFF)
2. **Black lines** (#000000), 2px stroke weight
3. **Grid alignment** - alles orthogonaal of op 45°
4. **Consistent spacing** - minimaal 20px tussen componenten
5. **Professional symbols**:
   - Weerstand: zigzag (Amerikaanse) of rechthoek (Europees)
   - Condensator: twee parallelle lijnen met spacing
   - Spoel: spiraal/coil symbol
   - Spanningsbron: cirkel met + en -

### **Label Requirements:**
1. **Component values** in standaard notatie:
   - Weerstand: "100 Ω" (niet 100Ω of 100 ohm)
   - Capaciteit: "10 μF" (niet 10uF)
   - Inductantie: "10 mH" (niet 10mH)
2. **Node labels** in hoofdletters: A, B, C, V1, V2
3. **Current labels** met pijlen: I, I₁, Iₓ
4. **Voltage labels** met polariteit: U, U₁, Uₜₕ

### **Technical Requirements:**
1. **SVG viewBox** optimaal ingesteld (geen excess whitespace)
2. **Embedded fonts** waar nodig voor speciale tekens (μ, Ω, φ)
3. **Max width:** 600-800px voor goede leesbaarheid in HTML
4. **Accessible:** Betekenisvol `<title>` en `<desc>` in SVG

---

## 📋 IMPLEMENTATIE VOLGORDE

### **Priority 1: Critical Fixes (Direct impact op werkend examen)**
1. ✅ Fix HTML image references (.png → .svg)
2. ✅ Rename "Opdrach16" → "Opdracht16"
3. ✅ Create "rl_fasediagram.svg" (nodig voor opgave 6)

### **Priority 2: Enhancement (Improved quality)**
4. ✨ Enhance opdracht2.svg - opdracht6.svg met labels
5. ✨ Enhance opdracht9.svg, 15.svg, 16.svg met labels
6. ✨ Create "delta_naar_ster_transformatie.svg"
7. ✨ Create "ster_driehoek_motor_vergelijking.svg"

### **Priority 3: Optional (Nice-to-have)**
8. 🎁 Create "knooppuntanalyse_labeled.svg" (duplicate enhancement)
9. 🎁 Create "motor_modulatie.svg" (PWM diagram voor opgave 12)

---

## ✅ VALIDATIE CHECKLIST

Voor elk diagram checken:
- [ ] Alle component waardes aanwezig en correct
- [ ] Nodes/klemmen gelabeld waar relevant
- [ ] Stroomrichtingen aangegeven waar nodig
- [ ] Spanningspolariteiten correct
- [ ] Geen typfouten in labels (μ, Ω, φ correct)
- [ ] SVG opent correct in browser
- [ ] Referenced correct in HTML
- [ ] Schaalbaar zonder kwaliteitsverlies
- [ ] Context van examenvraag behouden

---

## 📦 DELIVERABLES

### **Verbeterde Bestanden:**
```
images/Opdrachten examen/
├── opdracht2_v2.drawio.svg          [ENHANCED]
├── opdracht4_v2.drawio.svg          [ENHANCED]
├── opdracht5_v2.drawio.svg          [ENHANCED]
├── opdracht6_v2.drawio.svg          [ENHANCED]
├── opdracht9_v2.drawio.svg          [ENHANCED]
├── opdracht15_v2.drawio.svg         [ENHANCED]
├── opdracht16_v2.drawio.svg         [RENAMED + ENHANCED]
├── rl_fasediagram.svg               [NEW]
├── delta_naar_ster_transformatie.svg [NEW]
└── ster_driehoek_motor_vergelijking.svg [NEW]
```

### **Updated HTML:**
```
elektrische_netwerken_examen_PERFECT.html  [NEW VERSION]
```

### **Documentation:**
```
IMPROVEMENT_LOG.md                   [Change tracking]
IMAGE_REFERENCE_TABLE.md             [Complete mapping]
```

---

## 🎯 SUCCESS CRITERIA

✅ **Examen is perfect wanneer:**
1. Alle 16 opdrachten hebben werkende, high-quality afbeeldingen
2. Geen enkele broken image link in HTML
3. Alle circuits hebben correcte component waardes
4. Professionele uitstraling vergelijkbaar met officiële examenmateriaal
5. Studenten kunnen examen gebruiken zonder verwarring over ontbrekende/onduidelijke diagrammen

---

**Status:** 📋 Strategy Complete - Ready for Implementation
**Next Step:** Start met Priority 1 fixes

