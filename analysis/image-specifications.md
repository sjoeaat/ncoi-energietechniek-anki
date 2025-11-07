# Visuele Schema's Specificatie — NCOI Energietechniek Anki

**Datum:** 2025-11-06
**Bron:** Energietechniek_Anki_Samenvatting.md
**Doel:** Specificatie van 45+ schema's voor 80+ Anki-kaarten

---

## Samenvatting Totaal

- **Totaal schema's:** 45
- **HOOG prioriteit:** 18 (core concepts)
- **MIDDEL prioriteit:** 18 (aanvullend)
- **LAAG prioriteit:** 9 (optioneel)
- **Bestandslocatie:** `/images/` subdirectory per categorie
- **Formaat:** SVG (vector, schaalbaar, editeerbaar)

---

## CATEGORIE 1: NETWERKSCHEMA'S (12 schema's)

### 1.1 Basiscircuit met Kirchhoff wetten
- **Type:** Circuit schema
- **Doel:** Demonstreer 1e Kirchhoff (knoopwet) met stomen die in/uit knooppunt gaan
- **Elementen:**
  - Centraal knooppunt (grote dot)
  - 3-4 takken met stroompijlen (I₁, I₂, I₃, I₄)
  - Pijlrichtingen duidelijk
  - Label: "I₁ + I₃ = I₂ + I₄"
- **Kleuren:**
  - Knooppunt: rood
  - In-stromingen: groen
  - Uit-stromingen: oranje
- **Prioriteit:** HOOG
- **Bestandsnaam:** `01_kirchhoff_1e_wet.svg`

### 1.2 Gesloten kring met spanningen (Maaswet)
- **Type:** Circuit schema
- **Doel:** Toon 2e Kirchhoff (maaswet) met gesloten loop
- **Elementen:**
  - Rechthoekige kring met 4 componenten (spanningsbronnen/weerstanden)
  - Pijl rond de kring (gesloten loop)
  - Labels: U₁, U₂, U₃, U₄ met richtingen
  - Vergelijking: "U₁ - U₂ + U₃ - U₄ = 0"
- **Kleuren:**
  - Spanningen met pijlen: blauw
  - Loop-pijl: rood gestippeld
- **Prioriteit:** HOOG
- **Bestandsnaam:** `02_kirchhoff_2e_wet.svg`

### 1.3 Thévenin Equivalent Circuit
- **Type:** Circuit schema (2 delen: origineel + equivalent)
- **Doel:** Toon conversie van complex netwerk naar equivalente bron
- **Linker deel (origineel):**
  - Complex netwerk met 3-4 weerstanden en spanningsbron
  - Open-circuit spanning Uoc marked
  - Kortsluiting voor Rth berekening
- **Rechter deel (equivalent):**
  - Vth spanningsbron
  - Rth serieweerstand
  - Belasting Rload
  - Labels met formules: Vth = Uoc, Rth = Uoc/Isc
- **Annotaties:**
  - "Origineel netwerk" ← "Thévenin equivalent"
  - Pijl tussen beide
- **Prioriteit:** HOOG
- **Bestandsnaam:** `03_thevenin_equivalent.svg`

### 1.4 Norton Equivalent Circuit
- **Type:** Circuit schema (identiek aan Thévenin, ander vorm)
- **Doel:** Toon Norton stroombron equivalent
- **Elementen:**
  - Norton stroombron IN (parallel met cirkel + pijl)
  - RN parallelweerstand
  - Belasting Rload
  - Labels: IN = Vth/Rth, RN = Rth
- **Relatie aan Thévenin:**
  - Beide equivalenten side-by-side
  - Conversieformules erbij
- **Prioriteit:** HOOG
- **Bestandsnaam:** `04_norton_equivalent.svg`

### 1.5 Serie-parallel Weerstandscombinatie
- **Type:** Circuit schema
- **Doel:** Toon hoe serie- en parallelweerstanden vervangen worden
- **Stappen (verticaal gerangschikt):**
  1. Origineel: 4-5 weerstanden in gemengde schakeling
  2. Stap 1: 2 parallelle R's vervangen door R_parallel
  3. Stap 2: Serie R's vervangen door R_serie
  4. Eindresultaat: Enkele Rv
- **Formules naast elke stap**
- **Kleuren:**
  - Te vervangen componenten: geel highlight
  - Vervangen resultaat: groen highlight
- **Prioriteit:** HOOG
- **Bestandsnaam:** `05_serie_parallel_reduction.svg`

### 1.6 RLC Serie Circuit
- **Type:** Circuit schema
- **Doel:** Basis RLC serieschakeling met R, L, C, bron
- **Elementen:**
  - AC spanningsbron (sinuswaalgolf symbool)
  - Weerstand R (rechthoek)
  - Spoel L (spiraaltje)
  - Condensator C (twee lijnen)
  - Alle in serie
  - Stroom I door circuit
- **Labels:**
  - Impedantie Z = √(R² + (XL - XC)²)
  - Faseverschuiving φ = arctan((XL - XC)/R)
- **Prioriteit:** HOOG
- **Bestandsnaam:** `06_rlc_series_circuit.svg`

### 1.7 RLC Parallel Circuit
- **Type:** Circuit schema
- **Doel:** Parallel RLC schakeling
- **Elementen:**
  - Centrale AC bron
  - 3 parallelle takken: R, L, C
  - Stromen IR, IL, IC
  - Totaalstroom I
- **Annotaties:**
  - IT = √(IR² + (IC - IL)²)
  - Faseverschuiving
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `07_rlc_parallel_circuit.svg`

### 1.8 Transformator Ideaal Schema
- **Type:** Circuit schema
- **Doel:** Toon primaire en secundaire wikkeling met koppeling
- **Elementen:**
  - Primaire spoel (links, N₁ windingen)
  - Secundaire spoel (rechts, N₂ windingen)
  - Magnetische kern (verticale lijnen tussen spoelen)
  - Primaire spanning U₁, stroom I₁
  - Secundaire spanning U₂, stroom I₂
  - Transformatieverhouding labelen
- **Formules:**
  - U₁/U₂ = N₁/N₂
  - I₂/I₁ = N₁/N₂
- **Prioriteit:** HOOG
- **Bestandsnaam:** `08_transformer_ideal.svg`

### 1.9 Gekoppelde Spoelen (Transformator met k-factor)
- **Type:** Circuit schema
- **Doel:** Toon wederzijdse inductie met koppelfactor
- **Elementen:**
  - 2 spoelen met wederzijdse inductie M
  - Primaire: L₁, M
  - Secundaire: L₂, M
  - Koppelfactor k tussen beide aangegeven
  - Label: M = k√(L₁L₂)
- **Annotaties:**
  - k = 0 (geen koppeling)
  - k = 1 (perfecte koppeling)
  - Praktisch: k ≈ 0.95-0.99
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `09_coupled_coils.svg`

### 1.10 Ladder Netwerk (Vervangingsweerstand)
- **Type:** Circuit schema
- **Doel:** Toon hoe ladder netwerk stap-voor-stap gereduceerd wordt
- **Elementen:**
  - 3-4 stappen van linksboven naar rechtsboven
  - Elke stap toont vervangingsresultaat
  - Reverse engineering proces zichtbaar
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `10_ladder_network_reduction.svg`

### 1.11 Spanningsmeter vs Stroommeter in Circuit
- **Type:** Circuit schema
- **Doel:** Toon verschil tussen interne weerstand meten
- **2 configuraties:**
  - Links: Voltmeter parallel (hoge interne R)
  - Rechts: Ammeter in serie (lage interne R)
- **Annotaties:**
  - Rv >> Rcircuit (voltmeter)
  - Ra << Rcircuit (ammeter)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `11_voltmeter_ammeter.svg`

### 1.12 Wienbrug Circuit
- **Type:** Circuit schema (speciale afgebalanceerde brug)
- **Doel:** RLC filter netwerk voor resonantie
- **Elementen:**
  - Brug-configuratie (4 armen)
  - AC bron, detector
  - R en C componenten in specifiële rangschikking
- **Annotaties:**
  - Balanceringscondities
  - Resonantiefrequentie label
- **Prioriteit:** LAAG
- **Bestandsnaam:** `12_wien_bridge.svg`

---

## CATEGORIE 2: FASEDIAGRAMMEN & IMPEDANTIE (12 schema's)

### 2.1 Phasor Diagram - Zuiver Resistief (R)
- **Type:** Phasor/Vector diagram
- **Doel:** U en I in fase voor zuivere R
- **Elementen:**
  - Horizontale as (reëel)
  - Verticale as (imaginair)
  - U vector: horizontaal naar rechts
  - I vector: volledig overlappend U
  - Fase verschuiving φ = 0°
  - Arc met "φ = 0°" label
- **Kleuren:**
  - U: rood vector
  - I: blauw vector
- **Prioriteit:** HOOG
- **Bestandsnaam:** `20_phasor_resistive.svg`

### 2.2 Phasor Diagram - Zuiver Inductief (L)
- **Type:** Phasor/Vector diagram
- **Doel:** I loopt 90° achter U voor zuivere L
- **Elementen:**
  - Horizontale as (reëel)
  - Verticale as (imaginair)
  - U vector: horizontaal naar rechts
  - I vector: 90° omlaag (4e kwadrant)
  - Arc: φ = -90°
  - Label: "I lags U by 90°"
- **Kleuren:**
  - U: rood
  - I: groen (backward)
  - φ: blauw arc
- **Prioriteit:** HOOG
- **Bestandsnaam:** `21_phasor_inductive.svg`

### 2.3 Phasor Diagram - Zuiver Capacitief (C)
- **Type:** Phasor/Vector diagram
- **Doel:** I loopt 90° vooruit op U voor zuivere C
- **Elementen:**
  - U vector: horizontaal naar rechts
  - I vector: 90° omhoog (1e kwadrant)
  - Arc: φ = +90°
  - Label: "I leads U by 90°"
- **Kleuren:**
  - U: rood
  - I: groen (forward)
- **Prioriteit:** HOOG
- **Bestandsnaam:** `22_phasor_capacitive.svg`

### 2.4 Impedantie Driehoek (R-X-Z)
- **Type:** Grafisch diagram
- **Doel:** Relatie tussen R, XL, XC en Z
- **Elementen:**
  - Horizontale as (reëel): R
  - Verticale as (imaginair): X = XL - XC
  - Diagonale vector: Z = |Z|
  - Hoek φ aangegeven
  - Labels: Z = √(R² + X²)
  - tan φ = X/R
- **Cases weergegeven:**
  - XL > XC (inductief, φ > 0)
  - XC > XL (capacitief, φ < 0)
  - XL = XC (resistief, φ = 0)
- **Prioriteit:** HOOG
- **Bestandsnaam:** `23_impedance_triangle.svg`

### 2.5 Vermogen Driehoek (P-Q-S)
- **Type:** Grafisch diagram
- **Doel:** Relatie tussen actief (P), blind (Q) en schijnbaar vermogen (S)
- **Elementen:**
  - Horizontale as: P (actief vermogen, W)
  - Verticale as: Q (blind vermogen, VAr)
  - Diagonale vector: S (schijnbaar vermogen, VA)
  - Hoek φ aangegeven
  - Labels: S = √(P² + Q²)
  - cos φ = P/S
  - sin φ = Q/S
- **Twee cases:**
  - Inductieve belasting: Q positief omhoog
  - Capacitieve belasting: Q negatief omlaag
- **Kleuren:**
  - P: blauw
  - Q: rood
  - S: groen
  - φ: geel arc
- **Prioriteit:** HOOG
- **Bestandsnaam:** `24_power_triangle.svg`

### 2.6 RLC Serie - Impedantie Vector
- **Type:** Phasor diagram + impedantie
- **Doel:** Toon hoe impedantie zich opbouwt uit R, L, C
- **Elementen:**
  - Reële as: R
  - XL vector omhoog (+j)
  - XC vector omlaag (-j)
  - Netto X = XL - XC
  - Z vector onder hoek φ
  - Alle labels met waarden
- **Annotaties:**
  - Als XL > XC: inductief, φ > 0
  - Als XC > XL: capacitief, φ < 0
  - Als XL = XC: resonantie, φ = 0
- **Prioriteit:** HOOG
- **Bestandsnaam:** `25_rlc_impedance_vector.svg`

### 2.7 RLC Parallel - Admittantie Vector
- **Type:** Vector diagram
- **Doel:** Parallel RLC als admittantie (Y = 1/Z)
- **Elementen:**
  - G (conductance) op reële as
  - BL en BC (susceptance) op imaginaire as
  - Y vector resultante
  - Aangegeven: Y = √(G² + (BC - BL)²)
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `26_rlc_admittance_vector.svg`

### 2.8 Resonantie Fasediagram RLC
- **Type:** Phasor diagram (animatie-sequentie)
- **Doel:** Toon hoe phasors roteren met frequentie
- **Drie frequenties neergezet:**
  - f < f₀ (capacitief): IC > IL
  - f = f₀ (resonantie): IC = IL
  - f > f₀ (inductief): IL > IC
- **Voor elke frequentie:**
  - U vector (referentie horizontal)
  - IR vector (in fase)
  - IL vector (90° achter U)
  - IC vector (90° vooruit U)
  - Resultante I
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `27_resonance_phasors.svg`

### 2.9 Cosφ Correctie Vector (Blindvermogen)
- **Type:** Vector diagram
- **Doel:** Voor/na compensatie van blindvermogen
- **Twee kolommen:**
  - **Voor:**
    - P vector (actief vermogen)
    - Q vector (blind vermogen groot)
    - S vector onder grote hoek
    - cos φ (klein)
  - **Na:**
    - P vector (onveranderd)
    - Q' vector (klein, gecompenseerd)
    - S' vector onder kleine hoek
    - cos φ' (groot)
- **Condensatorbank aangegeven:**
  - QC = Q - Q' (gecompenseerde waarde)
- **Prioriteit:** HOOG
- **Bestandsnaam:** `28_cosphi_correction.svg`

### 2.10 Momentaan Vermogen Grafiek
- **Type:** Grafiek (tijd-domein)
- **Doel:** Toon oscillatie van momentaan vermogen
- **Elementen:**
  - X-as: tijd (ms of graden)
  - Y-as: vermogen (W)
  - Sinusvormige golf: p(t) = UI[cos φ - cos(2ωt + φ)]
  - Average lijn: P = UI cos φ
  - Oscillaties rond average
- **Cases:**
  - Zuiver R: constante P
  - Zuiver L of C: oscillatie rond 0
  - RL/RC: mixed oscillatie
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `29_instantaneous_power.svg`

### 2.11 Frequentierespons RLC (Bode-achtig)
- **Type:** Grafiek
- **Doel:** |Z| of |I| vs frequentie
- **X-as:** Logaritmische frequentie (f)
- **Y-as:** Lineaire impedantie of stroom
- **Curve karakteristieken:**
  - Minimum Z op resonantiefrequentie
  - Stijgende Z links van f₀ (capacitief: XC > XL)
  - Stijgende Z rechts van f₀ (inductief: XL > XC)
  - Peak markeren bij f₀
  - Bandbreedte aangegeven (f₁ - f₂ bij -3dB)
- **Annotations:**
  - f₀ = 1/(2π√LC)
  - Q-factor zichtbaar
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `30_frequency_response.svg`

### 2.12 Complexe Vlak (Polair ↔ Rechthoekig)
- **Type:** Vector diagram
- **Doel:** Conversie tussen polair en rechthoekig formaat
- **Elementen:**
  - Reële as (R, X-component)
  - Imaginaire as (X, Y-component)
  - Vector z onder hoek θ
  - Polair: z = r∠θ
  - Rechthoekig: z = a + jb
  - Relaties: r = √(a² + b²), θ = arctan(b/a)
- **Annotaties:**
  - z = r(cos θ + j sin θ) = r·cis(θ)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `31_polar_rectangular.svg`

---

## CATEGORIE 3: DRIEFASENSYSTEMEN (8 schema's)

### 3.1 Driefasige Sinusvormige Spanningen
- **Type:** Grafiek (tijd-domein)
- **Doel:** Toon 3 fasespanningen 120° uit fase
- **Elementen:**
  - X-as: tijd (ms of graden)
  - Y-as: spanningen (V)
  - 3 sinusvormen: UA, UB, UC
  - Gekleurd: rood, geel, blauw
  - 120° faseverschuiving aangegeven
  - Labels: UA = û·sin(ωt), UB = û·sin(ωt - 120°), UC = û·sin(ωt - 240°)
- **Annotaties:**
  - Effektieve waarden: U = û/√2
  - Frequentie: f = 50 Hz (Nederland)
- **Prioriteit:** HOOG
- **Bestandsnaam:** `40_three_phase_voltages.svg`

### 3.2 Driefasensysteem Ster-Koppeling (Y)
- **Type:** Circuit schema
- **Doel:** Toon ster-verbinding met nulpunt
- **Elementen:**
  - 3 fasespanningsbronnen (centraal, 120° uiteen)
  - Nulpunt (gemeenschappelijk)
  - 3 lasten Z (Y-gekoppeld)
  - Lijnen naar 3 lasten
  - Nulleider terug naar nulpunt
- **Labels:**
  - Lijnspanningen: UL (tussen fasedraden)
  - Fasespanningen: UF (tussen fase en nulpunt)
  - Relatie: UL = √3 · UF
  - Stromen: IL = IF (in Y-koppeling)
- **Kleuren:**
  - Fase A: rood
  - Fase B: geel
  - Fase C: blauw
  - Nul: zwart
- **Prioriteit:** HOOG
- **Bestandsnaam:** `41_star_connection.svg`

### 3.3 Driefasensysteem Delta-Koppeling (Δ)
- **Type:** Circuit schema
- **Doel:** Toon driehoek-verbinding zonder nulpunt
- **Elementen:**
  - 3 spanningsbronnen in driehoekschakeling
  - 3 lasten Z in delta
  - Geen nulleider
  - Lijn- en fasespanningen
- **Labels:**
  - Lijnspanningen = Fasespanningen (UL = UF)
  - Stroomrelatie: IL = √3 · IF
- **Prioriteit:** HOOG
- **Bestandsnaam:** `42_delta_connection.svg`

### 3.4 Ster-Delta Transformatie
- **Type:** Circuit schema + grafiek
- **Doel:** Visuele conversie Y ↔ Δ
- **2 delen:**
  - Links: Star-koppeling
  - Rechts: Delta-koppeling
  - Centrale pijl: transformatie-relatie
- **Formules:**
  - Y→Δ: ZΔ = 3·ZY (in symmetrische systemen)
  - Δ→Y: ZY = ZΔ/3
- **Prioriteit:** HOOG
- **Bestandsnaam:** `43_star_delta_transformation.svg`

### 3.5 Phasor Diagram 3-fase (Ster)
- **Type:** Vector diagram
- **Doel:** Toon 3 fasespanningen/stromen 120° uiteen
- **Elementen:**
  - 3 vectoren op 0°, 120°, 240°
  - UA (0°), UB (240°), UC (120°) — volgordeafhankelijk
  - Alle met dezelfde grootte
  - Vectorsom = 0
- **Annotaties:**
  - "Symmetrisch 3-fasensysteem"
  - UA + UB + UC = 0
- **Prioriteit:** HOOG
- **Bestandsnaam:** `44_three_phase_phasor_ij.svg`

### 3.6 Lijn- vs Fasespanning Phasor
- **Type:** Vector diagram
- **Doel:** Relatie UL = √3 · UF in star-systeem
- **Elementen:**
  - Fasespanningen (UA, UB, UC) in één kleur
  - Lijnspanningen (UAB, UBC, UCA) in andere kleur
  - Vectoroptelling: UAB = UA - UB
  - Grootteverschil: |UAB| = √3 · |UA|
  - Faseverschil: 30°
- **Prioriteit:** HOOG
- **Bestandsnaam:** `45_line_phase_voltage.svg`

### 3.7 Driefasenvermogen Diagram
- **Type:** Circuit + berekening
- **Doel:** Vermogen in 3-fasensystemen
- **Elementen:**
  - 3-fasige bron
  - Symmetrische belasting
  - Vermogensformules:
    - P = √3 · UL · IL · cos φ
    - Q = √3 · UL · IL · sin φ
    - S = √3 · UL · IL
  - Totaalvermogen = 3× per fase
- **Annotaties:**
  - Evenwichtige belasting: Pa = Pb = Pc
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `46_three_phase_power.svg`

### 3.8 Ongebalanceerde 3-fase Systeem
- **Type:** Circuit schema + phasor
- **Doel:** Toon verschil symmetrisch vs ongebalanceerd
- **Circuit:**
  - 3 verschillende lasten Z₁ ≠ Z₂ ≠ Z₃
  - Nulleider nodig voor aarding
  - Nulpuntverschuiving zichtbaar
- **Phasor:**
  - Ongelijke vectoren
  - Vectorsom ≠ 0
  - Nulstroom aangegeven
- **Prioriteit:** LAAG
- **Bestandsnaam:** `47_unbalanced_three_phase.svg`

---

## CATEGORIE 4: TRANSFORMATOREN & ENERGIE (7 schema's)

### 4.1 Transformator Ideaal - Energie Transfer
- **Type:** Energiediagram
- **Doel:** Toon geen energieverlies in ideale transformator
- **Elementen:**
  - Input vermogen (pin) links
  - Ideale transformator in centrum
  - Output vermogen (pout) rechts
  - Pin = Pout
  - Wikkelingverhouding N₁:N₂
- **Annotaties:**
  - Rendement η = 100%
  - Geen koper- of ijzerverlies
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `50_ideal_transformer_power.svg`

### 4.2 Reële Transformator met Verliezen
- **Type:** Circuit schema
- **Doel:** Toon interne weerstand en inductie
- **Primaire zijde:**
  - Ideale bron
  - Koperweerstand Rc1
  - Inductie Lc1
- **Secundaire zijde:**
  - Koperweerstand Rc2
  - Inductie Lc2
  - Belasting ZL
- **Energieflow:**
  - Pin → verlies (I²R, magnetische) → Pout
  - Rendement < 100%
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `51_real_transformer_losses.svg`

### 4.3 Transformator Belastingcurve
- **Type:** Grafiek
- **X-as:** Belastingstroom (% of A)
- **Y-as:** Secundaire spanning (V)
- **Eigenschappen:**
  - Stijgende belasting → dalende U2
  - Spanningsdaling tengevolge interne R en L
  - Regelkarakteristiek aangetoond
- **Annotaties:**
  - ΔU = I₂(Rc + jωLc) translated naar primaire
- **Prioriteit:** LAAG
- **Bestandsnaam:** `52_transformer_load_characteristic.svg`

### 4.4 Kabelweerstand & Spanningsverlies
- **Type:** Circuit schema + berekening
- **Doel:** Toon effect van kabel op spanning
- **Elementen:**
  - Bron (links)
  - Kabel met weerstand Rk = ρl/A (midden)
  - Belasting (rechts)
  - Spanningsdaling ΔU = I·Rk aangegeven
  - U_belasting = U_bron - ΔU
- **Formules:**
  - ΔU = I·ρ·(l/A)
  - Max. toegestaan: ΔU ≤ 0.02·Ufase
- **Kleuren:**
  - Oorspronkelijke spanning: groen
  - Verlies: rood
  - Eindspanning: oranje
- **Prioriteit:** HOOG
- **Bestandsnaam:** `53_cable_voltage_drop.svg`

### 4.5 Rendement Motor vs Frequentie
- **Type:** Grafiek
- **X-as:** Motorbelasting (% of vermogen)
- **Y-as:** Rendement (%)
- **Curve karakteristieken:**
  - Rendement laag bij lage belasting
  - Maximum rond 75-90% belasting
  - Daalt weer bij zeer hoge belasting
  - Rendement-optimale werkingspunt aangegeven
- **Prioriteit:** LAAG
- **Bestandsnaam:** `54_motor_efficiency.svg`

### 4.6 Energieverbruik Berekening
- **Type:** Infografisch diagram
- **Doel:** E = P·t met omrekeningen
- **Elementen:**
  - Vermogen (W of kW) input
  - Tijd (s of h) input
  - Energie output
  - Omrekening naar joules en kilowattuur
  - Gerelateerde energiebronnen ter vergelijking (lamp, huishouden)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `55_energy_consumption.svg`

### 4.7 Brandpuntsenergieverdeling (Sankey-diagram)
- **Type:** Sankey/Flow diagram
- **Doel:** Toon energieflow in industrieel systeem
- **Elementen:**
  - Input energie (100%)
  - Splitsing naar:
    - Nuttige output (80-90%)
    - Warmte-verlies (5-15%)
    - Stralingsverkies (1-5%)
  - Breedte van stromen = percentage
  - Kleuren: groen (nuttig), rood (verlies)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `56_energy_distribution_sankey.svg`

---

## CATEGORIE 5: RESONANTIE & FILTERS (6 schema's)

### 5.1 Resonantiefrequentie RLC
- **Type:** Grafiek
- **X-as:** Frequentie (f of ω)
- **Y-as:** Impedantie |Z|
- **Karakteristieken:**
  - Diepe dip op f₀ = 1/(2π√LC)
  - Links van f₀: capacitief (XC > XL)
  - Rechts van f₀: inductief (XL > XC)
  - Minimale Z op f₀
- **Annotaties:**
  - Faktor Q aangegeven (scherpte)
  - Bandbreedte BW = f₀/Q
- **Prioriteit:** HOOG
- **Bestandsnaam:** `60_resonance_frequency.svg`

### 5.2 Stroom bij Resonantie RLC
- **Type:** Grafiek
- **X-as:** Frequentie (f)
- **Y-as:** Stroom (I)
- **Karakteristieken:**
  - Piek op f₀ (maximale stroom)
  - Bepaald door R alleen: I_max = U/R
  - Breedte piek = Q-factor
  - Hoge Q → scherpe piek → selectiever
- **Annotaties:**
  - -3dB punten (f₁, f₂)
  - Bandbreedte = f₂ - f₁
- **Prioriteit:** HOOG
- **Bestandsnaam:** `61_resonance_current.svg`

### 5.3 Impedantie Hoek (φ) vs Frequentie
- **Type:** Grafiek
- **X-as:** Frequentie (f)
- **Y-as:** Faseverschuiving φ (graden)
- **Karakteristieken:**
  - Links van f₀: φ < 0 (capacitief, I vooruit)
  - Op f₀: φ = 0 (resistief)
  - Rechts van f₀: φ > 0 (inductief, I achter)
  - S-vormige curve
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `62_impedance_phase_vs_frequency.svg`

### 5.4 Q-factor en Bandbreedte
- **Type:** Grafiek + annotaties
- **X-as:** Frequentie (f)
- **Y-as:** Impedantie of stroom
- **Twee curves:**
  - Hoog Q (scherpe piek, smal):
    - Selectief, hoge Q-factor (Q = f₀/BW > 10)
  - Laag Q (brede piek, plat):
    - Breed resonantiegebied, lage Q-factor (Q < 1)
- **Annotaties:**
  - Q = f₀/BW
  - Q = ωL/R (inductief)
  - Q = 1/(ωRC) (capacitief)
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `63_q_factor_bandwidth.svg`

### 5.5 Parallel RLC Resonantie
- **Type:** Grafiek
- **X-as:** Frequentie (f)
- **Y-as:** Impedantie |Z|
- **Karakteristieken:**
  - PIEK (maximum) op resonantiefrequentie
  - Links/rechts: impedantie lager
  - Verschilt van serie (dip in serie, piek in parallel)
  - Stromen IL en IC kunnen hoog zijn ondanks totaal-I laag
- **Annotaties:**
  - Antiresonantie
  - Zeer hoge Z op f₀
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `64_parallel_rlc_resonance.svg`

### 5.6 Filter Frequency Response (Laag-doorlaatfilter)
- **Type:** Grafiek (Bode-achtig)
- **X-as:** Frequentie (log schaal)
- **Y-as:** Versterking (dB)
- **RC Laagdoorlaatfilter:**
  - Plat antwoord onder afsnijfrequentie
  - -3dB bij fc = 1/(2πRC)
  - -20dB/decade helling erna
  - Diepe labels
- **Varianten:**
  - 1e-orde RC
  - 2e-orde RLC
- **Prioriteit:** LAAG
- **Bestandsnaam:** `65_filter_frequency_response.svg`

---

## CATEGORIE 6: SPECIALE SCHEMA'S (6 schema's)

### 6.1 Maximaal Vermogensoverdracht (MPT)
- **Type:** Grafiek
- **X-as:** Belastingweerstand RL (Ω)
- **Y-as:** Vermogen naar belasting (W)
- **Karakteristieken:**
  - Parabola met piek
  - Maximum op RL = Rth (Thévenin-weerstand)
  - Voorbeelden: RL = 10Ω, 20Ω, 30Ω
  - Pmax = Vth²/(4·Rth)
- **Annotaties:**
  - "Maximum Power Transfer Theorem"
  - RL = Rth* (matched belasting)
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `70_maximum_power_transfer.svg`

### 6.2 Vervangingscapaciteit - Serie/Parallel
- **Type:** Diagram
- **3 voorbeelden:**
  - C1, C2, C3 in serie → 1/Cv = 1/C1 + 1/C2 + 1/C3
  - C1, C2, C3 parallel → Cv = C1 + C2 + C3
  - Gemengde schakeling (met stap-voor-stap reductie)
- **Berekeningen:**
  - Getallen in elke stap
  - Eindresultaat aangegeven
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `71_capacitor_combination.svg`

### 6.3 Vervangingsinductie - Serie/Parallel
- **Type:** Diagram
- **Identiek aan capaciteur:**
  - L1, L2, L3 in serie → Lv = L1 + L2 + L3
  - L1, L2, L3 parallel → 1/Lv = 1/L1 + 1/L2 + 1/L3
  - Gekoppelde spoelen (M term)
- **Prioriteit:** MIDDEL
- **Bestandsnaam:** `72_inductor_combination.svg`

### 6.4 AC vs DC Signaal
- **Type:** Grafiek
- **2 kolommen:**
  - DC: Vlakke lijn op hoogte U
  - AC: Sinusvormige oscillatie rond 0
- **Labels:**
  - DC: constante spanning
  - AC: effectieve waarde (RMS)
  - Piek-waarde (amplitude)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `73_ac_vs_dc.svg`

### 6.5 Spoelkarakteristiek (ω vs Z vs φ)
- **Type:** Dubbele grafiek
- **Bovenste grafiek:**
  - X-as: Frequentie (f)
  - Y-as: Impedantie (Ω)
  - Lineaire stijging: Z = XL = ωL
- **Onderste grafiek:**
  - X-as: Frequentie
  - Y-as: Fase (φ)
  - Constant: φ ≈ 90° (ideale spoel)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `74_coil_characteristics.svg`

### 6.6 Condensatorkarakteristiek (ω vs Z vs φ)
- **Type:** Dubbele grafiek
- **Bovenste grafiek:**
  - Dalende curve: Z = XC = 1/(ωC)
- **Onderste grafiek:**
  - Constant: φ ≈ -90° (ideale condensator)
- **Prioriteit:** LAAG
- **Bestandsnaam:** `75_capacitor_characteristics.svg`

---

## SAMENVATTINGSTABEL

| # | Naam | Type | Prioriteit | Bestandsnaam | Categorie |
|----|------|------|------------|--------------|-----------|
| 1.1 | Kirchhoff 1e wet | Schema | HOOG | 01_kirchhoff_1e_wet.svg | Netwerk |
| 1.2 | Kirchhoff 2e wet | Schema | HOOG | 02_kirchhoff_2e_wet.svg | Netwerk |
| 1.3 | Thévenin equivalent | Schema | HOOG | 03_thevenin_equivalent.svg | Netwerk |
| 1.4 | Norton equivalent | Schema | HOOG | 04_norton_equivalent.svg | Netwerk |
| 1.5 | Serie-parallel redutie | Schema | HOOG | 05_serie_parallel_reduction.svg | Netwerk |
| 1.6 | RLC serie | Schema | HOOG | 06_rlc_series_circuit.svg | Netwerk |
| 1.7 | RLC parallel | Schema | MIDDEL | 07_rlc_parallel_circuit.svg | Netwerk |
| 1.8 | Transformator ideaal | Schema | HOOG | 08_transformer_ideal.svg | Netwerk |
| 1.9 | Gekoppelde spoelen | Schema | MIDDEL | 09_coupled_coils.svg | Netwerk |
| 1.10 | Ladder netwerk | Schema | MIDDEL | 10_ladder_network_reduction.svg | Netwerk |
| 1.11 | Volt- en stroommeter | Schema | LAAG | 11_voltmeter_ammeter.svg | Netwerk |
| 1.12 | Wienbrug | Schema | LAAG | 12_wien_bridge.svg | Netwerk |
| 2.1 | Phasor resistief | Diagram | HOOG | 20_phasor_resistive.svg | Fase |
| 2.2 | Phasor inductief | Diagram | HOOG | 21_phasor_inductive.svg | Fase |
| 2.3 | Phasor capacitief | Diagram | HOOG | 22_phasor_capacitive.svg | Fase |
| 2.4 | Impedantie driehoek | Diagram | HOOG | 23_impedance_triangle.svg | Fase |
| 2.5 | Vermogen driehoek | Diagram | HOOG | 24_power_triangle.svg | Fase |
| 2.6 | RLC impedantie vector | Diagram | HOOG | 25_rlc_impedance_vector.svg | Fase |
| 2.7 | RLC admittantie | Diagram | MIDDEL | 26_rlc_admittance_vector.svg | Fase |
| 2.8 | Resonantie fasoren | Diagram | MIDDEL | 27_resonance_phasors.svg | Fase |
| 2.9 | Cosφ correctie | Diagram | HOOG | 28_cosphi_correction.svg | Fase |
| 2.10 | Momentaan vermogen | Grafiek | MIDDEL | 29_instantaneous_power.svg | Fase |
| 2.11 | Frequentierespons | Grafiek | MIDDEL | 30_frequency_response.svg | Fase |
| 2.12 | Polair/Rechthoekig | Diagram | LAAG | 31_polar_rectangular.svg | Fase |
| 3.1 | 3-fase spanningen | Grafiek | HOOG | 40_three_phase_voltages.svg | 3-Fase |
| 3.2 | Ster-koppeling | Schema | HOOG | 41_star_connection.svg | 3-Fase |
| 3.3 | Delta-koppeling | Schema | HOOG | 42_delta_connection.svg | 3-Fase |
| 3.4 | Ster-Delta transf. | Schema | HOOG | 43_star_delta_transformation.svg | 3-Fase |
| 3.5 | Phasor 3-fase | Diagram | HOOG | 44_three_phase_phasor_ij.svg | 3-Fase |
| 3.6 | Lijn-fase spanning | Diagram | HOOG | 45_line_phase_voltage.svg | 3-Fase |
| 3.7 | 3-fase vermogen | Diagram | MIDDEL | 46_three_phase_power.svg | 3-Fase |
| 3.8 | Ongebalanceerd 3-f | Schema | LAAG | 47_unbalanced_three_phase.svg | 3-Fase |
| 4.1 | Transformator energie | Diagram | MIDDEL | 50_ideal_transformer_power.svg | Energie |
| 4.2 | Reële transformator | Schema | MIDDEL | 51_real_transformer_losses.svg | Energie |
| 4.3 | Transformator belast. | Grafiek | LAAG | 52_transformer_load_characteristic.svg | Energie |
| 4.4 | Kabelspanningsverlies | Schema | HOOG | 53_cable_voltage_drop.svg | Energie |
| 4.5 | Motor rendement | Grafiek | LAAG | 54_motor_efficiency.svg | Energie |
| 4.6 | Energieverbruik | Diagram | LAAG | 55_energy_consumption.svg | Energie |
| 4.7 | Sankey energieflow | Diagram | LAAG | 56_energy_distribution_sankey.svg | Energie |
| 5.1 | Resonantiefrequentie | Grafiek | HOOG | 60_resonance_frequency.svg | Resonantie |
| 5.2 | Stroom resonantie | Grafiek | HOOG | 61_resonance_current.svg | Resonantie |
| 5.3 | Fase vs frequentie | Grafiek | MIDDEL | 62_impedance_phase_vs_frequency.svg | Resonantie |
| 5.4 | Q-factor/BW | Grafiek | MIDDEL | 63_q_factor_bandwidth.svg | Resonantie |
| 5.5 | Parallel RLC res. | Grafiek | MIDDEL | 64_parallel_rlc_resonance.svg | Resonantie |
| 5.6 | Filter response | Grafiek | LAAG | 65_filter_frequency_response.svg | Resonantie |
| 6.1 | Max vermogen | Grafiek | MIDDEL | 70_maximum_power_transfer.svg | Speciaal |
| 6.2 | Capaciteit combinatie | Diagram | MIDDEL | 71_capacitor_combination.svg | Speciaal |
| 6.3 | Inductie combinatie | Diagram | MIDDEL | 72_inductor_combination.svg | Speciaal |
| 6.4 | AC vs DC | Grafiek | LAAG | 73_ac_vs_dc.svg | Speciaal |
| 6.5 | Spoelkarakteristiek | Grafiek | LAAG | 74_coil_characteristics.svg | Speciaal |
| 6.6 | Condensatorkaraktr. | Grafiek | LAAG | 75_capacitor_characteristics.svg | Speciaal |

---

## PRIORITEITSVERDELING

**HOOG prioriteit (18 schema's) — DIRECT NODIG:**
- 01, 02, 03, 04, 05, 06, 08: Netwerktheorie (Kirchhoff, Thévenin, Norton, RLC)
- 20, 21, 22, 23, 24, 25, 28: Fasediagrammen (impedantie, vermogen, cosφ)
- 40, 41, 42, 43, 44, 45: Driefasensystemen
- 53: Kabelspanningsverlies
- 60, 61: Resonantie

**MIDDEL prioriteit (18 schema's) — ONDERSTEUNEND:**
- 07, 09, 10: Extra netwerkschema's
- 26, 27, 29, 30: Verdere faseanalyse
- 46, 47: 3-fase uitbreidingen
- 50, 51: Transformatorverlies
- 62, 63, 64: Resonantie diepte
- 70, 71, 72: Theorema's

**LAAG prioriteit (9 schema's) — OPTIONEEL:**
- 11, 12: Speciale netwerken
- 31: Polair/rechthoekig
- 52, 54, 55, 56: Transformator/energie grafieken
- 65: Filters
- 73, 74, 75: Signaal karakteristieken

---

## GENERATIEVOLGORDE AANBEVELING

**Fase 1 — Core Concepts (Week 1):**
1. Alle 18 HOOG prioriteit schema's
2. Focus op: Kirchhoff, Thévenin, RLC, Phasors, 3-fase

**Fase 2 — Verdieping (Week 2):**
3. Alle 18 MIDDEL prioriteit schema's
4. Focus op resonantie, transformatoren, vectoranalyse

**Fase 3 — Aanvulling (Week 3):**
5. LAAG prioriteit schema's naar behoefte
6. Focus op niche-onderwerpen

---

## BESTANDSSTRUCTUUR

```
ncoi-energietechniek-anki/
├── images/
│   ├── 01-networks/
│   │   ├── 01_kirchhoff_1e_wet.svg
│   │   ├── 02_kirchhoff_2e_wet.svg
│   │   ├── ... (tot 12)
│   ├── 02-phasors/
│   │   ├── 20_phasor_resistive.svg
│   │   ├── ... (tot 31)
│   ├── 03-threephase/
│   │   ├── 40_three_phase_voltages.svg
│   │   ├── ... (tot 47)
│   ├── 04-energy/
│   │   ├── 50_ideal_transformer_power.svg
│   │   ├── ... (tot 56)
│   ├── 05-resonance/
│   │   ├── 60_resonance_frequency.svg
│   │   ├── ... (tot 65)
│   └── 06-special/
│       ├── 70_maximum_power_transfer.svg
│       ├── ... (tot 75)
```

---

## KLEUREN STANDAARDEN

**Voor alle schema's:**
- **Spanningsbronnen:** ⚪ wit met + / - labels, rode grens
- **Weerstanden:** ⬜ vierkant of zigzag, bruin/rood
- **Spoelen:** 🔲 spiraal, groen
- **Condensatoren:** ⬚ twee lijnen, blauw
- **Stromen:** pijlen met label
- **Phasors:**
  - Spanningen: rood
  - Stromen: blauw
  - Impedantie: groen
  - Hoeken: geel arc

**3-fase:**
- Fase A: rood
- Fase B: geel
- Fase C: blauw
- Nul: zwart/grijs

---

## BESCHRIJVING PER SCHEMA — SAMENVATTING

Elk schema bevat:
1. **Titel + nummer** (bv. "1.3 Thévenin Equivalent Circuit")
2. **Type** (Circuit, Grafiek, Phasor, etc.)
3. **Doel** (wat leren?)
4. **Elementen** (componenten)
5. **Annotaties** (labels, formules)
6. **Kleuren** (voor duidelijkheid)
7. **Prioriteit** (HOOG/MIDDEL/LAAG)
8. **Bestandsnaam** (SVG pad)

---

**Status:** ✅ Specificatie voltooid
**Volgende stap:** SVG-generatie starten (Fase 1)
**Geschat aantal SVG-files:** 45
**Geschatte doorlooptijd:** 4-6 weken (afhankelijk van tool)

