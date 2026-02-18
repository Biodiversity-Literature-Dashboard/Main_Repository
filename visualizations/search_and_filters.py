from dash import dcc

def create_search_bar():
    search_bar = dcc.Input(
        id='searchbar',
        placeholder = 'Search for articles',
        type = 'search',
        value = ''
    )
    return search_bar