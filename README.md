# EEG-Based Cognitive Workload Recognition

An independent research project investigating EEG-based cognitive workload recognition using signal processing and classical machine-learning methods, with particular attention to **inter-subject variability and cross-subject generalization**.

The project explores the feasibility of identifying cognitive workload states from EEG spectral features and examines the challenges of developing models that generalize across individuals.

## Research Question

How effectively can EEG spectral features support cognitive workload recognition, and how does model performance change when evaluation moves from EEG windows to participant-level analysis?

## Dataset

The project uses the publicly available **STEW (Simultaneous Task EEG Workload)** dataset.

- EEG recordings from 14 channels
- Sampling frequency: 128 Hz
- Two workload conditions: low and high
- EEG recordings segmented into analysis windows

Raw EEG data are not included in this repository. Users should obtain the dataset from its original source and comply with its usage conditions.

## Methodology

The analysis involves the following stages:

### 1. EEG Preprocessing
- Signal filtering
- EEG segmentation
- Preparation of signals for feature extraction

### 2. Feature Extraction
Frequency-domain features are extracted from EEG recordings, including:
- Theta-band power
- Alpha-band power
- Beta-band power
- Additional spectral features

### 3. Machine Learning

Three classical machine-learning approaches have been investigated:

- Random Forest
- Logistic Regression
- Support Vector Machine (RBF kernel)

### 4. Model Evaluation

Two evaluation perspectives have been explored:

- **Window-level evaluation:** Assessing model performance across EEG segments.
- **Participant-level evaluation:** Examining performance under participant-based evaluation to investigate the effect of inter-subject variability.

### 5. Statistical Analysis

Additional analyses include:
- Statistical examination of EEG features
- Multiple-comparison correction using False Discovery Rate (FDR)
- Permutation testing to assess classification performance beyond chance.

## Preliminary Results

Initial experiments have produced the following results:

### Window-Level Evaluation

| Model | Balanced Accuracy | F1-score |
|---|---:|---:|
| Random Forest | 0.773 ± 0.027 | 0.777 |
| Logistic Regression | 0.663 ± 0.051 | 0.697 |
| RBF-SVM | 0.503 ± 0.047 | 0.548 |

### Participant-Level Evaluation

In an exploratory participant-level analysis, performance was lower:

| Model | Balanced Accuracy | Accuracy | F1-score |
|---|---:|---:|---:|
| Logistic Regression | 0.622 | 0.580 | 0.738 |
| RBF-SVM | 0.622 | 0.575 | 0.746 |
| Random Forest | 0.600 | 0.570 | 0.700 |

These preliminary findings suggest that classification performance can vary considerably depending on the evaluation strategy.

**Important:** Window-level performance should not be interpreted as evidence of subject-independent generalization. Further validation using rigorous subject-wise evaluation protocols is needed.

### Statistical Findings

- An exploratory permutation test did not establish statistically significant performance above chance (p ≈ 0.144).
- An initial feature-level analysis identified an uncorrected association involving F7 theta power; however, no feature remained statistically significant after FDR correction.

## Tools and Technologies

- Python
- MNE-Python
- NumPy
- SciPy
- Pandas
- scikit-learn
- Matplotlib

## Project Status

**Ongoing — Experimental Analysis**

The initial preprocessing, feature extraction, classification experiments, and exploratory statistical analyses have been conducted.

Further work will focus on refining participant-level evaluation, investigating inter-subject variability, and assessing the robustness of EEG-based workload recognition.

## Research Motivation

Reliable cognitive workload recognition could contribute to adaptive human–computer interaction systems that respond to changes in users' cognitive states.

Understanding the limitations of cross-subject generalization is an important step toward developing more robust and human-centered interactive systems.

## Repository Structure

```text
eeg-cognitive-workload/
│
├── README.md
├── requirements.txt
├── notebooks/
├── src/
├── results/
│   ├── figures/
│   └── evaluation/
└── docs/
```

## Research Focus

**EEG Signal Processing · Cognitive Workload Recognition · Machine Learning · Inter-Subject Variability · Human–Computer Interaction**

---

*This repository documents an ongoing independent research project. Experimental results are preliminary and may be updated as further analyses and validation experiments are conducted.*
