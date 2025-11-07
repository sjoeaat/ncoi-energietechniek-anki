#!/usr/bin/env python3
"""
Extract exam questions from HTML oefentoets file.
Analyzes structure and content of exam-style questions.
"""

import re
from pathlib import Path
from html.parser import HTMLParser


class QuestionExtractor(HTMLParser):
    """HTML parser to extract exam questions from oefentoets."""

    def __init__(self):
        super().__init__()
        self.questions = []
        self.current_question = None
        self.in_h2 = False
        self.in_p = False
        self.in_label = False
        self.in_hint = False
        self.in_meta = False
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'h2':
            # New question starts
            if self.current_question:
                self.questions.append(self.current_question)
            self.current_question = {
                'title': '',
                'text': [],
                'options': [],
                'hints': [],
                'meta': ''
            }
            self.in_h2 = True

        elif tag == 'p':
            self.in_p = True

        elif tag == 'label':
            self.in_label = True

        elif tag == 'div':
            if attrs_dict.get('class') == 'hint':
                self.in_hint = True
            elif attrs_dict.get('class') == 'meta':
                self.in_meta = True

    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h2 = False
        elif tag == 'p':
            self.in_p = False
            if self.current_text and self.current_question:
                text = ' '.join(self.current_text).strip()
                if text and not self.in_hint:
                    self.current_question['text'].append(text)
                self.current_text = []
        elif tag == 'label':
            self.in_label = False
            if self.current_text and self.current_question:
                option = ' '.join(self.current_text).strip()
                if option:
                    self.current_question['options'].append(option)
                self.current_text = []
        elif tag == 'div':
            if self.in_hint and self.current_text:
                hint = ' '.join(self.current_text).strip()
                if hint and self.current_question:
                    self.current_question['hints'].append(hint)
                self.current_text = []
            self.in_hint = False
            self.in_meta = False

    def handle_data(self, data):
        text = data.strip()
        if not text:
            return

        if self.in_h2 and self.current_question is not None:
            self.current_question['title'] = text

        elif self.in_meta:
            if self.current_question is not None:
                self.current_question['meta'] = text

        elif self.in_p or self.in_label or self.in_hint:
            self.current_text.append(text)

    def close(self):
        # Add last question
        if self.current_question:
            self.questions.append(self.current_question)
        super().close()


def extract_question_number(title):
    """Extract question number from title."""
    match = re.match(r'Vraag (\d+)', title)
    if match:
        return int(match.group(1))
    return None


def identify_topic(title):
    """Identify topic from question title."""
    # Extract topic after — if present
    match = re.search(r'— (.+?)(?:\(|$)', title)
    if match:
        return match.group(1).strip()
    return 'Onbekend'


def identify_format(question):
    """Identify question format."""
    if question['options']:
        if any('Juist / Onjuist' in opt for opt in question['options']):
            return 'Juist/Onjuist'
        return 'Multiple choice'
    return 'Open vraag / Berekening'


def clean_text(text):
    """Clean text for markdown output."""
    # Replace HTML entities
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    # Handle subscripts and superscripts
    text = re.sub(r'<sub>(.+?)</sub>', r'_\1', text)
    text = re.sub(r'<sup>(.+?)</sup>', r'^\1', text)
    return text


def generate_markdown(questions):
    """Generate markdown analysis of questions."""
    output = []
    output.append("# Oefentoets Examenstijl - Analyse")
    output.append("")
    output.append(f"**Aantal vragen:** {len(questions)}")
    output.append("")

    # Topic overview
    topics = {}
    for q in questions:
        topic = identify_topic(q['title'])
        topics[topic] = topics.get(topic, 0) + 1

    output.append("## Onderwerpen Overzicht")
    output.append("")
    for topic, count in sorted(topics.items()):
        output.append(f"- {topic}: {count} vraag(en)")
    output.append("")
    output.append("---")
    output.append("")

    # Individual questions
    for q in questions:
        q_num = extract_question_number(q['title'])
        topic = identify_topic(q['title'])
        q_format = identify_format(q)

        output.append(f"## Examenvraag {q_num}")
        output.append(f"**Onderwerp:** {topic}")
        output.append(f"**Format:** {q_format}")
        output.append("")

        output.append("**Vraag:**")
        for text in q['text']:
            clean = clean_text(text)
            output.append(clean)
            output.append("")

        if q['options']:
            output.append("**Opties:**")
            for opt in q['options']:
                clean = clean_text(opt)
                output.append(clean)
            output.append("")

        if q['hints']:
            output.append("**Hints/Uitwerking:**")
            for hint in q['hints']:
                clean = clean_text(hint)
                output.append(clean)
            output.append("")

        output.append("**Let op:**")
        output.append("- [Te analyseren: formules, valkuilen, aandachtspunten]")
        output.append("")
        output.append("---")
        output.append("")

    return '\n'.join(output)


def main():
    # Paths
    source_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\source-materials\Oefentoets_Energietechniek_16Vragen_examenstijl_v6.html")
    output_file = Path(r"C:\Users\sjoerd.van.der.heide\Documents\GitHub\ncoi-energietechniek-anki\analysis\oefentoets-examenstijl.md")

    # Read HTML
    print(f"Reading {source_file}...")
    html_content = source_file.read_text(encoding='utf-8')

    # Parse
    print("Parsing HTML...")
    parser = QuestionExtractor()
    parser.feed(html_content)
    parser.close()

    print(f"Found {len(parser.questions)} questions")

    # Generate markdown
    print("Generating markdown...")
    markdown = generate_markdown(parser.questions)

    # Write output
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(markdown, encoding='utf-8')

    print(f"Output written to {output_file}")

    # Print summary
    print("\n=== SUMMARY ===")
    print(f"Total questions: {len(parser.questions)}")

    topics = {}
    formats = {}
    for q in parser.questions:
        topic = identify_topic(q['title'])
        q_format = identify_format(q)
        topics[topic] = topics.get(topic, 0) + 1
        formats[q_format] = formats.get(q_format, 0) + 1

    print("\nTopics:")
    for topic, count in sorted(topics.items()):
        print(f"  - {topic}: {count}")

    print("\nFormats:")
    for fmt, count in sorted(formats.items()):
        print(f"  - {fmt}: {count}")


if __name__ == '__main__':
    main()
