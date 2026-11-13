
from pathlib import Path

import pandas as pd

from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from config import (
    PROJECT_ROOT,
    DATASET_DIR,
    CLASSIFICATION_DIR,
)

project_dir = PROJECT_ROOT
base_dir = DATASET_DIR.parent

# Load previously extracted spectral features
features = pd.read_csv(project_dir / "eeg_features.csv")

# Find the ratings file
rating_files = list(base_dir.rglob("ratings.txt"))
if not rating_files:
    raise FileNotFoundError("ratings.txt was not found")

ratings = pd.read_csv(
    rating_files[0],
    header=None,
    names=["subject", "rest_rating", "task_rating"],
    skipinitialspace=True
)

ratings = ratings.dropna(subset=["subject", "task_rating"])
ratings["subject"] = ratings["subject"].astype(int)
ratings["task_rating"] = pd.to_numeric(
    ratings["task_rating"], errors="coerce"
)
ratings = ratings.dropna(subset=["task_rating"])

# Keep only multitasking recordings and participants with ratings
df = features[features["condition"] == "hi"].merge(
    ratings[["subject", "task_rating"]],
    on="subject",
    how="inner"
)

# 0 = moderate workload (ratings 4-6)
# 1 = high workload (ratings 7-9)
df = df[df["task_rating"].between(4, 9)].copy()
df["target"] = (df["task_rating"] >= 7).astype(int)

feature_cols = [
    col for col in df.columns
    if col.endswith(("_theta", "_alpha", "_beta"))
]

X = df[feature_cols]
y = df["target"]
groups = df["subject"]

print("EEG windows:", len(df))
print("Participants:", groups.nunique())
print("\nParticipant-level rating counts:")
print(
    ratings[ratings["subject"].isin(groups.unique())]
    .assign(
        category=lambda x: x["task_rating"].apply(
            lambda v: "High (7-9)" if v >= 7 else "Moderate (4-6)"
        )
    )
    .groupby("category")["subject"]
    .nunique()
)

cv = GroupKFold(n_splits=5)

models = {
    "Logistic Regression": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        LogisticRegression(max_iter=2000)
    ),
    "SVM (RBF)": make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler(),
        SVC(kernel="rbf")
    ),
    "Random Forest": make_pipeline(
        SimpleImputer(strategy="median"),
        RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        )
    )
}

results = []

for name, model in models.items():
    print(f"\nEvaluating {name}...")

    # Every participant is held out from training in their test fold.
    window_predictions = cross_val_predict(
        model,
        X,
        y,
        groups=groups,
        cv=cv,
        n_jobs=-1,
        method="predict"
    )

    # Combine window predictions into one prediction per participant.
    evaluation = pd.DataFrame({
        "subject": groups.to_numpy(),
        "true": y.to_numpy(),
        "predicted": window_predictions
    })

    participant_results = evaluation.groupby("subject").agg(
        true=("true", "first"),
        predicted=("predicted", lambda s: int(s.mean() >= 0.5))
    )

    true = participant_results["true"]
    pred = participant_results["predicted"]

    accuracy = accuracy_score(true, pred)
    balanced = balanced_accuracy_score(true, pred)
    f1 = f1_score(true, pred, zero_division=0)

    results.append({
        "model": name,
        "participants": len(participant_results),
        "accuracy": accuracy,
        "balanced_accuracy": balanced,
        "f1": f1
    })

    print("Participant-level accuracy:", round(accuracy, 3))
    print("Balanced accuracy:", round(balanced, 3))
    print("F1:", round(f1, 3))
    print("\nConfusion matrix (rows=true, columns=predicted):")
    print(confusion_matrix(true, pred, labels=[0, 1]))
    print("\nClassification report:")
    print(classification_report(
        true,
        pred,
        labels=[0, 1],
        target_names=["Moderate", "High"],
        zero_division=0
    ))

results_df = pd.DataFrame(results)
output_path = CLASSIFICATION_DIR / "workload_model_results.csv"
results_df.to_csv(output_path, index=False)

print("\n=== Model comparison ===")
print(results_df.round(3).to_string(index=False))
print("\nSaved results to:", output_path)

