import dash_bootstrap_components as dbc
from dash import html, dcc
from layout.components.search_and_filters import create_search_bar
from layout.components.info_button import info_button

LOGO = "https://placehold.co/100x100"

def create_navbar():
    navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Interactive Biodiversity Dashboard", className="ms-2")),
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
        ]
    ),
    color="dark",
    dark=True,
    )
    return navbar
navigation_bar = create_navbar()
