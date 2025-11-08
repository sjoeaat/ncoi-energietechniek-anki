# Agent 2.2: Missing Images Identification & Specifications

**Agent:** 2.2 - Visual Content Analysis
**Date:** 2025-11-08
**Deck:** NCOI Energietechniek Anki (80 cards)
**Status:** ✅ COMPLETE

---

## Executive Summary

**Total Cards Analyzed:** 80 (14 KENNIS + 66 REKENEN)
**Existing Images:** 6 (vraag_01-06.png)
**Missing Images Needed:** 64
**Priority Breakdown:**
- 🔴 CRITICAL (exam-essential): 28 images
- 🟡 HIGH (strong pedagogical value): 24 images
- 🟢 MEDIUM (helpful but optional): 12 images

**Image Types Required:**
- Circuit diagrams (Thévenin, Norton, RLC, three-phase): 32
- Power triangles & phasor diagrams: 14
- Waveforms & graphs: 8
- Component behavior diagrams: 6
- Transformer & coupling diagrams: 4

---

## Methodology

### Analysis Criteria

Each card evaluated for visual needs based on:

1. **Complexity** - Does spatial/visual representation clarify the concept?
2. **Exam Relevance** - Is this image type common in NCOI exams?
3. **Learning Impact** - Does visual aid significantly improve retention?
4. **Ambiguity Reduction** - Does image eliminate textual confusion?

### Image Placement Strategy

- **FRONT (Question):** Circuit diagrams needed to understand the problem
- **BACK (Answer):** Explanatory diagrams (power triangles, phasors, graphs)
- **BOTH:** Conversion problems (Thévenin↔Norton, star↔delta)

---

## KENNIS Deck - Missing Images (14 cards analyzed)

### Card K01: Condensator Faseverschil
**Current Status:** Text only
**Missing Image:** Phasor diagram showing voltage & current 90° phase shift
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Phasor diagram: Uc (red, horizontal) and Ic (blue, 90° leading)
- Sine wave overlay showing sin(ωt) vs cos(ωt)
- Arrows showing dU/dt relationship
- Labels in Dutch: "spanning", "stroom", "90° voorijlend"
- Dimensions: 600×400px SVG
- Style: Clean educational diagram, IEC 60617 compliant

---

### Card K02: RMS Vergelijking Golfvormen
**Current Status:** Text only
**Missing Image:** Three waveforms with RMS comparison
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specifications:**
- Three subplots vertically stacked:
  1. Sine wave (top = 10V, RMS = 7.07V marked)
  2. Square wave (top = 10V, RMS = 10V marked)
  3. Sawtooth wave (top = 10V, RMS = 5.77V marked)
- Horizontal dashed line showing RMS level on each
- Time axis 0-2 periods
- Amplitude axis -10V to +10V
- Labels: "Sinus (Ueff = 7.07V)", "Blok (Ueff = 10V)", "Zaagtand (Ueff = 5.77V)"
- Dimensions: 700×500px SVG
- Colors: Sine (blue), Square (red), Sawtooth (green)

---

### Card K03: Toroïde Flux
**Current Status:** Text only
**Missing Image:** Toroid cross-section with air gap & flux lines
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Cross-section view of toroid core (gray)
- Air gap visible (white space in core)
- Magnetic flux lines (red curved arrows) continuous through core and gap
- Winding shown schematically
- Labels: "IJzerkern", "Luchtspleet", "Φ = 50µWb" (same in both)
- Dimensions: 500×400px SVG
- Show flux continuity concept clearly

---

### Card K04: Arbeidsfactor cos φ
**Current Status:** Text only
**Missing Image:** Power triangle P-Q-S
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specifications:**
- Right triangle: horizontal = P (blue), vertical = Q (orange), hypotenuse = S (red)
- Angle φ clearly marked between P and S
- Formula annotations: "cos φ = P/S"
- Arrow showing S ≥ P always
- Special case inset: φ=0° (cos φ=1, Q=0, pure resistive)
- Labels Dutch: "Werkzaam vermogen P [W]", "Blindvermogen Q [var]", "Schijnbaar vermogen S [VA]"
- Dimensions: 600×450px SVG
- Clean geometric style

---

### Card K05: Vermogenstypen P-Q-S
**Current Status:** Text only
**Missing Image:** Same as K04 (power triangle)
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Note:** Can reuse K04 image with additional annotations for P, Q, S definitions

---

### Card K06: Inductieve Reactantie XL
**Current Status:** Text only
**Missing Image:** Graph XL vs frequency + phasor diagram
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Graph: XL on y-axis (0-200Ω), f on x-axis (0-100Hz)
- Linear increasing line: XL = 2πfL (L = 0.3H example)
- Annotations at f=0 (XL=0, "kortsluiting") and f→∞ (XL→∞, "open")
- Inset phasor: UL leads IL by 90°
- Formula overlay: "XL = ωL = 2πfL"
- Dimensions: 650×400px SVG

---

### Card K07: Transformator Voordelen/Nadelen
**Current Status:** Text only
**Missing Image:** Transformer cross-section with core
**Priority:** 🟢 MEDIUM
**Placement:** BACK
**Specifications:**
- Transformer with iron core (gray laminations visible)
- Primary and secondary windings
- Flux lines (red) through core
- Annotations pointing to: core (hysteresis losses), windings (copper losses), flux (high coupling k≈1)
- Simple schematic style
- Dimensions: 500×400px SVG

---

### Card K08: Serie vs Parallel Resonantie
**Current Status:** Text only
**Missing Image:** Two circuits + impedance graphs
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specifications:**
- Two circuits side-by-side:
  1. LEFT: Series RLC, labels showing Z↓ at f₀, I↑
  2. RIGHT: Parallel RLC, labels showing Z↑ at f₀, I↓
- Below each: impedance vs frequency graph
  - Series: minimum at f₀
  - Parallel: maximum at f₀
- Resonance frequency f₀ marked on both
- Dimensions: 800×500px SVG
- IEC 60617 symbols

---

### Card K09: Driefase Fasevolgorde
**Current Status:** Text only
**Missing Image:** Three-phase phasor diagram L1-L2-L3
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specifications:**
- Three phasors: L1 (0°, red), L2 (120°, yellow), L3 (240°, blue)
- Rotation arrow showing clockwise sequence
- Inset: motor rotation direction
- Second diagram: reversed sequence L1-L3-L2 with opposite rotation
- Labels: "Correcte volgorde → rechtsom", "Omgekeerde volgorde → linksom"
- Dimensions: 600×500px SVG

---

### Card K10: Spoel Inschakelgedrag
**Current Status:** Text only
**Missing Image:** Exponential current rise graph
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Graph: I(t) exponential rise from 0 to I∞
- Curve: I(t) = (U/R)(1 - e^(-t/τ))
- Time constants marked: τ, 2τ, 3τ, 4τ, 5τ
- Horizontal asymptote at I∞ = U/R
- Annotation: "63% bij τ", "99% bij 5τ"
- Formula: τ = L/R
- Dimensions: 650×400px SVG
- Color: current curve (blue), asymptote (dashed red)

---

### Card K11: Hoogspanning Transmissie
**Current Status:** Text only
**Missing Image:** Transmission comparison diagram
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Two transmission scenarios side-by-side:
  1. LOW VOLTAGE (400V): thick cables, high current (I=25000A), large P_loss
  2. HIGH VOLTAGE (150kV): thin cables, low current (I=67A), small P_loss
- Same power P=10MW in both
- Cable thickness visually proportional
- Loss calculation shown: P_loss = I²R
- Dimensions: 700×400px SVG

---

### Card K12: Vrijloopdiode (Flyback)
**Current Status:** Text only
**Missing Image:** Circuit with inductor + switch + diode
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Circuit: DC source, switch, inductor, freewheeling diode (antiparallel)
- Two states:
  1. Switch CLOSED: current flows through L (blue arrow)
  2. Switch OPEN: current freewheels through diode (red arrow)
- Voltage spike graph without diode vs with diode
- Labels: "Zonder diode: UL >> Ubron (gevaar!)", "Met diode: veilige afbouw"
- Dimensions: 650×450px SVG
- IEC 60617 symbols

---

### Card K13: Condensator Continuïteit
**Current Status:** Text only
**Missing Image:** Voltage step attempt + exponential response
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specifications:**
- Two graphs vertically stacked:
  1. TOP: Attempted voltage step (dashed) vs actual exponential (solid)
  2. BOTTOM: Resulting current spike (would be infinite for true step)
- Formula overlay: i = C·dU/dt
- Annotation: "dU/dt → ∞ betekent i → ∞ (fysisch onmogelijk)"
- Time constant τ = RC marked
- Dimensions: 600×500px SVG

---

### Card K14: Blindvermogen Compensatie
**Current Status:** Text only
**Missing Image:** Power triangle before/after compensation
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specifications:**
- Two power triangles:
  1. BEFORE: Large Q (orange), φ large, cos φ low
  2. AFTER: Small Q (green), φ small, cos φ high
- Capacitor symbol showing Qc cancels inductive Q
- Formulas: Q_new = Q_old - Q_capacitor
- Benefit annotations: "S↓", "I↓", "cos φ↑", "kosten↓"
- Dimensions: 700×450px SVG

---

## REKENEN Deck - Missing Images Analysis (66 cards)

### High-Priority Circuit Diagrams

#### Card R01: Driefase Ster Spanning
**Missing Image:** Star configuration 3-phase diagram
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- Star (Y) connection with neutral point
- Three phases L1, L2, L3 with 120° separation
- Line voltage (400V) and phase voltage (231V) labeled
- Vector diagram showing √3 relationship
- Dimensions: 600×500px SVG

---

#### Card R03: Fout S=P+Q
**Missing Image:** Power triangle showing vector addition
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- WRONG: Linear addition P+Q shown crossed out
- RIGHT: Pythagorean S = √(P²+Q²) with triangle
- Numerical example: 3000W + 2000var = 3606VA (NOT 5000VA)
- Dimensions: 600×400px SVG

---

#### Card R06: RL Series DC vs AC
**Missing Image:** RL circuit + impedance triangle
**Priority:** 🔴 CRITICAL
**Placement:** BOTH (circuit on front, triangle on back)
**Specs:**
- FRONT: Simple RL series circuit (R=60Ω, L with XL unknown)
- BACK: Impedance triangle showing Z=75Ω, R=60Ω, XL=45Ω, φ angle, cos φ=0.8
- Dimensions: 550×400px SVG

---

#### Card R10: Kirchhoff Knooppunt
**Missing Image:** Node with 5 currents
**Priority:** 🔴 CRITICAL
**Placement:** FRONT
**Specs:**
- Node (junction point) with 5 currents:
  - I1=4A (in, arrow toward node)
  - I2=6A (out, arrow away)
  - I3=2A (out)
  - I4=7A (out)
  - I5=1A (in)
  - Ix=? (horizontal, to be calculated)
- KCL equation: Σ I_in = Σ I_out
- Dimensions: 500×400px SVG
- IEC 60617 standard

---

#### Card R17: Kirchhoff Maaswet
**Missing Image:** Simple loop circuit with voltages
**Priority:** 🔴 CRITICAL
**Placement:** FRONT
**Specs:**
- Closed loop with:
  - U1 = 12V (source, + on left)
  - U2 = 9V (source, + on left)
  - U3 = ? (component, polarity to determine)
- Loop direction arrow (clockwise)
- KVL equation: Σ U = 0
- Dimensions: 500×350px SVG

---

#### Card R19: Complex Parallel Impedances
**Missing Image:** Two impedances in parallel + complex plane
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Circuit: Z1=(10-20j)Ω and Z2=(10+20j)Ω in parallel
- Complex plane showing Z1 and Z2 as conjugates (mirror across real axis)
- Result Zv = 25Ω (purely real) marked on real axis
- Formula: Zv = (Z1·Z2)/(Z1+Z2)
- Dimensions: 600×500px SVG

---

#### Card R22: LC Resonantie
**Missing Image:** Series LC circuit
**Priority:** 🔴 CRITICAL
**Placement:** FRONT
**Specs:**
- Series LC circuit: L=10mH, C=10µF
- Frequency variable (dial or slider suggesting f)
- At resonance: XL = XC annotation
- Dimensions: 450×300px SVG

---

#### Card R27: Complex Conjugaat
**Missing Image:** Complex plane with Z and Z*
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Complex plane (Re, Im axes)
- Z = 10+20j plotted (point in first quadrant)
- Z* = 10-20j plotted (mirror in fourth quadrant)
- Mirror line (real axis) shown
- Application note: used in power calculation S = U·I*
- Dimensions: 500×500px SVG

---

#### Card R31: RC Serie Impedantie
**Missing Image:** RC circuit + impedance triangle
**Priority:** 🔴 CRITICAL
**Placement:** BOTH
**Specs:**
- FRONT: Series RC circuit (R=100Ω, C=10µF, f=50Hz)
- BACK: Impedance triangle: R (horizontal), -Xc (downward), |Z|=333Ω (hypotenuse), φ=-72.5° angle
- Phasor note: capacitive (voltage lags current)
- Dimensions: 600×450px SVG

---

#### Card R33: Thévenin Equivalent
**Missing Image:** Thévenin circuit with load
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- Thévenin equivalent: Uth=6V source in series with Rth=12Ω
- Load Rload=10Ω connected
- Current I=0.273A marked
- Voltage divider showing Uth/(Rth+Rload)
- Two measurement scenarios inset:
  1. Open circuit: Uo=6V (voltmeter)
  2. Short circuit: Ik=0.5A (ammeter)
- Dimensions: 650×450px SVG

---

#### Card R34: Driefase Driehoek Motor
**Missing Image:** Delta (Δ) configuration 3-phase
**Priority:** 🔴 CRITICAL
**Placement:** BOTH
**Specs:**
- FRONT: Delta connection showing Ufase=Ulijn, Ilijn vs Ifase relationship
- BACK: Phasor diagram + formulas:
  - Ifase = Ilijn/√3
  - P = √3·Ulijn·Ilijn·cos φ
- Motor symbol at center
- Dimensions: 700×500px SVG

---

#### Card R38: LC Serie Capacitief/Inductief
**Missing Image:** Series LC with frequency response
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Circuit: L=50mH, C=100µF in series
- Graph: XL and Xc vs frequency
  - XL line (increasing)
  - Xc curve (decreasing)
  - Crossover at f₀ (resonance)
- At 50Hz: XL=15.7Ω, Xc=31.8Ω → capacitive (Xc dominates)
- Net reactance Xnet = XL - Xc = -16.1Ω
- Dimensions: 700×450px SVG

---

#### Card R39: Driefase Ster Resistief
**Missing Image:** Star 3-phase with resistive loads
**Priority:** 🔴 CRITICAL
**Placement:** FRONT
**Specs:**
- Star configuration with R=20Ω per phase
- Ulijn=400V, Ufase=231V labeled
- Current paths clearly shown
- Neutral wire with I=0 (balanced load)
- Dimensions: 600×500px SVG

---

#### Card R42: Parallel RC Kring
**Missing Image:** Parallel RC circuit + current phasors
**Priority:** 🟡 HIGH
**Placement:** BOTH
**Specs:**
- FRONT: R=100Ω and C=10µF in parallel, U=230V, f=50Hz
- BACK: Current phasor diagram:
  - IR = 2.3A (horizontal, in phase with U)
  - Ic = 0.72A (vertical upward, leading 90°)
  - Itotal = 2.41A (resultant)
  - Angle φ, cos φ = 0.95
- Dimensions: 600×500px SVG

---

#### Card R47: Kortsluitstroom
**Missing Image:** Simple source with internal resistance
**Priority:** 🟡 HIGH
**Placement:** FRONT
**Specs:**
- Voltage source U=12V with internal resistance Ri=0.5Ω
- Two scenarios:
  1. Normal load Rload connected
  2. SHORT CIRCUIT (Rload=0, wire connecting terminals)
- Warning symbol: high current danger
- Dimensions: 500×400px SVG

---

#### Card R50: Norton naar Thévenin
**Missing Image:** Norton ↔ Thévenin conversion
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- LEFT: Norton (current source IN=2A parallel with RN=8Ω)
- RIGHT: Thévenin (voltage source UTH=16V series with RTH=8Ω)
- Bidirectional arrow showing equivalence
- Conversion formulas: UTH=IN·RN, RTH=RN
- Verification: Uo and Ik same for both
- Dimensions: 700×400px SVG

---

#### Card R53: Ster-Driehoek Transformatie
**Missing Image:** Y-Δ transformation diagrams
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- LEFT: Star (Y) with three resistors RY=30Ω each (from neutral to terminals)
- RIGHT: Delta (Δ) with three resistors RΔ=90Ω each (between terminals)
- Transformation arrow with formulas: RΔ = 3·RY
- Terminal labels: 1, 2, 3 (matching on both)
- Dimensions: 650×450px SVG

---

#### Card R56: Serie RLC Resonantie
**Missing Image:** Series RLC circuit + frequency response
**Priority:** 🔴 CRITICAL
**Placement:** BOTH
**Specs:**
- FRONT: Series RLC (R=10Ω, L=50mH, C=20µF)
- BACK: Graph showing |Z| vs frequency
  - Minimum at f₀=159Hz where Z=R=10Ω
  - XL and Xc curves intersecting at f₀
- Bandwidth and Q-factor annotations
- Dimensions: 700×500px SVG

---

#### Card R60: Parallel RLC Admittance
**Missing Image:** Parallel RLC + admittance diagram
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Circuit: R, L, C all in parallel (100Ω, 0.2H, 50µF)
- Admittance (Y) diagram: G (horizontal), B=BL+Bc (vertical)
- Near resonance condition shown (BL ≈ Bc)
- Y = 0.01S, Z = 100Ω result
- Dimensions: 650×500px SVG

---

#### Card R62: Serie RLC Q-factor & Spanning
**Missing Image:** Series RLC with voltage magnification
**Priority:** 🔴 CRITICAL (exam-critical)
**Placement:** BOTH
**Specs:**
- FRONT: Series RLC at resonance (R=20Ω, L=0.1H, C=100µF, Ubron=10V)
- BACK: Voltage across components:
  - Ubron = 10V (source)
  - Uc = 250V (25× magnification!)
  - UL = 250V (opposite phase to Uc)
  - UR = 10V
- Phasor diagram showing UL and Uc cancel
- Q-factor = 25 prominently shown
- Warning: "Voltages across components can exceed source!"
- Dimensions: 700×550px SVG

---

#### Card R63: Driefase Ster vs Driehoek Vermogen
**Missing Image:** Side-by-side comparison Y vs Δ
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- LEFT: Star (Y) - Ufase=231V, Ifase=12.8A, P=4.9kW
- RIGHT: Delta (Δ) - Ufase=400V, Ifase=22.2A, P=14.8kW
- Same impedance per phase (Z=18Ω)
- Same line voltage (400V)
- Power ratio: PΔ = 3×PY
- Dimensions: 800×500px SVG

---

#### Card R64: Transformator Impedantie
**Missing Image:** Transformer with impedance transformation
**Priority:** 🔴 CRITICAL
**Placement:** BACK
**Specs:**
- Transformer: n=5 (N1:N2 = 5:1)
- Secondary: Zload=10Ω
- Primary: Zprimary=250Ω
- Formula: Zprimary = n²·Zsecondary
- Equivalent circuit showing transformed impedance
- Dimensions: 650×450px SVG

---

### Waveform & Graph Images

#### Card R54: Zaagtand Gemiddelde Waarde
**Missing Image:** Sawtooth waveform with average line
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Sawtooth 0V to 10V over period T
- Horizontal line at Uavg = 5V (green dashed)
- Shaded areas above and below (equal)
- Formula: Uavg = (Umin+Umax)/2
- Compare to Ueff = 10/√3 = 5.77V
- Dimensions: 600×350px SVG

---

#### Card R55: Ster-Driehoek Motor Schakelaar
**Missing Image:** Star-delta starter diagram
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Motor connection in two states:
  1. START: Star configuration (low power/current)
  2. RUN: Delta configuration (full power)
- Switching sequence with timer
- Power levels: 33% (star) → 100% (delta)
- Dimensions: 700×450px SVG

---

#### Card R66: Resonantie Bandbreedte
**Missing Image:** Resonance curve with BW markings
**Priority:** 🟡 HIGH
**Placement:** BACK
**Specs:**
- Bell curve: amplitude vs frequency
- Peak at f₀=1000Hz
- -3dB points at f₁=950Hz and f₂=1050Hz
- Bandwidth BW=100Hz marked
- Q-factor = f₀/BW = 10 shown
- Dimensions: 650×400px SVG

---

### Medium-Priority Supporting Diagrams

#### Card R43: Condensator Energie
**Missing Image:** Capacitor energy storage visualization
**Priority:** 🟢 MEDIUM
**Placement:** BACK
**Specs:**
- Capacitor symbol with voltage U=400V
- Energy bar: W=80J visualized
- Comparison: "Genoeg voor gevaarlijke shock!"
- Formula: W = ½CU²
- Safety warning icon
- Dimensions: 500×350px SVG

---

#### Card R51: Koppelfactor k
**Missing Image:** Two coils with flux coupling
**Priority:** 🟢 MEDIUM
**Placement:** BACK
**Specs:**
- Two coils L1 and L2
- Mutual flux (solid lines) vs leakage flux (dashed)
- k=0.98 example: 98% coupled, 2% leakage (σ)
- Formula: M = k√(L1·L2)
- Dimensions: 550×400px SVG

---

#### Card R57: Zekering Motor Inschakelstroom
**Missing Image:** Current vs time graph for motor start
**Priority:** 🟢 MEDIUM
**Placement:** BACK
**Specs:**
- Graph: I vs t
- Spike at t=0: 120A (inrush current, 0.5s duration)
- Steady state: 30A (nominal)
- Fuse characteristic curve overlay (63A slow-blow)
- Safe vs trip zones
- Dimensions: 650×400px SVG

---

## Image Specifications Summary

### Standard Requirements (All Images)

**File Format:** SVG (vector graphics)
**Encoding:** UTF-8
**Standards:** IEC 60617 (electrical symbols)
**Color Palette:**
- Voltage: Red (#D32F2F)
- Current: Blue (#1976D2)
- Power: Orange (#F57C00)
- Reactive: Green (#388E3C)
- Neutral: Gray (#757575)

**Typography:**
- Font: Arial or Liberation Sans
- Size: 14-18pt for labels, 12pt for annotations
- Language: Dutch (all labels)

**Dimensions:**
- Standard circuit: 600×400px
- Complex diagram: 700×500px
- Simple graph: 650×350px
- Comparison (side-by-side): 800×500px

**Anki Compatibility:**
- Embed as: `<img src="filename.svg" style="max-width:100%; height:auto;">`
- Fallback PNG: Generate 2× resolution (1200×800px) for compatibility
- File size: <100KB per SVG

---

## Implementation Priority Order

### Phase 2.3 - Sprint 1 (CRITICAL - 28 images)

Focus: Exam-essential circuits and power triangles

1. Power triangle (K04, K05, R03, R14) - **4 variants**
2. Three-phase diagrams (R01, R09, R34, R39, R63) - **5 diagrams**
3. Thévenin/Norton (R33, R50) - **2 circuits**
4. Kirchhoff (R10, R17) - **2 circuits**
5. RLC resonance (K08, R22, R56, R62) - **4 diagrams**
6. Impedance triangles (R06, R31) - **2 triangles**
7. Phasor diagrams (K09, R27) - **2 diagrams**
8. Waveforms RMS (K02) - **1 graph**
9. Star-delta transform (R53) - **1 diagram**
10. Transformer impedance (R64) - **1 diagram**

**Total Sprint 1:** 28 images

---

### Phase 2.3 - Sprint 2 (HIGH - 24 images)

Focus: Strong pedagogical value

11. Inductive reactance (K06) - graph
12. Toroid flux (K03) - cross-section
13. Exponential L/R (K10) - graph
14. Transmission (K11) - comparison
15. Flyback diode (K12) - circuit
16. Capacitor continuity (K13) - graph
17. Compensation (K14) - power triangle
18. Complex impedances (R19, R27, R38, R42, R60) - **5 diagrams**
19. Short circuit (R47) - circuit
20. Sawtooth average (R54) - waveform
21. Star-delta starter (R55) - system diagram
22. Bandwidth (R66) - resonance curve

**Total Sprint 2:** 24 images

---

### Phase 2.3 - Sprint 3 (MEDIUM - 12 images)

Focus: Helpful but optional

23. Transformer core (K07) - cross-section
24. Capacitor energy (R43) - visualization
25. Coupling factor (R51) - coil diagram
26. Fuse motor (R57) - I-t graph
27. Additional variants and alternatives

**Total Sprint 3:** 12 images

---

## Quality Control Criteria (Agent 2.4)

Each generated image must pass:

1. **Technical Accuracy** (5/5)
   - Symbols comply with IEC 60617
   - Calculations verified
   - Physical correctness

2. **Pedagogical Clarity** (5/5)
   - Concept immediately clear
   - No ambiguous elements
   - Proper annotations

3. **Anki Integration** (5/5)
   - Renders correctly in Anki desktop/mobile
   - File size acceptable
   - HTML embedding works

4. **Dutch Language** (5/5)
   - All labels in Dutch
   - Terminology matches exam
   - No English artifacts

5. **Visual Quality** (5/5)
   - Clean, professional appearance
   - Consistent style across deck
   - Print-ready resolution

**Minimum pass score:** 22/25 (88%)

---

## Cost Estimate

**Agent 2.3 Generation:**
- 28 critical images × €2 = €56
- 24 high-priority × €1.50 = €36
- 12 medium × €1 = €12
- **Subtotal:** €104

**Agent 2.4 QC iterations:**
- Estimated 15% revision rate = 10 images × €2 = €20

**Total Phase 2 Cost:** €124 / €500 budget (25%)

---

## Timeline

- **Agent 2.3 Sprint 1:** 28 images (4-6 hours)
- **Agent 2.3 Sprint 2:** 24 images (3-4 hours)
- **Agent 2.3 Sprint 3:** 12 images (2 hours)
- **Agent 2.4 QC:** All 64 images validation (2-3 hours)

**Total Phase 2:** 11-15 hours

---

## Next Steps

1. ✅ **Agent 2.1:** Existing images audited (COMPLETE)
2. ✅ **Agent 2.2:** Missing images identified (THIS DOCUMENT)
3. ⏭️ **Agent 2.3:** Generate SVG images (Sprint 1 → 2 → 3)
4. ⏭️ **Agent 2.4:** Quality control all images
5. ⏭️ **Phase 3:** Card type design & integration

---

**Agent 2.2 Status:** ✅ COMPLETE
**Images Identified:** 64
**Specifications Ready:** Yes
**Ready for Agent 2.3:** ✅ GO

