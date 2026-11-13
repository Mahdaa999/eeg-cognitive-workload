# EEG-Based Cognitive Workload Analysis

An independent research project exploring EEG-based cognitive workload classification using signal processing, spectral feature extraction, and classical machine learning.

The project investigates the relationship between EEG spectral features and self-reported cognitive workload, with particular attention to inter-subject variability and the challenges of participant-level classification.

## Research Objectives

This project explores two related questions:

- Can spectral features extracted from EEG recordings help distinguish between different workload-related conditions?
- How does classification performance change when evaluation accounts for participant-level separation?

The broader motivation is to understand the potential and limitations of EEG-based cognitive state recognition for future human-centered and adaptive interactive systems.

## Dataset

This project uses the **STEW (Simultaneous Task EEG Workload) dataset**.

Dataset characteristics:

- 48 participants
- 14 EEG channels
- Sampling frequency: 128 Hz
- Two recording conditions: low workload (`lo`) and high workload (`hi`)
- Self-reported workload ratings available for 45 participants

For the workload classification experiments, recordings from the high-workload condition (`hi`) were analyzed. Participants with ratings from 4 to 9 were grouped into:

- **Moderate workload:** ratings 4–6
- **High workload:** ratings 7–9

Raw EEG recordings are not included in this repository. Users must obtain the dataset from its original source and comply with the applicable data-use conditions.

## Methodology

### 1. EEG Signal Processing

EEG recordings were segmented into non-overlapping 4-second windows. Different feature extraction approaches were investigated, including:

- Signal mean removal
- Band-pass filtering in an alternative preprocessing pipeline
- Welch power spectral density estimation
- Spectral feature extraction

### 2. Feature Extraction

Frequency-domain features were extracted from three frequency bands:

- Theta: 4–8 Hz
- Alpha: 8–13 Hz
- Beta: 13–30 Hz

Three feature extraction variants were explored:

- Original spectral features
- Alternative spectral estimation and feature aggregation (V2)
- Features extracted after band-pass filtering

These variants use different signal-processing configurations and are evaluated as separate experimental approaches.

### 3. Machine Learning

The following classical machine learning models were investigated:

- Logistic Regression
- Support Vector Machine (RBF kernel)
- Random Forest

### 4. Evaluation Strategy

Participant-based evaluation was conducted using **5-fold GroupKFold cross-validation**, ensuring that recordings from the same participant were not split between training and test folds.

For participant-level classification, window-level predictions were aggregated to obtain one prediction per participant.

This evaluation design examines performance under participant-wise separation. It is a grouped five-fold evaluation and should not be interpreted as Leave-One-Subject-Out (LOSO) validation.

### 5. Statistical and Exploratory Analyses

Additional experiments include:

- EEG feature comparisons
- Feature-level statistical analysis
- False Discovery Rate (FDR) correction for multiple comparisons
- Participant-level permutation testing
- Exploratory regression for predicting self-reported workload ratings

## Preliminary Results

All results below are preliminary and should be interpreted in the context of the corresponding experimental pipeline.

### Participant-Level Workload Classification

The following results were obtained using the original spectral feature set and 5-fold GroupKFold evaluation.

| Model | Accuracy | Balanced Accuracy | F1-score |
|---|---:|---:|---:|
| Logistic Regression | 0.622 | 0.575 | 0.746 |
| SVM (RBF) | 0.622 | 0.575 | 0.746 |
| Random Forest | 0.578 | 0.550 | 0.678 |

The results indicate limited and model-dependent classification performance at the participant level.

### Alternative Feature Extraction Experiments

Additional feature extraction approaches were investigated to examine how preprocessing and spectral estimation choices affect classification performance.

The V2 and filtered feature sets produced different results from the original feature set. These experiments are exploratory and should not be interpreted as directly controlled comparisons because their feature extraction and modeling configurations differ.

### Recording Condition Classification

A separate experiment investigated the classification of low- versus high-workload recording conditions (`lo` and `hi`) using grouped cross-validation.

The Random Forest model achieved a balanced accuracy of approximately 0.773 ± 0.027 in this experiment.

**This result concerns recording-condition classification and is not the participant-level Moderate-versus-High workload classification result reported above.**

### Permutation Testing

An exploratory participant-level permutation test was conducted using 200 permutations.

- Observed balanced accuracy: approximately 0.58
- Permutation-test p-value: approximately 0.144

The test did not provide statistically significant evidence of classification performance above chance at the conventional 0.05 significance level.

### Exploratory Workload Regression

Ridge Regression was also investigated to predict continuous self-reported workload ratings from participant-level spectral features.

The original feature set with alpha = 1000 achieved:

- MAE: 1.423
- RMSE: 1.807
- Spearman correlation: 0.006

The mean baseline achieved an MAE of approximately 1.246 and an RMSE of approximately 1.432.

Ridge Regression did not outperform the mean baseline in these experiments. The results do not provide convincing evidence of reliable continuous workload prediction.

## Interpretation and Limitations

The experiments highlight several challenges in EEG-based cognitive workload recognition:

- Inter-subject variability can affect classification performance.
- Results may differ depending on the feature extraction and preprocessing strategy.
- Window-level and participant-level evaluation answer different research questions.
- The current participant-level classification results are exploratory and do not establish robust generalization to unseen individuals.
- The regression experiments did not demonstrate improvement over a simple mean baseline.
- Further validation with larger datasets and additional subject-wise evaluation protocols is necessary.

## Tools and Technologies

- Python 3.13.9
- NumPy
- Pandas
- SciPy
- scikit-learn
- Matplotlib

## Project Status

**Ongoing — Exploratory Research**

The project includes EEG preprocessing, spectral feature extraction, machine learning classification, participant-level evaluation, and exploratory statistical analyses.

Future work may investigate more robust participant-level evaluation, feature selection, alternative modeling approaches, and the integration of EEG-based cognitive state recognition into adaptive human–computer interaction systems.

## Research Relevance

Understanding cognitive workload from EEG signals may contribute to human-centered computing applications, including adaptive interfaces, affective computing, and cognitive-state-aware interaction.

This project provides an exploratory investigation of the opportunities and methodological challenges involved in EEG-based workload recognition.

---

*This repository documents an independent research project. All reported results are preliminary and are presented with their methodological limitations. The code and findings are intended for research and educational purposes.*
