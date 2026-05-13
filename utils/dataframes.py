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


def bib_table(df):
    df = df[['Authors', 'Year', 'Title']]
    df = clean_authors(df)
    return df


bib_table = bib_table(df)


if __name__ == "__main__":
    print(bib_table)
