# EEG-Based Cognitive Workload Recognition

An ongoing independent research project investigating EEG-based recognition of cognitive workload, with a focus on **cross-subject generalization** and potential applications in adaptive human–computer interaction.

## Research Question

How well can EEG-based cognitive workload recognition generalize across individuals, and which EEG features and machine-learning approaches are most robust to inter-subject variability?

## Dataset

The project uses the publicly available **STEW (Simultaneous Task EEG Workload)** dataset.

The dataset contains EEG recordings collected during a mental workload experiment and includes data associated with different levels of cognitive workload.

## Planned Methodology

The analysis pipeline is planned to include:

1. **EEG preprocessing**

   * Signal filtering
   * Artifact handling
   * Preparation of EEG segments for analysis

2. **Spectral feature extraction**

   * Theta power
   * Alpha power
   * Beta power
   * Additional frequency-domain features where appropriate

3. **Machine learning**

   * Linear Discriminant Analysis (LDA)
   * Support Vector Machine (SVM)

4. **Cross-subject evaluation**

   * Leave-One-Subject-Out (LOSO) evaluation
   * Testing model generalization to participants not used during training

5. **Performance evaluation**

   * Accuracy
   * Macro-F1 score

## Tools

* Python
* MNE-Python
* NumPy
* SciPy
* scikit-learn
* Matplotlib

## Project Status

**In progress**

The project is currently at the research and analysis-design stage. The preprocessing pipeline, feature extraction methods, and evaluation protocol will be implemented and evaluated progressively.

The final experimental results are not yet available.

## Expected Outcome

The project aims to provide a systematic evaluation of EEG spectral features and classical machine-learning approaches for cross-subject cognitive workload recognition.

The analysis will also examine the challenges of inter-subject variability and the potential relevance of robust workload recognition for adaptive human–computer interaction.

## Planned Repository Structure

```text
eeg-cognitive-workload/
│
├── README.md
├── data/
├── notebooks/
├── src/
├── results/
└── docs/
```

Raw EEG data will not be uploaded to this repository. The dataset will be obtained directly from its original public source.

## Research Focus

**EEG Signal Processing · Cognitive Workload · Machine Learning · Cross-Subject Generalization · Human–Computer Interaction**

---

*This repository documents an ongoing independent research project. Methods and documentation will be updated as the project progresses.*
