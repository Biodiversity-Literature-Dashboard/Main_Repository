
from dash import dash_table
import datetime

#import pandas as pd

from sections.dataframes import ridley_bib_table

def articles_datatable(df):
    table = dash_table.DataTable(
    id ='article_table',
    columns=[
        {'name': 'Authors', 'id': 'Authors', 'type': 'text'},
        {'name': 'Year', 'id': 'Year', 'type': 'numeric'},
        {'name': 'Title', 'id': 'Title', 'type': 'text'},
    ],
    data=df.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
    )
    return table

articles_datatable = articles_datatable(ridley_bib_table)

