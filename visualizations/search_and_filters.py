import dash_bootstrap_components as dbc

def create_search_bar():
    search_bar = dbc.Row(
        [
            dbc.Col(dbc.Input(id = "searchbar", 
            type="search", 
            debounce = True,
            placeholder="Search articles")),
            dbc.Col(
                dbc.Button("Search", 
                color="primary", 
                className="ms-2", 
                n_clicks=0),
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="right",
    )
    return search_bar