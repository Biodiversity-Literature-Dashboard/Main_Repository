# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html
import dash_bootstrap_components as dbc


# Local imports
from layout.components.info_button import info_button
from layout.components.navigation import navigation_bar
from layout.layoutviews import left_view, right_view, filters_view


def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Views
    top_bar = filters_view
    right_bar = right_view
    left_bar = left_view

    # Main container
    main_container = dbc.Container([
        
        # Filters row
        dbc.Row([
            dbc.Col(top_bar),
        ], align="top", className="mb-3"),

        # Main content row
        dbc.Row([
            dbc.Col(left_bar, width=6),
            dbc.Col(right_bar, width=6),
        ], className="g-3"),

    ], fluid=True, style={"marginBottom": "80px"})

    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout