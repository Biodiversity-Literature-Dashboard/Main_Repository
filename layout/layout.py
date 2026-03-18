# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html, dcc
import dash_bootstrap_components as dbc


# Local imports
from layout.components.navigation import navigation_bar
from layout.layoutviews import filters_view, table_view, charts_view, map_view

def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Filter sidebar (left side)
    top_bar = filters_view
    right_bar = map_view
    left_bar = table_view

    
    # Main content area (right side)
    
    # Combine sidebar + main content in a row
    main_container = dbc.Container([
        dbc.Row([
            # Left column: Filters (25% width)
            dbc.Col(top_bar, align= "start"),
        ],align="top"),
        dbc.Row([
            dbc.Col(right_bar),
            dbc.Col(left_bar),
        ]),
            dbc.Row([ #Delete later
            dbc.Col(charts_view)
        ]),

    ], fluid=True)
    
    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout
