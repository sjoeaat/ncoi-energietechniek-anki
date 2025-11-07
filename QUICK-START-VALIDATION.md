# QUICK START - Kwaliteitsvalidatie voor Claude Web

**TL;DR:** Upload dit hele project naar Claude Web Projects en volg de stappen hieronder.

---

## 🎯 Doel

Alle Anki kaarten naar 100% examen-ready kwaliteit brengen:
- ✅ Zero fouten in formules/berekeningen
- ✅ 100% visuele coverage (alle benodigde afbeeldingen)
- ✅ Multi-stage AI validatie (15+ agents)
- ✅ Professionele kwaliteit (4.5+ score op alle dimensies)

**Budget:** €500 (kwaliteit > kosten)

---

## 📋 Checklist

### Voor Claude Web:

#### 1. Setup (30 min)
- [ ] Maak nieuw Claude Project: "NCOI Energietechniek - Quality Validation"
- [ ] Upload ALLE bestanden uit deze repo
- [ ] Clone Anki repo: `https://github.com/ankitects/anki`
- [ ] Upload relevante Anki docs naar project

#### 2. Lees Belangrijkste Context (15 min)
- [ ] `WERKINSTRUCTIE-CLAUDE-WEB-KWALITEITSVALIDATIE.md` (HET MASTER PLAN)
- [ ] `CLAUDE.md` (project background)
- [ ] `generated-cards/DECK-METADATA.md` (huidige status)
- [ ] `analysis/FINAL-COVERAGE-REPORT.md` (wat al gedaan is)

#### 3. Start Validatie (volg het plan)

**Week 1: Content**
- [ ] Fase 0: Anki best practices research
- [ ] Fase 1: Inhoudelijke validatie (3 agents)
- [ ] Output: `validation/phase1-*.md` bestanden

**Week 2: Visueel**
- [ ] Fase 2: Afbeeldingen audit en generatie (4 agents)
- [ ] Output: `images/circuits/`, `images/diagrams/`, etc.

**Week 3: Structuur**
- [ ] Fase 3: Card templates en tags (3 agents)
- [ ] Output: `anki-templates/`, nieuwe tag hiërarchie

**Week 4: QA**
- [ ] Fase 4: Multi-stage validatie (3 agents)
- [ ] Output: `validation/phase4-*.md` bestanden

**Week 5: Integratie**
- [ ] Fase 5: Final assembly en testing (2 agents)
- [ ] Output: `generated-cards/FINAL/` bestanden

**Week 6: Delivery**
- [ ] Fase 6: Package en documentatie
- [ ] Output: Complete final package + quality certificate

#### 4. Quality Gates

Na elke fase:
- [ ] Review output kwaliteit
- [ ] Check token usage (blijf binnen budget)
- [ ] Commit progress naar repo
- [ ] Documenteer beslissingen

---

## 🚀 Snelstart Commando's

```bash
# Als je eigen tools wilt draaien:
pip install schemdraw matplotlib numpy pandas

# Bestaande scripts gebruiken:
python scripts/extract_oefentoets.py
python scripts/add_images_to_cards.py

# Nieuwe scripts die je mag maken:
python scripts/validate_csv.py
python scripts/generate_circuits.py
python scripts/enforce_notation.py
```

---

## 📊 Verwachte Output

**Bij completion heb je:**

```
FINAL/
├── 5 Anki decks (CSV bestanden)
├── 60+ professionele afbeeldingen (SVG)
├── 5 custom card templates
├── Complete documentatie (study guide, troubleshooting, etc.)
├── Validation reports (alle fases)
└── Quality certificate (4.5+ overall score)
```

---

## 💡 Belangrijkste Instructies

1. **Kwaliteit boven alles** - Liever 2x checken dan 1 fout
2. **BLIJF BIJ DE BRONNEN** - ALLE wijzigingen moeten traceerbaar zijn naar:
   - Formuleblad Energietechniek v3 2023
   - Paul Holmes - Elektrische Netwerken (3e editie)
   - NCOI Oefenvragen + Oefentoets
3. **Wees proactief** - Zie je iets dat beter kan? Fix het (binnen brongrenzen!)
4. **Documenteer alles** - Toekomstige versie van jezelf zal je dankbaar zijn
5. **Gebruik het budget** - €500 is er om te GEBRUIKEN voor kwaliteit
6. **Vraag om hulp** - Web research, tools downloaden, external expertise - mag allemaal

## ⚠️ KRITISCHE REGEL: BRONMATERIAAL

**VERBODEN:**
- ❌ Formules toevoegen die NIET op Formuleblad v3 2023 staan
- ❌ Terminologie wijzigen (NCOI/Holmes is leidend)
- ❌ Engels gebruiken (Nederlands tenzij Holmes gebruikt)
- ❌ Concepten toevoegen buiten 10 NCOI examendomeinen
- ❌ Afwijken van NCOI moeilijkheidsniveau

**WEL toegestaan:**
- ✅ Verduidelijking (tussenstappen in berekeningen)
- ✅ Visuele hulp (diagrammen) toevoegen
- ✅ Correctie van fouten (mits consistent met bronnen)
- ✅ Kaartstructuur optimaliseren (content blijft gelijk)

---

## ❓ Eerste Stappen (letterlijk wat te doen)

### Als Claude Web:

1. **Lees eerst:**
   - Dit bestand (ben je nu al mee bezig ✅)
   - `WERKINSTRUCTIE-CLAUDE-WEB-KWALITEITSVALIDATIE.md` (de volledige instructies)

2. **Dan:**
   - Start met Fase 0 (Anki research)
   - Maak document: `analysis/ANKI-BEST-PRACTICES-VOOR-ENERGIETECHNIEK.md`

3. **Daarna:**
   - Deploy Agent 1.1 (Content Validator)
   - Work through het plan methodisch

4. **Gedurende proces:**
   - Track je voortgang in `validation/PROGRESS-TRACKER.md`
   - Update deze file elke dag met status

---

## 🎯 Success =

- ✅ Zero technische fouten
- ✅ 100% visuele coverage
- ✅ 4.5+ quality score
- ✅ Binnen €500 budget
- ✅ Student kan ermee slagen voor examen

**Maak er iets moois van! 🚀**
