import pandas as pd

def continent_filter(df,continent):
    if not column_exists(df, 'Continent_Ocean') or continent == 'all':
        return df
    continent_mask = mask(df, 'Continent_Ocean', [continent.lower()])
    return df[continent_mask]

def ecoregion_filter(df, ecoregion):
    if not column_exists(df, 'Ecoregion') or not apply_filter(ecoregion):
        return df
    eco_mask = mask(df, 'Ecoregion',ecoregion)
    return df[eco_mask]

def study_design_filter(df, study_design):
    if not column_exists(df, 'Study_design') or not apply_filter(study_design):
        return df
    study_design_mask = mask(df, 'Study_design',study_design)

    return df[study_design_mask]

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
    codes = split_by_semicolon(threat_codes)
    categories =extract_codes(codes)
    return categories

def split_by_semicolon(values):
    """Split by semicolon for multiple values"""
    return str(values).split(';')

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

def mask(df,column, search_value):
    """ Ensures that the filter still works if the row contains multiple values"""
    filter_mask = df[column].apply(
    lambda x: not set(search_value).isdisjoint(split_by_semicolon(x))
    )
    return filter_mask
