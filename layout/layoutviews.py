from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.components.maps import map_right, map_left
from layout.components.search_and_filters import (
    continent_filter,
    ecoregion_filter,
    study_design_filter,
    threat_category_filter,
    year_range_slider,
    search_bar
)
from layout.components.tables import articles_datatable_right, articles_datatable_left
from layout.components.navigation import change_views_left, change_views_right, create_change_views_button


# FILTER

def filters_view():
    filters_container = dbc.Card([
        dbc.CardHeader("Filters", style={"fontWeight": "bold"}),
        dbc.CardBody([
            html.Div([
                dbc.Row([
                    dbc.Col(
                        html.Div([
                            html.Label("Continent/Ocean:", className="fw-bold mb-2"),
                            continent_filter,
                        ])
                    ),
                    dbc.Col(
                        html.Div([
                            html.Label("Ecoregion:", className="fw-bold mb-2 mt-3"),
                            ecoregion_filter,
                        ])
                    ),
                    dbc.Col(
                        html.Div([
                            html.Label("Study Design:", className="fw-bold mb-2 mt-3"),
                            study_design_filter,
                        ])
                    ),
                    dbc.Col(
                        html.Div([
                            html.Label("Threat Category:", className="fw-bold mb-2 mt-3"),
                            threat_category_filter,
                        ])
                    ),
                    dbc.Col(
                        html.Div([
                            html.Label("Publication Year (Articles Table):", className="fw-bold mb-2 mt-3"),
                            year_range_slider,
                        ])
                    ),
                ], className="g-3")
            ]),
            html.Div([
                dbc.Row([
                    search_bar,
                    dbc.Col(
                        html.Div([
                            dbc.Button(
                                "Apply Filters",
                                id="apply-filters-btn",
                                color="primary",
                                className="mt-2"
                            ),
                            dbc.Button(
                                "Reset Filters",
                                id="reset-filters-btn",
                                color="secondary",
                                className="mt-2",
                                n_clicks=0
                            ),
                        ], className="d-flex flex-wrap gap-2 justify-content-end")
                    , width="auto")
                ], className="g-3 align-items-end")
            ]),
        ], className="filter-bar"),
    ], className="h-100")
    return filters_container


filters_view = filters_view()





#MAP





def map_view(side, selected_view="change"):
    if side == "left":
        change_views = create_change_views_button("_left", value=selected_view)
        map_side = map_left
    else:
        change_views = create_change_views_button("_right", value=selected_view)
        map_side = map_right

    map_container = dbc.CardBody([
        html.Div(change_views),
        html.Div(
            id='result-counter_' + side,
            children="Showing 15 of 15 articles",
            className="mb-2",
            style={'fontSize': '14px', 'color': '#666', 'fontWeight': '500'}
        ),
        # Map section
        html.H5("Study Locations Map", className="mb-3"),

        # Cite marine boundaries data source
        html.Div([
            map_side,
            html.Div([
                html.Small([
                    html.I("Marine boundaries data source: "),
                    "Flanders Marine Institute (2023). ",
                    html.A("Maritime Boundaries Geodatabase, v12.",
                        href="https://doi.org/10.14284/632",
                        target="_blank",
                        style={"color": "#6c757d", "textDecoration": "underline"}
                    )
                ], style={"fontSize": "10px", "color": "#6c757d"})
            ], style={"marginTop": "-10px", "textAlign": "right"})
        ])
    ])
    return map_container


# TABLE




def table_view(side, selected_view="change"):
    if side == "right":
        change_views = create_change_views_button("_right", value=selected_view)
        articles_datatable = articles_datatable_right
    else:
        change_views = create_change_views_button("_left", value=selected_view)
        articles_datatable = articles_datatable_left

    tables = dbc.CardBody([
        html.Div(
            change_views,
        ),
            dbc.Col([
                articles_datatable,
            ], ),
    ])
    return tables


# CHARTS


def charts_view(side, selected_view="change"):
    if side == "right":
        change_views = create_change_views_button("_right", value=selected_view)
    else:
        change_views = create_change_views_button("_left", value=selected_view)
    charts = dbc.CardBody([
        html.Div(change_views),
        dbc.Row([
            dbc.Col(dcc.Graph(id='threat-chart_' + side), width=12)
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id='study-design-chart_' + side), width=6),
            dbc.Col(dcc.Graph(id='wordcloud-chart_' + side), width=6)
        ]),
    ])
    return charts


def left_view():
    current_view = html.Div(map_view("left", selected_view="Map"), id="left_view")
    return current_view


def right_view():
    current_view = html.Div(table_view("right", selected_view="Article_Table"), id="right_view")
    return current_view


left_view = left_view()
right_view = right_view()