import pandas as pd

df = pd.read_csv("data/processed/ridley_articles_dashboard_cleaned.csv")

print("Cleaned dataset shape:", df.shape)

print("\nCheck cleaned columns exist:")
for col in ["Georef_ind_driver_clean", "Direct_driver_clean", "Indirect_driver_clean"]:
    print(f"{col}: {col in df.columns}")

print("\nPreview:")
print(df[[
    "ArticleID",
    "Georef_ind_driver", "Georef_ind_driver_clean",
    "Direct_driver", "Direct_driver_clean",
    "Indirect_driver", "Indirect_driver_clean"
]].head(10))