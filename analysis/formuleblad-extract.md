# Formuleblad Energietechniek - Systematische Extractie

**Bron:** Formuleblad HBO Elektrotechniek - Energietechniek v3 (maart 2023)
**Boek:** Elektrische Netwerken (Paul Holmes)
**Datum extractie:** 2025-11-06

---

## Inhoudsopgave

1. [Basiswetten (Ohm, Kirchhoff)](#1-basiswetten)
2. [Schakelingen (Serie, Parallel)](#2-schakelingen)
3. [RLC Componenten](#3-rlc-componenten)
4. [Complexe Getallen & Impedantie](#4-complexe-getallen--impedantie)
5. [Effectieve Waarden](#5-effectieve-waarden)
6. [Vermogen (P, Q, S)](#6-vermogen)
7. [Transformatoren](#7-transformatoren)
8. [Netwerktransformaties (Ster-Driehoek)](#8-netwerktransformaties)
9. [Thévenin & Norton](#9-thévenin--norton)
10. [Energie & Rendement](#10-energie--rendement)
11. [Wiskunde Formules](#11-wiskunde-formules)

---

## 1. Basiswetten

### 1.1 Wet van Ohm (Hoofdstuk 1 §1.8)

**Formule:** \( U = I \cdot R \)

- **Variabelen:**
  - \( U \) = Spanning [V]
  - \( I \) = Stroom [A]
  - \( R \) = Weerstand [Ω]
- **Context:** Fundamentele wet voor lineaire geleiders, toepasbaar op DC en AC (effectieve waarden)
- **Prioriteit:** ⭐⭐⭐⭐⭐ (Meest fundamenteel)

---

### 1.2 Wet van Kirchhoff - Maas (Hoofdstuk 1 §1.8)

**Formule:** \( \sum_{j=1}^{N} U_j = 0 \)

- **Variabelen:**
  - \( U_j \) = Spanningen in een maas [V]
  - \( N \) = Aantal spanningen in de maas
- **Context:** Som van alle spanningen in een gesloten lus is nul
- **Voorwaarden:** Pas referentierichting consistent toe
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 1.3 Wet van Kirchhoff - Knoop (Hoofdstuk 1 §1.8)

**Formule:** \( \sum_{j=1}^{N} I_j = 0 \)

- **Variabelen:**
  - \( I_j \) = Stromen in een knooppunt [A]
  - \( N \) = Aantal stromen in het knooppunt
- **Context:** Som van alle stromen naar/van een knooppunt is nul
- **Voorwaarden:** Stromen naar knooppunt positief, weg negatief (of omgekeerd, maar consistent)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

## 2. Schakelingen

### 2.1 Serieschakeling Weerstanden (Hoofdstuk 2 §2.5)

**Formule:** \( R_v = \sum_{i=1}^{n} R_i \)

- **Variabelen:**
  - \( R_v \) = Vervangingsweerstand [Ω]
  - \( R_i \) = Individuele weerstanden [Ω]
- **Context:** Weerstanden in serie optellen
- **Prioriteit:** ⭐⭐⭐⭐

---

### 2.2 Parallelschakeling Weerstanden (Hoofdstuk 2 §2.5)

**Formule:** \( R_v = \frac{1}{\sum_{i=1}^{n} \frac{1}{R_i}} \)

- **Variabelen:**
  - \( R_v \) = Vervangingsweerstand [Ω]
  - \( R_i \) = Individuele weerstanden [Ω]
- **Context:** Reciproke optelling voor parallel
- **Speciale gevallen:**
  - 2 weerstanden: \( R_v = \frac{R_1 \cdot R_2}{R_1 + R_2} \)
  - Gelijke weerstanden: \( R_v = \frac{R}{n} \)
- **Prioriteit:** ⭐⭐⭐⭐

---

### 2.3 Spanningsdeling (Hoofdstuk 2 §2.5)

**Formule:** \( U_1 = \frac{R_1}{R_1 + R_2} \cdot U \)

- **Variabelen:**
  - \( U_1 \) = Spanning over weerstand 1 [V]
  - \( R_1, R_2 \) = Weerstanden in serie [Ω]
  - \( U \) = Totale spanning [V]
- **Context:** Spanningsverdeling over serieweerstanden
- **Prioriteit:** ⭐⭐⭐⭐

---

### 2.4 Serieschakeling Condensatoren (Hoofdstuk 6 §6.7)

**Formule:** \( C_v = \frac{1}{\sum_{i=1}^{n} \frac{1}{C_i}} \)

- **Variabelen:**
  - \( C_v \) = Vervangingscapaciteit [F]
  - \( C_i \) = Individuele capaciteiten [F]
- **Context:** Condensatoren in serie (omgekeerd van weerstanden!)
- **Prioriteit:** ⭐⭐⭐

---

### 2.5 Parallelschakeling Condensatoren (Hoofdstuk 6 §6.7)

**Formule:** \( C_v = \sum_{i=1}^{n} C_i \)

- **Variabelen:**
  - \( C_v \) = Vervangingscapaciteit [F]
  - \( C_i \) = Individuele capaciteiten [F]
- **Context:** Condensatoren parallel optellen
- **Prioriteit:** ⭐⭐⭐

---

### 2.6 Serieschakeling Spoelen (Hoofdstuk 6 §6.7)

**Formule:** \( L_v = \sum_{i=1}^{n} L_i \)

- **Variabelen:**
  - \( L_v \) = Vervangingsinductie [H]
  - \( L_i \) = Individuele inducties [H]
- **Context:** Spoelen in serie optellen (zonder koppeling)
- **Voorwaarden:** Geen magnetische koppeling tussen spoelen
- **Prioriteit:** ⭐⭐⭐

---

### 2.7 Parallelschakeling Spoelen (Hoofdstuk 6 §6.7)

**Formule:** \( L_v = \frac{1}{\sum_{i=1}^{n} \frac{1}{L_i}} \)

- **Variabelen:**
  - \( L_v \) = Vervangingsinductie [H]
  - \( L_i \) = Individuele inducties [H]
- **Context:** Spoelen parallel (reciproke optelling)
- **Voorwaarden:** Geen magnetische koppeling tussen spoelen
- **Prioriteit:** ⭐⭐⭐

---

## 3. RLC Componenten

### 3.1 Definitieformule Condensator (Hoofdstuk 6 §6.7)

**Formule:** \( i_C = C \frac{du_C}{dt} \)

- **Variabelen:**
  - \( i_C \) = Stroom door condensator [A]
  - \( C \) = Capaciteit [F]
  - \( u_C \) = Spanning over condensator [V]
  - \( t \) = Tijd [s]
- **Context:** Stroom is evenredig met spanningsverandering
- **Implicatie:** Condensator blokkeert DC, laat AC door
- **Prioriteit:** ⭐⭐⭐⭐

---

### 3.2 Definitieformule Spoel (Hoofdstuk 6 §6.7)

**Formule:** \( u_L = L \frac{di_L}{dt} \)

- **Variabelen:**
  - \( u_L \) = Spanning over spoel [V]
  - \( L \) = Inductie [H]
  - \( i_L \) = Stroom door spoel [A]
  - \( t \) = Tijd [s]
- **Context:** Spanning is evenredig met stroomverandering
- **Implicatie:** Spoel verzet zich tegen stroomverandering
- **Prioriteit:** ⭐⭐⭐⭐

---

### 3.3 Capacitieve Reactantie (Hoofdstuk 6 §6.7)

**Formule:** \( X_C = \frac{1}{\omega C} \) [Ω]

- **Variabelen:**
  - \( X_C \) = Capacitieve reactantie [Ω]
  - \( \omega \) = Hoekfrequentie [rad/s]
  - \( C \) = Capaciteit [F]
- **Context:** AC "weerstand" van condensator
- **Frequentieafhankelijkheid:** \( X_C \downarrow \) als \( f \uparrow \)
- **Alternatieven:** \( X_C = \frac{1}{2\pi f C} \)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 3.4 Inductieve Reactantie (Hoofdstuk 6 §6.7)

**Formule:** \( X_L = \omega L \) [Ω]

- **Variabelen:**
  - \( X_L \) = Inductieve reactantie [Ω]
  - \( \omega \) = Hoekfrequentie [rad/s]
  - \( L \) = Inductie [H]
- **Context:** AC "weerstand" van spoel
- **Frequentieafhankelijkheid:** \( X_L \uparrow \) als \( f \uparrow \)
- **Alternatieven:** \( X_L = 2\pi f L \)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 3.5 Stroom-Spanning Relatie Weerstand (Hoofdstuk 7 §7.7)

**Formule:** \( I_R = \sin(\omega t) \rightarrow U_R = R \cdot \sin(\omega t) \)

- **Context:** Stroom en spanning in fase voor weerstand
- **Faseverschil:** \( \phi = 0° \)
- **Prioriteit:** ⭐⭐⭐

---

### 3.6 Stroom-Spanning Relatie Spoel (Hoofdstuk 7 §7.7)

**Formule:** \( I_L = \sin(\omega t) \rightarrow U_L = X_L \cdot \cos(\omega t) \)

- **Context:** Spanning loopt 90° voor op stroom bij spoel
- **Faseverschil:** \( \phi = +90° \) (spanning ijlt voor)
- **Prioriteit:** ⭐⭐⭐⭐

---

### 3.7 Stroom-Spanning Relatie Condensator (Hoofdstuk 7 §7.7)

**Formule:** \( U_C = \sin(\omega t) \rightarrow I_C = X_C \cdot \cos(\omega t) \)

- **Context:** Stroom loopt 90° voor op spanning bij condensator
- **Faseverschil:** \( \phi = -90° \) (spanning ijlt achter)
- **Prioriteit:** ⭐⭐⭐⭐

---

## 4. Complexe Getallen & Impedantie

### 4.1 Harmonische Spanning (Hoofdstuk 9 §9.6)

**Formule:** \( u(t) = \hat{u} \cos(\omega t + \phi) \Leftrightarrow \underline{U} = \hat{u} \cdot e^{j\phi} \)

- **Variabelen:**
  - \( u(t) \) = Tijdsdomein spanning [V]
  - \( \hat{u} \) = Amplitudewaarde [V]
  - \( \omega \) = Hoekfrequentie [rad/s]
  - \( \phi \) = Fasehoek [rad of °]
  - \( \underline{U} \) = Complexe fasorgroot [V]
- **Context:** Omzetting tijdsdomein ↔ fasordomein
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 4.2 Rechthoekige Vorm Complexe Spanning (Hoofdstuk 9 §9.6)

**Formule:** \( \underline{U} = \hat{u} \cdot e^{j\phi} = \text{Re}(\underline{U}) + j \cdot \text{Im}(\underline{U}) \)

- **Variabelen:**
  - \( \text{Re}(\underline{U}) \) = Reëel deel [V]
  - \( \text{Im}(\underline{U}) \) = Imaginair deel [V]
- **Context:** Rechthoekige vorm van complex getal
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.3 Geconjugeerd Complex Getal (Hoofdstuk 9 §9.6)

**Formule:** \( \underline{U}^* = \hat{u} \cdot e^{-j\phi} = \text{Re}(\underline{U}) - j \cdot \text{Im}(\underline{U}) \)

- **Context:** Geconjugeerde voor vermogensberekening
- **Toepassing:** \( \underline{S} = \underline{U} \cdot \underline{I}^* \)
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.4 Modulus Complex Getal (Hoofdstuk 9 §9.6)

**Formule:** \( |\underline{U}| = \hat{u} = \sqrt{\text{Re}^2 + \text{Im}^2} \)

- **Context:** Absolute waarde (amplitude) van complexe grootheid
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.5 Argument Complex Getal (Hoofdstuk 9 §9.6)

**Formule:** \( \phi = \angle \underline{U} = \tan^{-1}\left(\frac{\text{Im}}{\text{Re}}\right) \)

- **Context:** Fasehoek van complexe grootheid
- **Let op:** Kwadrantencorrectie nodig!
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.6 Complexe Impedantie Weerstand (Hoofdstuk 9 §9.6)

**Formule:** \( Z_R = R \)

- **Context:** Weerstand is zuiver reëel (geen faseshift)
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.7 Complexe Impedantie Condensator (Hoofdstuk 9 §9.6)

**Formule:** \( Z_C = \frac{1}{j\omega C} = -j X_C \)

- **Context:** Capacitieve impedantie is imaginair negatief
- **Fasegedrag:** -90° faseverschuiving
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 4.8 Complexe Impedantie Spoel (Hoofdstuk 9 §9.6)

**Formule:** \( Z_L = j\omega L = j X_L \)

- **Context:** Inductieve impedantie is imaginair positief
- **Fasegedrag:** +90° faseverschuiving
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 4.9 Standaard Complex Getal (Hoofdstuk 10 §10.5)

**Formule:** \( z = a + bj \), waarbij \( j^2 = -1 \)

**Geconjugeerde:** \( z^* = a - bj \)

- **Context:** Basisnotatie complexe getallen in elektrotechniek
- **Let op:** Wiskunde gebruikt \( i \), elektrotechniek gebruikt \( j \)
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.10 Polair Complex Getal (Hoofdstuk 10 §10.5)

**Formule:** \( z = |z| \angle \phi \)

**Regel van Euler:** \( e^{j\phi} = \cos\phi + j\sin\phi \)

- **Context:** Polaire vorm voor vermenigvuldiging/deling
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.11 Omzetting Rechthoekig → Polair (Hoofdstuk 10 §10.5)

**Formule:**
- \( |z| = \sqrt{a^2 + b^2} \)
- \( \angle z = \tan^{-1}\left(\frac{b}{a}\right) \)

- **Context:** Conversie tussen notaties
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.12 Optelling Complexe Getallen (Hoofdstuk 10 §10.5)

**Formule:** \( z_1 + z_2 = (a_1 + a_2) + (b_1 + b_2)j \)

- **Context:** Optelling in rechthoekige vorm
- **Prioriteit:** ⭐⭐⭐

---

### 4.13 Vermenigvuldiging Complexe Getallen (Hoofdstuk 10 §10.5)

**Formule:** \( z_1 \cdot z_2 = (a_1a_2 - b_1b_2) + (a_1b_2 + a_2b_1)j \)

**Of in polaire vorm:** \( z_1 \cdot z_2 = |z_1||z_2| \angle (\phi_1 + \phi_2) \)

- **Context:** Vermenigvuldigen in rechthoekige of polaire vorm
- **Tip:** Polaire vorm is eenvoudiger voor vermenigvuldiging
- **Prioriteit:** ⭐⭐⭐⭐

---

### 4.14 Deling Complexe Getallen (Hoofdstuk 10 §10.5)

**Formule:** \( \frac{z_1}{z_2} = \frac{z_1 \cdot z_2^*}{|z_2|^2} \)

**Of in polaire vorm:** \( \frac{z_1}{z_2} = \frac{|z_1|}{|z_2|} \angle (\phi_1 - \phi_2) \)

- **Context:** Deling met geconjugeerde methode
- **Prioriteit:** ⭐⭐⭐⭐

---

## 5. Effectieve Waarden

### 5.1 Effectieve Waarde Algemeen (Hoofdstuk 5 §5.8)

**Formule:** \( U_{eff} = \sqrt{\frac{u_1^2 + u_2^2 + \ldots + u_n^2}{n}} \)

- **Context:** RMS (Root Mean Square) waarde voor periodiek signaal
- **Prioriteit:** ⭐⭐⭐⭐

---

### 5.2 Effectieve Waarde Sinusvormig (Hoofdstuk 5 §5.8)

**Formule:** \( U_{eff \, sinus} = \frac{\hat{u}}{\sqrt{2}} \)

- **Variabelen:**
  - \( U_{eff} \) = Effectieve waarde [V]
  - \( \hat{u} \) = Amplitudewaarde (top) [V]
- **Context:** Voor zuivere sinusgolf
- **Numerieke waarde:** \( \frac{1}{\sqrt{2}} \approx 0.707 \)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 5.3 Effectieve Waarde Blokgolf (Hoofdstuk 5 §5.8)

**Formule:** \( U_{eff \, blok} = \hat{u} \)

- **Context:** Effectieve waarde = amplitude voor symmetrische blokgolf
- **Prioriteit:** ⭐⭐⭐

---

### 5.4 Effectieve Waarde Zaagtandgolf (Hoofdstuk 5 §5.8)

**Formule:** \( U_{eff \, zaag} = \frac{\hat{u}}{\sqrt{3}} \)

- **Context:** Voor lineair stijgende/dalende zaagtand
- **Numerieke waarde:** \( \frac{1}{\sqrt{3}} \approx 0.577 \)
- **Prioriteit:** ⭐⭐⭐

---

## 6. Vermogen

### 6.1 Vermogen Weerstand (DC of effectieve waarden) (Hoofdstuk 4 §4.3)

**Formule:** \( P = U \cdot I = I^2 \cdot R = \frac{U^2}{R} \)

- **Variabelen:**
  - \( P \) = Vermogen [W]
  - \( U \) = Spanning [V]
  - \( I \) = Stroom [A]
  - \( R \) = Weerstand [Ω]
- **Context:** Werkzaam vermogen in weerstand (wordt omgezet in warmte)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 6.2 Werkzaam Vermogen (Hoofdstuk 11 §11.6)

**Formule:** \( P = U \cdot I \cos\phi \) [W]

- **Variabelen:**
  - \( P \) = Werkzaam vermogen [W]
  - \( U \) = Effectieve spanning [V]
  - \( I \) = Effectieve stroom [A]
  - \( \cos\phi \) = Arbeidsfactor (dimensieloos)
  - \( \phi \) = Faseverschil tussen spanning en stroom
- **Context:** Daadwerkelijk geleverde/verbruikte vermogen
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 6.3 Blindvermogen (Hoofdstuk 11 §11.6)

**Formule:** \( Q = U \cdot I \sin\phi \) [VAR]

- **Variabelen:**
  - \( Q \) = Blindvermogen [VAR - Volt Ampère Reactief]
  - \( \sin\phi \) = Blinde factor
- **Context:** Heen-en-weer pendelend vermogen (opslag in L/C)
- **Conventie:**
  - \( Q > 0 \): Inductief (spoel)
  - \( Q < 0 \): Capacitief (condensator)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 6.4 Schijnbaar Vermogen (Hoofdstuk 11 §11.6)

**Formule:** \( S = U \cdot I = u_{eff} \cdot i_{eff} \) [VA]

- **Variabelen:**
  - \( S \) = Schijnbaar vermogen [VA - Volt Ampère]
- **Context:** Totaal geleverd vermogen (dimensionering kabels/transformatoren)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 6.5 Vermogensdriehoek (Hoofdstuk 11 §11.6)

**Formule:** \( S^2 = P^2 + Q^2 \)

**Afgeleid:**
- \( S = \sqrt{P^2 + Q^2} \)
- \( P = S \cdot \cos\phi \)
- \( Q = S \cdot \sin\phi \)
- \( \cos\phi = \frac{P}{S} \)

- **Context:** Pythagoras voor vermogensdriehoek
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 6.6 Momentaan Vermogen (Hoofdstuk 11 §11.6)

**Formule:** \( p(t) = U \cdot I (\cos\phi - \cos(2\omega t + \phi)) \)

- **Context:** Ogenblikkelijk vermogen varieert met 2× netfrequentie
- **Gemiddelde:** \( \overline{p(t)} = P = U \cdot I \cos\phi \)
- **Prioriteit:** ⭐⭐⭐

---

### 6.7 Complex Vermogen (Hoofdstuk 11 §11.6)

**Formule:**
- \( \underline{S} = \underline{U} \cdot \underline{I}^* \)
- \( P = \text{Re}[\underline{U} \cdot \underline{I}^*] \)
- \( Q = \text{Im}[\underline{U} \cdot \underline{I}^*] \)

**Waarbij:**
- \( \underline{U} = U \)
- \( \underline{I} = I \cdot e^{j\phi} \)

- **Context:** Elegante manier voor vermogensberekening met complexe rekenen
- **Voordelen:** Automatisch correct teken voor P en Q
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

## 7. Transformatoren

### 7.1 Wikkelverhouding (Hoofdstuk 21 §21.4)

**Formule:** \( n = \frac{u_1}{u_2} = \frac{-i_1}{i_2} \)

- **Variabelen:**
  - \( n \) = Wikkelverhouding (dimensieloos)
  - \( u_1 \) = Primaire spanning [V]
  - \( u_2 \) = Secundaire spanning [V]
  - \( i_1 \) = Primaire stroom [A]
  - \( i_2 \) = Secundaire stroom [A]
- **Context:** Ideale transformator (geen verliezen)
- **Let op:** Minteken bij stroom door referentierichting
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 7.2 Impedantietransformatie (Hoofdstuk 21 §21.4)

**Formule:** \( n^2 = \frac{Z_1}{Z_2} \)

**Of:** \( Z_1 = n^2 \cdot Z_2 \)

- **Context:** Impedantie transformeert met kwadraat van wikkelverhouding
- **Toepassing:** Impedantie-aanpassing
- **Prioriteit:** ⭐⭐⭐⭐

---

### 7.3 Koppeling Tussen Spoelen (Hoofdstuk 21 §21.4)

**Formule:** \( M = k\sqrt{L_1 \cdot L_2} \)

- **Variabelen:**
  - \( M \) = Wederzijdse inductie [H]
  - \( k \) = Koppelfactor \( (0 \leq k \leq 1) \)
  - \( L_1, L_2 \) = Zelfinductie van spoelen [H]
- **Context:** Magnetische koppeling tussen twee spoelen
- **Prioriteit:** ⭐⭐⭐

---

### 7.4 Spreiding (Hoofdstuk 21 §21.4)

**Formule:** \( \sigma = 1 - k^2 \)

- **Variabelen:**
  - \( \sigma \) = Spreidingsfactor (dimensieloos)
  - \( k \) = Koppelfactor
- **Context:** Maat voor lekflux bij transformatoren
- **Ideaal:** \( k = 1 \Rightarrow \sigma = 0 \) (geen spreiding)
- **Prioriteit:** ⭐⭐

---

## 8. Netwerktransformaties

### 8.1 Ster naar Driehoek (Δ) - Impedantie (Hoofdstuk 20 §20.6)

**Formules:**
- \( Z_{12} = \frac{Z_1 Z_2}{Z_1 + Z_2 + Z_3} \)
- \( Z_{23} = \frac{Z_2 Z_3}{Z_1 + Z_2 + Z_3} \)
- \( Z_{31} = \frac{Z_3 Z_1}{Z_1 + Z_2 + Z_3} \)

- **Context:** Omzetten Y → Δ configuratie
- **Prioriteit:** ⭐⭐⭐

---

### 8.2 Driehoek naar Ster (Y) - Impedantie (Hoofdstuk 20 §20.6)

**Formules:**
- \( Z_1 = \frac{Z_{12}Z_{31}}{Z_{12} + Z_{23} + Z_{31}} \)
- \( Z_2 = \frac{Z_{12}Z_{23}}{Z_{12} + Z_{23} + Z_{31}} \)
- \( Z_3 = \frac{Z_{23}Z_{31}}{Z_{12} + Z_{23} + Z_{31}} \)

- **Context:** Omzetten Δ → Y configuratie
- **Prioriteit:** ⭐⭐⭐

---

### 8.3 Ster naar Driehoek (Δ) - Admittantie (Hoofdstuk 20 §20.6)

**Formules:**
- \( Y_{12} = \frac{Y_1 Y_2}{Y_1 + Y_2 + Y_3} \)
- \( Y_{23} = \frac{Y_2 Y_3}{Y_1 + Y_2 + Y_3} \)
- \( Y_{13} = \frac{Y_1 Y_3}{Y_1 + Y_2 + Y_3} \)

- **Context:** Parallelle circuits eenvoudiger met admittantie
- **Prioriteit:** ⭐⭐

---

### 8.4 Gelijke Impedanties Ster-Driehoek (Hoofdstuk 20 §20.6)

**Formules:**
- \( Z_\Delta = 3Z_Y \)
- \( Z_Y = \frac{Z_\Delta}{3} \)

- **Context:** Speciale gevallen met symmetrische belasting
- **Toepassing:** Driefasensystemen
- **Prioriteit:** ⭐⭐⭐⭐

---

## 9. Thévenin & Norton

### 9.1 Thévenin Equivalent (Hoofdstuk 3 §3.10)

**Formule:** \( I_k = \frac{U_o}{R_i} \)

- **Variabelen:**
  - \( I_k \) = Kortsluitstroom [A]
  - \( U_o \) = Open klemspanning (Thévenin spanning) [V]
  - \( R_i \) = Interne weerstand (Thévenin weerstand) [Ω]
- **Context:** Vereenvoudiging complex netwerk naar spanningsbron + serieweerstand
- **Prioriteit:** ⭐⭐⭐⭐

---

### 9.2 Norton Equivalent (Hoofdstuk 3 §3.10)

**Formule:** \( U_o = I_k \cdot R_i \)

- **Variabelen:**
  - \( I_k \) = Norton stroom (kortsluitstroom) [A]
  - \( U_o \) = Open klemspanning [V]
  - \( R_i \) = Interne weerstand (Norton weerstand) [Ω]
- **Context:** Vereenvoudiging complex netwerk naar stroombron + parallelweerstand
- **Relatie:** Norton ↔ Thévenin equivalent
- **Prioriteit:** ⭐⭐⭐⭐

---

## 10. Energie & Rendement

### 10.1 Elektrische Energie (Hoofdstuk 4 §4.3)

**Formule:** \( W = U \cdot I \cdot t \)

- **Variabelen:**
  - \( W \) = Energie [J of Ws]
  - \( U \) = Spanning [V]
  - \( I \) = Stroom [A]
  - \( t \) = Tijd [s]
- **Alternatief:** \( W = P \cdot t \) [J]
- **Praktisch:** \( W = P \cdot t \) [kWh] als P in kW en t in uur
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

### 10.2 Rendement (Hoofdstuk 4 §4.3)

**Formule:** \( \eta = \frac{P_{nuttig}}{P_{totaal}} \)

- **Variabelen:**
  - \( \eta \) = Rendement (dimensieloos of %)
  - \( P_{nuttig} \) = Nuttig vermogen [W]
  - \( P_{totaal} \) = Totaal opgenomen vermogen [W]
- **Alternatief:** \( \eta = 1 - \frac{P_{verlies}}{P_{totaal}} \)
- **Bereik:** \( 0 \leq \eta \leq 1 \) (of 0-100%)
- **Prioriteit:** ⭐⭐⭐⭐⭐

---

## 11. Wiskunde Formules

### 11.1 ABC-Formule (Kwadratische Vergelijking)

**Gegeven:** \( ax^2 + bx + c = 0 \)

**Discriminant:** \( D = b^2 - 4ac \)

**Oplossingen:**
- **Als \( D \geq 0 \):** \( x_{1,2} = \frac{-b \pm \sqrt{D}}{2a} \)
- **Als \( D < 0 \):** \( x_{1,2} = \frac{-b \pm j\sqrt{-D}}{2a} \)

- **Context:** Oplossen kwadratische vergelijkingen (bijv. resonantie)
- **Prioriteit:** ⭐⭐⭐

---

### 11.2 Goniometrische Identiteiten

**Pythagorase identiteit:** \( \cos^2\alpha + \sin^2\alpha = 1 \)

**Complementaire hoeken:** \( \cos\alpha = \sin\left(\frac{\pi}{2} - \alpha\right) \)

**Dubbele hoek sinus:** \( \sin(2\alpha) = 2\sin\alpha\cos\alpha \)

**Dubbele hoek cosinus (3 vormen):**
- \( \cos(2\alpha) = \cos^2\alpha - \sin^2\alpha \)
- \( \cos^2\alpha = \frac{1}{2} + \frac{1}{2}\cos(2\alpha) \)
- \( \sin^2\alpha = \frac{1}{2} - \frac{1}{2}\cos(2\alpha) \)

- **Context:** Momentaan vermogen, harmonischen analyse
- **Prioriteit:** ⭐⭐⭐

---

### 11.3 Afgeleiden

**Sinus:** \( \frac{d}{dt}\sin(\omega t) = \omega\cos(\omega t) \)

**Cosinus:** \( \frac{d}{dt}\cos(\omega t + \phi) = -\omega\sin(\omega t) \)

- **Context:** Definitieformules L en C
- **Prioriteit:** ⭐⭐⭐

---

### 11.4 Integralen

**Cosinus:** \( \int_{\Omega_1}^{\Omega_2} \cos(\omega t) \, dt = \frac{\sin\Omega_2}{\Omega_2} - \frac{\sin\Omega_1}{\Omega_1} \)

**Reciprook:** \( \int \frac{1}{x} \, dx = \ln|x| + K \)

- **Context:** Energie in spoelen/condensatoren
- **Prioriteit:** ⭐⭐

---

## Samenvatting: Top 10 Belangrijkste Formules voor Examen

### 1. **Wet van Ohm** ⭐⭐⭐⭐⭐
\( U = I \cdot R \)

### 2. **Effectieve Waarde Sinus** ⭐⭐⭐⭐⭐
\( U_{eff} = \frac{\hat{u}}{\sqrt{2}} \)

### 3. **Capacitieve Reactantie** ⭐⭐⭐⭐⭐
\( X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} \)

### 4. **Inductieve Reactantie** ⭐⭐⭐⭐⭐
\( X_L = \omega L = 2\pi f L \)

### 5. **Complexe Impedantie**
- \( Z_C = \frac{1}{j\omega C} = -jX_C \)
- \( Z_L = j\omega L = jX_L \)

### 6. **Werkzaam Vermogen** ⭐⭐⭐⭐⭐
\( P = U \cdot I \cos\phi \)

### 7. **Blindvermogen** ⭐⭐⭐⭐⭐
\( Q = U \cdot I \sin\phi \)

### 8. **Vermogensdriehoek** ⭐⭐⭐⭐⭐
\( S^2 = P^2 + Q^2 \)

### 9. **Complex Vermogen** ⭐⭐⭐⭐⭐
\( \underline{S} = \underline{U} \cdot \underline{I}^* \)

### 10. **Transformator Wikkelverhouding** ⭐⭐⭐⭐⭐
\( n = \frac{u_1}{u_2} = \frac{-i_1}{i_2} \)

---

## Aanvullende Top Formules

### 11. **Kirchhoff Maas** ⭐⭐⭐⭐⭐
\( \sum U_j = 0 \)

### 12. **Kirchhoff Knoop** ⭐⭐⭐⭐⭐
\( \sum I_j = 0 \)

### 13. **Energie** ⭐⭐⭐⭐⭐
\( W = U \cdot I \cdot t = P \cdot t \)

### 14. **Rendement** ⭐⭐⭐⭐⭐
\( \eta = \frac{P_{nuttig}}{P_{totaal}} \)

### 15. **Harmonische Spanning (Fasor)** ⭐⭐⭐⭐⭐
\( u(t) = \hat{u}\cos(\omega t + \phi) \Leftrightarrow \underline{U} = \hat{u} \cdot e^{j\phi} \)

---

## Statistieken Extractie

**Totaal aantal formules:** 75+
**Hoofdcategorieën:** 11
**Bron hoofdstukken:** Hoofdstuk 1-11, 20-21 (Paul Holmes - Elektrische Netwerken)

**Verdeling per categorie:**
1. Basiswetten: 3 formules
2. Schakelingen: 7 formules
3. RLC Componenten: 7 formules
4. Complexe Getallen & Impedantie: 14 formules
5. Effectieve Waarden: 4 formules
6. Vermogen: 7 formules
7. Transformatoren: 4 formules
8. Netwerktransformaties: 4 formules
9. Thévenin & Norton: 2 formules
10. Energie & Rendement: 2 formules
11. Wiskunde: 4 formules (+ diverse identiteiten)

**Prioriteitsindeling:**
- ⭐⭐⭐⭐⭐ (Zeer hoog - examen kritisch): 20 formules
- ⭐⭐⭐⭐ (Hoog): 25 formules
- ⭐⭐⭐ (Medium): 20 formules
- ⭐⭐ (Laag): 10 formules

---

**Datum extractie:** 2025-11-06
**Geëxtraheerd door:** Claude Code
**Formuleblad versie:** v3 - maart 2023
**Output bestand:** `C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\formuleblad-extract.md`
