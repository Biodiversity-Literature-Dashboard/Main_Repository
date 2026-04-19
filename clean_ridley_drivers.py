import pandas as pd

# Use the updated merged dataset as input
input_file = "data/processed/ridley_articles_dashboard_updated.csv"
output_file = "data/processed/ridley_articles_dashboard_cleaned.csv"

df = pd.read_csv(input_file)

def clean_georef(value):
    if pd.isna(value):
        return "Unknown"

    value = str(value).strip().lower()

    if value == "1":
        return "Yes"
    elif value == "0":
        return "No"
    elif value == "na":
        return "Unknown"
    elif ";" in value:
        return "Mixed"
    else:
        return "Unknown"

def clean_driver_text(value):
    if pd.isna(value):
        return "Unknown"

    value = str(value).strip().lower()
    if value == "na":
        return "Unknown"

    value = value.replace("_", " ")
    value = value.replace(";", ", ")
    return value

# Create cleaned columns without overwriting raw source columns
df["Georef_ind_driver_clean"] = df["Georef_ind_driver"].apply(clean_georef)
df["Direct_driver_clean"] = df["Direct_driver"].apply(clean_driver_text)
df["Indirect_driver_clean"] = df["Indirect_driver"].apply(clean_driver_text)

# Save cleaned dataset as a NEW file
df.to_csv(output_file, index=False)

print("Cleaned file saved to:", output_file)
print("\nPreview of cleaned columns:")
print(df[[
    "Georef_ind_driver", "Georef_ind_driver_clean",
    "Direct_driver", "Direct_driver_clean",
    "Indirect_driver", "Indirect_driver_clean"
]].head(10))