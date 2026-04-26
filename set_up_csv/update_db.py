import sqlite3
import pandas as pd

# Load driver columns from CSV
df_csv = pd.read_csv('data/processed/ridley_articles_dashboard_cleaned.csv')
df_csv['ArticleID'] = df_csv['ArticleID'].astype(str)
driver_cols = df_csv[['ArticleID', 'Direct_driver_clean', 'Indirect_driver_clean']].copy()

conn = sqlite3.connect('database/database.db')
cur = conn.cursor()

# Check if columns already exist
cur.execute("PRAGMA table_info(processed)")
existing_cols = [row[1] for row in cur.fetchall()]
print("Existing columns:", existing_cols)

# Add columns if they don't exist
if 'Direct_driver_clean' not in existing_cols:
    cur.execute("ALTER TABLE processed ADD COLUMN Direct_driver_clean TEXT")
    print("Added Direct_driver_clean")
if 'Indirect_driver_clean' not in existing_cols:
    cur.execute("ALTER TABLE processed ADD COLUMN Indirect_driver_clean TEXT")
    print("Added Indirect_driver_clean")

conn.commit()

# Update each row
updated = 0
for _, row in driver_cols.iterrows():
    cur.execute(
        "UPDATE processed SET Direct_driver_clean=?, Indirect_driver_clean=? WHERE CAST(ArticleID AS TEXT)=?",
        (row['Direct_driver_clean'], row['Indirect_driver_clean'], row['ArticleID'])
    )
    updated += cur.rowcount

conn.commit()
conn.close()
print(f"Updated {updated} rows")

# Verify
conn2 = sqlite3.connect('database/database.db')
df_check = pd.read_sql("SELECT ArticleID, Direct_driver_clean, Indirect_driver_clean FROM processed WHERE Direct_driver_clean IS NOT NULL LIMIT 3", conn2)
conn2.close()
print(df_check.to_string())
