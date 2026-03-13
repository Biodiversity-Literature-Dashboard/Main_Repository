import pandas as pd

def continent_filter(df,continent):
    if not column_exists(df, 'Continent_Ocean') or continent == 'all':
        return df
    return df[df['Continent_Ocean'].str.lower() == continent.lower()]

def ecoregion_filter(df, ecoregions):
    if not column_exists(df, 'Ecoregion') or not apply_filter(ecoregions):
        return df
    eco_mask = df['Ecoregion'].apply(
        lambda x: any(eco in str(x) for eco in ecoregions) if pd.notna(x) else False
    )
    return df[eco_mask]

def study_design_filter(df, study_designs):
    if not column_exists(df, 'Study_design') or not apply_filter(study_designs):
        return df
    return df[df['Study_design'].isin(study_designs)]

def threat_category_filter(df, threat_category):
    if not column_exists(df, 'Threat') or threat_category=='all':
        return df
    threat_mask = df['Threat'].apply(
        lambda x: threat_category in extract_threat_category_from_code(x) if pd.notna(x) else False
    )
    return df[threat_mask]

def column_exists(df,column):
    column_exists = column in df.columns
    if not column_exists:
        print(f'Error: {column} column missing or not found')
    return column_exists

def apply_filter(df_filter):
    #check if filter should be applied
    return df_filter and len(df_filter) > 0

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