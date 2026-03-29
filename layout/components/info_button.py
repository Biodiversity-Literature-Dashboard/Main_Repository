from dash import html
import dash_bootstrap_components as dbc

def info_button():

    return html.Div([

        html.Button(
            "ℹ",
            id="info-button",
            n_clicks=0,
            className="btn btn-sm",
            style={
                "borderRadius": "50%",
                "width": "35px",
                "height": "35px",
                "fontWeight": "bold",
                "backgroundColor": "#808080",
                "color": "white",             
                "border": "none",             
                "position": "absolute", 
                "right": "20px",        # Distance from the right edge
                "top": "50%",           # Center vertically
                "transform": "translateY(-50%)" # Perfect vertical alignment
            
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