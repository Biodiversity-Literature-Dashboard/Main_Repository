# callbacks.py
from dash import Input, Output
import plotly.express as px

from utils.data_loader import load_ridley

RIDLEY_DF = load_ridley()


def apply_filters_and_search(df, search_text=None, continent=None, country=None):
    dff = df.copy()

    # filter by continent
    if continent and "Continent_Ocean" in dff.columns:
        dff = dff[dff["Continent_Ocean"].astype(str) == str(continent)]

    # filter by country/eez 
    if country and "country_eez" in dff.columns:
        dff = dff[dff["country_eez"].astype(str) == str(country)]

    # search authors 
    if search_text and str(search_text).strip():
        q = str(search_text).strip().lower()
        if "Authors" in dff.columns:
            dff = dff[dff["Authors"].astype(str).str.lower().str.contains(q, na=False)]

    return dff


def register_callbacks(app):
    @app.callback(
        Output("top_authors_graph", "figure"),
        Output("filtered-count", "children"),
        Input("search-input", "value"),
        Input("continent-dropdown", "value"),
        Input("country-dropdown", "value"),
    )
    def update_dashboard(search_text, continent, country):
        filtered_df = apply_filters_and_search(RIDLEY_DF, search_text, continent, country)

        if "Authors" not in filtered_df.columns or filtered_df.empty:
            return (
                {"data": [], "layout": {"title": "Top Authors (Filtered)"}},
                f"{len(filtered_df)} articles found",
            )

        top_authors = filtered_df["Authors"].value_counts().head(10).reset_index()
        top_authors.columns = ["Author", "Count"]

        fig = px.bar(top_authors, x="Author", y="Count", title="Top Authors (Filtered)")
        fig.update_layout(margin=dict(l=20, r=20, t=60, b=20))

        return fig, f"{len(filtered_df)} articles found"