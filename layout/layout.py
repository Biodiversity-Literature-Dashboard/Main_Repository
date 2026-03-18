# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html, dcc
import dash_bootstrap_components as dbc


# Local imports
from layout.components.navigation import navigation_bar
from layout.layout_views import filters_view, map_view, charts_view, table_view, cat

def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Filter bar (top)
    topbar = filters_view
    
    # Map view
    leftbar = map_view

    rightbar = table_view

    charts = charts_view
    
    # Combine sidebar + main content in a row
    main_container = dbc.Container([
        dbc.Row([
            # Left column: Filters (25% width)
            dbc.Col(topbar, width=3),
            #dbc.Col(leftbar),
            #Right column: Main content (75% width)
            dbc.Col(content, width=9)
        ])
    ], fluid=True),
    
    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout
