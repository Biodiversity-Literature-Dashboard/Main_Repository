import sqlite3 as lite
import pandas as pd
import json

conn = lite.connect("./database/database.db")
query = """SELECT *
        FROM Data_Dissagregated;
        """
# Load original Ridley dataset with threat columns
df = pd.read_sql(query,conn)

# Load threat decoding mappings
with open("data/processed/threat_codes.json", "r", encoding="utf-8") as f:
    threat_data = json.load(f)

threat_codes = threat_data["threat_codes"]
threat_categories = threat_data["threat_categories"]

# Select threat-related columns
threat_df = df[
    [
        "ArticleID",
        "Threat",
        "Threat1",
        "Threat_metric",
        "Threat_data",
        "Quantity_threats",
        "threat_precision",
        "threat_database",
    ]
].copy()

# Clean text columns
for col in ["Threat", "Threat1", "Threat_metric", "Threat_data", "threat_precision", "threat_database"]:
    if col in threat_df.columns:
        threat_df[col] = threat_df[col].astype(str).str.strip()

# Remove rows where both Threat and Threat1 are missing/empty
threat_df = threat_df[
    ~(
        threat_df["Threat"].replace("nan", "").eq("") &
        threat_df["Threat1"].replace("nan", "").eq("")
    )
].copy()

# Fix known raw-code typos/format issues before decoding
threat_df["Threat"] = threat_df["Threat"].replace({
    "2.5:AgUncpec": "2.5:AgUnspec",
    "4.5.UnspecLine": "4.5:UnspecLine"
})

# Decode full threat code (e.g. 2.3:AgLivestock -> Livestock Farming & Ranching)
threat_df["Threat_decoded"] = threat_df["Threat"].map(threat_codes)

# Decode high-level threat category (e.g. 2 -> Agriculture & Aquaculture)
threat_df["Threat1_decoded"] = threat_df["Threat1"].astype(str).map(threat_categories)

# Save clean processed dataframe
threat_df.to_sql("Threats_Clean", conn, index=False)

conn.close()

print("Saved Threats_Clean")
print(threat_df.head())
print("Columns:", threat_df.columns.tolist())
print("Rows:", len(threat_df))
print("Missing decoded Threat labels:", threat_df["Threat_decoded"].isna().sum())