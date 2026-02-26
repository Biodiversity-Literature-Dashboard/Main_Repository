from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

RIDLEY_PATH = PROCESSED_DIR / "ridley_articles_dashboard.csv"
GROSSI_PATH = PROCESSED_DIR / "grossi_included_clean.csv"


def _check_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}. Did you create it in data/processed?")


def load_ridley() -> pd.DataFrame:
    _check_exists(RIDLEY_PATH)
    return pd.read_csv(RIDLEY_PATH)


def load_grossi() -> pd.DataFrame:
    _check_exists(GROSSI_PATH)
    return pd.read_csv(GROSSI_PATH)