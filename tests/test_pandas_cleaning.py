import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

def test_processed_folder_exists():
    assert DATA_DIR.exists(), f"Processed data folder not found: {DATA_DIR}"

def test_ridley_processed_csv_exists():
    # change filename if your repo uses a different name
    candidates = list(DATA_DIR.glob("*ridley*.csv"))
    assert len(candidates) > 0, f"No Ridley processed CSV found in {DATA_DIR}"

def test_grossi_processed_csv_exists():
    candidates = list(DATA_DIR.glob("*grossi*.csv"))
    assert len(candidates) > 0, f"No Grossi processed CSV found in {DATA_DIR}"

def test_ridley_csv_loads_and_has_rows():
    ridley_file = list(DATA_DIR.glob("*ridley*.csv"))[0]
    df = pd.read_csv(ridley_file)
    assert len(df) > 0, "Ridley dataframe is empty"

def test_no_missing_in_key_columns_if_present():
    # this is a “soft” test: checks only columns that exist
    ridley_file = list(DATA_DIR.glob("*ridley*.csv"))[0]
    df = pd.read_csv(ridley_file)

    key_cols = ["ArticleID", "Country", "Continent_Ocean", "country_eez"]
    existing = [c for c in key_cols if c in df.columns]

    # if none exist, test should fail because dataset doesn't match expectations
    assert len(existing) > 0, f"None of expected columns exist. Found columns: {list(df.columns)[:20]}"

    # check missing
    for c in existing:
        assert df[c].isna().sum() == 0, f"Column {c} has missing values"