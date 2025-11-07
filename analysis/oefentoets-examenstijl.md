# Oefentoets Examenstijl - Analyse

**Aantal vragen:** 16

## Onderwerpen Overzicht

- 3‑fasen generator → lijnspanningen: 1 vraag(en)
- Aderdikte: 1 vraag(en)
- Condensatorbrug: 1 vraag(en)
- Juist / Onjuist: 1 vraag(en)
- Kirchhoff knooppunt: 1 vraag(en)
- LC-resonantie: 1 vraag(en)
- Motorvermogen: blindcomponent Q: 1 vraag(en)
- RL‑serie met toongenerator: 1 vraag(en)
- Spanningslus U₃: 1 vraag(en)
- Spanningsverlies 3‑fase + 2%‑norm: 1 vraag(en)
- Ster–Driehoek: 1 vraag(en)
- Thévenin met R₅: 1 vraag(en)
- Transformator: 1 vraag(en)
- Transformator‑kern: voor‑ en nadelen: 1 vraag(en)
- Zonnepanelen: jaaropbrengst: 1 vraag(en)
- cosφ‑correctie: 1 vraag(en)

---

## Examenvraag 1
**Onderwerp:** Aderdikte
**Format:** Multiple choice

**Vraag:**
Een koperleiding van 25 m heen en 25 m terug (effectief 50 m) mag maximaal 0,25 Ω totale weerstand hebben.
Welke minimale aderdikte kies je?

Gegeven: ρ Cu = 0,0178 Ω·mm²/m. Gebruik R = ρ·L/A .

**Opties:**
A) 1,5 mm²
B) 2,5 mm²
C) 4 mm²
D) 6 mm²

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): R = ρ·L/A (ρ(Cu) ≈ 0,0178 Ω·mm²/m). 1‑fase: effectieve lengte = heen + terug. A bepalen → eerstvolgende standaard‑mm².

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 2
**Onderwerp:** Condensatorbrug
**Format:** Open vraag / Berekening

**Vraag:**
Zie het netwerk hieronder. Alle condensatoren hebben dezelfde waarde C. Bepaal de vervangingscapaciteit C v tussen klemmen a en b:

Variant 2b — Enkelvoudige condensatorbelasting: f = 50 Hz, U = 10 V (RMS), C = 10 μF. Bepaal de totale stroom I tot . Hint: ω = 2πf, Z C = 1/(jωC).

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): Serie C: 1/C v = Σ(1/C); Parallel C: C v = Σ C. Brug in balans → midden‑tak beïnvloedt C v niet. Variant 2b: Z C = 1/(jωC), I = U/|Z C |.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 3
**Onderwerp:** Kirchhoff knooppunt
**Format:** Open vraag / Berekening

**Vraag:**
In een knooppunt vloeien stromen met zelfgekozen pijlen. Bepaal de aanwijzing van de ampèremeter en geef aan of de uitslag positief of negatief is. (Gebruik ΣI=0 met jouw tekenkeuze.)

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): KCL: ΣI = 0 met jouw pijlen. Negatieve uitslag = tegengestelde richting.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 4
**Onderwerp:** LC-resonantie
**Format:** Open vraag / Berekening

**Vraag:**
De bron voedt een L–C‑combinatie. Gegeven: L = 10 mH, C = 10 μF.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): f₀ = 1/(2π√(LC)); X L = ωL; X C = 1/(ωC). Serie: minimale Z; Parallel: maximale Z.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 5
**Onderwerp:** Ster–Driehoek
**Format:** Open vraag / Berekening

**Vraag:**
Zet het centrale gedeelte om van Δ→Y (of andersom indien handiger) en vereenvoudig het netwerk tot een serie/parallel‑combinatie zoals in de schets. Gebruik de getoonde waarden (Ω). Geef de omgezette waarden en het uiteindelijke equivalent.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): Δ→Y: Y‑tak = (Δ a ·Δ b )/(Δ a +Δ b +Δ c ). Y→Δ: Δ‑tak = (Y a Y b + Y b Y c + Y c Y a )/Y tegenover . Na omzetting opnieuw serie/parallel zoeken.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 6
**Onderwerp:** RL‑serie met toongenerator
**Format:** Open vraag / Berekening

**Vraag:**
Een toongenerator levert 10 V (RMS) op een RL‑serieschakeling met L = 10 mH en een onbekende R. De stroom is I = 125 mA. Het instrument geeft aan dat φ = 45°. Bepaal de frequentie f.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): |Z| = U/I; Z = R + jωL. tanφ = X L /R; X L = 2πfL (φ=45° ⇒ R = X L ).

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 7
**Onderwerp:** Thévenin met R₅
**Format:** Open vraag / Berekening

**Vraag:**
Teken het Thévenin‑vervangingsschema gezien over de klemmen van R₅ en bereken de stroom door R₅. Geef kort de stappen: U th , R th , I.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): U th = open‑klemspanning. R th : spanningsbronnen kort; stroombronnen open. I R5 = U th /(R th + R₅).

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 8
**Onderwerp:** Spanningslus U₃
**Format:** Open vraag / Berekening

**Vraag:**
Kies één maasrichting, noteer de polariteiten consequent en los op met ΣU=0 om U₃ te bepalen.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): KVL: ΣU = 0 met consistente polariteiten. Kies één maas en houd die aan.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 9
**Onderwerp:** Motorvermogen: blindcomponent Q
**Format:** Open vraag / Berekening

**Vraag:**
Een elektromotor neemt 60 kW actief vermogen op. Het schijnbaar vermogen is 68 kVA. Bepaal de blindcomponent Q in kVAr.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): Vermogensdriehoek: S² = P² + Q² ⇒ Q = √(S² − P²). Eenheden: W / var / VA (k‑prefix waar passend).

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 10
**Onderwerp:** Transformator
**Format:** Open vraag / Berekening

**Vraag:**
Een transformator heeft U₁ = 6000 V en U₂ = 800 V. Het aantal windingen aan de primaire zijde is N₁ = 300. Bepaal N₂.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): U₂/U₁ = N₂/N₁ (per fase bij 3‑fase). Verhouding op fase‑spanningen toepassen, daarna terug naar lijn indien nodig.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 11
**Onderwerp:** Zonnepanelen: jaaropbrengst
**Format:** Open vraag / Berekening

**Vraag:**
PV-systeem: 120 panelen, 360 Wp per paneel, paneeloppervlakte 2,0 m × 1,0 m, opbrengst 140 kWh/m²·jaar. Jaarverbruik is 40 MWh. Hoeveel panelen moeten minimaal extra geplaatst worden om energieneutraal te zijn?

**Hints/Uitwerking:**
Holmes‑stijl hint: E_jaar ≈ instraling (kWh/m²·jr) × oppervlak × η. Aantal panelen = E_doel / (paneel_kWh).

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 12
**Onderwerp:** cosφ‑correctie
**Format:** Open vraag / Berekening

**Vraag:**
Driefasenmotor (symmetrisch), P = 50 kW, cosφ₁ = 0,75 (230/400 V). Eis: cosφ₂ ≥ 0,92. Bereken het bij te schakelen blindvermogen van de condensatorbank (in kVAr).

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): Q_C = P (tanφ₁ − tanφ₂). cosφ = P/S; sinφ = Q/S.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 13
**Onderwerp:** Spanningsverlies 3‑fase + 2%‑norm
**Format:** Open vraag / Berekening

**Vraag:**
Een zuiver ohmse symmetrische belasting (R₁=R₂=R₃) is in ster op 230/400 V aangesloten. De fasestroom is 30 A.
Kabel: 5‑aderig, 35 mm², lengte 250 m, koper ρ = 0,0178·10⁻⁶ Ω·m. Toets of voldaan wordt aan de norm: maximaal 2% spanningsverlies over de fasespanning .

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): 3‑fase ohms: ΔU_phase ≈ I_phase · (ρ·L/A). Check ≤ 2% van U_phase (≈230 V).

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 14
**Onderwerp:** 3‑fasen generator → lijnspanningen
**Format:** Open vraag / Berekening

**Vraag:**
Gegeven onderstaande schakeling met |U₁0| = |U₂0| = |U₃0| = 400 V. Bereken |U₁₂|, |U₂₃| en |U₃₁|.

**Hints/Uitwerking:**
Holmes‑stijl hint (formuleblad): U₁₂ = U₁0 − U₂0 (vectorverschil); idem U₂₃, U₃₁. |U_lijn| = √3·|U_fase|, hoek +30° bij symmetrie.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 15
**Onderwerp:** Transformator‑kern: voor‑ en nadelen
**Format:** Open vraag / Berekening

**Vraag:**
Noem twee voordelen en drie nadelen van het toepassen van een magnetische kern in een transformator.

**Hints/Uitwerking:**
Holmes‑stijl hint: Pros: hogere koppeling, compacter, lager lekveld. Cons: hysterese/wiervelden, verzadiging, massa/kosten.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---

## Examenvraag 16
**Onderwerp:** Juist / Onjuist
**Format:** Open vraag / Berekening

**Vraag:**
**Hints/Uitwerking:**
Holmes‑stijl hint: k∈[0,1]; 1 C = 1 A·s; Q ↑ als cosφ ↓. Ster/Δ‑vermogen: let op definitie bij gelijke lijnspanning.

**Let op:**
- [Te analyseren: formules, valkuilen, aandachtspunten]

---
