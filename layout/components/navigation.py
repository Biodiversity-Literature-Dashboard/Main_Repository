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

def create_change_views_button(side):
    change_views = dcc.Dropdown(
        id='change_views'+side,
        options= [{'label': 'Change view...', 'value': 'change'}] +
                [{'label': 'Map', 'value': 'Map'}] +
                [{'label': 'Article Table', 'value': 'Article_Table'}] +
                [{'label': 'Charts', 'value': 'Charts'}],
        value="change",
        clearable=False,
        className="mb-3"
    )
    return change_views

change_views_left = create_change_views_button("_left")
change_views_right = create_change_views_button("_right")
