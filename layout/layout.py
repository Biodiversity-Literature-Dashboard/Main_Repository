# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html
import dash_bootstrap_components as dbc


# Local imports
from layout.components.info_button import info_button
from layout.components.navigation import navigation_bar
from layout.layoutviews import left_view,right_view, filters_view
def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Filter sidebar (left side)
    top_bar = filters_view
    right_bar = right_view
    left_bar = left_view

    
    # Main content area (right side)
    
    # Combine sidebar + main content in a row
    main_container = dbc.Container([
        dbc.Row([
            # Left column: Filters (25% width)
            dbc.Col(top_bar),
        ],align="top"),
        dbc.Row([
            dbc.Col(left_bar),
            dbc.Col(right_bar),
        ]),

    ], fluid=True, style={"marginBottom": "80px"}) #added margin bottom 
    
    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout
