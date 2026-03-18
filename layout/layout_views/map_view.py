
from dash import html
import dash_bootstrap_components as dbc

from layout.components.maps import empty_map

def map_view():
    map_container = dbc.CardBody([
            # Result counter
            html.Div(
                id='result-counter',
                children="Showing 15 of 15 articles",
                className="mb-2",
                style={'fontSize': '14px', 'color': '#666', 'fontWeight': '500'}
            ),
            
            # Map section
            html.H5("Study Locations Map", className="mb-3"),
            empty_map,
    ])
    return map_container

map_view = map_view()