
import sqlite3 as lite
import pandas as pd

CONNECT_PATH = "./database/database.db"

conn = lite.connect(CONNECT_PATH)
cursor = conn.cursor()

def merge_title(bib_table,completed_table):
    """Change table to be the name of the table containing Title row"""
    query = (f"SELECT  * FROM {bib_table}; ")
    bib = pd.read_sql(query,conn)
    query2 = (f"SELECT  * FROM {completed_table}; ")
    completed_table = pd.read_sql(query2,conn)

    bib.columns = bib.columns.str.strip()

    # Clean column names (handles weird spaces like "Year ")
    bib.columns = bib.columns.str.strip()
    completed_table.columns = completed_table.columns.str.strip()

    # Keep only ArticleID + Title from bibliography
    bib_small = bib[["ArticleID", "Title"]].drop_duplicates(subset=["ArticleID"])

    # Merge Title into processed ridley
    out = completed_table.merge(bib_small, on="ArticleID", how="left")

    print("Title added:", "Title" in out.columns)
    print("Missing Title %:", out["Title"].isna().mean())
    print(out[["ArticleID", "Title"]].head(5))

    # Save back to the processed file
    out.to_sql("processed", conn)


if __name__ == "__main__":
    merge_title("Full_Bibliography", "Completed_data_collection_tool")