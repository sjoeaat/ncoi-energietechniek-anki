# NCOI Energietechniek - Anki Deck Generator

**Doel:** Genereer 80+ hoogwaardige Anki-kaarten voor NCOI examen Energietechniek

**Referentie:** Elektrische netwerken (3e editie, Paul Holmes)

## Bronmateriaal

- **Formuleblad** Energietechniek v3 2023
- **Oefenvragen** Energietechniek (met antwoorden)
- **Oefentoets** 16 vragen examenstijl v6
- **Samenvatting** kernconcepten en formules

## Project Structuur

```
ncoi-energietechniek-anki/
├── source-materials/       # PDF's en bronbestanden
├── analysis/              # Agent outputs: extracties en analyses
├── generated-cards/       # Output CSV bestanden
├── images/
│   ├── schemas/          # Netwerkschema's (Thévenin, Norton, RLC)
│   └── fasors/           # Fasediagrammen, complexe impedantie
├── scripts/              # Generatie scripts (optioneel)
├── CARD-TAXONOMY.md      # Overzicht onderwerpen & kaartendekking
└── README.md
```

## Onderwerpen (volgens NCOI exameneisen)

1. Basiswetten (Ohm, Kirchhoff)
2. RLC-netwerken (serie/parallel)
3. Complex rekenen & fasoren
4. Thevenin & Norton
5. Transformatoren (ster/delta, vermogensverhouding)
6. Vermogensleer (P, Q, S, cosφ, compensatie)
7. Inductie & koppelfactor
8. Driefasenstelsels
9. Resonantie & filters
10. Energie, rendement, spanningsverlies

## Kaartsoorten

- **Begripsvragen** (definities, wetten, principes)
- **Rekenvoorbeelden** (volledige uitwerking met stappen)
- **Fasediagram/vectorvragen** (inclusief schema's)
- **Vergelijkingsvragen** ("wat verandert bij ster-delta-omzetting?")
- **Foutanalyse** ("wat is fout in deze berekening?")

## Output Formaat

CSV met kolommen: `Front,Back,Tag`
- UTF-8 encoding
- LaTeX formules: `\( ... \)` voor inline, `\[ ... \]` voor display
- Afbeeldingen: `<img src="images/schemas/thevenin_01.svg">`

## Kwaliteitscriteria

- Denkactiviteit uitlokken (geen triviale definities)
- Correcte formules + afgeronde antwoorden
- Nederlandse terminologie (spanningsval, fasehoek, schijnbaar vermogen)
- Korte toelichtingen waarom een stap logisch is
- Tags per hoofdstuk en onderwerp

## Generatie Status

- [x] Formuleblad geanalyseerd (47 formules)
- [x] Oefenvragen verwerkt (16 vragen)
- [x] HTML oefentoets geanalyseerd (16 examenvragen)
- [x] Schema's gespecificeerd (25+ visuele elementen)
- [x] Verificatie tegen lesmateriaal (240-290 kaarten mogelijk)
- [x] 80+ kaarten gegenereerd (v1.0 COMPLETE)
- [x] CSV export klaar voor Anki import

**Status v1.0:** ✅ Complete - 80 kaarten, KENNIS/REKENEN split, ready to use

---

## 🚀 NEXT PHASE: Quality Validation (v5.0)

**Doel:** Van goed naar EXCELLENT - Multi-stage AI validatie voor absolute topkwaliteit

**Zie:**
- 📄 **[WERKINSTRUCTIE-CLAUDE-WEB-KWALITEITSVALIDATIE.md](WERKINSTRUCTIE-CLAUDE-WEB-KWALITEITSVALIDATIE.md)** - Complete validatie plan
- 📄 **[QUICK-START-VALIDATION.md](QUICK-START-VALIDATION.md)** - Snelstart instructies
- 📄 **[CLAUDE.md](CLAUDE.md)** - Project context voor AI agents

**Scope:**
- ✅ 100% inhoudelijke correctheid validatie
- ✅ 60+ professionele afbeeldingen (circuits, diagrammen, grafieken)
- ✅ Multi-stage QA (15+ gespecialiseerde AI agents)
- ✅ Custom Anki card templates
- ✅ Hiërarchische tag structuur v2.0
- ✅ Complete documentatie & study guide

**Budget:** €500 (kwaliteit boven kosten)
**Timeline:** 6-8 weken
**Output:** v5.0 met 4.5+ quality score

---

## 📚 Belangrijke Documenten

### Voor Gebruikers
- `generated-cards/DECK-METADATA.md` - Import instructies en studieaanbevelingen
- `KOPPELING-IMAGES-AAN-KAARTEN.md` - Handleiding afbeeldingen toevoegen

### Voor AI Development
- `CLAUDE.md` - Project context en architectuur
- `WERKINSTRUCTIE-CLAUDE-WEB-KWALITEITSVALIDATIE.md` - Master validatie plan
- `QUICK-START-VALIDATION.md` - Snelstart voor validatie fase

### Analyse Documenten
- `analysis/FINAL-COVERAGE-REPORT.md` - Exam coverage verificatie
- `analysis/oefentoets-examenstijl-summary.md` - Exam style analysis

---

**Laatste update:** 2025-11-07
**Huidige versie:** v1.0 (production ready)
**Volgende versie:** v5.0 (quality validated - in planning)
