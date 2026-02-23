# Visualization and chart creation functions
# Functions to create various chart types using Plotly (bar charts, line charts, pie charts, etc.)

#pre-made packages
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

# local imports
#from sections.dataframes import top_10_authors
from utils.data_loader import extract_threat_category_from_code, get_threat_categories



# EMPTY CHARTS



def create_empty_chart(title):
    """Create an empty chart placeholder"""
    fig = go.Figure()
    fig.update_layout(
        title=title,
        height=300,
        annotations=[{
            'text': 'No data to display',
            'xref': 'paper',
            'yref': 'paper',
            'showarrow': False,
            'font': {'size': 14, 'color': 'gray'}
        }]
    )
    return fig


def create_empty_chart_column(id,title):
    chart_col = dbc.Col([
        dcc.Graph(
            id=id,
            figure=create_empty_chart(title),
            config={'displayModeBar': False}
        )
    ], width=6)
    return chart_col




# BAR CHARTS





# def top_authors_chart():
#     return px.bar(top_10_authors(), x="Authors", y="Count")


def create_threat_distribution_chart(df):
    """
    Create bar chart showing distribution of threat categories.
    Counts all threats (articles can have multiple).
    """
    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            title="Threat Category Distribution",
            height=300,
            annotations=[{
                'text': 'No data matches filters',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 14, 'color': 'gray'}
            }]
        )
        return fig
    
    # Extract all threat categories from all articles
    all_threats = []
    for threat_code in df['Threat'].dropna():
        categories = extract_threat_category_from_code(threat_code)
        all_threats.extend(categories)
    
    # Count occurrences
    threat_counts = pd.Series(all_threats).value_counts().reset_index()
    threat_counts.columns = ['Category', 'Count']
    
    # Add category names
    threat_cat_dict = dict(get_threat_categories())
    threat_counts['Name'] = threat_counts['Category'].map(
        lambda x: f"{x}. {threat_cat_dict.get(x, 'Unknown')}"
    )
    
    fig = px.bar(
        threat_counts,
        x='Name',
        y='Count',
        title='Threat Category Distribution',
        labels={'Name': 'Threat Category', 'Count': 'Number of Articles'}
    )
    
    fig.update_layout(
        height=300,
        xaxis_tickangle=-45,
        showlegend=False
    )
    
    return fig




# PIE CHARTS




def create_study_design_chart(df):
    """
    Create pie chart showing distribution of study designs.
    """
    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            title="Study Design Distribution",
            height=300,
            annotations=[{
                'text': 'No data matches filters',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 14, 'color': 'gray'}
            }]
        )
        return fig
    
    design_counts = df['Study_design'].value_counts().reset_index()
    design_counts.columns = ['Design', 'Count']
    
    fig = px.pie(
        design_counts,
        values='Count',
        names='Design',
        title='Study Design Distribution',
        hole=0.3  # Donut chart
    )
    
    fig.update_layout(height=300)
    
    return fig
