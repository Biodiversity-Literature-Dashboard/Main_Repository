import dash_bootstrap_components as dbc
from dash import html, dcc
from layout.components.info_button import info_button
from dash_bootstrap_components import DropdownMenu, DropdownMenuItem

LOGO = "https://placehold.co/100x100"

def create_navbar():
    navbar = dbc.Navbar(
    dbc.Container(
        [
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=LOGO, height="30px")),
                    dbc.Col(
                        DropdownMenu(
                            label=html.Span(
                                "Interactive Biodiversity Dashboard",
                                className="navbar-title-dropdown",
                            ),
                            children=[
                                DropdownMenuItem("Home", href="/"),
                                DropdownMenuItem("Map View", href="/map"),
                                DropdownMenuItem("Article Table", href="/table"),
                                DropdownMenuItem("Charts", href="/charts"),
                            ],
                            className="ms-2 navbar-dropdown",
                            nav=True,
                            in_navbar=True,
                            style={"minWidth": "max-content", "width": "auto"}
                        )
                    ),
                ],
                align="center",
                className="g-0",
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
        className="mb-3 view-dropdown",
        style={
            "borderRadius": "0.75rem",
            "boxShadow": "0 0.25rem 0.5rem rgba(0, 0, 0, 0.12)",
            "border": "1px solid #ced4da",
            "backgroundColor": "#ffffff",
            "minWidth": "180px",
        }
    )
    return change_views

change_views_left = create_change_views_button("_left")
change_views_right = create_change_views_button("_right")
