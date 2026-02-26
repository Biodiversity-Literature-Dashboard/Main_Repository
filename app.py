# app.py
from dash import Dash
import dash_bootstrap_components as dbc

from layout import build_layout
from callbacks import register_callbacks

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = build_layout()

# IMPORTANT: register callbacks AFTER app + layout exist
register_callbacks(app)

if __name__ == "__main__":
    print("Starting Dashboard...")
    app.run(debug=True)