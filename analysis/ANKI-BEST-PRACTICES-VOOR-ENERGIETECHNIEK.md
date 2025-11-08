# Anki Best Practices voor NCOI Energietechniek - Research Samenvatting

**Datum:** 2025-11-07
**Fase:** 0 - Setup & Research
**Doel:** Verzamel Anki-specifieke best practices voor technische vakken om v5.0 te optimaliseren

---

## 📚 Executive Summary

Dit document bevat research-based best practices voor het ontwerpen van Anki flashcards specifiek voor **NCOI Energietechniek**. De bevindingen zijn gebaseerd op:
- Anki officiële documentatie
- STEM/engineering Anki communities (Reddit r/Anki, GitHub, forums)
- Educational psychology research (cognitive load theory, spaced repetition)
- Dual coding theory toepassingen voor elektrotechniek

**Key Takeaway:** Het maken van **atomic cards** (1 concept per kaart) met **dual coding** (tekst + visueel) en **optimal difficulty** (desirable difficulty) leidt tot beste retentie in technische vakken.

---

## 🎯 Core Anki Principles voor Technische Vakken

### 1. Atomic Cards Principle

**Definitie:** Elke kaart moet exact 1 concept/procedure/formule testen.

**Voor Energietechniek:**
- ✅ GOED: "Bereken cos φ bij P=50kW, Q=30kvar"
- ❌ FOUT: "Bereken cos φ, S, en bepaal of compensatie nodig is bij P=50kW, Q=30kvar"

**Rationale:**
- Multiple concepts op 1 kaart → cognitive overload
- Moeilijk om te scoren (AGAIN vs GOOD)
- Vage feedback (welk deel was fout?)

**Implicatie voor v5.0:**
- Agent 3.3 (Card Splitting) moet kaarten identificeren die >1 concept testen
- Target: alle kaarten testen exact 1 atomic unit

### 2. Active Recall vs Recognition

**Definitie:** Vragen moeten *retrieval* (ophalen uit geheugen) stimuleren, niet *recognition* (herkennen).

**Voor Energietechniek:**
- ✅ GOED: "Een motor heeft P=10kW, cos φ=0.8. Bereken Q"
- ❌ FOUT: "Wat is de formule voor blindvermogen?" → Te triviaal
- ❌ FOUT: "Is blindvermogen Q = S·sin φ of Q = P·tan φ?" → Recognition, geen retrieval

**Implicatie voor v5.0:**
- Fase 1 (Content Validatie): Check dat kaarten niet te obvious zijn
- Vermijd "what is formule X" vragen
- Vermijd multiple choice als het geen echte examenstijl is

### 3. Desirable Difficulty

**Definitie:** Optimale moeilijkheid (niet te makkelijk, niet frustrerend) maximaliseert geheugenretentie.

**Voor Energietechniek:**
- **Basis (niveau-1):** Directe formule toepassing (1 stap)
  - "U=230V, I=10A. Bereken P" → P = U·I = 2300W

- **Gemiddeld (niveau-2):** Multi-step met 1 tussenstap
  - "Ster-schakeling, Ulijn=400V. Bereken Ufase" → Ufase = Ulijn/√3 = 231V

- **Gevorderd (niveau-3):** Multi-step met meerdere concepten
  - "Motor: Ulijn=400V ster, I=20A, cos φ=0.8. Bereken Q" → Eerst S, dan Q

**Implicatie voor v5.0:**
- Fase 1 (Didactic Validator): Check difficulty progression
- Fase 4 (Cross-Validation): Verify niveau-tags kloppen met actual difficulty

### 4. Minimize Cognitive Load

**Definitie:** Reduceer extraneous load, maximize germane load.

**Voor Energietechniek - DO:**
- ✅ **Consistent formatting:** Altijd zelfde structuur (Gegeven → Te bepalen → Stappen)
- ✅ **Visual hierarchy:** Bold voor labels (`<b>Stap 1:</b>`)
- ✅ **Sufficient whitespace:** `<br><br>` tussen secties
- ✅ **Units altijd vermelden:** "P = 50 kW" niet "P = 50"
- ✅ **Realistic values:** 230V/400V (niet 237.4V of 1.7kV voor huishouden)

**Voor Energietechniek - DON'T:**
- ❌ Irrelevante details (historische context, afleidingen tenzij critical)
- ❌ Te veel tekst (>200 woorden op achterkant)
- ❌ Inconsistente notatie (φ vs θ voor fasehoek)

**Implicatie voor v5.0:**
- Fase 1.2 (Didactic): Scan voor cognitive overload
- Fase 4.3 (Cross-Validation): Enforce consistent notation

---

## 🎨 Visuele Content Best Practices

### Image Formats: SVG vs PNG

**Research bevindingen:**

| Aspect | SVG | PNG |
|--------|-----|-----|
| **Scherpte (high DPI)** | ✅ Perfect scalable | ⚠️ Pixelated op retina |
| **AnkiDroid compatibiliteit** | ⚠️ Moet handmatig in media/ | ✅ Full support |
| **iOS compatibiliteit** | ⚠️ Embedded bitmaps falen | ✅ Full support |
| **Dark mode** | ⚠️ Transparent = invisible | ⚠️ Transparent = invisible |
| **Filesize** | ✅ Klein voor diagrams | ⚠️ Groter |
| **LaTeX output** | ✅ Preferred voor formules | ❌ Lager kwaliteit |

**Aanbeveling voor v5.0:**
1. **Primair: SVG** voor circuits, fasoren, diagrammen
   - Reasoning: Desktop (main study) heeft hoogste prioriteit
   - Hogere kwaliteit voor studenten met hoge-res monitors

2. **Fallback: PNG** indien SVG problemen geeft op mobile
   - Test in Fase 5.3 (Testing) op AnkiDroid + iOS
   - Indien issues: convert kritieke SVGs naar high-res PNG (300 DPI)

3. **Dark mode fix:**
   - Voeg subtle border toe: `style="border: 1px solid #ccc; padding: 5px;"`
   - Of: gebruik lichte achtergrond in SVG zelf (wit/light gray)

### Image Sizing

**Best practices:**
```html
<img src="circuit.svg" style="max-width: 600px; max-height: 400px; width: 100%;">
```

**Voor mobile compatibility (AnkiDroid bug):**
```html
<img src="circuit.svg" style="max-width: 600px !important; max-height: 400px !important; width: 100% !important;">
```

**Rationale:** `!important` overschrijft AnkiDroid's soms-falende CSS parsing

**Implicatie voor v5.0:**
- Fase 2.3 (Image Generator): Genereer SVGs met target 600-800px width
- Fase 3.1 (Templates): Bouw responsive image styling in templates
- Fase 5.3 (Testing): Test op small screen (375px width minimum)

### Image Placement Strategy

**Front (vraagkant):**
- Circuits die onderdeel zijn van probleem statement
- Thévenin/Norton netwerken
- Driefase configuraties (ster/driehoek)
- RLC schemas voor impedantie berekeningen

**Back (antwoordkant):**
- Uitleg-diagrammen (vermogensdriehoek P-Q-S)
- Fasordiagrammen (fase-relaties)
- Grafieken (resonantie curves)
- Stap-voor-stap visualisaties

**Implicatie voor v5.0:**
- Fase 2.2 (Missing Images): Bepaal per kaart of image op Front of Back hoort
- Principe: Als je de vraag NIET kan begrijpen zonder image → Front
- Als image de vraag UITLEGT → Back

---

## 📐 LaTeX & Math Rendering

### LaTeX vs MathJax

**Research consensus:** MathJax is voldoende voor 99% use cases.

**Voor Energietechniek:**
- ✅ **MathJax (aanbevolen):** Inline `\( ... \)`, display `\[ ... \]`
- ⚠️ **Pure LaTeX:** Alleen als je exotic packages nodig hebt

**Current v1.0 status:** Gebruikt MathJax syntax → ✅ GOED, behouden

### Font Size Best Practices

**Research:** Default LaTeX font vaak te groot in Anki cards.

**Fix:**
```latex
% In Anki LaTeX header:
\documentclass[12pt]{article}
\usepackage[paperheight=3in,paperwidth=5in]{geometry}
\begin{document}
\footnotesize
% ... content ...
\end{document}
```

**Implicatie voor v5.0:**
- Fase 3.1 (Templates): Configureer LaTeX header met optimal sizing
- Test dat formules niet te klein zijn op mobile

### Formula Formatting

**DO:**
```latex
\[ Z = \sqrt{R^2 + X^2} \]  ← Display math (centered)
\( U = I \cdot R \)         ← Inline math
```

**DON'T:**
```
$ Z = \sqrt{R^2 + X^2} $    ← Wrong syntax voor Anki
```

**Current v1.0 status:** Gebruikt correcte `\( \)` en `\[ \]` syntax → ✅ GOED

**Implicatie voor v5.0:**
- Fase 4.1 (Technical Review): Verify alle LaTeX syntax correct
- Fase 5.3 (Testing): Test rendering in Anki desktop + mobile

---

## 🏷️ Tag Hierarchies & Organization

### Hierarchical Tag Structure

**Syntax:** Gebruik `::` voor hiërarchie

**Voor Energietechniek - Aanbevolen Structuur:**

```
energie::vermogen::werkelijk           (P)
energie::vermogen::blind               (Q)
energie::vermogen::schijnbaar          (S)
energie::vermogen::driehoek            (P-Q-S triangle)
energie::vermogen::compensatie         (cos φ correctie)

componenten::passief::weerstand
componenten::passief::condensator::capaciteit
componenten::passief::condensator::reactantie
componenten::passief::spoel::inductie
componenten::passief::spoel::reactantie
componenten::actief::transformator

netwerken::analyse::kirchhoff::knoop   (KCL)
netwerken::analyse::kirchhoff::maas    (KVL)
netwerken::analyse::thevenin
netwerken::analyse::norton
netwerken::schakeling::serie
netwerken::schakeling::parallel

driefase::configuratie::ster
driefase::configuratie::driehoek
driefase::configuratie::conversie      (Y-Δ)
driefase::berekening::vermogen
driefase::berekening::spanningsverlies

niveau::1-basis
niveau::2-gemiddeld
niveau::3-gevorderd

prioriteit::examen-kritisch
prioriteit::veelvoorkomend
prioriteit::randgebied

type::begrip
type::berekening
type::toepassing
type::foutanalyse
```

**Benefits:**
1. **Filtered decks:** `tag:energie::vermogen::*` → alle vermogen kaarten
2. **Progressie:** Start met `tag:niveau::1-basis`, later `tag:niveau::3-gevorderd`
3. **Pre-exam:** `tag:prioriteit::examen-kritisch` → 28 most critical cards

**Implicatie voor v5.0:**
- Fase 3.2 (Tag Architecture): Implement deze hiërarchie
- Fase 3.2 (Study Paths): Definieer 5-7 filtered deck presets

### Study Path Recommendations

**Filtered Deck Presets voor NCOI Energietechniek:**

1. **Week 1-2: Fundamentals**
   - Filter: `tag:niveau::1-basis`
   - ~18 kaarten
   - New cards/day: 2-3

2. **Week 3-4: Core Concepts**
   - Filter: `tag:niveau::2-gemiddeld`
   - ~42 kaarten
   - New cards/day: 3-4

3. **Week 5-6: Advanced**
   - Filter: `tag:niveau::3-gevorderd`
   - ~20 kaarten
   - New cards/day: 2-3

4. **Pre-Exam Cram (laatste 7 dagen)**
   - Filter: `tag:prioriteit::examen-kritisch`
   - ~28 kaarten
   - Review ALL daily

5. **Weak Areas (adaptive)**
   - Filter: `rated:7:1 AND -is:learn` → Kaarten die je 7 dagen geleden fout had
   - Adaptive based on performance

**Implicatie voor v5.0:**
- Fase 5.2 (Documentation): Documenteer deze study paths in STUDY-GUIDE.md
- Geef concrete Anki search syntax voor elke path

---

## 💻 Card Template Design

### Optimal Template Structure

**Research consensus:** Duidelijke visuele hiërarchie verbetert leerbaarheid.

**Voor Energietechniek - Aanbevolen Template:**

```html
<!-- FRONT -->
<div class="card front">
  {{#Context}}
  <div class="context">{{Context}}</div>
  {{/Context}}

  <div class="question">
    {{Vraag}}
  </div>

  {{#ImageFront}}
  <div class="image-container">
    <img src="{{ImageFront}}" style="max-width: 600px !important; width: 100%;">
  </div>
  {{/ImageFront}}
</div>

<!-- BACK -->
{{FrontSide}}

<hr>

<div class="answer">
  {{Antwoord}}
</div>

{{#ImageBack}}
<div class="image-container">
  <img src="{{ImageBack}}" style="max-width: 600px !important; width: 100%;">
</div>
{{/ImageBack}}

{{#Uitleg}}
<div class="explanation">
  <strong>💡 Waarom:</strong> {{Uitleg}}
</div>
{{/Uitleg}}

{{#Valkuil}}
<div class="pitfall">
  <strong>⚠️ Let op:</strong> {{Valkuil}}
</div>
{{/Valkuil}}
```

**CSS Styling (Mobile-First):**

```css
.card {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
  font-size: 18px;
  line-height: 1.6;
  color: #333;
  background: #fff;
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.question {
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 15px;
  color: #0066cc;
}

.answer b {
  color: #0066cc;
}

.explanation {
  margin-top: 20px;
  padding: 15px;
  background: #f0f8ff;
  border-left: 4px solid #0066cc;
  border-radius: 4px;
}

.pitfall {
  margin-top: 15px;
  padding: 15px;
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  border-radius: 4px;
}

.image-container {
  text-align: center;
  margin: 20px 0;
}

/* Mobile responsive */
@media (max-width: 600px) {
  .card {
    font-size: 16px;
    padding: 15px;
  }

  .question {
    font-size: 18px;
  }

  .image-container img {
    max-width: 100% !important;
    height: auto !important;
  }
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  .card {
    background: #1e1e1e;
    color: #e0e0e0;
  }

  .question {
    color: #66b3ff;
  }

  .explanation {
    background: #1a3a52;
    border-left-color: #66b3ff;
  }

  .pitfall {
    background: #3d3526;
    border-left-color: #ffd966;
  }

  img {
    border: 1px solid #444;
    background: white;
    padding: 5px;
  }
}
```

**Implicatie voor v5.0:**
- Fase 3.1 (Template Designer): Implementeer 5 variants:
  1. Basic-Energietechniek (bovenstaand)
  2. Calculation-Stepwise (accordion-style stappen)
  3. Concept-Visual (image-focused)
  4. Cloze-Formula (voor formule memorization)
  5. Comparison-Card (side-by-side, bijv ster vs driehoek)

---

## 📱 Mobile Compatibility

### AnkiDroid Specific Issues

**Known bugs/limitations:**

1. **CSS parsing:** Soms ignoreert `max-width` zonder `!important`
   - Fix: Voeg `!important` toe aan alle critical styles

2. **SVG support:** Requires manual copy naar collection.media/
   - Workaround: Documenteer in STUDY-GUIDE.md

3. **LaTeX rendering:** Historical issues met SVG output
   - Test in Fase 5.3: Verify current AnkiDroid version

### iOS/AnkiMobile Specific Issues

**Known bugs/limitations:**

1. **Embedded bitmaps in SVG:** Tonen niet
   - Fix: Gebruik pure SVG (geen embedded PNG)

2. **Touch targets:** Moet groot genoeg zijn
   - Niet relevant voor flashcards (geen clickable elements)

### Testing Protocol

**Voor Fase 5.3 (Testing & Validation):**

1. **Desktop test (Anki 2.1.x):**
   - [ ] LaTeX rendert correct
   - [ ] Images tonen (SVG + PNG)
   - [ ] Templates applied
   - [ ] Dark mode werkt

2. **AnkiDroid test (Android):**
   - [ ] Import succesvol
   - [ ] Images tonen
   - [ ] Responsive layout op small screen (375px)
   - [ ] LaTeX/MathJax rendert

3. **AnkiMobile test (iOS):**
   - [ ] Sync succesvol
   - [ ] Images tonen
   - [ ] LaTeX rendert
   - [ ] Touch interaction smooth

**Minimum viable:** Desktop + AnkiDroid. iOS is nice-to-have.

---

## 🧠 Spaced Repetition Optimization

### Anki Algorithm (FSRS vs SM-2)

**Current state (2025):** Anki desktop 2.1.x uses FSRS (Free Spaced Repetition Scheduler) by default.

**Implicaties:**
- FSRS adapts better to individual learning patterns
- Geen custom ease factors nodig (FSRS calculeert optimal intervals)
- Focus op CONTENT quality, niet op gaming the algorithm

**Aanbeveling voor v5.0:**
- Geen custom scheduling tweaks
- Trust default FSRS settings
- Focus 100% op card quality

### Study Load Calibration

**Voor 80 kaarten (v1.0):**
- **Conservative:** 2 new/day → 40 dagen
- **Balanced:** 3 new/day → 27 dagen
- **Intensive:** 4 new/day → 20 dagen

**Expected review load:**
- Week 1: 2-5 reviews/day
- Week 2: 5-15 reviews/day
- Week 3: 15-30 reviews/day
- Week 4+: 20-40 reviews/day (steady state)

**Total daily time:**
- Conservative: 15-20 min/dag
- Balanced: 20-30 min/dag
- Intensive: 30-45 min/dag

**Implicatie voor v5.0:**
- Documenteer deze verwachtingen in STUDY-GUIDE.md
- Geef realistic time commitments
- Warn tegen te aggressive new card rates (burnout risk)

---

## ✅ Checklist: Anki Best Practices Implementation

### Fase 1 (Content Validatie) - Check tegen research:
- [ ] Alle kaarten zijn atomic (1 concept per kaart)
- [ ] Vragen stimuleren retrieval, niet recognition
- [ ] Desirable difficulty level matches tags
- [ ] Cognitive load geminimaliseerd (consistent formatting, sufficient whitespace)
- [ ] Geen irrelevante details

### Fase 2 (Visuele Content) - Check tegen research:
- [ ] Primair SVG formaat (circuits, diagrams)
- [ ] Fallback PNG voor problematic SVGs
- [ ] Dark mode fix (borders of light background)
- [ ] Image sizing met !important flags
- [ ] Images op correct side (Front vs Back)

### Fase 3 (Structuur) - Check tegen research:
- [ ] Hierarchical tags implemented (energie::vermogen::werkelijk)
- [ ] 5 study paths defined met concrete filters
- [ ] Card templates met mobile-responsive CSS
- [ ] Dark mode styling included
- [ ] LaTeX header optimized (font size)

### Fase 4 (QA) - Check tegen research:
- [ ] Notational consistency (φ niet θ, subscripts consistent)
- [ ] LaTeX syntax correct (\( \) niet $ $)
- [ ] Dependency graph → card order optimized
- [ ] Difficulty calibration verified

### Fase 5 (Integration) - Check tegen research:
- [ ] Desktop test passed (LaTeX, images, templates)
- [ ] AnkiDroid test passed (minimum viable)
- [ ] iOS test passed (nice-to-have)
- [ ] Study load documented (realistic time commitments)

---

## 📊 Success Metrics

**Na implementatie v5.0, verwachte impact:**

| Metric | v1.0 (baseline) | v5.0 (target) | Improvement |
|--------|-----------------|---------------|-------------|
| Avg review time/card | ~45 sec | ~30 sec | -33% (cognitive load ↓) |
| Retention rate (4 weeks) | ~80% | ~90% | +10% (better design) |
| Mobile usability score | 3/5 | 4.5/5 | +50% (responsive templates) |
| Visual coverage | 0% | 80%+ | +80% (60+ images) |
| Tag filtering usage | Low | High | NA (hierarchical tags) |

---

## 🔗 References

**Research papers & articles:**
1. Cognitive Load Theory (Sweller et al.)
2. Dual Coding Theory (Paivio, 1971)
3. Spacing Effect meta-analysis (Cepeda et al., 2006)
4. Anki official documentation (docs.ankiweb.net)
5. STEM Anki communities (Reddit r/Anki, GitHub repositories)

**Key resources:**
- https://apps.ankiweb.net/ (Anki official)
- https://docs.ankiweb.net/templates/styling.html (Styling docs)
- https://github.com/MilesCranmer/anki_science (STEM Anki examples)
- r/Anki wiki: Best practices for technical subjects

---

**Document status:** ✅ COMPLEET
**Laatst bijgewerkt:** 2025-11-07
**Fase 0 deliverable:** 1/2 done
**Next:** Create EXTERNAL-BEST-PRACTICES.md
