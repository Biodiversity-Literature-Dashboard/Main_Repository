import pandas as pd
from utils.data_loader import df_ridley_bib

def get_authors(df):
    return df['Authors']

def clean_authors(df):
    cleaned_df = df.replace({"_etal": " et al."},regex=True)
    return cleaned_df

def count_values(row):
    return row.value_counts()

def get_top_10(row_counted):
    return row_counted.head(10)

def top_10_authors(df):
    authors = get_authors(df)
    authors_counted = count_values(authors)
    top_authors = get_top_10(authors_counted)
    return pd.DataFrame({'Authors':top_authors.index, 'Count':top_authors.values})

def create_ridley_bib_table():
    df= df_ridley_bib[['Authors','Year','Title']]
    df =clean_authors(df)
    return df

ridley_bib_table = create_ridley_bib_table()


if __name__ == "__main__":
    print(create_ridley_bib_table())