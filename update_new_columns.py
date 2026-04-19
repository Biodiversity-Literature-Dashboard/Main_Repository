import pandas as pd

# File paths
project_file = "data/processed/ridley_articles_dashboard.csv"
client_file = r"C:\Users\IamAb\Downloads\Ridley_et_al_13750_2022_279_MOESM4_ESM(Completed data collection tool).csv"
output_file = "data/processed/ridley_articles_dashboard_updated.csv"

# Load datasets
project_df = pd.read_csv(project_file)
client_df = pd.read_csv(client_file)

# Keep only the needed columns from client file
client_subset = client_df[[
    "ArticleID",
    "Georef_ind_driver",
    "Direct_driver",
    "Indirect_driver"
]].copy()

# Remove duplicate ArticleID rows if they exist
client_subset = client_subset.drop_duplicates(subset="ArticleID")

# Merge safely by ArticleID
merged_df = project_df.merge(client_subset, on="ArticleID", how="left")

# Save as a NEW file
merged_df.to_csv(output_file, index=False)

print("Updated file saved to:", output_file)
print("Original project rows:", len(project_df))
print("Merged rows:", len(merged_df))
print("\nNew columns present:")
for col in ["Georef_ind_driver", "Direct_driver", "Indirect_driver"]:
    print(f"{col}: {col in merged_df.columns}")

print("\nMissing values in new columns:")
print(merged_df[["Georef_ind_driver", "Direct_driver", "Indirect_driver"]].isna().sum())