import dash_bootstrap_components as dbc
from dash import html, dcc
from layout.components.info_button import info_button

LOGO = "https://placehold.co/100x100"

def create_navbar():
    navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                       dbc.Row([
                    dbc.Col(html.Img(src=LOGO, height="30px")),
                    dbc.Col(
                        html.Div([
                            dbc.NavbarBrand(
                                "What is the evidence on indirect drivers of biodiversity loss? A systematic map",
                                className="ms-2 dashboard-title",
                                style={"fontFamily": "Tahoma, Geneva, sans-serif",
                                       "fontSize": "1rem", "fontWeight": "700"}
                            ),
                        ])
                    ),
                ],
                    align="center",
                    className="g-0",
                ),

                href="https://placehold.co/",
                style={"textDecoration": "none"},
            ),
                dbc.Nav(
                    [
                        dbc.NavItem(info_button())
                    ],
                    className="ms-auto",   #pushes to right
                    navbar=True
                ),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True,
        style={"paddingLeft": "1.5rem", "paddingRight": "1.5rem"},
    ),
    color="dark",
    dark=True,
    )
    return navbar
def create_description_banner():
    """Text banner displayed directly below the navbar."""
    return html.Div(
        className="study-description-banner",
        style={"marginLeft": "-1.5rem", "marginRight": "-1.5rem"},
        children=[
            html.P("Interactive dashboard on the indirect drivers of biodiversity loss",
                    className="ms-2 dashboard-subtitle"),
            html.P(
                "This map displays studies identified through a systematic literature review "
                "that examine the indirect drivers of biodiversity loss at multi-national "
                "scales or below.",
                style={"marginBottom": "0.25rem"}
            ),
            html.Div(
                className="reference-block",
                children=[
                    html.Strong("Reference: "),
                    html.Span(
                        '[Author(s), Year]. "Title of the open-access publication." '
                        "Journal, volume, pages. DOI: [insert DOI]"
                    ),
                ]
            ),
        ]
    )
navigation_bar = create_navbar()
description_banner = create_description_banner()

def create_change_views_button(side, value="change"):
    change_views = dcc.Dropdown(
        id='change_views'+side,
        options=[
            {'label': 'Change view...', 'value': 'change'},
            {'label': 'Map', 'value': 'Map'},
            {'label': 'Article Table', 'value': 'Article_Table'},
            {'label': 'Charts', 'value': 'Charts'},
        ],
        value=value,
        clearable=False,
        className="mb-0"
    )
    return change_views
