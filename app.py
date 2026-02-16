# Main Dash application entry point
# This file initializes the Dash app and runs the server

from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout
from config import DEBUG_MODE

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Set layout
app.layout = create_layout()

# Run server
if __name__ == "__main__":
    print("Starting Dashboard...")
    print("Open browser at: http://127.0.0.1:8050")
    app.run(debug=DEBUG_MODE)
