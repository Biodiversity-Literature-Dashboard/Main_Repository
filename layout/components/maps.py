import plotly.graph_objects as go

def create_empty_map(): # we have to create create_map() later
    """Create an empty world map placeholder"""
    fig = go.Figure(go.Scattergeo())
    fig.update_geos(
        showcountries=True,
        showcoastlines=True,
        projection_type="natural earth"
    )
    fig.update_layout(
        title="Study Locations (Loading...)",
        height=500,
        margin={"r": 0, "t": 40, "l": 0, "b": 0}
    )
    return fig

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

empty_map = create_empty_map()
#world_map = create_world_map()