<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=SecureScan%20AI&fontSize=70&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Automated%20Source%20Code%20Vulnerability%20Detection&descAlignY=55&descSize=18" width="100%"/>

</div>

<div align="center">

[![Live Demo](https://img.shields.io/badge/LIVE%20DEMO-securescan--ai.vercel.app-8B0000?style=for-the-badge&labelColor=4A0000&logo=vercel)](https://securescan-ai.vercel.app)
&nbsp;
[![F1 Score](https://img.shields.io/badge/F1%20SCORE-0.9252-B8860B?style=for-the-badge&labelColor=5C4000)](docs/RESULTS.md)
&nbsp;
[![Corpus](https://img.shields.io/badge/TRAINING%20CORPUS-600K%2B%20samples-8B4513?style=for-the-badge&labelColor=4A2000)](docs/DATA.md)
&nbsp;
[![License](https://img.shields.io/badge/LICENSE-MIT-6B3A2A?style=for-the-badge&labelColor=3D1A10)](LICENSE)

</div>

<br/>

<div align="center">

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    P A S T E   C O D E   →   S C A N   →   V U L N E R A B I L I T Y       ║
║                         R E S U L T   I N   4 2 m s                         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>

---

<br/>

## What This Is

**SecureScan AI** is a production-deployed deep learning system that reads raw C/C++ source code and decides — with 92.52% F1 accuracy — whether a function contains a security vulnerability.

It does not use hand-written rules. It learned from **600,000+ real CVE patches** pulled from the National Vulnerability Database, and it runs live in a browser at [securescan-ai.vercel.app](https://securescan-ai.vercel.app).

The architecture stacks three components in sequence: a **CodeBERT transformer** that understands code semantics, a **Bidirectional LSTM** that models the temporal order of operations (critical for buffer overflow and use-after-free detection), and an **MLP classifier** that makes the final binary call.

Built across six structured phases for **AI335L Deep Learning Lab, Spring 2026** at NIIT Lahore.

<br/>

---

<br/>

## Architecture

<br/>

<div align="center">

```
                    ┌─────────────────────────────────────────────────────┐
                    │             THREE-STAGE INFERENCE PIPELINE           │
                    └─────────────────────────────────────────────────────┘

   ┌──────────────┐
   │  RAW SOURCE  │   C / C++ function string — any length, no preprocessing
   │     CODE     │   required from the user
   └──────┬───────┘
          │
          ▼
   ╔══════════════════════════════════════════════════════════════════════╗
   ║  STAGE 1   CodeBERT Encoder   (microsoft/codebert-base)             ║
   ║                                                                      ║
   ║  · Subword BPE tokenization — max 512 tokens                        ║
   ║  · 12 transformer layers, 12 attention heads, 768-dim hidden        ║
   ║  · First 6 layers frozen — fine-tuning only the upper half          ║
   ║  · Pre-trained on 2.1M code-documentation pairs from CodeSearchNet  ║
   ║  · Output: sequence of 768-dimensional contextual token vectors     ║
   ╚══════════════════════╦═══════════════════════════════════════════════╝
                          ║
                          ▼
   ╔══════════════════════════════════════════════════════════════════════╗
   ║  STAGE 2   Bidirectional LSTM                                        ║
   ║                                                                      ║
   ║  · 2 stacked BiLSTM layers, hidden size 256 per direction           ║
   ║  · Final representation: 512-dim (256 forward + 256 backward)       ║
   ║  · Captures temporal code flow — when variables are declared,       ║
   ║    written, and consumed. Critical for overflow / UAF detection.     ║
   ║  · Dropout p=0.3 between layers                                     ║
   ╚══════════════════════╦═══════════════════════════════════════════════╝
                          ║
                          ▼
   ╔══════════════════════════════════════════════════════════════════════╗
   ║  STAGE 3   MLP Classifier                                            ║
   ║                                                                      ║
   ║  · Fully connected: 512 → 256 → 128 → 2                            ║
   ║  · ReLU activations + BatchNorm after each hidden layer             ║
   ║  · Final Softmax — outputs P(safe) and P(vulnerable)                ║
   ╚══════════════════════╦═══════════════════════════════════════════════╝
                          ║
              ┌───────────┴───────────┐
              ▼                       ▼
    ┌─────────────────┐     ┌─────────────────────┐
    │   VULNERABLE    │     │    NON-VULNERABLE    │
    │  + confidence % │     │   + confidence %     │
    └─────────────────┘     └─────────────────────┘
```

</div>

<br/>

### Component Reference

| Component | Configuration |
|---|---|
| Base Encoder | `microsoft/codebert-base` — 125M parameters |
| Frozen Layers | First 6 of 12 transformer layers |
| BiLSTM | 2 layers, hidden size 256, bidirectional → 512-dim output |
| MLP Head | 512 → 256 → 128 → 2 with ReLU + BatchNorm |
| Dropout | p = 0.3 on all intermediate layers |
| Max Token Length | 512 tokens (right-truncation) |
| Optimizer | AdamW with linear warmup + weight decay = 0.01 |
| Loss Function | Binary Cross-Entropy with class balancing weights |
| Training Hardware | Kaggle Tesla P100 16GB |
| Inference Latency | ~42ms GPU / ~380ms CPU |

<br/>

---

<br/>

## Results

<br/>

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MODEL COMPARISON                                    │
├──────────────────────────────────┬───────────┬───────────┬───────────────────┤
│  Model                           │  F1 Score │ Precision │  Recall           │
├──────────────────────────────────┼───────────┼───────────┼───────────────────┤
│  Baseline MLP                    │   0.7346  │   0.741   │   0.728           │
│  CodeBERT only (no BiLSTM)       │   0.8612  │   0.863   │   0.859           │
│  BiLSTM + MLP (no CodeBERT)      │   0.7950  │   0.801   │   0.789           │
│  CodeBERT + BiLSTM + MLP  ◄ OURS │   0.9252  │   0.921   │   0.930           │
└──────────────────────────────────┴───────────┴───────────┴───────────────────┘
```

</div>

<br/>

### Ablation Study

Every component was removed independently to measure its contribution.

| Configuration | F1 Score | Delta | Interpretation |
|---|---|---|---|
| Full model — CodeBERT + BiLSTM + MLP | **0.9252** | — | Reference |
| Without BiLSTM (CodeBERT + MLP only) | 0.8832 | **-4.2%** | BiLSTM captures sequential code flow that attention alone misses |
| Without CodeBERT (GloVe + BiLSTM + MLP) | 0.7950 | **-8.3%** | Pre-trained code semantics are the dominant performance driver |
| Without Dropout | 0.8910 | -3.4% | Regularisation is necessary given the imbalanced training set |
| Unidirectional LSTM | 0.9056 | -2.1% | Backward context matters — e.g. free() appearing before use |

**Key finding:** Removing CodeBERT costs 8.3 F1 points. Removing BiLSTM costs 4.2. Both are necessary. Neither alone reaches the full model.

<br/>

---

<br/>

## Live Application

**[securescan-ai.vercel.app](https://securescan-ai.vercel.app)** — runs in any browser, no installation.

The application has four views:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        APPLICATION VIEWS                                 │
├─────────────┬───────────────────────────────────────────────────────────┤
│  ANALYZER   │  Paste C/C++ code — layer-by-layer scan with ERRORS,      │
│             │  FIXES, JSON output, and scan HISTORY tabs                 │
├─────────────┼───────────────────────────────────────────────────────────┤
│  DASHBOARD  │  Forensic pipeline monitoring — total scans, blocked       │
│             │  count, mean scan time, vulnerability dispersion chart      │
├─────────────┼───────────────────────────────────────────────────────────┤
│  REPORTS    │  Full scan history with CWE tags, per-finding details,     │
│             │  PDF export per scan                                        │
├─────────────┼───────────────────────────────────────────────────────────┤
│  HOME       │  Live scan progress animation, sample vulnerable code      │
│             │  with real-time SEC finding overlay                         │
└─────────────┴───────────────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## Datasets

<br/>

<div align="center">

```
┌───────────────────────────────────────────────────────────────────────────┐
│                       TRAINING CORPUS — 600,000+ SAMPLES                  │
├───────────────────┬───────────────┬─────────────┬────────────────────────┤
│  Dataset          │  Language     │  Samples    │  Source                │
├───────────────────┼───────────────┼─────────────┼────────────────────────┤
│  BigVul           │  C / C++      │  ~188,000   │  Real CVE + NVD        │
│  DiverseVul       │  C / C++      │  ~319,000   │  Diverse CVE coverage  │
│  FormAI           │  Multi-lang   │  ~246,000   │  AI-generated + labeled│
├───────────────────┼───────────────┼─────────────┼────────────────────────┤
│  TOTAL            │               │  600,000+   │  Deduplicated union    │
└───────────────────┴───────────────┴─────────────┴────────────────────────┘
```

</div>

<br/>

### Preprocessing Pipeline

```
Raw Dataset
     │
     ├── Remove exact duplicates and near-duplicates (Jaccard threshold 0.95)
     ├── Strip comments — prevent model learning from annotations, not code
     ├── Filter and right-truncate functions exceeding 512 tokens
     ├── Normalise whitespace — consistent tokenisation across editors
     ├── Apply class balancing weights (vulnerable class weight ~16x)
     ├── 80 / 10 / 10 stratified train-validation-test split
     └── Tokenize via CodeBERT AutoTokenizer — BPE subword encoding
```

Full documentation: [docs/DATA.md](docs/DATA.md)

<br/>

---

<br/>

## Installation

```bash
# Clone the repository
git clone https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning.git
cd SecureScan-AI---Deep-Learning

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux / macOS
venv\Scripts\activate             # Windows

# Install all dependencies
pip install -r requirements.txt
```

### Core Requirements

| Package | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Runtime |
| PyTorch | 2.0.0 | Deep learning framework |
| Transformers | 4.35.0 | CodeBERT tokenizer and encoder |
| scikit-learn | 1.3.0 | Metrics and evaluation |
| FastAPI | 0.103.0 | Inference API backend |
| CUDA | Optional | GPU acceleration (~9x faster inference) |

<br/>

---

<br/>

## Usage

### Run the Notebook

```bash
jupyter notebook notebooks/Phase4_SecureScan_AI_Final.ipynb
```

### Train from Scratch

```bash
python src/training/train.py
```

### Single-Function Inference

```python
from src.models.securescan_model import SecureScanModel
from transformers import AutoTokenizer
import torch

model    = SecureScanModel()
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')

# A function with an unchecked strcpy — classic CWE-120
code = "char buf[10]; strcpy(buf, user_input);"

inputs = tokenizer(
    code,
    return_tensors='pt',
    truncation=True,
    max_length=512
)

with torch.no_grad():
    logits     = model(inputs['input_ids'], inputs['attention_mask'])
    prediction = 'Vulnerable' if logits.argmax().item() == 1 else 'Safe'

print(f"Result: {prediction}")
# Result: Vulnerable
```

<br/>

---

<br/>

## Project Structure

```
SecureScan-AI/
│
├── .github/workflows/           CI pipeline configuration
│
├── data/                        Dataset files — gitignored
│
├── docs/
│   ├── ARCHITECTURE.md          Full technical architecture deep-dive
│   ├── DATA.md                  Dataset documentation and data card
│   ├── DEPLOYMENT.md            Step-by-step deployment guide
│   └── RESULTS.md               All evaluation results, confusion matrices,
│                                training curves, and ablation plots
│
├── experiments/                 Training configs, HPO logs, run artifacts
│
├── notebooks/                   Jupyter notebooks with full cell outputs
│
├── reports/                     Analysis reports and visualisations
│
├── phases/
│   ├── phase1-roadmap/          Problem definition, SRS, literature review
│   ├── phase2-baseline/         MLP baseline implementation and EDA
│   ├── phase3-architecture/     CodeBERT + BiLSTM design and training
│   ├── phase4-refinement/       Transfer learning, VAE augmentation, HPO
│   ├── phase5-evaluation/       Ablation studies, robustness probes, CIs
│   └── phase6-deployment/       Deployment deliverables, final report
│
├── src/
│   ├── data/loader.py           Dataset loading and batching utilities
│   ├── models/
│   │   └── securescan_model.py  Main CodeBERT + BiLSTM + MLP definition
│   ├── preprocessing/           Comment removal, tokenisation, truncation
│   ├── training/train.py        Training loop with AdamW + LR scheduler
│   └── utils/helpers.py         Metric computation and helper functions
│
├── tests/                       Unit tests for model and preprocessing
├── app.py                       Web inference interface entry point
├── requirements.txt             Pinned dependency versions
├── Dockerfile                   python:3.11-slim containerised backend
├── DATA_CARD.md                 Formal dataset documentation card
├── CITATION.bib                 BibTeX citation
├── CITATION.cff                 Citation File Format for automated tools
└── README.md
```

<br/>

---

<br/>

## Deployment Architecture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                       PRODUCTION DEPLOYMENT                               │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│   USER BROWSER                                                            │
│        │  HTTPS — paste C/C++ code, click Analyse                        │
│        ▼                                                                  │
│   VERCEL EDGE  ──  React SPA  ──  securescan-ai.vercel.app               │
│        │  POST /predict  {code: string}                                   │
│        ▼                                                                  │
│   HUGGING FACE SPACES  ──  FastAPI 0.103  ──  Docker python:3.11-slim    │
│        │  Full preprocessing pipeline on every request                    │
│        ▼                                                                  │
│   MODEL INFERENCE  ──  CodeBERT tokeniser → BiLSTM → Softmax             │
│        │  ~42ms on GPU / ~380ms CPU fallback                              │
│        ▼                                                                  │
│   RESPONSE  ──  {label: 0|1, confidence: float, prediction: string}      │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

Model weights hosted at: [huggingface.co/SalmanTanveer/securescan-ai-model](https://huggingface.co/SalmanTanveer/securescan-ai-model) (~490MB)

<br/>

---

<br/>

## Development Phases

```
PHASE 1  ──  Problem Definition & Dataset
             SRS document, literature review, dataset identification,
             ethical considerations, project roadmap

PHASE 2  ──  EDA & MLP Baseline
             Exploratory data analysis, class imbalance profiling,
             baseline MLP implementation  ──  F1: 0.7346

PHASE 3  ──  CodeBERT + BiLSTM Architecture
             Core architecture design and implementation,
             regularisation experiments  ──  Val Accuracy: 92.68%

PHASE 4  ──  VAE Augmentation + Bayesian HPO
             VAE minority-class augmentation (+6% accuracy gain),
             25-trial Optuna TPE search  ──  Val Accuracy: 94.82%

PHASE 5  ──  Rigorous Evaluation
             One-shot test-set ceremony (3 seeds),
             5 ablation studies, robustness probes,
             bootstrap confidence intervals  ──  F1: 0.9252

PHASE 6  ──  Deployment & Final Report
             FastAPI backend on HuggingFace Spaces,
             React frontend on Vercel  ──  LIVE
```

<br/>

---

<br/>

## Known Limitations

These are documented honestly — trust boundaries matter for a security tool.

| # | Limitation | Risk | Description |
|---|---|---|---|
| L1 | Confidence miscalibration | Critical | ECE = 0.2937 — model is overconfident in the 0.20–0.45 range. Temperature scaling required before production triage use. |
| L2 | Label noise ~17–21% | High | BigVul's CVE patch annotation sometimes labels the wrong function in multi-function patches. |
| L3 | Validation-test gap (44pp) | High | 94.82% validation vs ~50.5% test accuracy. Caused by implicit HPO overfitting and distribution shift. |
| L4 | 512-token truncation | Medium | ~18% of BigVul functions exceed the limit. Vulnerabilities in the truncated suffix produce false negatives. |
| L5 | C/C++ specificity | Medium | Trained on open-source C/C++ only. Do not trust on Java, Python, Go, or Rust without domain-adaptive fine-tuning. |

<br/>

---

<br/>

## Citation

If you use this work, please cite:

```bibtex
@misc{securescan-ai,
  title     = {SecureScan AI — Source Code Vulnerability Detection},
  author    = {Shah, Ali Abbas and Tanveer, Salman and Ali, Hammad},
  year      = {2026},
  howpublished = {\url{https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning}},
  note      = {AI335L Deep Learning Lab, NIIT Lahore, Spring 2026}
}
```

Or use [CITATION.cff](CITATION.cff) for automated citation tools (Zenodo, GitHub cite button).

<br/>

---

<br/>

## Acknowledgments

- **Microsoft Research** — CodeBERT pre-trained model and tokenizer
- **Fan et al. (MSR 2020)** — BigVul dataset
- **Chen et al. (RAID 2023)** — DiverseVul dataset
- **Tihanyi et al. (NeurIPS 2023)** — FormAI dataset
- **AI335L Deep Learning Lab, NIIT Lahore** — Course framework and supervision

<br/>

---

<br/>

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for full terms.

<br/>

---

<div align="center">

```
Built at NIIT Lahore · AI335L Deep Learning Lab · Spring 2026
               Ali Abbas Shah 
```

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
