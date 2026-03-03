from dash import dcc
import plotly.graph_objects as go
import pandas as pd

# EMPTY MAPS

def create_empty_map(): # we have to create create_map() later
    """Create an empty world map placeholder"""
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        projection_type='natural earth'
    )
    fig.update_layout(
        title="Study Locations (Loading...)",
        height=500,
        margin={'r': 100, 't': 40, 'l': 0, 'b': 0}
    )
    return fig

def create_empty_dcc_graph_map():
    graph = dcc.Graph(
        id='world-map',
        figure=create_empty_map(),
        config={'displayModeBar': True, 'scrollZoom': True},
        style={'height': '500px'}
    )
    return graph

empty_map = create_empty_dcc_graph_map()



# NON-EMPTY MAPS

def create_world_map(df):
    """
    Create world map with country markers from filtered data.
    Shows number of studies per country.
    """
    # Create the colorscale
    colorscale = [
        [0, '#c4c4c4'],
        [0.000001, "#b6edbd"],
        [0.5, "#53a95d"],
        [1.0, "#12671C"]
    ]
    
    # Count studies per country
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Studies']
    
    #Empty state
    if df.empty:
        fig = go.Figure(go.Choropleth(
            locations=[],
            locationmode='country names',
            z=[],
            zmin=0,
            zmax=1,
            colorscale=colorscale,
            marker_line_color='white',
            marker_line_width=0.5,
            hovertemplate='<b>%{location}</b><br>Studies: %{z}<extra></extra>',
            colorbar=dict(
                title='Number of Studies',
                thickness=0.02,
                thicknessmode='fraction',
                len=0.4, 
                lenmode='fraction',
                x=1.02,
                xanchor='left',
                y=0,
                yanchor='bottom',
                outlinewidth=0.5,
                bgcolor='white',
                tickfont=dict(size=10)
            )
        ))
        fig.update_geos(
            showcountries=True,
            showcoastlines=True,
            projection_type='natural earth',
            countrycolor='lightgray'
        )
        fig.update_layout(
            title='Study Locations (No matches)',
            height=500,
            margin={'r': 100, 't': 40, 'l': 0, 'b': 0},
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
    
    # Create choropleth map
    fig = go.Figure(go.Choropleth(
        locations=country_counts['Country'],
        locationmode='country names',
        z=country_counts['Studies'],
        zmin=0,
        zmax=country_counts['Studies'].max(),
        colorscale=colorscale,
        marker_line_color='white',
        marker_line_width=0.5,
        hovertemplate='<b>%{location}</b><br>Studies: %{z}<extra></extra>',
        colorbar=dict(
            title='Number of Studies',
            thickness=0.02,
            thicknessmode='fraction',
            len=0.4, 
            lenmode='fraction',
            x=1.02,
            xanchor='left',
            y=0,
            yanchor='bottom',
            outlinewidth=0.5,
            bgcolor='white',
            tickfont=dict(size=10)
        )
    ))
    
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        projection_type='natural earth',
        countrycolor='lightgray'
    )
    
    fig.update_layout(
        title=f"Study Locations ({len(df)} articles)",
        height=500,
        margin={'r': 100, 't': 40, 'l': 0, 'b': 0}
    )
    
    return fig
