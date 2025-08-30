
---

# 🔒 AI Privacy NER Demo

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)](https://huggingface.co/transformers/)
[![Gradio](https://img.shields.io/badge/UI-Gradio-green.svg)](https://gradio.app/)

## 📌 Relevant Problem Statement

This project addresses **Problem Statement 1: Prevent Privacy Leakage in Using Generative AI**, focusing on **PII detection in prompts**.

Our solution prevents sensitive user information (names, phone numbers, organizations, etc.) from leaking when users interact with cloud-based LLM services.

---

## ✨ Features

* ✅ Detects **PII (names, orgs, numbers, locations, etc.)** in text using Hugging Face NER model
* ✅ Provides **3 redaction strategies**:

  * **Mask** → `*****`
  * **Tag** → `<PER>`, `<ORG>` …
  * **Redact** → `[REDACTED]`
* ✅ Works **fully offline / on-device**
* ✅ Clean **Gradio Web UI** for easy testing

---

## 📺 Demo Video

🎥 Watch the demo on YouTube:
👉 [Demo Video Link](在这里放你的 YouTube 链接)

*(Less than 3 minutes, showing redaction in action.)*

---

## 🛠 Development Tools

* **Language**: Python 3.10+
* **IDE**: VSCode / PyCharm
* **Version Control**: Git & GitHub

---

## 🔗 APIs & Assets

* Hugging Face Transformers: [`dslim/bert-base-NER`](https://huggingface.co/dslim/bert-base-NER)
* Assets: synthetic test prompts with names, IDs, and other PII

---

## 📚 Libraries Used

```txt
transformers
torch
gradio
```

---

## 🚀 Getting Started

Clone the repo and run locally:

```bash
git clone https://github.com/<your-team-name>/ai-privacy-ner-demo.git
cd ai-privacy-ner-demo

pip install -r requirements.txt
python app.py
```

Open your browser at [http://127.0.0.1:7860](http://127.0.0.1:7860).

---

## 📂 Deliverables

1. ✅ Functional Prototype
2. ✅ Project Code (open source)
3. ✅ README with features & problem statement
4. ✅ GitHub Repository (this repo)
5. ✅ Demo Video (linked above)

---

## 🔮 Future Work

* Fine-tune with **synthetic PII datasets** (phone numbers, credit cards, etc.)
* Extend to **image privacy protection** (photo gallery blurring, location masking)
* Integrate with **LLM proxy middleware** for safe cloud usage

---

📧 Questions? Contact: `<441167862@qq.com>`

---

