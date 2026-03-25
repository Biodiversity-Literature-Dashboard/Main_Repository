
from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.components.maps import empty_map
from layout.components.search_and_filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter, year_range_slider, search_bar
from layout.components.tables import articles_datatable
from layout.components.charts import create_empty_chart_column, create_wordcloud_chart
from layout.components.navigation import change_views_left, change_views_right


# FILTER

def filters_view():
        filters_container = dbc.Card([
                dbc.CardHeader("Filters", style={"fontWeight": "bold"}),
                dbc.CardBody([
                    # Continent filter
                html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div([
                            html.Label("Continent/Ocean:", className="fw-bold mb-2"),
                            continent_filter,
                                ]
                                )
                            ),
                            dbc.Col(
                                html.Div([
                            # Ecoregion filter (checkboxes - can select multiple)
                            html.Label("Ecoregion:", className="fw-bold mb-2 mt-3"),
                            ecoregion_filter,
                                ]
                                )
                            ),

                            dbc.Col(
                                html.Div([
                            # Study Design filter (checkboxes)
                            html.Label("Study Design:", className="fw-bold mb-2 mt-3"),
                            study_design_filter,
                                ]
                                )
                            ),
                            dbc.Col(
                                html.Div([
                            # Threat Category filter
                            html.Label("Threat Category:", className="fw-bold mb-2 mt-3"),
                            threat_category_filter,
                                ]
                                )
                            ),
                            dbc.Col(
                                html.Div([
                            # Year range filter (filters articles table)
                            html.Label("Publication Year (Articles Table):", className="fw-bold mb-2 mt-3"),
                            year_range_slider,
                                ]
                                )
                            ),
                        ]
                    ),
                ]
                ),
                html.Div(
                [
                    dbc.Row(
                        [
                            search_bar,
                            dbc.Col(
                                html.Div([
                                    # Apply button (will wire up in callbacks later)
                                    dbc.Button("Apply Filters", id="apply-filters-btn", color="primary", className="w-100 mt-2"),
                                    #reset button
                                    dbc.Button("Reset Filters", id="reset-filters-btn", color="secondary", className="w-100 mt-2", n_clicks=0)
                                    ])
                                )
                        ]),
                ]),
                ], className= "filter-bar"),
            ], className="h-100")
        return filters_container

filters_view = filters_view()





#MAP





def map_view(change_views):
    if change_views == "left":
        change_views = change_views_left
    else:
        change_views = change_views_right
    map_container = dbc.CardBody([
        html.Div(
            change_views,
        ),
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






# TABLE




def table_view(change_views):
    if change_views == "right":
        change_views = change_views_right
    else:
        change_views = change_views_left
    tables = dbc.CardBody([
        html.Div(
            change_views,
        ),
        html.H5("Article table", className="mt-4 mb-3"),
            dbc.Col([
                articles_datatable,
            ], ),
    ])
    return tables




# CHARTS


def charts_view(change_views):
    if change_views == "right":
        change_views = change_views_right
    else:
        change_views = change_views_left
    charts = dbc.CardBody([
            html.Div(
                change_views,
            ),
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


def left_view():
    current_view = html.Div(map_view("left"),id="left_view")
    return current_view

def right_view():
    current_view = html.Div(table_view("right"),id="right_view")
    return current_view

left_view = left_view()
right_view = right_view()
