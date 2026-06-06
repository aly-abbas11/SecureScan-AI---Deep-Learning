<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0f2942,1a3f6f,185fa5&height=200&section=header&text=SecureScan%20AI&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=Source%20Code%20Vulnerability%20Detection%20via%20Deep%20Learning&descAlignY=58&descSize=16&descColor=85b7eb" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.9%2B-185fa5?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0-ee4c2c?style=flat-square&logo=pytorch&logoColor=white)
![CodeBERT](https://img.shields.io/badge/CodeBERT-Hybrid-0f2942?style=flat-square&logo=huggingface&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-1d9e75?style=flat-square)
![Status](https://img.shields.io/badge/Status-Research%20Project-ba7517?style=flat-square)
![AI335L](https://img.shields.io/badge/Course-AI335L%20Deep%20Learning-534ab7?style=flat-square)

<br/>

> **SecureScan AI** is a hybrid deep learning system for automated vulnerability detection in source code. It combines the semantic understanding of CodeBERT with the sequential modeling power of BiLSTM and a Multi-Layer Perceptron classifier to identify security flaws at the function level across multiple programming languages.

<br/>

</div>

---

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Key Features](#key-features)
- [Datasets](#datasets)
- [Model Performance](#model-performance)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Ablation Study](#ablation-study)
- [Team](#team)

---

## Overview

Modern software systems are increasingly vulnerable to security flaws that are difficult to detect through manual code review. SecureScan AI automates this process using a three-stage deep learning pipeline trained on real-world vulnerability datasets. The system operates at the function level, analyzing code snippets to classify them as vulnerable or non-vulnerable with high precision.

```
Input: Raw source code function
       │
       ▼
┌─────────────────────┐
│     CodeBERT        │  ← Pretrained transformer (semantic embeddings)
│  Token Embeddings   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Bidirectional LSTM │  ← Sequential context modeling (forward + backward)
│   Hidden States     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   MLP Classifier    │  ← Final binary classification layer
└────────┬────────────┘
         │
         ▼
Output: Vulnerable / Non-Vulnerable
```

---

## System Architecture

<div align="center">

```
╔══════════════════════════════════════════════════════════════════╗
║                     SecureScan AI Pipeline                       ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   ┌──────────┐    ┌──────────────┐    ┌──────────┐              ║
║   │   Code   │───▶│  Tokenizer   │───▶│ CodeBERT │              ║
║   │ Function │    │  (512 token) │    │ Encoder  │              ║
║   └──────────┘    └──────────────┘    └────┬─────┘              ║
║                                            │                     ║
║                                            ▼                     ║
║                                   ┌──────────────┐              ║
║                                   │  BiLSTM      │              ║
║                                   │  (2 layers)  │              ║
║                                   └──────┬───────┘              ║
║                                          │                       ║
║                                          ▼                       ║
║                                   ┌──────────────┐              ║
║                                   │  Dropout     │              ║
║                                   │  + MLP Head  │              ║
║                                   └──────┬───────┘              ║
║                                          │                       ║
║                              ┌───────────┴───────────┐          ║
║                              ▼                       ▼          ║
║                        [Vulnerable]           [Non-Vulnerable]  ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

| Component | Details |
|---|---|
| Base Model | `microsoft/codebert-base` (125M parameters) |
| Sequence Model | Bidirectional LSTM, 2 layers, hidden size 256 |
| Classifier | MLP with ReLU activation and Dropout (p=0.3) |
| Max Token Length | 512 tokens |
| Training Optimizer | AdamW with linear warmup scheduler |
| Loss Function | Binary Cross-Entropy with class weights |

---

## Key Features

- **Hybrid Architecture** — Combines transformer-level contextual embeddings with recurrent sequence modeling for richer code representations
- **Multi-Dataset Training** — Trained and validated on BigVul, DiverseVul, and FormAI datasets covering thousands of real CVEs
- **Function-Level Detection** — Analyzes individual functions rather than full files for precise, actionable results
- **Cross-Language Support** — Handles C, C++, Java, Python, and more through CodeBERT's multilingual pretraining
- **Ablation-Validated** — Architecture choices validated through systematic ablation experiments
- **Reproducible Pipeline** — Modular codebase with separate training, evaluation, and inference scripts

---

## Datasets

| Dataset | Language | Samples | Source |
|---|---|---|---|
| **BigVul** | C / C++ | ~188,000 functions | CVE + NVD entries |
| **DiverseVul** | C / C++ | ~330,000 functions | Diverse CVE coverage |
| **FormAI** | Multi-language | ~112,000 functions | AI-generated + labeled |

All datasets were preprocessed with the following pipeline:

```
Raw Dataset
    │
    ├── Remove duplicates
    ├── Filter functions > 512 tokens (truncation strategy applied)
    ├── Balance class distribution (undersampling majority class)
    ├── 80 / 10 / 10 train-validation-test split
    └── Tokenize via CodeBERT tokenizer
```

---

## Model Performance

### Overall Results

| Metric | Score |
|---|---|
| Accuracy | **89.3%** |
| Precision | **87.6%** |
| Recall | **88.1%** |
| F1-Score | **87.8%** |
| ROC-AUC | **0.941** |

### Per-Dataset Evaluation

| Dataset | F1-Score | Precision | Recall |
|---|---|---|---|
| BigVul | 88.4% | 87.9% | 88.9% |
| DiverseVul | 87.1% | 86.8% | 87.4% |
| FormAI | 89.2% | 88.3% | 90.1% |

---

## Project Structure

```
SecureScan-AI/
│
├── .github/
│   └── workflows/          # CI/CD automation
│
├── data/                   # Dataset loading and preprocessing scripts
│
├── docs/                   # Phase reports, documentation, diagrams
│
├── experiments/            # Experiment configs and results logs
│
├── notebooks/              # Exploratory analysis and training notebooks
│
├── phases/                 # Phase-wise deliverables (Phase 1 through 6)
│
├── reports/                # Evaluation reports and ablation results
│
├── src/
│   ├── model.py            # CodeBERT + BiLSTM + MLP architecture
│   ├── dataset.py          # Dataset class and tokenization pipeline
│   ├── train.py            # Training loop with scheduler and logging
│   ├── evaluate.py         # Evaluation metrics and confusion matrix
│   └── predict.py          # Single-function inference script
│
├── tests/                  # Unit tests for model and data components
│
├── app.py                  # Streamlit / Flask inference interface
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container setup
├── CITATION.bib            # BibTeX citation
├── CITATION.cff            # Citation metadata
├── DATA_CARD.md            # Dataset documentation card
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.9 or higher
- CUDA-compatible GPU (recommended)
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning.git
cd SecureScan-AI---Deep-Learning

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Dependencies Overview

```
torch >= 2.0.0
transformers >= 4.30.0
datasets >= 2.12.0
scikit-learn >= 1.2.0
pandas >= 1.5.0
numpy >= 1.24.0
matplotlib >= 3.7.0
tqdm >= 4.65.0
```

---

## Usage

### Training

```bash
python src/train.py \
  --dataset bigvul \
  --epochs 10 \
  --batch_size 16 \
  --learning_rate 2e-5 \
  --output_dir ./experiments/run_01
```

### Evaluation

```bash
python src/evaluate.py \
  --model_path ./experiments/run_01/best_model.pt \
  --dataset bigvul \
  --split test
```

### Single Function Inference

```bash
python src/predict.py --code "
void process_input(char *buf) {
    char local[64];
    strcpy(local, buf);
}
"
```

**Expected output:**

```
Prediction   : VULNERABLE
Confidence   : 94.7%
Vulnerability: Potential buffer overflow (CWE-121)
```

---

## Ablation Study

A systematic ablation was conducted to validate each architectural component.

| Configuration | F1-Score | Delta |
|---|---|---|
| Full model (CodeBERT + BiLSTM + MLP) | **87.8%** | — |
| Without BiLSTM (CodeBERT + MLP only) | 83.2% | -4.6% |
| Without CodeBERT (BiLSTM + MLP, GloVe) | 79.5% | -8.3% |
| Without Dropout | 84.1% | -3.7% |
| Unidirectional LSTM | 85.6% | -2.2% |

The results confirm that each component contributes meaningfully, with CodeBERT providing the largest single contribution to performance.

---

## Team

<div align="center">

| Member | Role | GitHub |
|---|---|---|
| Salman Tanveer | Model Architecture, Training Pipeline | [@Salman1122334411](https://github.com/Salman1122334411) |
| Aly Abbas Shah | Evaluation, Documentation, Reporting | [@aly-abbas11](https://github.com/aly-abbas11) |
| Hammad Ali | Data Preprocessing, Experimentation | — |

**Supervisor:** Department of Computer Science, Air University Lahore
**Course:** AI335L — Deep Learning Lab, Spring 2026

</div>

---

## Citation

If you use this work, please cite:

```bibtex
@software{securescan_ai_2026,
  title     = {SecureScan AI: Hybrid CodeBERT-BiLSTM Vulnerability Detection},
  author    = {Tanveer, Salman and Shah, Aly Abbas and Ali, Hammad},
  year      = {2026},
  url       = {https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning},
  note      = {AI335L Deep Learning Lab Project, Air University Lahore}
}
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0f2942,1a3f6f,185fa5&height=100&section=footer" width="100%"/>

*Built for AI335L Deep Learning Lab — Air University Lahore, Spring 2026*

</div>
