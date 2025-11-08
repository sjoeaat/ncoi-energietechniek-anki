# Content Enhancement Guidelines

**Doel:** Verbeter de uitleg-kwaliteit BINNEN de Paul Holmes methodologie

---

## Strikte Richtlijnen

### ✅ WAT WEL

1. **Gebruik officiële formules uit formuleblad:**
   - `U = I · R` (Wet van Ohm)
   - `∑ Ij = 0` (Kirchhoff knoop)
   - `∑ Uj = 0` (Kirchhoff maas)

2. **Holmes notatie conventies:**
   - Middelpunt voor vermenigvuldiging: `·` (niet `×` of `*`)
   - Subscripts: `U1`, `R2`, `I3`
   - Griekse letters: `φ` (fasehoek), `ω` (hoekfrequentie)

3. **Hoofdstukverwijzingen:**
   - "Volgens Hoofdstuk X §Y.Z van Holmes..."
   - "Zie formuleblad sectie [naam]"

4. **Pedagogische verbeteringen:**
   - Duidelijkere stappen
   - Betere uitleg WHY (maar niet anders dan Holmes!)
   - Fysische interpretatie
   - Eenhedencontrole
   - Tabel voor gegeven waarden

5. **Formule-opmaak verbeteren:**
   - Van: `U = I•R => R = U/I` (lelijk)
   - Naar: `U = I · R ⇒ R = U/I` (proper pijl, middelpunt)
   - Display math voor belangrijke vergelijkingen

### ❌ WAT NIET

1. **Geen afwijkende formules:**
   - Gebruik ALLEEN formules uit het formuleblad
   - Geen "slimme" alternatieve afleidingen die Holmes niet gebruikt

2. **Geen andere methodologie:**
   - Blijf bij Holmes benadering
   - Geen "moderne" notaties als die niet in het boek staan

3. **Geen weglatingen:**
   - Alle stappen die Holmes belangrijk vindt, behouden
   - Spanningsrichtingen consistent

4. **Geen overbodige complexiteit:**
   - Holmes houdt het practisch - geen theoretische diepgang die niet nodig is

---

## Verbeteringstemplate

```markdown
**Opgave [N]:** [Vraagstelling uit origineel]

**Uitwerking:**

**Stap 1: Gegeven waarden**

| Grootheid | Symbool | Waarde | Eenheid |
|-----------|---------|--------|---------|
| ...       | ...     | ...    | ...     |

**Stap 2: Relevante wet/formule**

[Welke wet? Waarom?]

Volgens [Holmes Hoofdstuk X §Y.Z / Formuleblad sectie Z]:

$$[Formule uit formuleblad]$$

**Stap 3: Toepassen op dit probleem**

[Redenering - waarom past deze formule hier?]

**Stap 4: Algebraïsche bewerking**

[Herleid naar gevraagde grootheid - stap voor stap]

$$[Formule herleid]$$

**Stap 5: Numerieke substitutie**

[Vul waarden in met eenheden]

$$[Berekening met waarden]$$

**Stap 6: Controle & interpretatie**

- **Eenhedencontrole:** [Check dimensies]
- **Realiteitscheck:** [Is het antwoord realistisch?]
- **Fysische betekenis:** [Wat betekent dit resultaat praktisch?]

**Antwoord:** [Finale antwoord met eenheid]
```

---

## Formule-opmaak Verbeteringen

### Origineel (slecht):
```
U = I•R => R = U/I
R = 4,5/0,3 = 15 Ω
```

### Verbeterd (goed):
```latex
Wet van Ohm (Holmes §1.8, Formuleblad 1.1):

$$U = I \cdot R$$

Herleid naar R:

$$U = I \cdot R \quad \Rightarrow \quad R = \frac{U}{I}$$

Substitueer waarden:

$$R = \frac{4{,}5 \text{ V}}{0{,}3 \text{ A}} = 15 \text{ Ω}$$
```

**Verschillen:**
- `•` → `\cdot` (proper middelpunt)
- `=>` → `\Rightarrow` (wiskundige implicatie pijl)
- `/` → `\frac{}{}` (proper breuk)
- Eenheden expliciet in formule
- Verwijzing naar Holmes hoofdstuk

---

## Voorbeelden per Type Opgave

### Type 1: Basis Ohm (Opgave 1, 2)

**Structuur:**
1. Gegeven (tabel)
2. Wet van Ohm toepassen
3. Herleiden
4. Berekenen
5. Interpretatie (vermogen, realiteit)

### Type 2: Kirchhoff Knoop/Maas (Opgave 3, 4)

**Structuur:**
1. Schets analyseren
2. Kirchhoff wet toepassen (som =0)
3. Relaties tussen grootheden
4. Stelsel oplossen
5. Verificatie (som check)

### Type 3: Thévenin/Norton (Opgave X)

**Structuur:**
1. Open-klemspanning Uo bepalen
2. Kortsluitstroom Ik bepalen
3. Rth = Uo/Ik (formuleblad 9.1)
4. Equivalent tekenen
5. Verificatie met origineel circuit

---

## Kwaliteitscheck

Elk verbeterde opgave moet:

- [ ] Formules uit formuleblad gebruiken
- [ ] Holmes notatie volgen (· voor ×, subscripts, etc.)
- [ ] Hoofdstuk/formuleblad referenties hebben
- [ ] Stap-voor-stap zijn (niet sprongen maken)
- [ ] Eenhedencontrole bevatten
- [ ] Fysische interpretatie geven
- [ ] Display math gebruiken voor key equations
- [ ] Proper LaTeX opmaak hebben
- [ ] GEEN afwijkende methodologie introduceren

---

## Resources

1. **Formuleblad:** `analysis/formuleblad-extract.md`
2. **Holmes boek:** Elektrische Netwerken 3e editie
3. **Originele opgaven:** `study-guide/uitwerkingen-pandoc-raw.html`

---

**BELANGRIJK:** Bij twijfel - blijf bij de originele Holmes uitleg, maar maak die DUIDELIJKER en BETER GESTRUCTUREERD. Geen nieuwe trucjes introduceren!
