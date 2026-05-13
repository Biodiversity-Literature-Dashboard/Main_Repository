import pandas as pd
from utils.data_loader import df

def test_article_id_unique():
    assert df["ArticleID"].is_unique

def test_no_empty_filter_values():
    for col in ["Study_design", "Ecoregion", "Continent_Ocean", "country_eez"]:
        if col in df.columns:
            assert df[col].notna().all()
            assert (df[col].astype(str).str.strip() != "").all()
