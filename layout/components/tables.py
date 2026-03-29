
from dash import dash_table

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
    page_size = 15, # show 15 rows per page
    style_table={
        'height': 500,
        'overflowY': 'scroll',
    },
    style_data={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    },
    style_cell_conditional=[
        {'if': {'column_id': 'Authors'},
         'width': '100px',
         'maxWidth': '100px',
         'minWidth': '100px'},
        {'if': {'column_id': 'Year'},
         'width': '30px',
         'maxWidth': '30px',
         'minWidth': '30px'},
        {'if': {'column_id': 'Title'},
         'width': '100px',
         'maxWidth': '200px',
         'minWidth': '100px'},
    ],
    tooltip_data =[],# start with empty tooltip data, will be populated by callback
    tooltip_duration = None #tooltip stays until user moves mouse away
    )
    return table

articles_datatable = articles_datatable(ridley_bib_table)

