
import gradio as gr
from ner_model import NERPrivacyFilter

ner_filter = NERPrivacyFilter()

def redact_text(user_text, strategy):
    redacted = ner_filter.redact(user_text, strategy)
    return redacted

with gr.Blocks() as demo:
    gr.Markdown("## 🔒 NLP-based Privacy Filter (DistilBERT/NER)")
    with gr.Row():
        inp = gr.Textbox(label="Input Text", placeholder="Enter text with PII (names, numbers, etc.)")
        strat = gr.Radio(["mask", "tag", "redact"], value="mask", label="Redaction Strategy")
    out = gr.Textbox(label="Redacted Text")

    btn = gr.Button("Redact")
    btn.click(fn=redact_text, inputs=[inp, strat], outputs=out)

if __name__ == "__main__":
    demo.launch()
