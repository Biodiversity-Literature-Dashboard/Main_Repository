# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html, dcc
import dash_bootstrap_components as dbc


# Local imports
from layout.components.navigation import navigation_bar
from layout.components.tables import articles_datatable
from layout.components.maps import empty_map
from layout.components.charts import create_empty_chart_column, create_wordcloud_chart
from layout.layout_views.filters_view import filters_view

def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Filter sidebar (left side)
    filter_sidebar = filters_view
    
    # Main content area (right side)
    main_content = dbc.Card([
        dbc.CardBody([
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
            
            html.Hr(),
            
            # Charts section
            html.H5("Analysis Charts", className="mt-4 mb-3"),
            dbc.Row([
                # Left chart: Threat Distribution
                create_empty_chart_column('threat-chart', "Threat Types Distribution", width=4),

                # Middle chart: Study Design
                create_empty_chart_column('study-design-chart', "Study Design Distribution", width=4),

                # Right chart: Wordcloud
                dbc.Col([
                    dcc.Graph(
                        id='wordcloud-chart',
                        figure=create_wordcloud_chart(),
                        config={'displayModeBar': False}
                    )
                ], width=4)
            ]),
            html.H5("Articles table", className="mt-4 mb-3"),
            dbc.Row([
                dbc.Col([
                    articles_datatable
                ], ),

            ]),

        ])
    ])
    
    # Combine sidebar + main content in a row
    main_container = dbc.Container([
        dbc.Row([
            # Left column: Filters (25% width)
            dbc.Col(filter_sidebar, width=3),
            
            # Right column: Main content (75% width)
            dbc.Col(main_content, width=9)
        ])
    ], fluid=True)
    
    # Combine navbar + container
    layout = html.Div([
        navbar,
        main_container
    ])
    
    return layout
