# SecureScan-AI
AI-powered source code vulnerability detection system using CodeBERT + BiLSTM + MLP. Trained on BigVul, DiverseVul, and FormAI datasets. Deep Learning ESP Project - AI335L
Use this:

---

**Title:** SecureScan AI — Source Code Vulnerability Detection

**Description:**
```
# SecureScan AI 🔐

An AI-powered system for detecting security vulnerabilities in source code using Deep Learning.

## Team
- Ali Abbas Shah
- Salman Tanveer  
- Hammad Ali

## Course
AI335L Deep Learning Lab — Spring 2026

## Project Overview
SecureScan AI uses a CodeBERT + BiLSTM + MLP architecture to detect vulnerabilities in C/C++ and Python code. Trained on 600,000+ samples from BigVul, DiverseVul, and FormAI datasets.

## Results
| Model | F1 Score |
|---|---|
| Baseline MLP | 0.7346 |
| CodeBERT + BiLSTM + MLP | 0.9252 |

## Datasets
- BigVul — 188K real CVE samples
- DiverseVul — 319K C/C++ samples
- FormAI — 246K AI-generated code samples

## How to Run
```bash
git clone https://github.com/YOUR_USERNAME/SecureScan-AI
cd SecureScan-AI
pip install -r requirements.txt
python src/training/train.py
```

## Model Architecture
- CodeBERT (microsoft/codebert-base) — pretrained, freeze first 6 layers
- Bidirectional LSTM — hidden size 256, 2 layers
- MLP Classifier — 512→256→128→2

## License
MIT
```

---

Paste this as your README, create the repo, and tell me when done! 🚀
