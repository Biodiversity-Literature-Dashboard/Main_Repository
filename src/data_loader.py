import pandas as pd


def load_data(file_path, sheet_name=0):
    """Load data from Excel file"""
    return pd.read_excel(file_path, sheet_name=sheet_name)


# Load datasets 
# here we are extracting just the 'Data extraction' sheet from grossi dataset.
df1 = load_data('../data/Grossi_et_al._Piloted_data_extraction_strategy.xlsx', sheet_name='Data extraction')
df2 = load_data('../data/Ridley_et_al_13750_2022_279_MOESM4_ESM.xlsx')
