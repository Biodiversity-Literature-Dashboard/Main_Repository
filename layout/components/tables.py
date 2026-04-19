from dash import dash_table

from sections.dataframes import ridley_bib_table

def articles_datatable(df, side):
    table = dash_table.DataTable(
        id='article_table' + side,
        columns=[
            {'name': 'Authors', 'id': 'Authors', 'type': 'text'},
            {'name': 'Year', 'id': 'Year', 'type': 'numeric'},
            {'name': 'Title', 'id': 'Title', 'type': 'text'},
            {'name': 'Georeferenced Indirect Driver', 'id': 'Georef_ind_driver_clean', 'type': 'text'},
            {'name': 'Direct Drivers', 'id': 'Direct_driver_clean', 'type': 'text'},
            {'name': 'Indirect Drivers', 'id': 'Indirect_driver_clean', 'type': 'text'},
        ],
        data=df.to_dict('records'),
        filter_action='native',
        page_size=15,
        style_table={
            'height': 500,
            'overflowY': 'scroll',
            'overflowX': 'auto',
        },
        style_data={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
        style_cell_conditional=[
            {'if': {'column_id': 'Authors'},
             'width': '100px',
             'maxWidth': '120px',
             'minWidth': '100px'},
            {'if': {'column_id': 'Year'},
             'width': '50px',
             'maxWidth': '60px',
             'minWidth': '50px'},
            {'if': {'column_id': 'Title'},
             'width': '220px',
             'maxWidth': '300px',
             'minWidth': '180px'},
            {'if': {'column_id': 'Georef_ind_driver_clean'},
             'width': '250px',
             'maxWidth': '250px',
             'minWidth': '180px'},
            {'if': {'column_id': 'Direct_driver_clean'},
             'width': '230px',
             'maxWidth': '320px',
             'minWidth': '200px'},
            {'if': {'column_id': 'Indirect_driver_clean'},
             'width': '260px',
             'maxWidth': '360px',
             'minWidth': '220px'},
        ],
        tooltip_data=[],  # start with empty tooltip data, will be populated by callback
        tooltip_duration=None  # tooltip stays until user moves mouse away
    )
    return table

articles_datatable_right = articles_datatable(ridley_bib_table, "_right")
articles_datatable_left = articles_datatable(ridley_bib_table, "_left")