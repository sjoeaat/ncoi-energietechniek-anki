#!/usr/bin/env python3
"""
Extract questions from EXAM-SIMULATOR.html and prepare for Anki conversion
Version: 1.0
Purpose: Parse 125 MC questions, categorize, and structure for Anki flashcard generation
"""

import json
import re
from pathlib import Path

def parse_exam_simulator_questions():
    """Extract all questions from EXAM-SIMULATOR.html JavaScript"""

    html_path = Path(__file__).parent.parent / "study-guide" / "EXAM-SIMULATOR.html"

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the questionDatabase JavaScript object
    # Pattern: { q: "...", a: [...], correct: N }
    pattern = r'\{\s*q:\s*"([^"]+)",\s*a:\s*\[([^\]]+)\],\s*correct:\s*(\d+)\s*\}'

    matches = re.findall(pattern, content, re.DOTALL)

    questions = []

    for match in matches:
        question_text = match[0]
        answers_str = match[1]
        correct_index = int(match[2])

        # Parse answers array
        answers = re.findall(r'"([^"]+)"', answers_str)

        questions.append({
            "question": question_text,
            "answers": answers,
            "correct_index": correct_index,
            "correct_answer": answers[correct_index] if correct_index < len(answers) else None
        })

    return questions

def categorize_questions(questions):
    """Categorize questions by topic/domain based on content keywords"""

    categories = {
        "basiswetten": {
            "keywords": ["Ohm", "Kirchhoff", "KCL", "KVL", "serie", "parallel", "knooppunt", "maas"],
            "questions": []
        },
        "vermogen": {
            "keywords": ["vermogen", "Watt", "energie", "Joule", "rendement", "P =", "E ="],
            "questions": []
        },
        "thevenin_norton": {
            "keywords": ["Thévenin", "Norton", "U_th", "I_N", "R_th", "equivalent", "vermogensaanpassing"],
            "questions": []
        },
        "rlc_componenten": {
            "keywords": ["condensator", "spoel", "reactantie", "X_C", "X_L", "inductie", "capaciteit"],
            "questions": []
        },
        "ac_begrippen": {
            "keywords": ["RMS", "effectieve", "sinusgolf", "frequentie", "Hz", "hoekfrequentie", "ijlt"],
            "questions": []
        },
        "vermogen_ac": {
            "keywords": ["werkzaam", "blind", "schijnbaar", "cos φ", "arbeidsfactor", "compensatie", "P/Q/S"],
            "questions": []
        },
        "driefase": {
            "keywords": ["driefase", "ster", "driehoek", "lijn", "fase", "√3", "120°", "nulleider"],
            "questions": []
        },
        "resonantie": {
            "keywords": ["resonantie", "f₀", "X_L = X_C", "kwaliteitsfactor", "bandbreedte", "filter"],
            "questions": []
        },
        "complexe_rekening": {
            "keywords": ["impedantie", "Z =", "φ", "fasehoek", "complex", "jX", "arctan", "arg"],
            "questions": []
        },
        "transformator": {
            "keywords": ["transformator", "wikkel", "N1/N2", "koppelfactor", "hysterese", "kern"],
            "questions": []
        },
        "magnetisme": {
            "keywords": ["flux", "toroïde", "magnetisch", "zelfinductie", "di/dt", "φ"],
            "questions": []
        },
        "praktijk": {
            "keywords": ["hoogspanning", "transmissie", "skin-effect", "zonnepaneel", "kabel", "spanningsverlies"],
            "questions": []
        }
    }

    categorized = {cat: [] for cat in categories}
    uncategorized = []

    for q in questions:
        full_text = q["question"] + " " + " ".join(q["answers"])
        matched = False

        for category, data in categories.items():
            for keyword in data["keywords"]:
                if keyword.lower() in full_text.lower():
                    categorized[category].append(q)
                    matched = True
                    break
            if matched:
                break

        if not matched:
            uncategorized.append(q)

    return categorized, uncategorized

def analyze_questions(questions):
    """Analyze question distribution and complexity"""

    stats = {
        "total": len(questions),
        "by_difficulty": {
            "easy": 0,
            "medium": 0,
            "hard": 0
        },
        "needs_calculation": 0,
        "needs_image": 0,
        "formula_questions": 0
    }

    # Heuristics for complexity
    for q in questions:
        full_text = q["question"] + " " + " ".join(q["answers"])

        # Check if calculation needed
        if any(keyword in full_text for keyword in ["Bereken", "bereken", "=", "µA", "kΩ", "mH", "kW", "MWh"]):
            stats["needs_calculation"] += 1

        # Check if image would help
        if any(keyword in full_text for keyword in ["netwerk", "schakeling", "circuit", "diagram", "driehoek", "ster"]):
            stats["needs_image"] += 1

        # Check if formula question
        if "=" in full_text or "×" in full_text or "/" in full_text:
            stats["formula_questions"] += 1

    return stats

def main():
    print("🔍 EXAM SIMULATOR QUESTIONS EXTRACTOR")
    print("=" * 60)

    # Extract questions
    print("\n📥 Extracting questions from EXAM-SIMULATOR.html...")
    questions = parse_exam_simulator_questions()
    print(f"✅ Extracted {len(questions)} questions")

    # Categorize
    print("\n📊 Categorizing questions by domain...")
    categorized, uncategorized = categorize_questions(questions)

    print("\n📈 Distribution by category:")
    total_categorized = 0
    for category, qs in categorized.items():
        if qs:
            print(f"  {category:20s}: {len(qs):3d} questions")
            total_categorized += len(qs)

    print(f"\n  {'TOTAL CATEGORIZED':20s}: {total_categorized:3d}")
    print(f"  {'Uncategorized':20s}: {len(uncategorized):3d}")

    # Analyze
    print("\n🔬 Analyzing question complexity...")
    stats = analyze_questions(questions)

    print(f"\n  Total questions:        {stats['total']}")
    print(f"  Needs calculation:      {stats['needs_calculation']} ({stats['needs_calculation']/stats['total']*100:.1f}%)")
    print(f"  Needs image:            {stats['needs_image']} ({stats['needs_image']/stats['total']*100:.1f}%)")
    print(f"  Formula questions:      {stats['formula_questions']} ({stats['formula_questions']/stats['total']*100:.1f}%)")

    # Save to JSON
    output_path = Path(__file__).parent.parent / "generated-cards" / "exam-simulator-questions-raw.json"
    output_path.parent.mkdir(exist_ok=True)

    output_data = {
        "metadata": {
            "total_questions": len(questions),
            "extraction_date": "2025-11-09",
            "source_file": "study-guide/EXAM-SIMULATOR.html"
        },
        "questions": questions,
        "categorized": {k: [q["question"] for q in v] for k, v in categorized.items()},
        "statistics": stats
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Saved structured data to: {output_path}")
    print("\n✅ Extraction complete!")
    print("\n📋 NEXT STEPS:")
    print("  1. Review categorization accuracy")
    print("  2. Create full explanations for each question")
    print("  3. Add LaTeX formulas and Dutch terminology")
    print("  4. Verify against Formuleblad v3 2023")
    print("  5. Generate Anki CSV files")

if __name__ == "__main__":
    main()
