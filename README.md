<div align="center">

<!-- HERO BANNER -->
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=12,20,24&height=4&section=header" width="100%"/>

<br/>

<!-- 3D TITLE SVG -->
<svg width="900" height="180" viewBox="0 0 900 180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#C0392B"/>
      <stop offset="50%" style="stop-color:#E74C3C"/>
      <stop offset="100%" style="stop-color:#C0392B"/>
    </linearGradient>
    <linearGradient id="subGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#E67E22"/>
      <stop offset="100%" style="stop-color:#F39C12"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="shadow3d">
      <feDropShadow dx="4" dy="4" stdDeviation="3" flood-color="#7B241C" flood-opacity="0.8"/>
    </filter>
  </defs>
  <!-- 3D shadow letters -->
  <text x="452" y="108" text-anchor="middle" font-family="Georgia, serif" font-size="88" font-weight="900" fill="#7B241C" letter-spacing="-2">SecureScan AI</text>
  <text x="450" y="106" text-anchor="middle" font-family="Georgia, serif" font-size="88" font-weight="900" fill="url(#titleGrad)" filter="url(#glow)" letter-spacing="-2">SecureScan AI</text>
  <text x="450" y="148" text-anchor="middle" font-family="Georgia, serif" font-size="18" fill="url(#subGrad)" letter-spacing="6">AUTOMATED VULNERABILITY DETECTION</text>
  <!-- decorative lines -->
  <line x1="100" y1="160" x2="340" y2="160" stroke="#C0392B" stroke-width="1.5" opacity="0.6"/>
  <line x1="560" y1="160" x2="800" y2="160" stroke="#C0392B" stroke-width="1.5" opacity="0.6"/>
  <circle cx="450" cy="160" r="4" fill="#E74C3C"/>
  <circle cx="340" cy="160" r="2" fill="#C0392B" opacity="0.6"/>
  <circle cx="560" cy="160" r="2" fill="#C0392B" opacity="0.6"/>
</svg>

<br/>

<!-- BADGES ROW 1 -->
[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-securescan--ai.vercel.app-C0392B?style=for-the-badge&labelColor=7B241C&logo=vercel&logoColor=white)](https://securescan-ai.vercel.app)
&nbsp;
[![F1 Score](https://img.shields.io/badge/F1_SCORE-0.9252-E67E22?style=for-the-badge&labelColor=873600&logo=target&logoColor=white)](docs/RESULTS.md)
&nbsp;
[![Samples](https://img.shields.io/badge/TRAINING_CORPUS-600K%2B_CVE_samples-8E44AD?style=for-the-badge&labelColor=512E5F)](docs/DATA.md)

<br/>

<!-- BADGES ROW 2 -->
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white&labelColor=7B241C)](requirements.txt)
&nbsp;
[![HuggingFace](https://img.shields.io/badge/CodeBERT-125M_params-F39C12?style=for-the-badge&logo=huggingface&logoColor=white&labelColor=784212)](https://huggingface.co/microsoft/codebert-base)
&nbsp;
[![Deploy](https://img.shields.io/badge/FastAPI_%2B_React-Deployed-27AE60?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=145A32)](https://securescan-ai.vercel.app)
&nbsp;
[![License](https://img.shields.io/badge/MIT-License-95A5A6?style=for-the-badge&labelColor=2C3E50)](LICENSE)

<br/><br/>

<!-- STAT CARDS SVG -->
<svg width="860" height="110" viewBox="0 0 860 110" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="card1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#922B21"/>
      <stop offset="100%" style="stop-color:#C0392B"/>
    </linearGradient>
    <linearGradient id="card2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#784212"/>
      <stop offset="100%" style="stop-color:#E67E22"/>
    </linearGradient>
    <linearGradient id="card3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#512E5F"/>
      <stop offset="100%" style="stop-color:#8E44AD"/>
    </linearGradient>
    <linearGradient id="card4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#145A32"/>
      <stop offset="100%" style="stop-color:#27AE60"/>
    </linearGradient>
    <filter id="cardShadow">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-opacity="0.4"/>
    </filter>
  </defs>
  <!-- Card 1 -->
  <rect x="10" y="10" width="190" height="90" rx="12" fill="url(#card1)" filter="url(#cardShadow)"/>
  <rect x="10" y="10" width="190" height="3" rx="2" fill="#E74C3C"/>
  <text x="105" y="52" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="900" fill="white">0.9252</text>
  <text x="105" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8" letter-spacing="2">WEIGHTED F1</text>
  <!-- Card 2 -->
  <rect x="225" y="10" width="190" height="90" rx="12" fill="url(#card2)" filter="url(#cardShadow)"/>
  <rect x="225" y="10" width="190" height="3" rx="2" fill="#F39C12"/>
  <text x="320" y="52" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="900" fill="white">600K+</text>
  <text x="320" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0" letter-spacing="2">CVE SAMPLES</text>
  <!-- Card 3 -->
  <rect x="440" y="10" width="190" height="90" rx="12" fill="url(#card3)" filter="url(#cardShadow)"/>
  <rect x="440" y="10" width="190" height="3" rx="2" fill="#9B59B6"/>
  <text x="535" y="52" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="900" fill="white">42ms</text>
  <text x="535" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF" letter-spacing="2">GPU INFERENCE</text>
  <!-- Card 4 -->
  <rect x="655" y="10" width="190" height="90" rx="12" fill="url(#card4)" filter="url(#cardShadow)"/>
  <rect x="655" y="10" width="190" height="3" rx="2" fill="#2ECC71"/>
  <text x="750" y="52" text-anchor="middle" font-family="Georgia,serif" font-size="32" font-weight="900" fill="white">125M</text>
  <text x="750" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3" letter-spacing="2">CODEBERT PARAMS</text>
</svg>

</div>

<br/>

---

<br/>

## What SecureScan AI Does

SecureScan AI reads raw C/C++ source code and decides — with **92.52% F1 accuracy** — whether a function contains a security vulnerability. No hand-written rules. No compiler required. It learned from **600,000+ real CVE patches** pulled directly from the National Vulnerability Database.

The architecture chains three components: a **CodeBERT transformer** for code semantics, a **Bidirectional LSTM** for temporal operation flow (critical for buffer overflow and use-after-free detection), and an **MLP classifier** for the final binary verdict. The whole pipeline runs live in a browser at [securescan-ai.vercel.app](https://securescan-ai.vercel.app) — paste code, get a result in 42ms.

> Built across six structured phases for **AI335L Deep Learning Lab — Spring 2026, NIIT Lahore.**

<br/>

---

<br/>

## Live Application

<div align="center">

![SecureScan AI — Live Application](https://raw.githubusercontent.com/aly-abbas11/SecureScan-AI---Deep-Learning/main/docs/Demo.png)

</div>

<br/>

<div align="center">

<!-- APP VIEWS SVG -->
<svg width="860" height="240" viewBox="0 0 860 240" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="panelGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#1C0A00"/>
      <stop offset="100%" style="stop-color:#2C1100"/>
    </linearGradient>
    <linearGradient id="accentRed" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#922B21"/>
      <stop offset="100%" style="stop-color:#E74C3C"/>
    </linearGradient>
    <linearGradient id="accentOrange" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#784212"/>
      <stop offset="100%" style="stop-color:#E67E22"/>
    </linearGradient>
    <linearGradient id="accentPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#512E5F"/>
      <stop offset="100%" style="stop-color:#8E44AD"/>
    </linearGradient>
    <linearGradient id="accentGreen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#145A32"/>
      <stop offset="100%" style="stop-color:#27AE60"/>
    </linearGradient>
    <filter id="panelShadow">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>
  <!-- Panel 1: ANALYZER -->
  <rect x="10" y="10" width="190" height="220" rx="14" fill="url(#panelGrad)" filter="url(#panelShadow)" stroke="#3D1A00" stroke-width="1"/>
  <rect x="10" y="10" width="190" height="4" rx="2" fill="url(#accentRed)"/>
  <text x="105" y="42" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E74C3C" letter-spacing="3" font-weight="700">ANALYZER</text>
  <rect x="30" y="55" width="150" height="1" fill="#3D1A00"/>
  <text x="105" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">Paste C/C++ code</text>
  <text x="105" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">Layer-by-layer scan</text>
  <text x="105" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">ERRORS · FIXES tabs</text>
  <text x="105" y="136" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">JSON output</text>
  <text x="105" y="154" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">Scan HISTORY</text>
  <rect x="30" y="175" width="150" height="36" rx="8" fill="#922B21"/>
  <text x="105" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="white" font-weight="700">START ANALYZER</text>
  <!-- Panel 2: DASHBOARD -->
  <rect x="225" y="10" width="190" height="220" rx="14" fill="url(#panelGrad)" filter="url(#panelShadow)" stroke="#3D1A00" stroke-width="1"/>
  <rect x="225" y="10" width="190" height="4" rx="2" fill="url(#accentOrange)"/>
  <text x="320" y="42" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E67E22" letter-spacing="3" font-weight="700">DASHBOARD</text>
  <rect x="245" y="55" width="150" height="1" fill="#3D1A00"/>
  <text x="320" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Total scans counter</text>
  <text x="320" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Blocked / passed split</text>
  <text x="320" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Mean scan time</text>
  <text x="320" y="136" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Vuln dispersion chart</text>
  <text x="320" y="154" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Pipeline monitoring</text>
  <rect x="245" y="175" width="150" height="36" rx="8" fill="#784212"/>
  <text x="320" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="white" font-weight="700">VIEW PIPELINE</text>
  <!-- Panel 3: REPORTS -->
  <rect x="440" y="10" width="190" height="220" rx="14" fill="url(#panelGrad)" filter="url(#panelShadow)" stroke="#3D1A00" stroke-width="1"/>
  <rect x="440" y="10" width="190" height="4" rx="2" fill="url(#accentPurple)"/>
  <text x="535" y="42" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#9B59B6" letter-spacing="3" font-weight="700">REPORTS</text>
  <rect x="460" y="55" width="150" height="1" fill="#3D1A00"/>
  <text x="535" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">Full scan history</text>
  <text x="535" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">CWE tag per finding</text>
  <text x="535" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">Confidence scores</text>
  <text x="535" y="136" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">PDF export per scan</text>
  <text x="535" y="154" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">BLOCKED / PASSED</text>
  <rect x="460" y="175" width="150" height="36" rx="8" fill="#512E5F"/>
  <text x="535" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="white" font-weight="700">VIEW REPORTS</text>
  <!-- Panel 4: DEPLOYMENT -->
  <rect x="655" y="10" width="190" height="220" rx="14" fill="url(#panelGrad)" filter="url(#panelShadow)" stroke="#3D1A00" stroke-width="1"/>
  <rect x="655" y="10" width="190" height="4" rx="2" fill="url(#accentGreen)"/>
  <text x="750" y="42" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#27AE60" letter-spacing="3" font-weight="700">DEPLOYMENT</text>
  <rect x="675" y="55" width="150" height="1" fill="#3D1A00"/>
  <text x="750" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3">React SPA on Vercel</text>
  <text x="750" y="100" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3">FastAPI on HF Spaces</text>
  <text x="750" y="118" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3">Docker containerised</text>
  <text x="750" y="136" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3">42ms GPU latency</text>
  <text x="750" y="154" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#D5F5E3">REST API — /predict</text>
  <rect x="675" y="175" width="150" height="36" rx="8" fill="#145A32"/>
  <text x="750" y="198" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="white" font-weight="700">LIVE NOW</text>
</svg>

</div>

<br/>

---

<br/>

## Architecture

<div align="center">

<!-- 3D ARCHITECTURE PIPELINE SVG -->
<svg width="860" height="460" viewBox="0 0 860 460" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="pipeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1C0A00"/>
      <stop offset="100%" style="stop-color:#2C1100"/>
    </linearGradient>
    <linearGradient id="block1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#922B21"/>
      <stop offset="100%" style="stop-color:#C0392B"/>
    </linearGradient>
    <linearGradient id="block2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#784212"/>
      <stop offset="100%" style="stop-color:#CA6F1E"/>
    </linearGradient>
    <linearGradient id="block3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#512E5F"/>
      <stop offset="100%" style="stop-color:#7D3C98"/>
    </linearGradient>
    <linearGradient id="block4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#145A32"/>
      <stop offset="100%" style="stop-color:#1E8449"/>
    </linearGradient>
    <linearGradient id="block5" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1A5276"/>
      <stop offset="100%" style="stop-color:#2471A3"/>
    </linearGradient>
    <filter id="blockShadow">
      <feDropShadow dx="3" dy="5" stdDeviation="5" flood-color="#000" flood-opacity="0.6"/>
    </filter>
    <filter id="arrowGlow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#E74C3C"/>
    </marker>
  </defs>
  <!-- Background -->
  <rect width="860" height="460" rx="16" fill="#0D0500" stroke="#3D1A00" stroke-width="1.5"/>
  <!-- Title bar -->
  <rect x="0" y="0" width="860" height="44" rx="16" fill="#1C0A00"/>
  <rect x="0" y="30" width="860" height="14" fill="#1C0A00"/>
  <circle cx="26" cy="22" r="7" fill="#C0392B"/>
  <circle cx="50" cy="22" r="7" fill="#E67E22"/>
  <circle cx="74" cy="22" r="7" fill="#27AE60"/>
  <text x="430" y="27" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#7F8C8D" letter-spacing="4">THREE-STAGE INFERENCE PIPELINE</text>
  <!-- INPUT NODE -->
  <rect x="340" y="62" width="180" height="52" rx="10" fill="#1C0A00" stroke="#C0392B" stroke-width="1.5" filter="url(#blockShadow)"/>
  <text x="430" y="83" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E74C3C" letter-spacing="3" font-weight="700">INPUT</text>
  <text x="430" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">Raw C / C++ function string</text>
  <!-- Arrow 1 -->
  <line x1="430" y1="114" x2="430" y2="136" stroke="#E74C3C" stroke-width="2" marker-end="url(#arrow)" filter="url(#arrowGlow)"/>
  <!-- STAGE 1: CodeBERT -->
  <rect x="60" y="140" width="740" height="88" rx="12" fill="url(#block1)" filter="url(#blockShadow)"/>
  <!-- 3D top face -->
  <rect x="60" y="140" width="740" height="4" rx="2" fill="#E74C3C" opacity="0.8"/>
  <text x="160" y="168" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FADBD8" letter-spacing="3" font-weight="700">STAGE 01</text>
  <text x="430" y="168" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="white" font-weight="700">CodeBERT Encoder</text>
  <text x="700" y="168" text-anchor="middle" font-family="Arial,monospace" font-size="10" fill="#FADBD8">microsoft/codebert-base</text>
  <line x1="60" y1="176" x2="800" y2="176" stroke="#E74C3C" stroke-width="0.5" opacity="0.4"/>
  <text x="215" y="196" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">12 transformer layers</text>
  <text x="430" y="196" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">768-dim hidden states</text>
  <text x="645" y="196" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8">First 6 layers frozen</text>
  <text x="430" y="214" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FADBD8" font-style="italic">Output: sequence of 768-dimensional contextual token vectors</text>
  <!-- Arrow 2 -->
  <line x1="430" y1="228" x2="430" y2="252" stroke="#CA6F1E" stroke-width="2" marker-end="url(#arrow)" filter="url(#arrowGlow)"/>
  <!-- STAGE 2: BiLSTM -->
  <rect x="60" y="256" width="740" height="76" rx="12" fill="url(#block2)" filter="url(#blockShadow)"/>
  <rect x="60" y="256" width="740" height="4" rx="2" fill="#E67E22" opacity="0.8"/>
  <text x="160" y="282" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FDEBD0" letter-spacing="3" font-weight="700">STAGE 02</text>
  <text x="430" y="282" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="white" font-weight="700">Bidirectional LSTM</text>
  <text x="700" y="282" text-anchor="middle" font-family="Arial,monospace" font-size="10" fill="#FDEBD0">sequential code flow</text>
  <line x1="60" y1="290" x2="800" y2="290" stroke="#E67E22" stroke-width="0.5" opacity="0.4"/>
  <text x="215" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">2 stacked BiLSTM layers</text>
  <text x="430" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">256 hidden per direction → 512-dim</text>
  <text x="645" y="310" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#FDEBD0">Dropout p=0.3</text>
  <!-- Arrow 3 -->
  <line x1="430" y1="332" x2="430" y2="356" stroke="#7D3C98" stroke-width="2" marker-end="url(#arrow)" filter="url(#arrowGlow)"/>
  <!-- STAGE 3: MLP -->
  <rect x="60" y="360" width="740" height="68" rx="12" fill="url(#block3)" filter="url(#blockShadow)"/>
  <rect x="60" y="360" width="740" height="4" rx="2" fill="#9B59B6" opacity="0.8"/>
  <text x="160" y="386" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E8DAEF" letter-spacing="3" font-weight="700">STAGE 03</text>
  <text x="430" y="386" text-anchor="middle" font-family="Georgia,serif" font-size="16" fill="white" font-weight="700">MLP Classifier</text>
  <text x="700" y="386" text-anchor="middle" font-family="Arial,monospace" font-size="10" fill="#E8DAEF">binary decision</text>
  <line x1="60" y1="394" x2="800" y2="394" stroke="#9B59B6" stroke-width="0.5" opacity="0.4"/>
  <text x="215" y="414" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">512 → 256 → 128 → 2</text>
  <text x="430" y="414" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">ReLU + BatchNorm + Dropout</text>
  <text x="645" y="414" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#E8DAEF">Softmax output</text>
  <!-- Output arrows -->
  <line x1="310" y1="428" x2="220" y2="448" stroke="#E74C3C" stroke-width="1.5" stroke-dasharray="4,3"/>
  <line x1="550" y1="428" x2="640" y2="448" stroke="#27AE60" stroke-width="1.5" stroke-dasharray="4,3"/>
  <!-- Output boxes -->
  <rect x="100" y="440" width="230" height="14" rx="4" fill="#922B21" opacity="0.9"/>
  <text x="215" y="451" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="white" font-weight="700" letter-spacing="2">VULNERABLE + CONFIDENCE %</text>
  <rect x="530" y="440" width="230" height="14" rx="4" fill="#145A32" opacity="0.9"/>
  <text x="645" y="451" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="white" font-weight="700" letter-spacing="2">NON-VULNERABLE + CONFIDENCE %</text>
</svg>

</div>

<br/>

### Component Reference

| Component | Configuration |
|---|---|
| Base Encoder | `microsoft/codebert-base` — 125M parameters, RoBERTa architecture |
| Frozen Layers | First 6 of 12 transformer layers during fine-tuning |
| BiLSTM | 2 layers, hidden size 256, bidirectional → 512-dim final representation |
| MLP Head | 512 → 256 → 128 → 2 with ReLU + BatchNorm after each layer |
| Dropout | p = 0.3 on all intermediate layers |
| Max Token Length | 512 BPE subword tokens (right-truncation) |
| Optimizer | AdamW — lr=8.57e-5, weight decay=0.01, linear warmup |
| Loss Function | Binary Cross-Entropy with class balancing weights (~16× for vulnerable) |
| Training Hardware | Kaggle Tesla P100 16GB HBM2 |
| Inference Latency | ~42ms GPU · ~380ms CPU fallback |

<br/>

---

<br/>

## Results

<div align="center">

<!-- 3D RESULTS BAR CHART SVG -->
<svg width="860" height="300" viewBox="0 0 860 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="barBase" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#566573"/>
      <stop offset="100%" style="stop-color:#2C3E50"/>
    </linearGradient>
    <linearGradient id="barCodeBERT" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#CA6F1E"/>
      <stop offset="100%" style="stop-color:#784212"/>
    </linearGradient>
    <linearGradient id="barBiLSTM" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#7D3C98"/>
      <stop offset="100%" style="stop-color:#512E5F"/>
    </linearGradient>
    <linearGradient id="barFull" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#E74C3C"/>
      <stop offset="100%" style="stop-color:#922B21"/>
    </linearGradient>
    <filter id="barShadow">
      <feDropShadow dx="3" dy="3" stdDeviation="3" flood-opacity="0.5"/>
    </filter>
  </defs>
  <rect width="860" height="300" rx="14" fill="#0D0500" stroke="#3D1A00" stroke-width="1.5"/>
  <!-- Title -->
  <text x="430" y="30" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#7F8C8D" letter-spacing="4" font-weight="700">MODEL COMPARISON — F1 SCORE</text>
  <line x1="40" y1="40" x2="820" y2="40" stroke="#3D1A00" stroke-width="1"/>
  <!-- Y axis grid lines -->
  <line x1="80" y1="60" x2="820" y2="60" stroke="#1C0A00" stroke-width="1"/>
  <line x1="80" y1="100" x2="820" y2="100" stroke="#1C0A00" stroke-width="1"/>
  <line x1="80" y1="140" x2="820" y2="140" stroke="#1C0A00" stroke-width="1"/>
  <line x1="80" y1="180" x2="820" y2="180" stroke="#1C0A00" stroke-width="1"/>
  <line x1="80" y1="220" x2="820" y2="220" stroke="#1C0A00" stroke-width="1"/>
  <!-- Y axis labels -->
  <text x="70" y="64" text-anchor="end" font-family="monospace" font-size="10" fill="#566573">1.00</text>
  <text x="70" y="104" text-anchor="end" font-family="monospace" font-size="10" fill="#566573">0.90</text>
  <text x="70" y="144" text-anchor="end" font-family="monospace" font-size="10" fill="#566573">0.80</text>
  <text x="70" y="184" text-anchor="end" font-family="monospace" font-size="10" fill="#566573">0.70</text>
  <text x="70" y="224" text-anchor="end" font-family="monospace" font-size="10" fill="#566573">0.60</text>
  <!-- Axis line -->
  <line x1="80" y1="55" x2="80" y2="230" stroke="#3D1A00" stroke-width="1.5"/>
  <line x1="80" y1="230" x2="820" y2="230" stroke="#3D1A00" stroke-width="1.5"/>
  <!-- BAR 1: MLP Baseline F1=0.7346 → height = 0.7346*170 = 124.9 -->
  <rect x="130" y="105" width="120" height="125" rx="4" fill="url(#barBase)" filter="url(#barShadow)"/>
  <!-- 3D side face -->
  <polygon points="250,105 262,97 262,222 250,230" fill="#1C2833" opacity="0.7"/>
  <!-- 3D top face -->
  <polygon points="130,105 142,97 262,97 250,105" fill="#7F8C8D" opacity="0.6"/>
  <text x="190" y="96" text-anchor="middle" font-family="monospace" font-size="12" fill="#95A5A6" font-weight="700">0.7346</text>
  <text x="196" y="252" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D">Baseline MLP</text>
  <!-- BAR 2: CodeBERT only F1=0.8612 → height = 0.8612*170 = 146.4 -->
  <rect x="320" y="84" width="120" height="146" rx="4" fill="url(#barCodeBERT)" filter="url(#barShadow)"/>
  <polygon points="440,84 452,76 452,230 440,230" fill="#512E00" opacity="0.7"/>
  <polygon points="320,84 332,76 452,76 440,84" fill="#E67E22" opacity="0.5"/>
  <text x="380" y="75" text-anchor="middle" font-family="monospace" font-size="12" fill="#F39C12" font-weight="700">0.8612</text>
  <text x="386" y="252" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#CA6F1E">CodeBERT only</text>
  <!-- BAR 3: BiLSTM+MLP F1=0.7950 → height = 0.7950*170 = 135.2 -->
  <rect x="510" y="95" width="120" height="135" rx="4" fill="url(#barBiLSTM)" filter="url(#barShadow)"/>
  <polygon points="630,95 642,87 642,230 630,230" fill="#2C1A40" opacity="0.7"/>
  <polygon points="510,95 522,87 642,87 630,95" fill="#9B59B6" opacity="0.5"/>
  <text x="570" y="86" text-anchor="middle" font-family="monospace" font-size="12" fill="#D2B4DE" font-weight="700">0.7950</text>
  <text x="576" y="252" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#7D3C98">BiLSTM+MLP</text>
  <!-- BAR 4: Full model F1=0.9252 → height = 0.9252*170 = 157.3 -->
  <rect x="700" y="73" width="120" height="157" rx="4" fill="url(#barFull)" filter="url(#barShadow)"/>
  <polygon points="820,73 832,65 832,230 820,230" fill="#641E16" opacity="0.7"/>
  <polygon points="700,73 712,65 832,65 820,73" fill="#E74C3C" opacity="0.6"/>
  <text x="760" y="64" text-anchor="middle" font-family="monospace" font-size="14" fill="#E74C3C" font-weight="900">0.9252</text>
  <text x="766" y="252" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E74C3C" font-weight="700">Full Model (OURS)</text>
  <!-- Winner crown indicator -->
  <text x="760" y="50" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#E74C3C" letter-spacing="2">BEST</text>
  <line x1="700" y1="230" x2="820" y2="230" stroke="#E74C3C" stroke-width="2"/>
  <!-- Legend -->
  <rect x="100" y="272" width="10" height="10" fill="#566573"/>
  <text x="116" y="281" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D">Baseline MLP</text>
  <rect x="230" y="272" width="10" height="10" fill="#CA6F1E"/>
  <text x="246" y="281" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D">CodeBERT only</text>
  <rect x="370" y="272" width="10" height="10" fill="#7D3C98"/>
  <text x="386" y="281" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D">BiLSTM+MLP</text>
  <rect x="490" y="272" width="10" height="10" fill="#E74C3C"/>
  <text x="506" y="281" font-family="Arial,sans-serif" font-size="10" fill="#E74C3C" font-weight="700">Full Model (CodeBERT+BiLSTM+MLP)</text>
</svg>

</div>

<br/>

### Ablation Study

Every component removed independently to measure its exact contribution.

| Configuration | F1 Score | Delta | Verdict |
|---|---|---|---|
| Full model — CodeBERT + BiLSTM + MLP | **0.9252** | reference | Production build |
| Without BiLSTM (CodeBERT + MLP only) | 0.8832 | **-4.2%** | BiLSTM captures temporal flow attention misses |
| Without CodeBERT (GloVe + BiLSTM + MLP) | 0.7950 | **-8.3%** | Pre-trained semantics are the dominant driver |
| Without Dropout | 0.8910 | -3.4% | Regularisation critical on imbalanced data |
| Unidirectional LSTM | 0.9056 | -2.1% | Backward context matters — free() before use |

<br/>

---

<br/>

## Datasets

<div align="center">

<!-- DATASET DONUT CHART SVG -->
<svg width="860" height="220" viewBox="0 0 860 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="donutShadow">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.5"/>
    </filter>
  </defs>
  <rect width="860" height="220" rx="14" fill="#0D0500" stroke="#3D1A00" stroke-width="1.5"/>
  <text x="430" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="12" fill="#7F8C8D" letter-spacing="4" font-weight="700">TRAINING CORPUS DISTRIBUTION</text>
  <line x1="40" y1="38" x2="820" y2="38" stroke="#3D1A00" stroke-width="1"/>
  <!-- Donut chart arcs — total = 753K, BigVul=188K(25%), DiverseVul=319K(42.4%), FormAI=246K(32.6%) -->
  <!-- BigVul: 25% = 90deg arc, from -90deg to 0deg -->
  <path d="M 200 130 L 200 70 A 60 60 0 0 1 260 130 Z" fill="#C0392B" filter="url(#donutShadow)"/>
  <!-- DiverseVul: 42.4% ≈ 152.6deg arc -->
  <path d="M 200 130 L 260 130 A 60 60 0 0 1 172 186 Z" fill="#E67E22" filter="url(#donutShadow)"/>
  <!-- FormAI: 32.6% ≈ 117.4deg arc -->
  <path d="M 200 130 L 172 186 A 60 60 0 0 1 200 70 Z" fill="#8E44AD" filter="url(#donutShadow)"/>
  <!-- Inner circle (donut hole) -->
  <circle cx="200" cy="130" r="35" fill="#0D0500"/>
  <text x="200" y="126" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D">TOTAL</text>
  <text x="200" y="142" text-anchor="middle" font-family="Georgia,serif" font-size="14" fill="white" font-weight="700">600K+</text>
  <!-- Legend + Stats -->
  <!-- BigVul -->
  <rect x="320" y="65" width="14" height="14" rx="3" fill="#C0392B"/>
  <text x="342" y="76" font-family="Arial,sans-serif" font-size="13" fill="white" font-weight="700">BigVul</text>
  <text x="342" y="92" font-family="Arial,sans-serif" font-size="11" fill="#7F8C8D">~188,000 samples · C / C++ · Real CVE + NVD entries · 25%</text>
  <!-- DiverseVul -->
  <rect x="320" y="110" width="14" height="14" rx="3" fill="#E67E22"/>
  <text x="342" y="121" font-family="Arial,sans-serif" font-size="13" fill="white" font-weight="700">DiverseVul</text>
  <text x="342" y="137" font-family="Arial,sans-serif" font-size="11" fill="#7F8C8D">~319,000 samples · C / C++ · Diverse CVE coverage · 42.4%</text>
  <!-- FormAI -->
  <rect x="320" y="155" width="14" height="14" rx="3" fill="#8E44AD"/>
  <text x="342" y="166" font-family="Arial,sans-serif" font-size="13" fill="white" font-weight="700">FormAI</text>
  <text x="342" y="182" font-family="Arial,sans-serif" font-size="11" fill="#7F8C8D">~246,000 samples · Multi-language · AI-generated + labeled · 32.6%</text>
  <!-- Right side stats -->
  <line x1="680" y1="55" x2="680" y2="190" stroke="#3D1A00" stroke-width="1"/>
  <text x="760" y="90" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="#E74C3C" font-weight="900">16:1</text>
  <text x="760" y="108" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D" letter-spacing="2">CLASS IMBALANCE</text>
  <line x1="700" y1="118" x2="820" y2="118" stroke="#3D1A00" stroke-width="1"/>
  <text x="760" y="145" text-anchor="middle" font-family="Georgia,serif" font-size="28" fill="#E67E22" font-weight="900">+6%</text>
  <text x="760" y="163" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#7F8C8D" letter-spacing="2">VAE ACCURACY GAIN</text>
</svg>

</div>

<br/>

---

<br/>

## Development Phases

<div align="center">

<!-- TIMELINE SVG -->
<svg width="860" height="200" viewBox="0 0 860 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="timelineGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#C0392B"/>
      <stop offset="20%" style="stop-color:#E67E22"/>
      <stop offset="40%" style="stop-color:#F1C40F"/>
      <stop offset="60%" style="stop-color:#27AE60"/>
      <stop offset="80%" style="stop-color:#2471A3"/>
      <stop offset="100%" style="stop-color:#8E44AD"/>
    </linearGradient>
  </defs>
  <rect width="860" height="200" rx="14" fill="#0D0500" stroke="#3D1A00" stroke-width="1.5"/>
  <!-- Timeline line -->
  <line x1="60" y1="100" x2="800" y2="100" stroke="url(#timelineGrad)" stroke-width="3"/>
  <!-- Phase nodes and labels -->
  <!-- Phase 1 -->
  <circle cx="60" cy="100" r="12" fill="#C0392B" stroke="#922B21" stroke-width="2"/>
  <text x="60" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="700">01</text>
  <text x="60" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E74C3C" font-weight="700">PHASE 1</text>
  <text x="60" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">Definition</text>
  <text x="60" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">SRS + EDA</text>
  <!-- Phase 2 -->
  <circle cx="188" cy="100" r="12" fill="#E67E22" stroke="#CA6F1E" stroke-width="2"/>
  <text x="188" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="700">02</text>
  <text x="188" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E67E22" font-weight="700">PHASE 2</text>
  <text x="188" y="144" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">MLP Baseline</text>
  <text x="188" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#F39C12" font-weight="700">0.7346</text>
  <!-- Phase 3 -->
  <circle cx="316" cy="100" r="12" fill="#F1C40F" stroke="#D4AC0D" stroke-width="2"/>
  <text x="316" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#2C3E50" font-weight="700">03</text>
  <text x="316" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#F1C40F" font-weight="700">PHASE 3</text>
  <text x="316" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">CodeBERT+BiLSTM</text>
  <text x="316" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#F1C40F" font-weight="700">92.68%</text>
  <!-- Phase 4 -->
  <circle cx="444" cy="100" r="12" fill="#27AE60" stroke="#1E8449" stroke-width="2"/>
  <text x="444" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="700">04</text>
  <text x="444" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#27AE60" font-weight="700">PHASE 4</text>
  <text x="444" y="144" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">VAE + HPO</text>
  <text x="444" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#2ECC71" font-weight="700">94.82%</text>
  <!-- Phase 5 -->
  <circle cx="572" cy="100" r="12" fill="#2471A3" stroke="#1A5276" stroke-width="2"/>
  <text x="572" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="700">05</text>
  <text x="572" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#2471A3" font-weight="700">PHASE 5</text>
  <text x="572" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">Evaluation</text>
  <text x="572" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#5DADE2" font-weight="700">F1: 0.9252</text>
  <!-- Phase 6 -->
  <circle cx="700" cy="100" r="14" fill="#8E44AD" stroke="#7D3C98" stroke-width="2"/>
  <text x="700" y="104" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="white" font-weight="700">06</text>
  <text x="700" y="130" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#9B59B6" font-weight="700">PHASE 6</text>
  <text x="700" y="144" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">Deployment</text>
  <text x="700" y="72" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="#A9CCE3" font-weight="700">LIVE</text>
  <!-- End cap -->
  <circle cx="800" cy="100" r="6" fill="#8E44AD" opacity="0.5"/>
  <circle cx="800" cy="100" r="3" fill="#8E44AD"/>
</svg>

</div>

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
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install all dependencies
pip install -r requirements.txt
```

| Package | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Runtime |
| PyTorch | 2.0.0 | Deep learning framework |
| Transformers | 4.35.0 | CodeBERT tokenizer and weights |
| scikit-learn | 1.3.0 | Metrics and evaluation utilities |
| FastAPI | 0.103.0 | Inference REST API backend |
| CUDA | Optional | GPU acceleration — ~9× faster |

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

model     = SecureScanModel()
tokenizer = AutoTokenizer.from_pretrained('microsoft/codebert-base')

# Classic CWE-120 — buffer overflow via unchecked strcpy
code = "char buf[10]; strcpy(buf, user_input);"

inputs = tokenizer(code, return_tensors='pt', truncation=True, max_length=512)

with torch.no_grad():
    logits     = model(inputs['input_ids'], inputs['attention_mask'])
    prediction = 'Vulnerable' if logits.argmax().item() == 1 else 'Safe'

print(f"Result: {prediction}")
# Result: Vulnerable
```

<br/>

---

<br/>

## Deployment Architecture

<div align="center">

<!-- DEPLOYMENT FLOW SVG -->
<svg width="860" height="180" viewBox="0 0 860 180" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="depFlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1C0A00"/>
      <stop offset="100%" style="stop-color:#2C1100"/>
    </linearGradient>
    <marker id="depArrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#E67E22"/>
    </marker>
  </defs>
  <rect width="860" height="180" rx="14" fill="#0D0500" stroke="#3D1A00" stroke-width="1.5"/>
  <!-- Node 1: Browser -->
  <rect x="20" y="60" width="120" height="60" rx="10" fill="#1C0A00" stroke="#C0392B" stroke-width="1.5"/>
  <text x="80" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#E74C3C" letter-spacing="2" font-weight="700">USER BROWSER</text>
  <text x="80" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FADBD8">Paste C/C++</text>
  <text x="80" y="114" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FADBD8">click Analyse</text>
  <!-- Arrow -->
  <line x1="140" y1="90" x2="178" y2="90" stroke="#E67E22" stroke-width="1.5" marker-end="url(#depArrow)"/>
  <text x="159" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7F8C8D">HTTPS</text>
  <!-- Node 2: Vercel -->
  <rect x="180" y="60" width="140" height="60" rx="10" fill="#1C0A00" stroke="#E67E22" stroke-width="1.5"/>
  <text x="250" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#E67E22" letter-spacing="2" font-weight="700">VERCEL EDGE</text>
  <text x="250" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FDEBD0">React SPA</text>
  <text x="250" y="114" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">securescan-ai.vercel.app</text>
  <!-- Arrow -->
  <line x1="320" y1="90" x2="358" y2="90" stroke="#E67E22" stroke-width="1.5" marker-end="url(#depArrow)"/>
  <text x="339" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7F8C8D">POST /predict</text>
  <!-- Node 3: HF Spaces -->
  <rect x="360" y="60" width="160" height="60" rx="10" fill="#1C0A00" stroke="#F1C40F" stroke-width="1.5"/>
  <text x="440" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#F1C40F" letter-spacing="2" font-weight="700">HF SPACES</text>
  <text x="440" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#FCF3CF">FastAPI + Docker</text>
  <text x="440" y="114" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">python:3.11-slim</text>
  <!-- Arrow -->
  <line x1="520" y1="90" x2="558" y2="90" stroke="#E67E22" stroke-width="1.5" marker-end="url(#depArrow)"/>
  <text x="539" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7F8C8D">inference</text>
  <!-- Node 4: Model -->
  <rect x="560" y="60" width="140" height="60" rx="10" fill="#1C0A00" stroke="#27AE60" stroke-width="1.5"/>
  <text x="630" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#27AE60" letter-spacing="2" font-weight="700">MODEL</text>
  <text x="630" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#D5F5E3">CodeBERT+BiLSTM</text>
  <text x="630" y="114" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">~42ms GPU</text>
  <!-- Arrow -->
  <line x1="700" y1="90" x2="738" y2="90" stroke="#E67E22" stroke-width="1.5" marker-end="url(#depArrow)"/>
  <text x="719" y="82" text-anchor="middle" font-family="Arial,sans-serif" font-size="8" fill="#7F8C8D">JSON</text>
  <!-- Node 5: Response -->
  <rect x="740" y="60" width="100" height="60" rx="10" fill="#1C0A00" stroke="#8E44AD" stroke-width="1.5"/>
  <text x="790" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#9B59B6" letter-spacing="2" font-weight="700">RESPONSE</text>
  <text x="790" y="102" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#E8DAEF">label + conf</text>
  <text x="790" y="114" text-anchor="middle" font-family="Arial,sans-serif" font-size="9" fill="#7F8C8D">0 / 1 + float</text>
  <!-- Bottom note -->
  <text x="430" y="158" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#566573">Model weights: huggingface.co/SalmanTanveer/securescan-ai-model  (~490 MB)</text>
</svg>

</div>

<br/>

---

<br/>

## Known Limitations

Documented honestly — trust boundaries matter for any security tool.

| # | Limitation | Severity | Fix |
|---|---|---|---|
| L1 | Confidence miscalibration — ECE = 0.2937 | Critical | Temperature scaling on validation set — one-parameter, no retraining |
| L2 | Label noise ~17–21% in BigVul | High | Near-duplicate removal + label re-verification |
| L3 | 44pp validation-test accuracy gap | High | Caused by implicit HPO overfitting to validation split |
| L4 | 512-token truncation (~18% of functions) | Medium | Hierarchical or sliding-window encoder |
| L5 | C/C++ specificity only | Medium | Domain-adaptive fine-tuning on Java/Python datasets |

<br/>

---

<br/>

## Project Structure

```
SecureScan-AI/
├── .github/workflows/          CI pipeline
├── data/                       Dataset files — gitignored
├── docs/
│   ├── ARCHITECTURE.md         Full technical architecture
│   ├── DATA.md                 Dataset documentation and data card
│   ├── DEPLOYMENT.md           Step-by-step deployment guide
│   ├── RESULTS.md              All results, confusion matrices, plots
│   └── Demo.png                Application screenshot
├── experiments/                Training configs, HPO logs, run artifacts
├── notebooks/                  Jupyter notebooks with full cell outputs
├── reports/                    Analysis reports and visualisations
├── phases/
│   ├── phase1-roadmap/         Problem definition, SRS, literature review
│   ├── phase2-baseline/        MLP baseline implementation and EDA
│   ├── phase3-architecture/    CodeBERT + BiLSTM design and training
│   ├── phase4-refinement/      Transfer learning, VAE augmentation, HPO
│   ├── phase5-evaluation/      Ablation studies, robustness, CIs
│   └── phase6-deployment/      Deployment deliverables and final report
├── src/
│   ├── data/loader.py          Dataset loading and batching
│   ├── models/securescan_model.py  CodeBERT + BiLSTM + MLP definition
│   ├── preprocessing/          Comment removal, tokenisation, truncation
│   ├── training/train.py       Training loop with AdamW + LR scheduler
│   └── utils/helpers.py        Metrics and helper functions
├── tests/                      Unit tests
├── app.py                      Web inference interface
├── requirements.txt            Pinned dependencies
├── Dockerfile                  python:3.11-slim container
├── DATA_CARD.md                Formal dataset documentation
├── CITATION.bib                BibTeX citation
├── CITATION.cff                Citation File Format
└── README.md
```

<br/>

---

<br/>

## Citation

```bibtex
@misc{securescan-ai,
  title        = {SecureScan AI — Source Code Vulnerability Detection},
  author       = {Shah, Ali Abbas and Tanveer, Salman and Ali, Hammad},
  year         = {2026},
  howpublished = {\url{https://github.com/aly-abbas11/SecureScan-AI---Deep-Learning}},
  note         = {AI335L Deep Learning Lab, NIIT Lahore, Spring 2026}
}
```

<br/>

---

<br/>

## Acknowledgments

| | |
|---|---|
| **Microsoft Research** | CodeBERT pre-trained model and tokenizer |
| **Fan et al. — MSR 2020** | BigVul dataset |
| **Chen et al. — RAID 2023** | DiverseVul dataset |
| **Tihanyi et al. — NeurIPS 2023** | FormAI dataset |
| **AI335L Deep Learning Lab** | Course framework, NIIT Lahore |

<br/>

---

<div align="center">

<svg width="600" height="50" viewBox="0 0 600 50" xmlns="http://www.w3.org/2000/svg">
  <line x1="0" y1="25" x2="600" y2="25" stroke="#3D1A00" stroke-width="1"/>
  <circle cx="300" cy="25" r="4" fill="#C0392B"/>
  <circle cx="280" cy="25" r="2" fill="#E67E22" opacity="0.6"/>
  <circle cx="320" cy="25" r="2" fill="#E67E22" opacity="0.6"/>
  <text x="300" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#566573" letter-spacing="3">NIIT LAHORE · AI335L · SPRING 2026</text>
</svg>

**Ali Abbas Shah · Salman Tanveer · Hammad Ali**

[![GitHub](https://img.shields.io/badge/aly--abbas11-GitHub-C0392B?style=flat-square&logo=github&logoColor=white)](https://github.com/aly-abbas11)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-E67E22?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/alyabbas11)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=80&section=footer" width="100%"/>

</div>
