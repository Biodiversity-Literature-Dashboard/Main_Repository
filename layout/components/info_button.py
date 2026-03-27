from dash import html
import dash_bootstrap_components as dbc

def info_button():

    return html.Div([

        html.Button(
            "ℹ",
            id="info-button",
            n_clicks=0,
            className="btn btn-primary btn-sm",
            style={
                "borderRadius": "50%",
                "width": "40px",
                "height": "40px",
                "padding": "0",
                "fontWeight": "bold"
            }
        ),

        dbc.Modal(
            [
                dbc.ModalHeader("Information"),
                dbc.ModalBody("This dashboard shows threats analysis."),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-info", n_clicks=0)
                ),
            ],
            id="info-modal",
            is_open=False,
        )
    ])