import os
import sys
import sqlite3 as lite
from pathlib import Path
import pandas as pd

# Add parent directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import THREAT_CATEGORIES, THREAT_CODES
from utils.logic.filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter

def load_csv_data(csv):
    dataf = pd.read_csv(csv)
    dataf.columns = dataf.columns.str.strip()
    return dataf

def load_sql_data(connection,table):
    conn = lite.connect(connection)
    query = f"SELECT * FROM {table}; "
    dataf = pd.read_sql(query,conn)
    dataf.columns = dataf.columns.str.strip()
    conn.close()
    return dataf



# Load datasets on import
df = load_sql_data("./database/database.db","processed") # MAIN DATAFRAME


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


def filter_data(dataframe=df,continent='all', ecoregions=None, study_designs=None, threat_category='all'):
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
    dataf = dataframe.copy()
    dataf =continent_filter(dataf,continent)

    dataf= ecoregion_filter(dataf, ecoregions)

    dataf = study_design_filter(dataf, study_designs)

    dataf = threat_category_filter(dataf, threat_category)

    return dataf


# Test if run directly
if __name__ == "__main__":
    print(f"\nRidley: {len(df)} rows, {len(df.columns)} columns")
    print(f"   Columns: {df.columns.tolist()[:5]}")
