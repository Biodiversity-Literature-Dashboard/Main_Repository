# Main Dash application entry point
# This file initializes the Dash app and runs the server

from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    "Dashboard"
                ])
            ])
        ])
    ])
])

if __name__ == "__main__":
    print("Starting Dashboard...")
    app.run(debug=True)
