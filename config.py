
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent

DATASET_DIR = Path(
    os.environ.get(
        "STEW_DATA_DIR",
        str(Path.home() / "Documents" / "STEW" / "STEW Dataset")
    )
).expanduser()

RESULTS_DIR = PROJECT_ROOT / "results"
FEATURES_DIR = RESULTS_DIR / "features"
CLASSIFICATION_DIR = RESULTS_DIR / "classification"
REGRESSION_DIR = RESULTS_DIR / "regression"
FIGURES_DIR = RESULTS_DIR / "figures"

for directory in [
    RESULTS_DIR,
    FEATURES_DIR,
    CLASSIFICATION_DIR,
    REGRESSION_DIR,
    FIGURES_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

