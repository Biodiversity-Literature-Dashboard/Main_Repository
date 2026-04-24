from dash import dash_table

from utils.dataframes import bib_table

def articles_datatable(df,side):
    table = dash_table.DataTable(
    id ='article_table'+side,
    columns=[
        {'name': 'Authors', 'id': 'Authors', 'type': 'text'},
        {'name': 'Year', 'id': 'Year', 'type': 'numeric'},
        {'name': 'Title', 'id': 'Title', 'type': 'text'},
        {'name': 'Georef Indirect Driver', 'id': 'Georef_ind_driver_clean', 'type': 'text'},
        {'name': 'Direct Driver', 'id': 'Direct_driver_clean', 'type': 'text'},
        {'name': 'Indirect Driver', 'id': 'Indirect_driver_clean', 'type': 'text'},
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
        {'if': {'column_id': 'Georef_ind_driver_clean'},
         'width': '120px',
         'maxWidth': '200px',
         'minWidth': '120px'},
        {'if': {'column_id': 'Direct_driver_clean'},
         'width': '120px',
         'maxWidth': '200px',
         'minWidth': '120px'},
        {'if': {'column_id': 'Indirect_driver_clean'},
         'width': '120px',
         'maxWidth': '200px',
         'minWidth': '120px'},
    ],
    tooltip_data =[],# start with empty tooltip data, will be populated by callback
    tooltip_duration = None #tooltip stays until user moves mouse away
    )
    return table

articles_datatable_right = articles_datatable(bib_table, "_right")
articles_datatable_left = articles_datatable(bib_table, "_left")
