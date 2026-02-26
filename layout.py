# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc
from utils.data_loader import load_ridley


def build_layout():
    df = load_ridley()

    continents = (
        sorted(df["Continent_Ocean"].dropna().astype(str).unique())
        if "Continent_Ocean" in df.columns
        else []
    )

    countries = (
        sorted(df["country_eez"].dropna().astype(str).unique())
        if "country_eez" in df.columns
        else []
    )

    return dbc.Container(
        [
            html.H1("Biodiversity Dashboard", className="my-4"),

            dbc.Row(
                [
                    dbc.Col(
                        dcc.Input(
                            id="search-input",
                            type="text",
                            placeholder="Search authors...",
                            className="form-control",
                        ),
                        width=4,
                    ),

                    dbc.Col(
                        dcc.Dropdown(
                            id="continent-dropdown",
                            options=[{"label": c, "value": c} for c in continents],
                            placeholder="Select continent",
                            clearable=True,
                        ),
                        width=4,
                    ),

                    dbc.Col(
                        dcc.Dropdown(
                            id="country-dropdown",
                            options=[{"label": c, "value": c} for c in countries],
                            placeholder="Select country/EEZ",
                            clearable=True,
                        ),
                        width=4,
                    ),
                ],
                className="mb-2",
            ),

            html.Div(id="filtered-count", className="mb-3"),

            # give an initial empty figure so it doesn't look "broken"
            dcc.Graph(
                id="top_authors_graph",
                figure={"data": [], "layout": {"title": "Top Authors (Filtered)"}},
            ),
        ],
        fluid=True,
    )