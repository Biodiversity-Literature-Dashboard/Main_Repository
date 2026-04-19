import pandas as pd
from utils.data_loader import df

def get_authors(df):
    return df['Authors']

def clean_authors(df):
    cleaned_df = df.replace({"_etal": " et al."}, regex=True)
    return cleaned_df

def count_values(row):
    return row.value_counts()

def get_top_10(row_counted):
    return row_counted.head(10)

def top_10_authors(df):
    authors = get_authors(df)
    authors_counted = count_values(authors)
    top_authors = get_top_10(authors_counted)
    return pd.DataFrame({'Authors': top_authors.index, 'Count': top_authors.values})

def create_ridley_bib_table():
    table_df = df[['Authors', 'Year', 'Title', 'Georef_ind_driver_clean', 'Direct_driver_clean', 'Indirect_driver_clean']].copy()
    table_df = clean_authors(table_df)
    return table_df

ridley_bib_table = create_ridley_bib_table()

if __name__ == "__main__":
    print(create_ridley_bib_table())