import dash_bootstrap_components as dbc
from dash import dcc


from utils.data_loader import df_grossi, get_threat_categories



# SEARCH BARS



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


search_bar = create_search_bar()



# DROPDOWN FILTERS





def create_continent_filter():
    # Continent filter
    continent_filter = dcc.Dropdown(
        id='continent-filter',
        options=[{'label': 'All', 'value': 'all'}] + 
                [{'label': cont.title(), 'value': cont} 
                    for cont in sorted(df_grossi['Continent_Ocean'].dropna().unique())],
        value='all',
        clearable=False,
        className="mb-3"
    )
    return continent_filter


def create_threat_category_filter():
    threat_category_filter = dcc.Dropdown(
        id='threat-category-filter',
        options=[{'label': 'All Categories', 'value': 'all'}] + 
                [{'label': f"{cat[0]}. {cat[1]}", 'value': cat[0]} 
                    for cat in get_threat_categories()],
        value='all',
        clearable=False,
        className="mb-3"
    )
    return threat_category_filter


continent_filter = create_continent_filter()
threat_category_filter = create_threat_category_filter()



# CHECKBOX FILTERS



def create_ecoregion_filter():
    ecoregion_filter = dcc.Checklist(
        id='ecoregion-filter',
        options=[
            {'label': ' Terrestrial', 'value': 'Terrestrial'},
            {'label': ' Marine', 'value': 'Marine'},
            {'label': ' Freshwater', 'value': 'Freshwater'}
        ],
        value=['Terrestrial', 'Marine', 'Freshwater'],  # All selected by default
        className="mb-3"
    )
    return ecoregion_filter

def create_study_design_filter():
        study_design_filter = dcc.Checklist(
            id='study-design-filter',
            options=[
                {'label': ' Observational', 'value': 'Observational'},
                {'label': ' Experimental', 'value': 'Experimental'}
            ],
            value=['Observational', 'Experimental'],  # All selected by default
            className="mb-3"
        )
        return study_design_filter

ecoregion_filter = create_ecoregion_filter()
study_design_filter = create_study_design_filter()