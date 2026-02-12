# Data loading utilities
# Functions to load and process data from various sources (CSV, Excel, databases)
import pandas as pd


def load_data(file_path, sheet_name=0):
    """Load data from csv file"""
    return pd.read_csv(file_path)


# Load datasets 
df1 = load_data('data/Grossi_et_al_Piloted_data_extraction_strategy.csv')
df2 = load_data('data/Ridley_et_al_13750_2022_279_MOESM4_ESM.csv')