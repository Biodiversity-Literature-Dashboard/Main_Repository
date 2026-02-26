import pandas as pd

PATH = "data/processed/ridley_articles_dashboard.csv"

def test_article_id_unique():
    df = pd.read_csv(PATH)
    assert df["ArticleID"].is_unique

def test_no_empty_filter_values():
    df = pd.read_csv(PATH)
    for col in ["Study_design", "Ecoregion", "Continent_Ocean", "country_eez"]:
        if col in df.columns:
            assert df[col].notna().all()
            assert (df[col].astype(str).str.strip() != "").all()
