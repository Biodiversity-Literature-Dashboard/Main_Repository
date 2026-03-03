# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

# Pre-made packages
from dash import html, dcc
import dash_bootstrap_components as dbc


# Local imports
from layout.components.navigation import navigation_bar
from layout.components.tables import articles_datatable
from layout.components.search_and_filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter, reset_filters, year_range_slider
from layout.components.maps import empty_map
from layout.components.charts import create_empty_chart_column, create_wordcloud_chart

def create_layout():
    """Create the main dashboard layout"""

    # Navbar at top
    navbar = navigation_bar
    
    # Filter sidebar (left side)
    filter_sidebar = dbc.Card([
        dbc.CardHeader("Filters", style={"fontWeight": "bold"}),
        dbc.CardBody([
            # Continent filter
            html.Label("Continent/Ocean:", className="fw-bold mb-2"),
            continent_filter,
            
            # Ecoregion filter (checkboxes - can select multiple)
            html.Label("Ecoregion:", className="fw-bold mb-2 mt-3"),
            ecoregion_filter,
            
            # Study Design filter (checkboxes)
            html.Label("Study Design:", className="fw-bold mb-2 mt-3"),
            study_design_filter,
            
            # Threat Category filter
            html.Label("Threat Category:", className="fw-bold mb-2 mt-3"),
            threat_category_filter,

            # Year range filter (filters articles table)
            html.Label("Publication Year (Articles Table):", className="fw-bold mb-2 mt-3"),
            year_range_slider,

            # Apply button (will wire up in callbacks later)
            html.Hr(),
            dbc.Button("Apply Filters", id="apply-filters-btn", color="primary", className="w-100 mt-2"),
            #reset button
            dbc.Button("Reset Filters", id="reset-filters-btn", color="secondary", className="w-100 mt-2", n_clicks=0)
        ])
    ], className="h-100")
    
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
