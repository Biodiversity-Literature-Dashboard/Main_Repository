from pathlib import Path
import pandas as pd
import os
import sys

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import GROSSI_CSV, RIDLEY_CSV, THREAT_CATEGORIES, THREAT_CODES, RIDLEY_BIB
from utils.logic.filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter

def load_csv_data(csv):
    df = pd.read_csv(csv)
    df.columns = df.columns.str.strip()
    return df

# Load datasets on import
df_grossi = load_csv_data(GROSSI_CSV)
df_ridley = load_csv_data(RIDLEY_CSV)
df_ridley_bib = load_csv_data(RIDLEY_BIB)

# Keep old names for backward compatibility
df1 = df_grossi
df2 = df_ridley


def get_threat_categories():
    """
    Get main threat categories from JSON configuration.
    Returns list of tuples: (category_number, category_name)
    
    Note: Currently returns main categories only (from threat_codes.json). 
    TODO: Add option to return specific subcategories (48 codes) for detailed filtering
    """
    # Convert dict to sorted list of tuples
    categories = [(k, v) for k, v in THREAT_CATEGORIES.items()]
    # Sort by category number (some are strings like '11', '12')
    categories.sort(key=lambda x: int(x[0]))
    return categories


def get_threat_code_descriptions():
    """
    Get all 48 detailed threat codes and their descriptions.
    Returns dict of threat codes (e.g., '2.1:AgNTC') mapped to descriptions.
    """
    return THREAT_CODES


def extract_threat_category_from_code(threat_code):
    """
    Extract main category number from threat code.
    Example: '6.3:Other' -> '6', '2.1:AgNTC;9.5:PollAir' -> ['2', '9']
    """
    if pd.isna(threat_code):
        return []
    
    categories = set()
    # Split by semicolon for multiple threats
    codes = str(threat_code).split(';')
    for code in codes:
        # Extract number before the dot
        if '.' in code:
            category = code.split('.')[0].strip()
            categories.add(category)
    
    return sorted(list(categories))


def filter_data(df=df_ridley,continent='all', ecoregions=None, study_designs=None, threat_category='all'):
    """
    Filter Grossi dataset based on user selections.
    Uses INCLUSIVE filtering (OR logic) for multi-value fields.

    Args:
        continent: String continent/ocean name or 'all'
        ecoregions: List of ecoregion values to include (e.g., ['Terrestrial', 'Marine'])
        study_designs: List of study designs to include (e.g., ['Observational'])
        threat_category: Threat category number (1-12) or 'all'

    Returns:
        Filtered dataframe
    """
    df = df.copy()
    print(f"dataframe shape (rows,colums) {str(df.shape)}")

    df =continent_filter(df,continent)

    df= ecoregion_filter(df, ecoregions)

    df = study_design_filter(df, study_designs)

    df = threat_category_filter(df, threat_category)

    return df


# Test if run directly
if __name__ == "__main__":
    print(f"Grossi: {len(df_grossi)} rows, {len(df_grossi.columns)} columns")
    print(f"   Columns: {df_grossi.columns.tolist()[:5]}")
    print(f"\nRidley: {len(df_ridley)} rows, {len(df_ridley.columns)} columns")
    print(f"   Columns: {df_ridley.columns.tolist()[:5]}")
