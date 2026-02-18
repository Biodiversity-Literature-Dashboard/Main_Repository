
import dash_bootstrap_components as dbc
from dash import html
from visualizations.search_and_filters import create_search_bar


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
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                create_search_bar(),
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