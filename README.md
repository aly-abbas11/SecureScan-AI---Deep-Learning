<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0a1628,0f2942,185fa5,378add&height=220&section=header&text=SecureScan%20AI&fontSize=60&fontColor=ffffff&fontAlignY=40&desc=AI-Powered%20Source%20Code%20Vulnerability%20Detection&descAlignY=60&descSize=17&descColor=85b7eb&animation=fadeIn" width="100%"/>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-185fa5?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-2.0-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/CodeBERT-Microsoft-0f2942?style=for-the-badge&logo=microsoft&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-1d9e75?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Course-AI335L%20Deep%20Learning-534ab7?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Accuracy-89.3%25-ba7517?style=for-the-badge"/>
</p>

<br/>

<p align="center">
  <a href="https://securescan-ai.vercel.app">
    <img src="https://img.shields.io/badge/LIVE%20DEMO-%E2%86%92%20Try%20SecureScan%20AI-185fa5?style=for-the-badge&logo=vercel&logoColor=white"/>
  </a>
</p>

<br/>

<table>
<tr>
<td align="center" width="200">
<img src="https://img.shields.io/badge/600K%2B-Samples%20Trained-0f2942?style=flat-square" /><br/>
<sub>BigVul + DiverseVul + FormAI</sub>
</td>
<td align="center" width="200">
<img src="https://img.shields.io/badge/92.5%25-F1%20Score-1d9e75?style=flat-square" /><br/>
<sub>CodeBERT + BiLSTM + MLP</sub>
</td>
<td align="center" width="200">
<img src="https://img.shields.io/badge/3%20Stage-Deep%20Pipeline-534ab7?style=flat-square" /><br/>
<sub>Transformer → Recurrent → Classifier</sub>
</td>
<td align="center" width="200">
<img src="https://img.shields.io/badge/6%20Phases-Research%20Project-ba7517?style=flat-square" /><br/>
<sub>Planning through Deployment</sub>
</td>
</tr>
</table>

</div>

---

## What is SecureScan AI

SecureScan AI is a hybrid deep learning system that automatically detects security vulnerabilities in source code at the function level. By combining the semantic power of Microsoft's CodeBERT transformer with Bidirectional LSTM sequence modeling and an MLP classifier, it achieves state-of-the-art detection accuracy across C, C++, Java, and Python codebases — trained on over 600,000 real-world CVE-backed samples.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SecureScan AI — Core Idea                       │
│                                                                         │
│    Developer writes code                                                │
│           │                                                             │
│           ▼                                                             │
│    SecureScan AI scans the function                                     │
│           │                                                             │
│           ├──▶  VULNERABLE  (e.g. buffer overflow, SQL injection)       │
│           └──▶  SAFE        (no known vulnerability pattern detected)   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Architecture

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════════╗
║               SecureScan AI — Three-Stage Pipeline                    ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║   INPUT: Raw source code function (C / C++ / Java / Python)           ║
║                          │                                            ║
║                          ▼                                            ║
║   ┌───────────────────────────────────────────────────────────┐       ║
║   │  STAGE 1 — CodeBERT Encoder (microsoft/codebert-base)     │       ║
║   │                                                           │       ║
║   │  • Tokenize input (max 512 tokens)                        │       ║
║   │  • First 6 transformer layers frozen                      │       ║
║   │  • Outputs: contextual token embeddings (768-dim)         │       ║
║   └─────────────────────────┬─────────────────────────────────┘       ║
║                             │                                         ║
║                             ▼                                         ║
║   ┌───────────────────────────────────────────────────────────┐       ║
║   │  STAGE 2 — Bidirectional LSTM                             │       ║
║   │                                                           │       ║
║   │  • 2 stacked BiLSTM layers                                │       ║
║   │  • Hidden size: 256 (512 bidirectional)                   │       ║
║   │  • Captures forward + backward code context               │       ║
║   └─────────────────────────┬─────────────────────────────────┘       ║
║                             │                                         ║
║                             ▼                                         ║
║   ┌───────────────────────────────────────────────────────────┐       ║
║   │  STAGE 3 — MLP Classifier                                 │       ║
║   │                                                           │       ║
║   │  • 512 → 256 → 128 → 2 fully connected layers             │       ║
║   │  • ReLU activation + BatchNorm + Dropout (p=0.3)          │       ║
║   │  • Softmax output over two classes                        │       ║
║   └─────────────────────────┬─────────────────────────────────┘       ║
║                             │                                         ║
║              ┌──────────────┴──────────────┐                         ║
║              ▼                             ▼                         ║
║       [ VULNERABLE ]               [ NON-VULNERABLE ]                ║
╚═══════════════════════════════════════════════════════════════════════╝
```

</div>

| Component | Configuration |
|---|---|
| Base Encoder | `microsoft/codebert-base` — 125M parameters |
| Frozen Layers | First 6 of 12 transformer layers |
| BiLSTM | 2 layers, hidden size 256, bidirectional |
| MLP Head | 512 → 256 → 128 → 2 with ReLU + BatchNorm |
| Dropout | p = 0.3 on all intermediate layers |
| Max Token Length | 512 tokens |
| Optimizer | AdamW with linear warmup + weight decay |
| Loss Function | Binary Cross-Entropy with class balancing weights |

---

## Demo

**Live Application:** [securescan-ai.vercel.app](https://securescan-ai.vercel.app)

Run a vulnerability scan directly in your browser — no setup required.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning.git
cd SecureScan-AI---Deep-Learning

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install all dependencies
pip install -r requirements.txt
```

**Core requirements:**

| Package | Version |
|---|---|
| Python | 3.9+ |
| PyTorch | 2.0.0 |
| Transformers | 4.35.0 |
| scikit-learn | 1.3.0 |
| CUDA | Optional — for GPU acceleration |

---

## Usage

### Run the Notebook

```bash
jupyter notebook notebooks/Phase4_SecureScan_AI_Final.ipynb
```

### Train from Scratch

```bash
python src/training/train.py
```

### Inference on a Single Function

```python
from src.models.securescan_model import SecureScanModel
from transformers import AutoTokenizer
import torch

# Load model and tokenizer
model = SecureScanModel()
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')

# Analyze a vulnerable function
code = "char buf[10]; strcpy(buf, input);"

inputs = tokenizer(code, return_tensors='pt', truncation=True, max_length=512)

with torch.no_grad():
    logits = model(inputs['input_ids'], inputs['attention_mask'])
    prediction = 'Vulnerable' if logits.argmax().item() == 1 else 'Safe'

print(f"Result: {prediction}")
# Output: Result: Vulnerable
```

---

## Project Structure

```
SecureScan-AI/
│
├── data/                        # Dataset files (gitignored)
│
├── docs/
│   ├── ARCHITECTURE.md          # Full technical architecture
│   ├── DATA.md                  # Dataset documentation
│   ├── DEPLOYMENT.md            # Deployment guide
│   └── RESULTS.md               # Evaluation results and plots
│
├── experiments/                 # Training configs, runs, logs
│
├── notebooks/                   # Jupyter notebooks with full outputs
│
├── reports/                     # Analysis reports and visualizations
│
├── phases/
│   ├── phase1-roadmap/          # Project planning and roadmap
│   ├── phase2-baseline/         # Baseline MLP implementation
│   ├── phase3-architecture/     # Core deep architecture design
│   ├── phase4-refinement/       # Transfer learning and HPO
│   ├── phase5-evaluation/       # Ablation studies and evaluation
│   └── phase6-deployment/       # Deployment deliverables
│
├── src/
│   ├── data/loader.py           # Dataset loading utilities
│   ├── models/                  # Model class definitions
│   │   └── securescan_model.py  # Main CodeBERT+BiLSTM+MLP model
│   ├── preprocessing/           # Data cleaning and tokenization
│   ├── training/train.py        # Training loop with scheduler
│   └── utils/helpers.py         # Helper functions and metrics
│
├── tests/                       # Unit tests
├── app.py                       # Web inference interface
├── requirements.txt
├── Dockerfile
├── CITATION.bib
├── CITATION.cff
├── DATA_CARD.md
└── README.md
```

---

## Datasets

| Dataset | Language | Samples | Source |
|---|---|---|---|
| **BigVul** | C / C++ | ~188,000 | Real CVE + NVD entries |
| **DiverseVul** | C / C++ | ~319,000 | Diverse CVE coverage |
| **FormAI** | Multi-language | ~246,000 | AI-generated and labeled |

**Total training corpus: 600,000+ labeled functions**

Preprocessing pipeline applied to all datasets:

```
Raw Dataset
    │
    ├── Remove duplicates and near-duplicates
    ├── Filter and truncate functions > 512 tokens
    ├── Balance class distribution via undersampling
    ├── 80 / 10 / 10 train-validation-test split
    └── Tokenize via CodeBERT tokenizer
```

Full documentation in [docs/DATA.md](docs/DATA.md).

---

## Results

### Model Comparison

| Model | F1 Score | Precision | Recall |
|---|---|---|---|
| Baseline MLP | 0.7346 | 0.741 | 0.728 |
| CodeBERT only | 0.8612 | 0.863 | 0.859 |
| BiLSTM + MLP (no CodeBERT) | 0.7950 | 0.801 | 0.789 |
| **CodeBERT + BiLSTM + MLP** | **0.9252** | **0.921** | **0.930** |

### Ablation Study

| Configuration | F1 Score | Change |
|---|---|---|
| Full model (CodeBERT + BiLSTM + MLP) | **0.9252** | — |
| Without BiLSTM (CodeBERT + MLP only) | 0.8832 | -4.2% |
| Without CodeBERT (GloVe + BiLSTM + MLP) | 0.7950 | -8.3% |
| Without Dropout | 0.8910 | -3.4% |
| Unidirectional LSTM | 0.9056 | -2.1% |

Full results, confusion matrices, and training curves in [docs/RESULTS.md](docs/RESULTS.md).

---

## Citation

```bibtex
@misc{securescan-ai,
  title     = {SecureScan AI — Source Code Vulnerability Detection},
  author    = {Shah, Aly Abbas},
  year      = {2026},
  howpublished = {\url{https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning}},
  note      = {AI335L Deep Learning Lab, Air University Lahore}
}
```

Or use [CITATION.cff](CITATION.cff) for automated citation tools.

---

## Acknowledgments

- **CodeBERT** — Microsoft Research
- **BigVul Dataset** — MSR
- **DiverseVul Dataset** — Ahmed Tabib
- **Course Supervisor** — AI335L Deep Learning Lab, Air University Lahore

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for full details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0a1628,0f2942,185fa5,378add&height=120&section=footer&animation=fadeIn" width="100%"/>

<sub>AI335L Deep Learning Lab — Air University Lahore, Spring 2026</sub>

</div>
