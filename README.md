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
- [ ] 80+ kaarten gegenereerd
- [ ] CSV export klaar voor Anki import

**Status:** ✅ Analysefase compleet - Gereed voor kaarten generatie

---

**Gegenereerd:** 2025-11-06
**Versie:** 1.0
