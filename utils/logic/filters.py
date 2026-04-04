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
        print(study_designs)
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
    c_exists = column in df.columns
    if not c_exists:
        print(f'Error: {column} column missing or not found')
    return c_exists

def apply_filter(df_filter):
    """check if filter should be applied"""
    return df_filter and len(df_filter) > 0

def extract_threat_category_from_code(threat_codes):
    """
    Extract main category number from threat code.
    Example: '6.3:Other' -> '6', '2.1:AgNTC;9.5:PollAir' -> ['2', '9']
    """
    if pd.isna(threat_codes):
        return []
    codes = split_threat_codes(threat_codes)
    categories =extract_codes(codes)
    return categories

def split_threat_codes(threat_codes):
    """Split by semicolon for multiple threats"""
    return str(threat_codes).split(';')

def extract_codes(codes):
    """For loop for extracting threat categories"""
    categories = set()
    for code in codes:
        categories = number_before_dot(code,categories)
    return to_sorted_list(categories)

def to_sorted_list(categories):
    return sorted(list(categories))

def number_before_dot(code,categories):
    """ Extract number before the dot and add it to categories"""
    if '.' in code:
        category = code.split('.')[0].strip()
        categories.add(category)
    return categories
