import pandas as pd

project_file = "data/processed/ridley_articles_dashboard.csv"
client_file = r"C:\Users\IamAb\Downloads\Ridley_et_al_13750_2022_279_MOESM4_ESM(Completed data collection tool).csv"
output_file = "data/processed/ridley_articles_dashboard_updated.csv"

project_df = pd.read_csv(project_file)
client_df = pd.read_csv(client_file)

# Keep only needed columns from client file
client_subset = client_df[["ArticleID", "Georef_ind_driver", "Direct_driver", "Indirect_driver"]].copy()

# Make sure ArticleID type matches
project_df["ArticleID"] = project_df["ArticleID"].astype(str)
client_subset["ArticleID"] = client_subset["ArticleID"].astype(str)

# Merge into project dataset
merged_df = project_df.merge(client_subset, on="ArticleID", how="left")

# Save
merged_df.to_csv(output_file, index=False)

print("Original project rows:", len(project_df))
print("Merged rows:", len(merged_df))
print("\nNew columns present:")
print("Georef_ind_driver:", "Georef_ind_driver" in merged_df.columns)
print("Direct_driver:", "Direct_driver" in merged_df.columns)
print("Indirect_driver:", "Indirect_driver" in merged_df.columns)
print("\nMissing values in new columns:")
print(merged_df[["Georef_ind_driver", "Direct_driver", "Indirect_driver"]].isna().sum())