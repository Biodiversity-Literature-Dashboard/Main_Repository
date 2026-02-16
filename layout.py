# Dashboard layout structure
# Define the overall layout, navigation, tabs, and component arrangement

from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from config import APP_TITLE
from utils.data_loader import df_grossi


def create_empty_map(): # we have to create create_map() later
    """Create an empty world map placeholder"""
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        projection_type="natural earth"
    )
    fig.update_layout(
        title="Study Locations (Loading...)",
        height=500,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    return fig


def create_empty_chart(title):
    """Create an empty chart placeholder"""
    fig = go.Figure()
    fig.update_layout(
        title=title,
        height=300,
        annotations=[{
            'text': 'No data to display',
            'xref': 'paper',
            'yref': 'paper',
            'showarrow': False,
            'font': {'size': 14, 'color': 'gray'}
        }]
    )
    return fig


def create_layout():
    """Create the main dashboard layout"""
    
    # Navbar at top
    navbar = dbc.NavbarSimple(
        brand=APP_TITLE,
        brand_style={"fontSize": "1.5rem", "fontWeight": "bold"},
        color="primary",
        dark=True,
        fluid=True,
        className="mb-3"
    )
    
    # Filter sidebar (left side)
    filter_sidebar = dbc.Card([
        dbc.CardHeader("Filters", style={"fontWeight": "bold"}),
        dbc.CardBody([
            # Continent filter
            html.Label("Continent/Ocean:", className="fw-bold mb-2"),
            dcc.Dropdown(
                id='continent-filter',
                options=[{'label': 'All', 'value': 'all'}] + 
                        [{'label': cont.title(), 'value': cont} 
                         for cont in sorted(df_grossi['Continent_Ocean'].dropna().unique())],
                value='all',
                clearable=False,
                className="mb-3"
            ),
            
            # Apply button (will wire up in callbacks later)
            dbc.Button("Apply Filters", id="apply-filters-btn", color="primary", className="w-100")
        ])
    ], className="h-100")
    
    # Main content area (right side)
    main_content = dbc.Card([
        dbc.CardBody([
            # Map section
            html.H5("Study Locations Map", className="mb-3"),
            dcc.Graph(
                id='world-map',
                figure=create_empty_map(),
                config={'displayModeBar': True, 'scrollZoom': True},
                style={'height': '500px'}
            ),
            
            html.Hr(),
            
            # Charts section
            html.H5("Analysis Charts", className="mt-4 mb-3"),
            dbc.Row([
                # Left chart: Threat Distribution
                dbc.Col([
                    dcc.Graph(
                        id='threat-chart',
                        figure=create_empty_chart("Threat Types Distribution"),
                        config={'displayModeBar': False}
                    )
                ], width=6),
                
                # Right chart: Study Design
                dbc.Col([
                    dcc.Graph(
                        id='study-design-chart',
                        figure=create_empty_chart("Study Design Distribution"),
                        config={'displayModeBar': False}
                    )
                ], width=6)
            ])
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
