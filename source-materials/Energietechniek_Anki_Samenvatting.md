# 📘 Examen Energietechniek — Structuur & Inhoud voor Anki-kaarten

Gebaseerd op:
- *Oefenvragen Energietechniek* (NCOI)
- *Antwoorden oefenvragen Energietechniek*
- *Uitwerkingen Opgaven Energietechniek V0.8*
- *Formuleblad Energietechniek v3 2023*

---

## 🧩 Examendomeinen

### 1. **Basiswetten & Netwerken**
- **Wet van Ohm**:  
  \( U = I \cdot R \)
- **Eerste wet van Kirchhoff (Knoopwet)**:  
  De som van de stromen in een knooppunt is nul.  
  \( \sum I_{in} = \sum I_{uit} \)
- **Tweede wet van Kirchhoff (Maaswet)**:  
  De som van de spanningen in een gesloten kring is nul.  
  \( \sum U = 0 \)
- **Vervangingsweerstand/impedantie**:  
  - Serie: \( R_v = R_1 + R_2 + ... \)  
  - Parallel: \( \frac{1}{R_v} = \frac{1}{R_1} + \frac{1}{R_2} + ... \)

---

### 2. **Thévenin & Norton**
- **Thévenin**:  
  \( U_{th} = U_{open} \)  
  \( R_{th} = R_{ingang} \text{ (met bronnen kortgesloten)} \)  
  \( I = \frac{U_{th}}{R_{th} + R_{load}} \)
- **Norton**:  
  \( I_N = \frac{U_{th}}{R_{th}} \), \( R_N = R_{th} \)
- **Maximaal vermogen**:  
  \( R_{load} = R_{th} \)

---

### 3. **Capaciteiten & Inducties**
- **Condensator**:
  - Serie: \( \frac{1}{C_v} = \frac{1}{C_1} + \frac{1}{C_2} + ... \)
  - Parallel: \( C_v = C_1 + C_2 + ... \)
  - Stroom: \( i_C = C \frac{du}{dt} \)
  - Reactantie: \( X_C = \frac{1}{\omega C} \)
- **Spoel (Inductor)**:
  - Serie: \( L_v = L_1 + L_2 + ... \)
  - Parallel: \( \frac{1}{L_v} = \frac{1}{L_1} + \frac{1}{L_2} + ... \)
  - Spanning: \( u_L = L \frac{di}{dt} \)
  - Reactantie: \( X_L = \omega L \)

---

### 4. **Complexe Impedantie en Faseverschuiving**
- **Complexe vormen**:
  - \( Z_R = R \)
  - \( Z_L = j\omega L \)
  - \( Z_C = \frac{1}{j\omega C} = -j\frac{1}{\omega C} \)
- **Fasorrepresentatie**:
  - \( u(t) = \hat{U}\cos(\omega t + \phi) \Rightarrow U = \hat{U} e^{j\phi} \)
- **Polair naar Rec**:
  - \( z = r ∠\theta = r(\cos\theta + j\sin\theta) \)
- **Cosφ en tanφ**:
  - \( \tan\phi = \frac{X_L - X_C}{R} \)
  - \( \cos\phi = \frac{R}{|Z|} \)

---

### 5. **Vermogen en Rendement**
- **Actief (P)**: \( P = U I \cos\phi \) [W]  
- **Blind (Q)**: \( Q = U I \sin\phi \) [var]  
- **Schijnbaar (S)**: \( S = U I \) [VA]  
  \( S^2 = P^2 + Q^2 \)
- **Rendement**:  
  \( \eta = \frac{P_{nuttig}}{P_{totaal}} \)
- **Momentaan vermogen**:  
  \( p(t) = U I [\cos\phi - \cos(2\omega t + \phi)] \)

---

### 6. **Transformatoren & Spoelen**
- **Wikkelverhouding**:  
  \( \frac{N_1}{N_2} = \frac{U_1}{U_2} = \frac{I_2}{I_1} \)
- **Koppeling**:  
  \( M = k\sqrt{L_1 L_2} \)
  - \( k \) = koppelfactor (0–1)
- **Inducties in serie/parallel**:
  - Serie: \( L_t = L_1 + L_2 ± 2M \)
  - Parallel: \( L_t = \frac{L_1 L_2 - M^2}{L_1 + L_2 ∓ 2M} \)

---

### 7. **Driefasensystemen**
- **Spanningen**:
  - Lijn → Fase: \( U_L = \sqrt{3} U_F \)
- **Ster**:
  \( U_{fase} = \frac{U_{lijn}}{\sqrt{3}} \)
- **Driehoek**:
  \( I_{lijn} = \sqrt{3} I_{fase} \)
- **Vermogen**:
  \( P = \sqrt{3} U_L I_L \cos\phi \)
  \( Q = \sqrt{3} U_L I_L \sin\phi \)

---

### 8. **Blindvermogencompensatie**
- **Condensatorbank**:
  - \( Q_c = Q_1 - Q_2 \)
  - \( Q = U^2 \cdot 2πf \cdot C \)
  - \( C = \frac{Q}{U^2 2πf} \)
- **Doel**: verhogen van cosφ naar gewenste waarde.

---

### 9. **Energie & Efficiëntie**
- **Energieverbruik**:
  \( W = P \cdot t \)
- **Omrekening**:
  \( 1 \text{ kWh} = 3,6 \times 10^6 \text{ J} \)
- **Spanningsverlies kabel**:
  \( ΔU = I \cdot ρ \cdot \frac{l}{A} \)
- **Max. spanningsverlies**:
  \( U_{verlies,max} = 0,02 \cdot U_{fase} \)

---

### 10. **Resonantie & Filternetwerken**
- **Serieschakeling RLC**:  
  \( \omega_0 = \frac{1}{\sqrt{LC}} \)
- **Resonantie**:  
  \( X_L = X_C \)
- **Bepaal resonantiefrequentie**:  
  \( f_0 = \frac{1}{2π\sqrt{LC}} \)
- **Wienbrug** en **LCR-netwerken**:
  - Impedantieanalyse via complexe som
  - In resonantie is i(t) = 0 of maximale stroom door R

---

## 🧮 Typische Examenformules
| Onderwerp | Formule | Toepassing |
|------------|----------|------------|
| Cosφ | \( \frac{R}{\sqrt{R^2 + (X_L - X_C)^2}} \) | Faseverschuiving |
| Capaciteit bij kortsluiting | \( C_v = C_1 + C_2 \) | Bij C3 doorslag |
| Blindvermogen | \( Q = S \sin\phi \) | Cosφ-correctie |
| Thévenin | \( R_{th} = \frac{U_{open}}{I_{kort}} \) | Eenvoudiger netwerk |
| Impedantie parallel | \( Z = \frac{Z_1 Z_2}{Z_1 + Z_2} \) | Complexe netwerken |
| Vermogen motor | \( P = \sqrt{3} U_L I_L \cos\phi \) | Driefase motor |
| Transformator | \( N_2 = \frac{U_2}{U_1} N_1 \) | Aantal windingen |
| Energie | \( E = P \cdot t \) | Verbruik of opbrengst |

---

## 🧠 Structuur voor Anki-kaarten

Elke kaart bevat:
- **Vraag**: examenvraag of deelconcept (zoals in oefenvragen)
- **Antwoord**: uitgewerkt, met formule en conclusie
- **Bronverwijzing**: hoofdstuk of oefenopgave (H#.# of vraagnummer)
- **Tags**: `thevenin`, `blindvermogen`, `cosphi`, `driefase`, `kirchhoff`, etc.

**Voorbeeld:**

**Front:**  
Een condensatornetwerk met C1=10µF, C2=8µF, C3=12µF. Wat gebeurt er met de vervangingscapaciteit als C3 doorslaat?

**Back:**  
C3 wordt kortgesloten → vervangingscapaciteit stijgt.  
\( C_v \) vóór: 14,8µF  
\( C_v \) na: 18µF  
→ Toename: +3,2µF

**Tags:** `condensator`, `netwerk`, `serie-parallel`, `examen-2023-vraag1`

---

## 📚 Prioritaire Examenonderwerpen
1. **Kirchhoff-wetten** (stromen/spanningen)
2. **Thévenin/Norton**-vervanging
3. **RLC- en impedantieberekeningen**
4. **Cosφ en blindvermogen**
5. **Driefasenstelsels en vermogensbalans**
6. **Transformatorwetten**
7. **Koppelfactor en magnetische koppeling**
8. **Spanningsverlies en kabelweerstand**
9. **Energie en rendement**
10. **Resonantie en fasoren**

---

## 💡 Tip voor AI-Anki-agent
Gebruik dit document om kaarten te genereren met:
- Automatische LaTeX-weergave voor formules
- Schema’s waar relevant (Thévenin, fasordiagrammen, ster-driehoek)
- Herhaalformuleherkenning per thema
- Cloze-kaarten voor kernformules (bijv. \( C = \frac{Q}{U} \))

---

**Doel:** alle theorie, formules en vraagtypen in dit examen kunnen herkennen, herleiden en oplossen.  
**Niveau:** HBO Energietechniek (Paul Holmes, Pearson 3e editie)

---
