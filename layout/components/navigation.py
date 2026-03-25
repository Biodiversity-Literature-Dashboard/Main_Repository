
import dash_bootstrap_components as dbc
from dash import html, dcc
from layout.components.search_and_filters import create_search_bar


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

def create_change_views_button(value):
    change_views = dcc.Dropdown(
        id='change_views'+value,
        options=[{'label': 'Map', 'value': 'Map'}] + 
                [{'label': 'Article Table', 'value': 'Article_Table'}] +
                [{'label': 'Charts', 'value': 'Charts'}],
        value=value,
        clearable=False,
        className="mb-3"
    )
    return change_views

change_views_map = create_change_views_button("Map")

change_views_charts = create_change_views_button("Charts")

change_views_article_table = create_change_views_button("Article_Table")