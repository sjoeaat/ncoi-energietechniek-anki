# Oefenvragen Energietechniek - Extractie

**Bron:** Oefenvragen Energietechniek (NCOI)
**Datum extractie:** 2025-11-06
**Totaal aantal vragen:** 16

---

## Vraag 1
- **Type:** Rekenvraag / Analysevraag
- **Onderwerp:** Condensatornetwerken, vervangingscapaciteit, foutanalyse
- **Moeilijkheid:** Gemiddeld
- **Tags:** `condensator`, `serie-parallel`, `netwerk`, `kortsluiting`, `capaciteit`

**Vraag:**
Het hieronder afgebeelde condensator netwerk wordt aangesloten op een spanningsbron.
Met welke waarde verandert de vervangingscapaciteit van dit netwerk wanneer condensator C3 doorslaat (dus een kortsluiting vormt)? Geef duidelijk aan of de vervangingscapaciteit toeneemt of afneemt.

**Schema:**
- C2 = 8 µF (parallel met C3)
- C3 = 12 µF (parallel met C2)
- C1 = 10 µF (serie met C2||C3)

**Gegeven:**
- C1 = 10 µF
- C2 = 8 µF
- C3 = 12 µF

**Gevraagd:**
Met welke waarde verandert de vervangingscapaciteit wanneer C3 doorslaat?

**Antwoord:**

**Stap 1: Berekening voor normale situatie**

Cv23 = (C2 × C3)/(C2 + C3) = (8 × 12)/(8 + 12) = 96/20 = 4,8 µF

Cv voor doorslag = Cv23 + C1 = 4,8 µF + 10 µF = **14,8 µF**

**Stap 2: Berekening na doorslag C3**

Indien C3 doorslaat (kortsluiting), geldt dat de vervangingscapaciteit bestaat uit de parallelschakeling van C1 en C2:

Cv na doorslag = C2 + C1 = 8 µF + 10 µF = **18 µF**

**Conclusie:**
De vervangingscapaciteit **neemt toe** met 18 µF - 14,8 µF = **3,2 µF**

---

## Vraag 2
- **Type:** Rekenvraag
- **Onderwerp:** Wet van Kirchhoff, knooppunten, stroomanalyse
- **Moeilijkheid:** Basis
- **Tags:** `kirchhoff`, `knooppunt`, `stroom`, `ampèremeter`

**Vraag:**
Gegeven is het hieronder afgebeelde knooppunt.
Welke stroom geeft de ampèremeter aan? Geef ook duidelijk aan of de ampèremeter positief of juist negatief zal uitslaan.

**Schema:**
- Stroom naar beneden: 4A
- Stroom naar boven: 6A
- Stroom naar links: 2A
- Stroom naar beneden: 7A
- Stroom naar boven: 1A
- Ampèremeter horizontaal aan rechterzijde

**Gegeven:**
- Diverse stromen in knooppunt zoals getoond in schema

**Gevraagd:**
Stroom door ampèremeter (grootte en richting)

**Antwoord:**

**Eerste wet van Kirchhoff:**
De som van de stromen die in een knooppunt samenkomen is nul.

Σi naar knooppunt toe = Σi van knooppunt af

Σi naar knooppunt toe = 4A + 1A = 5A

Σi van knooppunt af = 6A + 2A + 7A + Iamp meter = 15A + Iamp meter

5A = 15A + Iamp meter

Iamp meter = 5A - 15A = **-10A**

**Conclusie:** De ampèremeter geeft **10A** aan en slaat **negatief** uit.

---

## Vraag 3
- **Type:** Begripsvraag / Analysevraag
- **Onderwerp:** Magnetische flux, toroïde, luchtspleet
- **Moeilijkheid:** Gemiddeld
- **Tags:** `magnetisme`, `flux`, `toroide`, `luchtspleet`

**Vraag:**
In de luchtspleet van een toroïde bedraagt de magnetische flux 50 µWb.
Hoe groot is de flux in het kernmateriaal? Motiveer uw antwoord.

**Gegeven:**
- Flux in luchtspleet = 50 µWb
- Toroïde met luchtspleet

**Gevraagd:**
Flux in kernmateriaal

**Antwoord:**

**Eerste benadering:**
De flux in het kernmateriaal bedraagt ook **50 µWb**.

**Motivering:**
Het magnetische veld van een toroïde is vrijwel geheel beperkt tot de ruimte binnen de spoel. Uit symmetrieoverwegingen volgt dat de veldlijnen concentrische cirkels zijn en dus is de flux in het kernmateriaal gelijk aan de flux in de luchtspleet.

**Tweede benadering:**
ϕ = (N × I)/(Rmijzer + Rlucht)

De flux ϕ wordt bepaald door de serieschakeling van de magnetische weerstand in het kernmateriaal en de magnetische weerstand in de luchtspleet. Omdat het een serieschakeling is, moet de flux dan wel overal dezelfde waarde bezitten.

---

## Vraag 4
- **Type:** Rekenvraag
- **Onderwerp:** Zelfinductie, geïnduceerde spanning
- **Moeilijkheid:** Gemiddeld
- **Tags:** `zelfinductie`, `inductie`, `coëfficiënt`, `formule`

**Vraag:**
De stroom door een zelfinductie neemt in 300 ms lineair af van 0,65 A tot 0,25 A.
Hierbij wordt een zelfinductie bronspanning geïnduceerd van 800 µV.
Hoe groot is de coëfficiënt van zelfinductie van deze spoel?

**Gegeven:**
- Tijd: dt = 300 ms
- Stroom begint: 0,65 A
- Stroom eind: 0,25 A
- Geïnduceerde spanning: 800 µV

**Gevraagd:**
Coëfficiënt van zelfinductie L

**Antwoord:**

Voor een zelfinductie geldt:
ezelfinductie = -L × (di/dt) (formuleblad 5.16)

Gegeven waarden invullen:
800 µV = -L × (0,25A - 0,65A)/(300 ms)

L = -(800 µV × 300 ms)/(-0,4A)

L = (800 × 10⁻⁶ × 300 × 10⁻³)/0,4

L = **600 µH = 0,6 mH**

Of eerst de formule naar L schrijven:
L = -ezelfinductie × (dt/di)

---

## Vraag 5
- **Type:** Rekenvraag
- **Onderwerp:** RL-kring, wisselspanning vs gelijkspanning, arbeidsfactor
- **Moeilijkheid:** Gevorderd
- **Tags:** `impedantie`, `cosφ`, `serie-schakeling`, `RL-kring`

**Vraag:**
Een ideale spoel en een zuivere Ohmse weerstand worden in serie geschakeld en daarna aangesloten aan een batterij met een bronspanning van 9 Volt. Er blijkt nu een stroom te gaan lopen van 150 mA. De inwendige weerstand van de batterij is verwaarloosbaar.

Daarna wordt deze serieschakeling aangesloten op een wisselspanningsbron waarvan de bronspanning ook 9 V bedraagt. Er blijkt nu echter een stroom van 120 mA te gaan lopen.

Bereken de cosφ die hierbij ontstaat.

**Gegeven:**
- DC: Ubron = 9V, I = 150 mA
- AC: Ubron = 9V, I = 120 mA

**Gevraagd:**
cos φ bij wisselspanning

**Antwoord:**

**Situatie 1: Batterij (gelijkspanning)**
De zelfinductie heeft geen invloed op de stroomsterkte:

I = Ebron/R

R = Ebron/I = 9V/(150 mA) = **60 Ω**

**Situatie 2: Wisselspanningsbron**
De impedantie van de serieschakeling wordt bepaald door zowel de weerstand als de zelfinductie:

Xl = Ebron/I = 9V/(120 mA) = 75 Ω

Voor de tan φ geldt:
tan φ = X/R = 75/60 = 1,25
φ = tan⁻¹(1,25) = 51,3°

Hieruit is dan cos φ te bepalen.

**Of direct berekenen:**
Voor de cos φ geldt: cos φ = R/Z

cos φ = 60/√(60² + 75²) = 60/96 = **0,62**

---

## Vraag 6
- **Type:** Rekenvraag
- **Onderwerp:** Complexe impedantie, parallelschakeling
- **Moeilijkheid:** Gemiddeld
- **Tags:** `complexe-rekening`, `impedantie`, `parallel`, `j-operator`

**Vraag:**
Voor component Z1 geldt een impedantie van (10 - 20j) Ω.
Voor component Z2 geldt een impedantie van (10 + 20j) Ω.
Bereken met behulp van de complexe rekenwijze de vervangingsimpedantie indien deze twee componenten parallel worden geschakeld.

**Gegeven:**
- Z1 = (10 - 20j) Ω
- Z2 = (10 + 20j) Ω

**Gevraagd:**
Zv bij parallelschakeling

**Antwoord:**

Zv = (Z1 × Z2)/(Z1 + Z2)

Zv = [(10 - 20j)(10 + 20j)]/[(10 - 20j) + (10 + 20j)]

Zv = (100 - 400j²)/20

Zv = (100 + 400)/20

Zv = 500/20 = **25 Ω**

---

## Vraag 7
- **Type:** Rekenvraag / Analysevraag
- **Onderwerp:** Theorema van Thévenin
- **Moeilijkheid:** Gevorderd
- **Tags:** `thevenin`, `netwerk-analyse`, `vervangingsschema`

**Vraag:**
Gegeven is de hieronder afgebeelde schakeling.
Bereken met behulp van het theorema van Thévenin de stroom door de weerstand R5. Teken ook het Thévenin-vervangingsschema.

**Schema:**
- Uv = 6V
- R1 = 10 kΩ (serie met R2)
- R2 = 10 kΩ (serie met R1)
- R3 = 10 kΩ (serie met R4)
- R4 = 15 kΩ (serie met R3)
- R5 = 5 kΩ (tussen punten A en B)

**Gegeven:**
- Uv = 6V
- R1 = 10 kΩ, R2 = 10 kΩ, R3 = 10 kΩ, R4 = 15 kΩ, R5 = 5 kΩ

**Gevraagd:**
Stroom door R5 met Thévenin-methode

**Antwoord:**

**Stap 1: Open klemspanning bepalen**

Neem R5 uit de schakeling:

UA = (R2/(R1 + R2)) × Uv = (10k/(10k + 10k)) × 6V = 3V

UB = (R4/(R3 + R4)) × Uv = (15k/(10k + 15k)) × 6V = 3,6V

UAB = UA - UB = 3V - 3,6V = -0,6V

De potentiaal in punt A is lager dan de potentiaal in punt B.
Voor berekening gebruiken we: **UT = 0,6V**

**Stap 2: RThévenin bepalen**

Spanningsbronnen kortsluiten:

RT = (R1 × R2)/(R1 + R2) + (R3 × R4)/(R3 + R4)

RT = (10k × 10k)/(10k + 10k) + (10k × 15k)/(10k + 15k)

RT = 5 kΩ + 6 kΩ = **11 kΩ**

**Stap 3: Thévenin-vervangingsschema**

Spanningsbron UT = 0,6V in serie met RT = 11 kΩ en R5 = 5 kΩ

**Stap 4: Stroom door R5 berekenen**

IR5 = UT/(RT + R5) = 0,6V/(11 kΩ + 5 kΩ) = 0,6V/16 kΩ

IR5 = **0,0375 mA = 37,5 µA**

---

## Vraag 8
- **Type:** Rekenvraag
- **Onderwerp:** Kirchhoff spanningswet, maslus
- **Moeilijkheid:** Basis
- **Tags:** `kirchhoff`, `spanning`, `maslus`, `polariteit`

**Vraag:**
Bereken de spanning U3 voor de hieronder afgebeelde schakeling.
Laat je berekening zien en geef de polariteit van deze spanning aan.

**Schema:**
- U1 = 12V (bron links)
- U2 = 9V (bron rechts)
- R1 = 100 Ω, R2 = 100 Ω, R3 = 50 Ω
- U3 over R3

**Gegeven:**
- U1 = 12V
- U2 = 9V
- R1 = 100 Ω, R2 = 100 Ω, R3 = 50 Ω

**Gevraagd:**
U3 en polariteit

**Antwoord:**

**Benadering 1:**
De weerstandwaarden zijn hier niet relevant.
De Kirchhoff-vergelijking van de middenlus luidt:

U1 + U3 + U2 = 0
12 + U3 + 9 = 0
U3 = **-21V** (polariteit van de spanning U3 is negatief)

**Benadering 2:**
Door de componenten te herrangschikken is direct af te lezen dat U3 de som is van U1 en U2, maar in teken omgekeerd moet worden:

U3 = -(12V + 9V) = **-21V**

---

## Vraag 9
- **Type:** Rekenvraag
- **Onderwerp:** Vermogen, blindvermogen
- **Moeilijkheid:** Gemiddeld
- **Tags:** `vermogen`, `schijnbaar-vermogen`, `blindvermogen`, `driehoek`

**Vraag:**
Een elektromotor neemt een vermogen op van 60 kW. Het schijnbare vermogen van deze motor bedraagt 68 kVA.
Hoe groot is de blindcomponent van dit vermogen?

**Gegeven:**
- P = 60 kW (werkelijk vermogen)
- S = 68 kVA (schijnbaar vermogen)

**Gevraagd:**
Q (blindvermogen)

**Antwoord:**

**Oplossingsmethode 1:**

S = √(P² + Q²) (formuleblad 14.10)

Ofwel:
S² = P² + Q² => Q² = S² - P²

Q = √(S² - P²)

Q = √(68² - 60²) = √(4624 - 3600) = √1024

Q = **32 kvar**

**Oplossingsmethode 2:**

cos φ = P/S = 60 kW/68 kVA = 0,8824 (formuleblad 14.11)

φ = cos⁻¹(0,8824) = 28,1°

sin φ = sin(28,1°) = 0,471

Q = S × sin φ = 68 × 0,471 = **32 kvar** (formuleblad 14.11)

---

## Vraag 10
- **Type:** Rekenvraag
- **Onderwerp:** Transformator, windingsverhouding
- **Moeilijkheid:** Basis
- **Tags:** `transformator`, `windingen`, `spanning`, `verhouding`

**Vraag:**
Een transformator is ontworpen voor een primaire spanning van 6000 V en een secundaire spanning van 800 V.
Het aantal windingen aan de primaire zijde van de transformator bedraagt 300.
Wat is het aantal windingen aan de secundaire zijde?

**Gegeven:**
- Uprim = 6000 V
- Usec = 800 V
- Nprim = 300

**Gevraagd:**
Nsec

**Antwoord:**

Nsecundair = (Usec/Uprim) × Nprimair

Nsecundair = (800/6000) × 300

Nsecundair = **40 windingen**

---

## Vraag 11
- **Type:** Rekenvraag / Toepassingsvraag
- **Onderwerp:** Zonne-energie, energieberekening
- **Moeilijkheid:** Gemiddeld
- **Tags:** `zonnepanelen`, `energie`, `vermogen`, `capaciteit`

**Vraag:**
Voor een kantoor is een energieneutrale elektriciteitsvoorziening ontworpen, waarbij gebruik is gemaakt van zonnepanelen.

Voor de gekozen zonnepanelen gelden de volgende specificaties:
- Vermogen per paneel: 360 Wattpeak
- Oppervlakte per paneel: 2000mm x 1000 mm
- Aantal geïnstalleerde zonnepanelen: 120
- Per m² paneel wordt er op jaarbasis 140 kWh opgewekt

De elektrische energiebehoefte op jaarbasis bedraagt 40 MWh.
Men heeft het gevoel dat de installatie niet toereikend is voor de eigen energiebehoefte.

Hoeveel panelen dienen er minimaal extra geïnstalleerd te worden om in de eigen energiebehoefte te voorzien?

**Gegeven:**
- Vermogen per paneel: 360 Wp
- Oppervlakte per paneel: 2 m²
- Aantal panelen: 120
- Opbrengst: 140 kWh/m²/jaar
- Behoefte: 40 MWh/jaar

**Gevraagd:**
Aantal extra panelen nodig

**Antwoord:**

**Stap 1: Huidige opbrengst**

Oppervlakte van één paneel = 2000 mm × 1000 mm = 2 m²
Aantal geïnstalleerde panelen = 120
Geïnstalleerd oppervlakte = 240 m²
Opgewekte energie op jaarbasis = 140 kWh/m²

De installatie zal op jaarbasis een energie opwekken van:
140 kWh/m² × 240 m² = 33.600 kWh = 33,6 MWh

**Stap 2: Tekort berekenen**

Omdat de energiebehoefte hoger is (40 MWh) is deze installatie niet toereikend.

Er moet 40 MWh - 33,6 MWh = 6,4 MWh = 6400 kWh aan extra energie worden opgewekt.

**Stap 3: Extra panelen**

Dit komt neer op een oppervlakte aan zonnepanelen van:
6400 kWh / 140 kWh/m² = 45,7 m², afgerond 46 m²

**Conclusie:**
Er moeten dus minimaal **23 panelen** extra worden geïnstalleerd.

---

## Vraag 12
- **Type:** Rekenvraag
- **Onderwerp:** Blindvermogencorrectie, cos φ verbetering
- **Moeilijkheid:** Gevorderd
- **Tags:** `blindvermogen`, `cosφ`, `condensatorbank`, `driefasen`

**Vraag:**
Een driefasenmotor met een cos φ van 0,75 neemt een vermogen op van 50 kW (230 V / 400 V). Je mag uitgaan van een symmetrische belasting. Het energiebedrijf eist dat je de cos φ verbetert zodat deze minimaal 0,92 bedraagt.

Bereken het bij te schakelen blindvermogen van de condensatorbank om de vereiste cos φ-norm van 0,92 te behalen.

**Gegeven:**
- P = 50 kW
- cos φhuidig = 0,75
- cos φnieuw = 0,92 (vereist)
- Driefasensysteem 230V/400V

**Gevraagd:**
Benodigde Qcondensatorbank

**Antwoord:**

**Stap 1: Huidige situatie**

Shuidig = P/cos φhuidig = 50 kW/0,75 = 66,7 kVA (formuleblad 14.11)

φhuidig = cos⁻¹(0,75) = 41,4°

sin φhuidig = sin(41,4°) = 0,661

Qhuidig = Shuidig × sin φhuidig
Qhuidig = 66,7 kVA × 0,661 = **44,1 kvar**

**Stap 2: Nieuwe situatie**

Voor het nieuwe schijnbare vermogen moet gelden:
Snieuw = P/cos φnieuw = 50 kW/0,92 = 54,3 kVA

Voor het nieuwe maximale blindvermogen moet gelden:
φnieuw = cos⁻¹(0,92) = 23,1°

sin φnieuw = sin(23,1°) = 0,392

Qnieuw = Snieuw × sin φnieuw
Qnieuw = 54,3 kVA × 0,392 = **21,3 kvar**

**Stap 3: Condensatorbank bepalen**

De condensatorbatterij moet dus:
Qhuidig - Qnieuw = 44,1 kvar - 21,3 kvar = 22,8 kvar ≈ **23 kvar**

blindvermogen gaan leveren.

---

## Vraag 13
- **Type:** Rekenvraag
- **Onderwerp:** Spanningsverlies in kabel, driefasensysteem
- **Moeilijkheid:** Gevorderd
- **Tags:** `spanningsverlies`, `kabel`, `driefasen`, `soortelijke-weerstand`

**Vraag:**
Een symmetrische zuivere Ohmse belasting (R1 = R2 = R3) wordt in ster aangesloten op een driefasenet 230 V / 400 V.

De fasestroom bedraagt 30 A. De vijfaderige kabel (L1, L2, L3, N + PE) heeft een aderdoorsnede van 35 mm². Volgens de norm mag het maximale spanningsverlies over de kabel niet groter zijn dan 2% van de fasespanning. De kabel heeft een lengte van 250 meter.

De soortelijke weerstand van het in de kabel gebruikte koper is 0,0178 × 10⁻⁶ Ωm.

Bereken of er wel of niet aan de norm van 2% spanningsverlies wordt voldaan.

**Gegeven:**
- Ufase = 230 V
- Ifase = 30 A
- Lengte kabel: 250 m
- Doorsnede: 35 mm²
- ρ = 0,0178 × 10⁻⁶ Ωm
- Max verlies: 2% van Ufase
- Symmetrische belasting in ster

**Gevraagd:**
Wordt aan norm voldaan?

**Antwoord:**

**Stap 1: Weerstand van de kabel**

Omdat het een symmetrische belasting is zal er geen stroom vloeien door de nulleider. Enkel in de aders L1, L2 en L3 zal daarom spanningsverlies optreden.

Voor elke ader geldt:
Rader = ρ × (l/A) = 0,0178 × 10⁻⁶ × (250/(35 × 10⁻⁶)) = **0,127 Ω** (formuleblad 2.2)

**Stap 2: Spanningsverlies per ader**

Uverlies = If × Rader = 30 × 0,127 = **3,8 V** (formuleblad 2.1)

**Stap 3: Maximale verliesspanning**

2% van de fasespanning:
Uverlies max = 0,02 × Uf = 0,02 × 230 V = **4,6 V**

**Conclusie:**
Omdat Uverlies (3,8V) < Uverlies max (4,6V) wordt hier **wel aan de norm voldaan**.

---

## Vraag 14
- **Type:** Rekenvraag
- **Onderwerp:** Driefasensysteem, ster-driehoek, spanningsrelaties
- **Moeilijkheid:** Gemiddeld
- **Tags:** `driefasen`, `ster`, `driehoek`, `lijnspanning`, `fasespanning`

**Vraag:**
Gegeven is de hieronder afgebeelde schakeling.
Voor de generatorspanningen geldt: |U10| = |U20| = |U30| = 400 V.
Bereken de spanningen |U12|, |U23| en |U31|.

**Schema:**
Generator in ster, belasting in driehoek

**Gegeven:**
- |U10| = |U20| = |U30| = 400 V (fasespanningen generator)
- Generator: ster
- Belasting: driehoek

**Gevraagd:**
|U12|, |U23|, |U31| (lijnspanningen)

**Antwoord:**

Omdat de generator in ster is geschakeld en de belasting in driehoek is geldt:

Ubelasting = Ulijn

Ulijn = √3 × Ufase

Ufase = 400 V

Hieruit volgt:
Ubelasting = √3 × Ufase = √3 × 400 V = 693 V

**Antwoord:**
|U12| = |U23| = |U31| = **693 V**

---

## Vraag 15
- **Type:** Begripsvraag
- **Onderwerp:** Transformator, kernmateriaal
- **Moeilijkheid:** Gemiddeld
- **Tags:** `transformator`, `kern`, `voordelen`, `nadelen`

**Vraag:**
In principe vormen twee gekoppelde spoelen een transformator. Bij een goed functionerende transformator past men echter altijd een kern toe.
Benoem twee voordelen en drie nadelen van het toepassen van een kern.

**Gegeven:**
Context: gekoppelde spoelen vs transformator met kern

**Gevraagd:**
2 voordelen en 3 nadelen van kern

**Antwoord:**

**Mogelijke voordelen (kies 2):**
- De koppelfactor k is nagenoeg gelijk aan 1
- De magnetische flux blijft in het ijzer, waardoor de kans op elektromagnetische storingen verkleint
- Hoger rendement
- Kleiner strooiveld

**Mogelijke nadelen (kies 3):**
- Niet-lineariteit
- Inschakelstromen
- Verliezen in het ijzer
- Warmteontwikkeling
- Hysterisisverliezen
- Wervelstroomverliezen
- Ongewenste geluiden (brom)

---

## Vraag 16
- **Type:** Begripsvraag (waar/niet waar)
- **Onderwerp:** Diverse concepten
- **Moeilijkheid:** Gemiddeld
- **Tags:** `koppelfactor`, `ster-driehoek`, `magnetische-koppeling`, `eenheden`, `blindvermogen`

**Vraag:**
Hieronder volgen 5 beweringen. Geef per bewering aan of deze juist of onjuist is.

**Bewering 1:**
De koppelfactor k is altijd een positief getal dat de kwaliteit aangeeft van de magnetische koppeling tussen twee spoelen.

**Bewering 2:**
Wanneer een elektromotor in ster wordt geschakeld, neemt deze meer vermogen op dan wanneer deze motor in driehoek wordt geschakeld.

**Bewering 3:**
Voor het hieronder afgebeelde schema van magnetische koppeling geldt dat M positief is.
(Schema toont twee spoelen met tegengestelde wikkeling)

**Bewering 4:**
De eenheid Coulomb kan worden uitgedrukt in de grondeenheden elektrische stroom en tijd.

**Bewering 5:**
Het blindvermogen neemt toe wanneer de cosφ afneemt.

**Antwoord:**

- **Bewering 1:** ONJUIST (k kan ook negatief zijn afhankelijk van wikkelrichting)
- **Bewering 2:** ONJUIST (in driehoek neemt motor meer vermogen op)
- **Bewering 3:** ONJUIST (M is negatief bij tegengestelde wikkelrichting)
- **Bewering 4:** JUIST (C = A × s)
- **Bewering 5:** JUIST (Q = S × sin φ, bij cos φ↓ wordt sin φ↑)

---

# Samenvatting Statistieken

## Totaal aantal vragen: 16

## Verdeling per type:
- **Rekenvraag:** 11 (vragen 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
- **Begripsvraag:** 3 (vragen 3, 15, 16)
- **Analysevraag:** 2 (vragen 1, 7 - combinatie met rekenvraag)
- **Toepassingsvraag:** 1 (vraag 11 - combinatie met rekenvraag)

## Verdeling per onderwerp:
- **Condensatoren/Capaciteit:** 1 (vraag 1)
- **Kirchhoff/Knooppunten:** 2 (vragen 2, 8)
- **Magnetisme/Inductie:** 3 (vragen 3, 4, 15)
- **Impedantie/RL-kringen:** 2 (vragen 5, 6)
- **Netwerk-analyse (Thévenin):** 1 (vraag 7)
- **Vermogen (P, Q, S, cos φ):** 3 (vragen 9, 12, 16-deel)
- **Transformatoren:** 2 (vragen 10, 15)
- **Zonne-energie:** 1 (vraag 11)
- **Driefasensystemen:** 3 (vragen 12, 13, 14)
- **Kabels/Spanningsverlies:** 1 (vraag 13)
- **Algemene begrippen:** 1 (vraag 16)

## Verdeling per moeilijkheidsgraad:
- **Basis:** 3 (vragen 2, 8, 10)
- **Gemiddeld:** 9 (vragen 1, 3, 4, 6, 9, 11, 14, 15, 16)
- **Gevorderd:** 4 (vragen 5, 7, 12, 13)

## Prioriteit voor Anki-kaarten:

### Hoge prioriteit (essentiële basiskennis):
1. **Vraag 2** - Kirchhoff knooppunten (basis circuit analyse)
2. **Vraag 8** - Kirchhoff maslussen (basis circuit analyse)
3. **Vraag 10** - Transformator windingsverhouding (basisformule)
4. **Vraag 9** - Vermogensdriehoek (P, Q, S relaties)
5. **Vraag 14** - Ster-driehoek spanningsrelaties

### Gemiddelde prioriteit (belangrijke toepassingen):
6. **Vraag 1** - Condensatornetwerken en foutanalyse
7. **Vraag 4** - Zelfinductie berekeningen
8. **Vraag 6** - Complexe impedantie parallel
9. **Vraag 11** - Praktische energieberekening
10. **Vraag 13** - Spanningsverlies in kabels
11. **Vraag 15** - Transformator voor-/nadelen

### Lagere prioriteit (geavanceerde technieken):
12. **Vraag 5** - RL-kring AC vs DC analyse
13. **Vraag 7** - Thévenin-theorema
14. **Vraag 12** - Blindvermogencorrectie
15. **Vraag 3** - Magnetische flux concepten
16. **Vraag 16** - Algemene begrippen (toets)

## Aanbevelingen:

1. **Begin met basis Kirchhoff-vragen** (2, 8) - fundamenteel voor alle circuit analyse
2. **Focus op vermogensberekeningen** (9, 12, 14) - komt veel voor in praktijk
3. **Oefen complexe impedantie** (5, 6) - essentieel voor AC-circuits
4. **Maak voldoende oefeningen met driefasensystemen** (12, 13, 14) - belangrijk onderwerp
5. **Leer Thévenin goed** (vraag 7) - krachtige analyse-techniek
6. **Begrijp transformator-principes** (10, 15) - basis voor veel toepassingen

## Bestandslocatie:
C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\oefenvragen-extract.md
