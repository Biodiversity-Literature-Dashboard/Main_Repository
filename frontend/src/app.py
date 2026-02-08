# run using python3 -m frontend.src.app in root folder

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from backend.src.tables import top_10_authors
app = Dash()
top_10_authors = top_10_authors()

authors_fig = px.bar(top_10_authors, x="Authors", y="Count")

app.layout = html.Div(children=[
    html.H1(children='Biodiversity Dashboard'),

    html.Div(children='''
        Authors who have written the most articles.
    '''),

    dcc.Graph(
        id='top_authors_graph',
        figure=authors_fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
