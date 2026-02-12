# Visualization and chart creation functions
# Functions to create various chart types using Plotly (bar charts, line charts, pie charts, etc.)

import plotly.express as px
from sections.dataframes import top_10_authors

def top_authors_chart():
    return px.bar(top_10_authors(), x="Authors", y="Count")