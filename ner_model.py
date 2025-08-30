from transformers import pipeline
import re

class NERPrivacyFilter:
    def __init__(self, model_name="dslim/bert-base-NER"):
        self.ner = pipeline("ner", model=model_name, grouped_entities=True)
        self.sg_phone_pattern = re.compile(r"\b[689]\d{7}\b")

    def detect_entities(self, text: str):
        entities = self.ner(text)
        for m in self.sg_phone_pattern.finditer(text):
            entities.append({
                "entity_group": "PHONE",
                "start": m.start(),
                "end": m.end(),
                "word": m.group()
            })
        return entities

    def redact(self, text: str, strategy="mask"):
        entities = self.detect_entities(text)
        redacted_text = text
        for ent in sorted(entities, key=lambda e: e['start'], reverse=True):
            if strategy == "mask":
                replacement = "*" * (ent['end'] - ent['start'])
            elif strategy == "tag":
                replacement = f"<{ent['entity_group']}>"
            else:
                replacement = "[REDACTED]"
            redacted_text = redacted_text[:ent['start']] + replacement + redacted_text[ent['end']:]
        return redacted_text
