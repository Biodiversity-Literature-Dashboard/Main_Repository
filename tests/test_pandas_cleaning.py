import sqlite3 as lite
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "database"

conn = lite.connect(DATA_DIR/"database.db")

def test_database_folder_exists():
    assert DATA_DIR.exists(), f"Processed data folder not found: {DATA_DIR}"

def test_database_file_exists():
    # change filename if your repo uses a different name
    candidates = list(DATA_DIR.glob("**.db"))
    assert len(candidates) > 0, f"Database file found in {DATA_DIR}"

def test_processed_table_exists():
    query = "SELECT * FROM processed;"
    candidates = pd.read_sql(query,conn)
    assert len(candidates) > 0, f"No processed table found in {DATA_DIR}"

def test_all_needed_columns_exists():
    # checks if columns needed in the dashboard are present
    query = "SELECT * FROM processed;"
    df = pd.read_sql(query,conn)

    key_cols = ["ArticleID", "Authors", "Year", "Continent_Ocean", "Country_EEZ", "Study_design", "Direct_driver", "Indirect_driver","Georef_ind_driver","Threat","Title"]

    # check missing
    for c in key_cols:
        assert c in df.columns, f"Column {c} missing"

def test_no_missing_in_key_columns_if_present():
    # this is a “soft” test: checks only columns that exist
    query = "SELECT * FROM processed;"
    df = pd.read_sql(query,conn)

    key_cols = ["ArticleID", "Authors", "Year", "Continent_Ocean", "Country_EEZ", "Study_design", "Direct_driver", "Indirect_driver","Georef_ind_driver","Threat","Title"]
    existing = [c for c in key_cols if c in df.columns]

    # if none exist, test should fail because dataset doesn't match expectations
    assert len(existing) > 0, f"None of expected columns exist. Found columns: {list(df.columns)[:20]}"

    # check missing
    for c in existing:
        assert df[c].isna().sum() == 0, f"Column {c} has missing values"
