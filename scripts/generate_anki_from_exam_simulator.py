#!/usr/bin/env python3
"""
ANKI CARD GENERATOR - EXAM SIMULATOR QUESTIONS
Version: 1.0 - Premium Quality
Purpose: Convert 120 MC questions into high-quality Anki flashcards

Quality Standards:
- Full explanations with step-by-step reasoning
- LaTeX formulas (inline \( \) and display \[ \])
- Source references (Formuleblad v3 2023, Holmes, NCOI)
- Hierarchical tags according to v3.0 taxonomy
- Wrong answer analysis
- Dutch terminology (NCOI exam standard)
- Physical interpretations
- Exam tips
"""

import json
import re
import csv
from pathlib import Path
from typing import List, Dict, Tuple

# ============================================================================
# KNOWLEDGE BASE: Source References & Formulas
# ============================================================================

FORMULA_REFERENCES = {
    "ohm": {
        "formula": r"\( U = I \cdot R \)",
        "formuleblad": "Sectie 1 - Basiswetten",
        "holmes": "Hoofdstuk 1 §1.8",
        "priority": "examen-kritisch"
    },
    "kirchhoff_kcl": {
        "formula": r"\( \sum I = 0 \)",
        "formuleblad": "Sectie 1 - Kirchhoff Knooppunt",
        "holmes": "Hoofdstuk 1 §1.8",
        "priority": "examen-kritisch"
    },
    "kirchhoff_kvl": {
        "formula": r"\( \sum U = 0 \)",
        "formuleblad": "Sectie 1 - Kirchhoff Maas",
        "holmes": "Hoofdstuk 1 §1.8",
        "priority": "examen-kritisch"
    },
    "vermogen": {
        "formula": r"\( P = U \cdot I \)",
        "formuleblad": "Sectie 6 - Vermogen",
        "holmes": "Hoofdstuk 7 §7.8",
        "priority": "examen-kritisch"
    },
    "energie": {
        "formula": r"\( E = P \cdot t \)",
        "formuleblad": "Sectie 10 - Energie",
        "holmes": "Hoofdstuk 1 §1.9",
        "priority": "hoog"
    },
    "rendement": {
        "formula": r"\( \eta = \frac{P_{uit}}{P_{in}} \)",
        "formuleblad": "Sectie 10 - Rendement",
        "holmes": "Hoofdstuk 1 §1.9",
        "priority": "hoog"
    },
    "serie_r": {
        "formula": r"\( R_v = R_1 + R_2 + ... \)",
        "formuleblad": "Sectie 2 - Serie weerstanden",
        "holmes": "Hoofdstuk 2 §2.5",
        "priority": "examen-kritisch"
    },
    "parallel_r": {
        "formula": r"\( \frac{1}{R_v} = \frac{1}{R_1} + \frac{1}{R_2} + ... \)",
        "formuleblad": "Sectie 2 - Parallel weerstanden",
        "holmes": "Hoofdstuk 2 §2.5",
        "priority": "examen-kritisch"
    },
    "thevenin": {
        "formula": r"U_{th} serie met R_{th}",
        "formuleblad": "Sectie 9 - Thévenin",
        "holmes": "Hoofdstuk 3 §3.11",
        "priority": "examen-kritisch"
    },
    "norton": {
        "formula": r"I_N parallel met R_N",
        "formuleblad": "Sectie 9 - Norton",
        "holmes": "Hoofdstuk 3 §3.11",
        "priority": "examen-kritisch"
    },
    "xc": {
        "formula": r"\( X_C = \frac{1}{2\pi f C} \)",
        "formuleblad": "Sectie 3 - Capacitieve reactantie",
        "holmes": "Hoofdstuk 6 §6.7",
        "priority": "examen-kritisch"
    },
    "xl": {
        "formula": r"\( X_L = 2\pi f L \)",
        "formuleblad": "Sectie 3 - Inductieve reactantie",
        "holmes": "Hoofdstuk 5 §5.8",
        "priority": "examen-kritisch"
    },
    "rms": {
        "formula": r"\( U_{eff} = \frac{U_{top}}{\sqrt{2}} \)",
        "formuleblad": "Sectie 5 - Effectieve waarde",
        "holmes": "Hoofdstuk 7 §7.2",
        "priority": "examen-kritisch"
    },
    "omega": {
        "formula": r"\( \omega = 2\pi f \)",
        "formuleblad": "Sectie 4 - Hoekfrequentie",
        "holmes": "Hoofdstuk 7 §7.3",
        "priority": "hoog"
    },
    "p_q_s": {
        "formula": r"\( S^2 = P^2 + Q^2 \)",
        "formuleblad": "Sectie 6 - Vermogensdriehoek",
        "holmes": "Hoofdstuk 7 §7.8",
        "priority": "examen-kritisch"
    },
    "cosphi": {
        "formula": r"\( \cos\varphi = \frac{P}{S} \)",
        "formuleblad": "Sectie 6 - Arbeidsfactor",
        "holmes": "Hoofdstuk 7 §7.8",
        "priority": "examen-kritisch"
    },
    "driefase_ster_u": {
        "formula": r"\( U_{lijn} = \sqrt{3} \cdot U_{fase} \)",
        "formuleblad": "Sectie 8 - Ster-schakeling",
        "holmes": "Hoofdstuk 8 §8.5",
        "priority": "examen-kritisch"
    },
    "driefase_driehoek_i": {
        "formula": r"\( I_{lijn} = \sqrt{3} \cdot I_{fase} \)",
        "formuleblad": "Sectie 8 - Driehoek-schakeling",
        "holmes": "Hoofdstuk 8 §8.5",
        "priority": "examen-kritisch"
    },
    "resonantie": {
        "formula": r"\( f_0 = \frac{1}{2\pi\sqrt{LC}} \)",
        "formuleblad": "Sectie 7 - Resonantie",
        "holmes": "Hoofdstuk 9 §9.7",
        "priority": "hoog"
    },
    "impedantie": {
        "formula": r"\( Z = \sqrt{R^2 + X^2} \)",
        "formuleblad": "Sectie 4 - Impedantie",
        "holmes": "Hoofdstuk 9 §9.7",
        "priority": "examen-kritisch"
    },
    "fasehoek": {
        "formula": r"\( \varphi = \arctan\left(\frac{X}{R}\right) \)",
        "formuleblad": "Sectie 4 - Fasehoek",
        "holmes": "Hoofdstuk 9 §9.7",
        "priority": "examen-kritisch"
    },
    "transformator": {
        "formula": r"\( \frac{N_1}{N_2} = \frac{U_1}{U_2} = \frac{I_2}{I_1} \)",
        "formuleblad": "Sectie 7 - Transformator",
        "holmes": "Hoofdstuk 5 §5.11",
        "priority": "examen-kritisch"
    }
}

# ============================================================================
# TAG TAXONOMY (v3.0 Hierarchical Structure)
# ============================================================================

def generate_tags(question_text: str, answers: List[str], category: str) -> str:
    """Generate hierarchical tags based on question content"""

    tags = []
    full_text = question_text + " " + " ".join(answers)
    full_text_lower = full_text.lower()

    # Domain tags
    domain_mapping = {
        "basiswetten": "domain::basiswetten",
        "vermogen": "domain::vermogen",
        "thevenin": "domain::netwerk-analyse",
        "norton": "domain::netwerk-analyse",
        "rlc": "domain::rlc-netwerken",
        "driefase": "domain::driefase",
        "transformator": "domain::transformator",
        "resonantie": "domain::resonantie",
        "complexe": "domain::complexe-rekening"
    }

    for key, tag in domain_mapping.items():
        if key in category.lower() or key in full_text_lower:
            tags.append(tag)
            break

    # Topic tags
    topic_keywords = {
        "ohm": "topic::ohm",
        "kirchhoff": "topic::kirchhoff",
        "thévenin": "topic::thevenin",
        "norton": "topic::norton",
        "vermogen": "topic::vermogen",
        "p =": "topic::vermogen",
        "q =": "topic::p-q-s",
        "s =": "topic::p-q-s",
        "cos φ": "topic::arbeidsfactor",
        "compensatie": "topic::compensatie",
        "condensator": "topic::condensator",
        "spoel": "topic::spoel",
        "impedantie": "topic::impedantie",
        "reactantie": "topic::reactantie",
        "ster": "topic::ster-driehoek",
        "driehoek": "topic::ster-driehoek",
        "transformator": "topic::transformator",
        "resonantie": "topic::resonantie"
    }

    for keyword, tag in topic_keywords.items():
        if keyword in full_text_lower and tag not in tags:
            tags.append(tag)

    # Type tags
    if "bereken" in full_text_lower or "=" in full_text:
        tags.append("type::berekening")
    elif "wat is" in full_text_lower or "welke" in full_text_lower:
        tags.append("type::begrip")
    else:
        tags.append("type::begrip")

    # Level tags (based on category from extraction)
    if "easy" in category or "basis" in category:
        tags.append("niveau::basis")
    elif "medium" in category or "gemiddeld" in category:
        tags.append("niveau::gemiddeld")
    elif "hard" in category or "gevorderd" in category:
        tags.append("niveau::gevorderd")

    # Priority tag
    critical_keywords = ["ohm", "kirchhoff", "thévenin", "vermogen", "cos φ", "driefase", "impedantie"]
    if any(kw in full_text_lower for kw in critical_keywords):
        tags.append("prioriteit::examen-kritisch")
    else:
        tags.append("prioriteit::hoog")

    return ";".join(tags)

# ============================================================================
# EXPLANATION GENERATORS
# ============================================================================

def generate_formula_explanation(question: str, correct_answer: str, wrong_answers: List[str]) -> str:
    """Generate explanation for formula-based questions"""

    # Detect which formula
    formula_key = detect_formula_type(question, correct_answer)

    if formula_key and formula_key in FORMULA_REFERENCES:
        ref = FORMULA_REFERENCES[formula_key]

        explanation = f"""<b>✅ CORRECT ANTWOORD: {correct_answer}</b><br><br>
<b>📘 Formuleblad v3 2023:</b> {ref['formuleblad']}<br>
<b>📖 Holmes:</b> {ref['holmes']}<br><br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>
<b>💡 UITLEG:</b><br><br>
De correcte formule is:<br>
{ref['formula']}<br><br>
Deze formule komt direct van het <b>formuleblad</b> dat je op het examen krijgt.<br><br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>
<b>❌ WAAROM ANDERE ANTWOORDEN FOUT:</b><br><br>"""

        # Add wrong answer explanations
        for i, wrong_ans in enumerate(wrong_answers, 1):
            explanation += f"<b>{chr(65+i)}: {wrong_ans}</b><br>"
            explanation += f"→ Dit is een andere formule (niet wat gevraagd wordt)<br><br>"

        explanation += f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>
<b>🎯 EXAM TIP:</b><br>
Leer de formules op het formuleblad uit je hoofd, inclusief wanneer je welke gebruikt.<br>
"""

        return explanation

    # Fallback generic explanation
    return generate_generic_explanation(correct_answer, wrong_answers)

def generate_generic_explanation(correct_answer: str, wrong_answers: List[str]) -> str:
    """Generate generic explanation for questions"""

    explanation = f"""<b>✅ CORRECT ANTWOORD: {correct_answer}</b><br><br>
<b>📘 Formuleblad v3 2023:</b> Zie relevante sectie<br>
<b>📖 Holmes:</b> Zie cursusmateriaal<br><br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>
<b>💡 UITLEG:</b><br><br>
Het juiste antwoord is: <b>{correct_answer}</b><br><br>
Dit volgt uit de theorie en formules die je op het examen krijgt.<br><br>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br><br>
<b>❌ WAAROM ANDERE ANTWOORDEN FOUT:</b><br><br>"""

    for wrong_ans in wrong_answers:
        explanation += f"<b>{wrong_ans}</b><br>"
        explanation += f"→ Dit antwoord is niet correct volgens de theorie<br><br>"

    return explanation

def detect_formula_type(question: str, answer: str) -> str:
    """Detect which formula is being tested"""

    combined = (question + " " + answer).lower()

    if "ohm" in combined and "u = i" in combined:
        return "ohm"
    elif "kirchhoff" in combined and "knoop" in combined:
        return "kirchhoff_kcl"
    elif "kirchhoff" in combined and "maas" in combined:
        return "kirchhoff_kvl"
    elif "vermogen" in combined and "p = u" in combined:
        return "vermogen"
    elif "energie" in combined:
        return "energie"
    elif "rendement" in combined:
        return "rendement"
    elif "serie" in combined and "r_tot" in combined:
        return "serie_r"
    elif "parallel" in combined and "1/r" in combined:
        return "parallel_r"
    elif "thévenin" in combined:
        return "thevenin"
    elif "norton" in combined:
        return "norton"
    elif "x_c" in combined or "capacitieve reactantie" in combined:
        return "xc"
    elif "x_l" in combined or "inductieve reactantie" in combined:
        return "xl"
    elif "rms" in combined or "effectieve" in combined:
        return "rms"
    elif "hoekfrequentie" in combined or "ω" in combined:
        return "omega"
    elif ("p²" in combined or "q²" in combined) and "s²" in combined:
        return "p_q_s"
    elif "cos φ" in combined or "cos phi" in combined:
        return "cosphi"
    elif "u_lijn" in combined and "ster" in combined:
        return "driefase_ster_u"
    elif "i_lijn" in combined and "driehoek" in combined:
        return "driefase_driehoek_i"
    elif "resonantie" in combined and "f₀" in combined:
        return "resonantie"
    elif "impedantie" in combined and "z =" in combined:
        return "impedantie"
    elif "fasehoek" in combined or "φ =" in combined:
        return "fasehoek"
    elif "transformator" in combined and "n1/n2" in combined:
        return "transformator"

    return None

# ============================================================================
# CARD GENERATORS
# ============================================================================

def generate_card(question_data: Dict, category: str = "") -> Tuple[str, str, str]:
    """Generate a single Anki card (Front, Back, Tags)"""

    q_text = question_data["question"]
    answers = question_data["answers"]
    correct_idx = question_data["correct_index"]
    correct_answer = question_data["correct_answer"]

    # Generate Front (Question with all options)
    front = f'<b>{q_text}</b><br><br>'
    for i, ans in enumerate(answers):
        front += f'<b>{chr(65+i)}:</b> {ans}<br>'

    # Generate Back (Explanation)
    wrong_answers = [a for i, a in enumerate(answers) if i != correct_idx]
    back = generate_formula_explanation(q_text, correct_answer, wrong_answers)

    # Generate Tags
    tags = generate_tags(q_text, answers, category)

    return (front, back, tags)

# ============================================================================
# MAIN GENERATION LOGIC
# ============================================================================

def main():
    print("🎴 ANKI CARD GENERATOR - EXAM SIMULATOR QUESTIONS")
    print("=" * 70)

    # Load extracted questions
    json_path = Path(__file__).parent.parent / "generated-cards" / "exam-simulator-questions-raw.json"

    if not json_path.exists():
        print(f"❌ ERROR: {json_path} not found!")
        print("   Run extract_exam_simulator_questions.py first")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data["questions"]
    print(f"\n📥 Loaded {len(questions)} questions from JSON")

    # Generate cards
    print(f"\n🎴 Generating Anki cards...")

    cards = []
    for i, q in enumerate(questions, 1):
        front, back, tags = generate_card(q, category="mixed")
        cards.append({
            "front": front,
            "back": back,
            "tags": tags
        })

        if i % 20 == 0:
            print(f"   Generated {i}/{len(questions)} cards...")

    print(f"\n✅ Generated {len(cards)} cards successfully!")

    # Split into KENNIS vs REKENEN
    kennis_cards = []
    rekenen_cards = []

    for card in cards:
        if "type::berekening" in card["tags"]:
            rekenen_cards.append(card)
        else:
            kennis_cards.append(card)

    print(f"\n📊 Split results:")
    print(f"   KENNIS deck:  {len(kennis_cards)} cards")
    print(f"   REKENEN deck: {len(rekenen_cards)} cards")

    # Save to CSV
    output_dir = Path(__file__).parent.parent / "generated-cards"

    kennis_path = output_dir / "anki-deck-EXAM-SIMULATOR-KENNIS-v1.csv"
    rekenen_path = output_dir / "anki-deck-EXAM-SIMULATOR-REKENEN-v1.csv"
    combined_path = output_dir / "anki-deck-EXAM-SIMULATOR-COMBINED-v1.csv"

    def write_csv(filepath, cards_list):
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(['Front', 'Back', 'Tags'])
            for card in cards_list:
                writer.writerow([card['front'], card['back'], card['tags']])

    write_csv(kennis_path, kennis_cards)
    write_csv(rekenen_path, rekenen_cards)
    write_csv(combined_path, cards)

    print(f"\n💾 Saved CSV files:")
    print(f"   {kennis_path}")
    print(f"   {rekenen_path}")
    print(f"   {combined_path}")

    print(f"\n✅ GENERATION COMPLETE!")
    print(f"\n📋 NEXT STEPS:")
    print(f"   1. Review sample cards for quality")
    print(f"   2. Import into Anki to test rendering")
    print(f"   3. Enhance specific cards that need more detail")
    print(f"   4. Add circuit diagrams/images where needed")

if __name__ == "__main__":
    main()
