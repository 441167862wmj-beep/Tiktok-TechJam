
from transformers import pipeline

class NERPrivacyFilter:
    def __init__(self, model_name="dslim/bert-base-NER"):
        # 加载预训练 NER pipeline
        self.ner = pipeline("ner", model=model_name, grouped_entities=True)

    def detect_entities(self, text: str):
        return self.ner(text)

    def redact(self, text: str, strategy="mask"):
        entities = self.detect_entities(text)
        redacted_text = text
        # 按偏移位置逆序替换，避免位置错乱
        for ent in sorted(entities, key=lambda e: e['start'], reverse=True):
            if strategy == "mask":
                replacement = "*" * (ent['end'] - ent['start'])
            elif strategy == "tag":
                replacement = f"<{ent['entity_group']}>"
            else:
                replacement = "[REDACTED]"
            redacted_text = redacted_text[:ent['start']] + replacement + redacted_text[ent['end']:]
        return redacted_text
