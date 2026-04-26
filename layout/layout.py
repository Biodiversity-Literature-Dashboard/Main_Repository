# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html
import dash_bootstrap_components as dbc


# Local imports
from layout.components.info_button import info_button
from layout.components.navigation import navigation_bar, description_banner
from layout.layoutviews import left_panel, right_panel, filters_view
def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    banner = description_banner
    # Filter sidebar (left side)
    top_bar = filters_view
    right_bar = right_panel
    left_bar = left_panel

    
    # Main content area (right side)
    
    # Combine sidebar + main content in a row
    main_container = dbc.Container([
        banner,
        dbc.Row([
            # Left column: Filters (25% width)
            dbc.Col(top_bar),
        ], align="top"),
        dbc.Row([
            dbc.Col(left_bar, id="left-col", className="col-6"),
            dbc.Col(right_bar, id="right-col", className="col-6"),
        ], className="mt-2 g-2"),

    ], fluid=True, style={"marginBottom": "80px", "paddingLeft": "1.5rem", "paddingRight": "1.5rem"}) #added margin bottom 
    
    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout
