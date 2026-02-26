# Visualization and chart creation functions
# Functions to create various chart types using Plotly (bar charts, line charts, pie charts, etc.)

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sections.dataframes import top_10_authors
from utils.data_loader import extract_threat_category_from_code, get_threat_categories


def top_authors_chart():
    return px.bar(top_10_authors(), x="Authors", y="Count")


def create_world_map(df):
    """
    Create world map with country markers from filtered data.
    Shows number of studies per country.
    """
    if df.empty:
        # Empty state
        fig = go.Figure(go.Scattergeo())
        fig.update_geos(
            showcountries=True,
            showcoastlines=True,
            projection_type="natural earth",
            countrycolor="lightgray"
        )
        fig.update_layout(
            title="Study Locations (No matches)",
            height=500,
            margin={"r": 0, "t": 40, "l": 0, "b": 0},
            annotations=[{
                'text': 'No articles match the selected filters',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 16, 'color': 'gray'}
            }]
        )
        return fig
    
    # Count studies per country
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Studies']
    
    # Create scatter geo plot
    fig = go.Figure(data=go.Scattergeo(
        lon=[0] * len(country_counts),  # Will be auto-positioned by country name
        lat=[0] * len(country_counts),
        text=country_counts['Country'],
        mode='markers+text',
        marker=dict(
            size=country_counts['Studies'] * 15 + 5,
            color='green',
            line=dict(width=1, color='darkgreen'),
            opacity=0.7
        ),
        textposition="top center",
        hovertemplate='<b>%{text}</b><br>Studies: %{marker.size}<extra></extra>',
        locations=country_counts['Country'],
        locationmode='country names'
    ))
    
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        projection_type="natural earth",
        countrycolor="lightgray"
    )
    
    fig.update_layout(
        title=f"Study Locations ({len(df)} articles)",
        height=500,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    
    return fig


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
