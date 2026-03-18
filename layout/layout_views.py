
from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.components.maps import empty_map
from layout.components.search_and_filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter, year_range_slider
from layout.components.tables import articles_datatable
from layout.components.charts import create_empty_chart_column, create_wordcloud_chart



# FILTER

def filters_view():
        filters_container = dbc.Card([
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
        return filters_container

filters_view = filters_view()





# MAP





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






# TABLE




def table_view():
    tables = dbc.CardBody([
        html.H5("Articles table", className="mt-4 mb-3"),
            dbc.Col([
                articles_datatable,
            ], ),
    ])
    return tables

table_view = table_view()




# CHARTS


def charts_view():
    charts = dbc.CardBody([
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
    ])
    return charts

charts_view = charts_view()

def content():
    main = dbc.Card([
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
    return main

content = content()


def cat():
    return 1