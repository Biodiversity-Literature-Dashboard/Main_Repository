
from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.components.maps import map_right, map_left
from layout.components.search_and_filters import (continent_filter,
                                                    ecoregion_filter,
                                                    study_design_filter,
                                                    threat_category_filter,
                                                    year_range_slider)
from layout.components.tables import articles_datatable_right, articles_datatable_left
from layout.components.navigation import change_views_left, change_views_right, create_change_views_button


# FILTER

def filters_view():
    filters_container = dbc.Card([
            dbc.CardHeader(
                dbc.Row([
                    dbc.Col(html.Span("Filters", style={"fontWeight": "bold"}), width="auto"),
                    dbc.Col(
                        dbc.Input(
                            id="searchbar",
                            type="search",
                            debounce=True,
                            placeholder="Search articles...",
                            size="sm",
                        ),
                        width=6,
                    ),
                    dbc.Col(
                        dbc.Button("Apply Filters", id="apply-filters-btn", color="primary",
                                   size="sm", style={"minWidth": "120px"}),
                        width="auto",
                    ),
                    dbc.Col(
                        dbc.Button("Reset Filters", id="reset-filters-btn", color="secondary",
                                   size="sm", style={"minWidth": "120px"}, n_clicks=0),
                        width="auto",
                    ),
                    dbc.Col(
                        dbc.Button("▼ Hide Filters", id="toggle-filter-btn", size="sm",
                                   color="link", className="p-0 ms-auto"),
                        className="ms-auto", width="auto"
                    ),
                ], align="center", className="g-2 flex-nowrap"),
            ),
            dbc.Collapse(
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
            ], className= "filter-bar"),
                id="filter-collapse",
                is_open=True,
            ),
        ], className="h-100")
    return filters_container

filters_view = filters_view()





#MAP





def map_view(side, selected_view="change"):
    if side == "left":
        map_side = map_left
    else:
        map_side = map_right
    map_container = dbc.CardBody([
        # Result counter
        html.Div(
            id='result-counter_'+side,
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
        articles_datatable = articles_datatable_right
    else:
        articles_datatable = articles_datatable_left
    tables = dbc.CardBody([
            dbc.Col([
                articles_datatable,
            ], ),
    ])
    return tables




# CHARTS


def charts_view(side, selected_view="change"):
    chart_order = [
        ('threat-chart_' + side,       'Threat Categories',  '360px', '410px'),
        ('driver-sankey_' + side,      'Driver Pathways',    '620px', '680px'),
        ('study-design-chart_' + side, 'Study Design',       '360px', '410px'),
        ('wordcloud-chart_' + side,    'Key Terms',          '360px', '410px'),
    ]

    chart_items = [
        html.Div([
            html.P(label, className="chart-card-title"),
            dcc.Graph(
                id=graph_id,
                style={'height': graph_h, 'width': '100%'},
                config={'responsive': False},
            ),
        ], className="chart-card", id='anchor-' + graph_id,
           style={'minHeight': card_h})
        for graph_id, label, graph_h, card_h in chart_order
    ]

    charts = dbc.CardBody([
        html.Div(chart_items, className="charts-inner-scroll", id='charts-scroll-' + side),
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


# PANEL WRAPPERS (collapsible cards around left/right views)

def left_panel():
    panel = dbc.Card([
        dbc.CardHeader(
            dbc.Row([
                dbc.Col(
                    create_change_views_button("_left", value="Map"),
                ),
                dbc.Col(
                    dbc.Button("▼ Hide", id="toggle-left-btn", size="sm",
                               color="link", className="p-0"),
                    width="auto"
                ),
            ], align="center", className="g-2"),
        ),
        dbc.Collapse(
            left_view,
            id="left-collapse",
            is_open=True,
        ),
    ])
    return panel

def right_panel():
    panel = dbc.Card([
        dbc.CardHeader(
            dbc.Row([
                dbc.Col(
                    create_change_views_button("_right", value="Article_Table"),
                ),
                dbc.Col(
                    dbc.Button("▼ Hide", id="toggle-right-btn", size="sm",
                               color="link", className="p-0"),
                    width="auto"
                ),
            ], align="center", className="g-2"),
        ),
        dbc.Collapse(
            right_view,
            id="right-collapse",
            is_open=True,
        ),
    ])
    return panel

left_panel = left_panel()
right_panel = right_panel()
