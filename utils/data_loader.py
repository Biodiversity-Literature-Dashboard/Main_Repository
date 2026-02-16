# Data loading utilities
# Functions to load and process data from various sources (CSV, Excel, databases)
import pandas as pd
import os
import sys

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import GROSSI_CSV, RIDLEY_CSV


def load_grossi_data():
    """Load processed Grossi dataset (cleaned, included articles only)"""
    df = pd.read_csv(GROSSI_CSV)
    df.columns = df.columns.str.strip()
    return df


def load_ridley_data():
    """Load processed Ridley dataset (article-level data for dashboard)"""
    df = pd.read_csv(RIDLEY_CSV)
    df.columns = df.columns.str.strip()
    return df


# Load datasets on import
df_grossi = load_grossi_data()
df_ridley = load_ridley_data()

# Keep old names for backward compatibility
df1 = df_grossi
df2 = df_ridley

# Test if run directly
if __name__ == "__main__":
    print(f"Grossi: {len(df_grossi)} rows, {len(df_grossi.columns)} columns")
    print(f"   Columns: {df_grossi.columns.tolist()[:5]}")
    print(f"\nRidley: {len(df_ridley)} rows, {len(df_ridley.columns)} columns")
    print(f"   Columns: {df_ridley.columns.tolist()[:5]}")
