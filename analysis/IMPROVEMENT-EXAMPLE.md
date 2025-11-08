# Content Improvement - Voorbeeld Opgave 1

**Doel:** Verbeteren van uitlegtekst + proper formule-opmaak

---

## ORIGINEEL (uit Word doc)

**Opgave 1:**
In een zaklantaarn zit een 4,5V-batterij. Door het lampje loopt een stroom van 0,3 A.
Hoe groot is de weerstand van het lampje?
Teken het netwerkschema.

**Uitwerking opgave 1:**
Wet van ohm:
```
U = I•R  => R = U/I
R = 4,5/0,3 = 15 Ω
```

### Problemen met origineel:
❌ Te kort - geen stappen
❌ "= >" is lelijke notatie
❌ "•" voor vermenigvuldiging
❌ Geen uitleg WHY
❌ Geen fysische interpretatie

---

## VERBETERD (nieuwe versie)

**Opgave 1:**
In een zaklantaarn zit een 4,5V-batterij. Door het lampje loopt een stroom van 0,3 A.
Hoe groot is de weerstand van het lampje?
Teken het netwerkschema.

**Uitwerking opgave 1:**

**Stap 1: Analyseer de gegeven informatie**

| Grootheid | Symbool | Waarde | Eenheid |
|-----------|---------|--------|---------|
| Spanning  | U       | 4,5    | V       |
| Stroom    | I       | 0,3    | A       |
| Weerstand | R       | ?      | Ω       |

**Stap 2: Kies de juiste natuurkundige wet**

We gebruiken de **wet van Ohm**, die het lineaire verband beschrijft tussen spanning over een weerstand en de stroom erdoor:

$$U = I \cdot R$$

Deze wet geldt voor ohmse weerstanden (lineair gedrag) en vormt de basis van veel elektrische analyses.

**Stap 3: Herleid de formule naar de gevraagde grootheid**

Omdat we R willen berekenen, isoleren we R door beide zijden van de vergelijking te delen door I:

$$U = I \cdot R$$

$$\Rightarrow \frac{U}{I} = \frac{I \cdot R}{I}$$

$$\Rightarrow R = \frac{U}{I}$$

**Stap 4: Substitueer de numerieke waarden**

$$R = \frac{U}{I} = \frac{4{,}5 \text{ V}}{0{,}3 \text{ A}} = 15 \text{ Ω}$$

**Stap 5: Controleer dimensionaliteit**

De eenhedencontrole:
$$\frac{[\text{V}]}{[\text{A}]} = [\text{Ω}]$$ ✓

Dit klopt, want per definitie geldt: $1 \text{ Ω} = 1 \frac{\text{V}}{\text{A}}$

**Antwoord:** De weerstand van het lampje is **R = 15 Ω**

**Fysische interpretatie:**

Een gloeilampje met een weerstand van 15 Ω is typisch voor een zaklantaarnlampje.

- **Vermogen:** Het lampje dissipeert: $P = U \cdot I = 4{,}5 \text{ V} \times 0{,}3 \text{ A} = 1{,}35 \text{ W}$
- **Energieverbruik:** Dit is een redelijk laag vermogen, geschikt voor batterijvoeding
- **Gedrag bij andere spanningen:** Als de spanning zou toenemen tot 6V (bijv. 4×AA batterijen), zou de stroom toenemen tot 0,4 A en het vermogen tot 2,4 W - het lampje zou helderder branden maar ook sneller leeg raken

**Netwerk schema:**

[Circuit diagram - image4.PNG]

Het schema toont:
- Spanningsbron U = 4,5V
- Weerstand R = 15Ω (het lampje)
- Stroom I = 0,3A (stroomrichting aangegeven)

---

## Vergelijking

| Aspect | Origineel | Verbeterd |
|--------|-----------|-----------|
| **Lengte** | 2 regels | ~20 regels |
| **Structuur** | Geen stappen | 5 duidelijke stappen |
| **Formules** | "= >" slordig | Proper $\Rightarrow$ |
| **Uitleg** | Alleen formule | WHY + HOW + WHAT |
| **Controle** | Geen | Eenhedencheck |
| **Context** | Geen | Vermogen, fysische betekenis |
| **Pedagogiek** | Zwak | Sterk (tabel, stappen, interpretatie) |

---

## Formule Verbeteringen

### Origineel (slecht):
```
U = I•R  => R = U/I
```

### Verbeterd (goed):
```latex
$$U = I \cdot R$$
$$\Rightarrow R = \frac{U}{I}$$
```

**Verschillen:**
- `•` → `\cdot` (proper punt operator)
- `=>` → `\Rightarrow` (wiskundige implicatie)
- `/` → `\frac{}{}` (proper breuk notatie)
- Display math (`$$`) ipv inline voor belangrijke vergelijkingen

---

## Volgende Stappen

Als dit voorbeeld goedgekeurd wordt:

1. Maak systematisch alle ~90 opgaven op deze manier beter
2. Gebruik AI-assisted content generation voor consistentie
3. Valideer alle formules op correctheid
4. Genereer nieuwe HTML met verbeterde content

**Geschatte tijdsinvestering:**
- Per opgave: 10-15 minuten verbetering
- Totaal: ~15-20 uur werk
- Met AI assistance: ~4-6 uur

**User goedkeuring nodig:** Akkoord met deze stijl?
