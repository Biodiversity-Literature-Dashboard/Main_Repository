import pandas as pd

BIB_PATH = r"data\Ridley_bibliography.csv"
PROCESSED_PATH = r"data\processed\ridley_articles_dashboard.csv"

bib = pd.read_csv(BIB_PATH)
rid = pd.read_csv(PROCESSED_PATH)

# Clean column names (handles weird spaces like "Year ")
bib.columns = bib.columns.str.strip()
rid.columns = rid.columns.str.strip()

# Keep only ArticleID + Title from bibliography
bib_small = bib[["ArticleID", "Title"]].drop_duplicates(subset=["ArticleID"])

# Merge Title into processed ridley
out = rid.merge(bib_small, on="ArticleID", how="left")

print("Title added:", "Title" in out.columns)
print("Missing Title %:", out["Title"].isna().mean())
print(out[["ArticleID", "Title"]].head(5))

# Save back to the processed file
out.to_csv(PROCESSED_PATH, index=False)
print("Saved:", PROCESSED_PATH)