import pandas as pd
from utils.data_loader import df1,df2

def get_authors(df):
    return df['Authors']

def count_values(row):
    return row.value_counts()

def get_top_10(row_counted):
    return row_counted.head(10)

def top_10_authors():
    authors = get_authors(df2)
    authors_counted = count_values(authors)
    top_authors = get_top_10(authors_counted)
    return pd.DataFrame({'Authors':top_authors.index, 'Count':top_authors.values})


#print(top_10_authors())