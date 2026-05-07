from dash import dcc
import plotly.graph_objects as go
import pandas as pd
import os
import json

# Read the master_countries.csv file to get the list of countries and their ISO codes
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "master_countries.csv")
master_countries = pd.read_csv(csv_path)

# Read the small_countries.csv file to get the list of small countries and their ISO codes
small_csv_path = os.path.join(current_dir, "small_countries.csv")
small_countries = pd.read_csv(small_csv_path)

# Read the marine GeoJSON file
marine_json_path = os.path.join(current_dir, "eez_v12.json")
with open(marine_json_path, encoding="utf-8") as f:
    marine_geojson = json.load(f)
    
# Check and fix the winding order of GeoJSON files
def is_clockwise(coords):
    """Check if polygon coordinates are clockwise."""
    total = 0
    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        total += (x2 - x1) * (y2 + y1)
    return total > 0

def ensure_clockwise(coords):
    """Ensure polygon coordinates are clockwise (required for Plotly geo choropleth)."""
    if not is_clockwise(coords):
        return coords[::-1]
    return coords

# Apply winding order fix to marine GeoJSON 
for feature in marine_geojson["features"]:
    geom_type = feature["geometry"]["type"]
    coords = feature["geometry"]["coordinates"]
    if geom_type == "Polygon":
        coords[0] = ensure_clockwise(coords[0])
    elif geom_type == "MultiPolygon":
        for polygon in coords:
            polygon[0] = ensure_clockwise(polygon[0])


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

def create_empty_dcc_graph_map(side):
    graph = dcc.Graph(
        id='world-map'+side,
        figure=create_empty_map(),
        config={'displayModeBar': True, 'scrollZoom': True},
        style={'height': '560px'}
    )
    return graph

map_right = create_empty_dcc_graph_map("_right")
map_left = create_empty_dcc_graph_map("_left")


# NON-EMPTY MAPS

def unstrip_countries(df,country_col):
    all_countries = []
    for country in df[country_col]:
        study_countries = str(country).split(";")
        all_countries += study_countries
    return all_countries

def create_world_map(df):
    """
    Create world map with country markers from filtered data.
    Shows number of studies per country.
    """
    # Create the colorscale
    colorscale = [
        [0, "#c4c4c4"],
        [0.000001, "#b6edbd"],
        [0.5, "#53a95d"],
        [1.0, "#12671C"]
    ]
    
    # Create marine colorscale
    marine_colorscale = [
        [0, "#9ecae1"],
        [0.5, "#4292c6"],
        [1.0, "#08306b"]
    ]
    
    # Count studies per country (support both 'Country' and 'country_eez' column names)
    country_col = 'Country' if 'Country' in df.columns else 'Country_EEZ'
    eco_col = "Ecoregion"
    all_countries = unstrip_countries(df, country_col)

    country_counts = pd.Series(all_countries).value_counts().reset_index()
    country_counts.columns = ['Country', 'Studies']

    
    #Count studies per ecoregion
    if eco_col in df.columns:
        df[country_col] = df[country_col].str.split(';')
        exploded_df = df.explode(country_col)
        eco_df = pd.DataFrame({

            "Country": exploded_df[country_col],
            "Terrestrial": exploded_df[eco_col].astype(str).str.contains("Terrestrial", case=False, na=False).astype(int),
            "Freshwater": exploded_df[eco_col].astype(str).str.contains("Freshwater", case=False, na=False).astype(int),
            "Marine": exploded_df[eco_col].astype(str).str.contains("Marine", case=False, na=False).astype(int)
        })
        eco_counts = eco_df.groupby("Country").sum().reset_index()
    else:
        eco_counts = pd.DataFrame({
            "Country": country_counts["Country"],
            "Terrestrial": [0] * len(country_counts),
            "Freshwater": [0] * len(country_counts),
            "Marine": [0] * len(country_counts)
        })
    merged_counts = pd.merge(country_counts, eco_counts, on="Country", how="left")
    
    # Merge with master_countries to get get ISO codes and include with 0 studies
    full_country_data = pd.merge(master_countries, merged_counts, on="Country", how="left")
    full_country_data.fillna({"Studies": 0, "Terrestrial": 0, "Freshwater": 0, "Marine": 0}, inplace=True)
    
    # Manual name fixes (This might not be necessary anymore)
    marine_name_fixes = {
        "Comoros": "Comores",
        "Greenland": "Denmark",
        "Cook Islands": "New Zealand",
        "American Samoa": "United States",
        "Puerto Rico": "United States",
        "Anguilla": "United Kingdom",
        "Gibraltar": "United Kingdom",
        "New Caledonia": "France",
        "French Guiana": "France"
    }
    full_country_data["Country"] = full_country_data["Country"].replace(marine_name_fixes)
    full_country_data = full_country_data.groupby("Country").sum().reset_index()
    max_studies = max(full_country_data["Studies"].max(), 1) if not full_country_data.empty else 1
    max_marine = max(full_country_data["Marine"].max(), 1) if not full_country_data.empty else 1
    
    # Isolate data for small countries
    small_country_list = small_countries["Country"].tolist()
    small_country_data = full_country_data[full_country_data["Country"].isin(small_country_list)]
    
    # Empty state
    if df.empty:
        fig = go.Figure(go.Choropleth(
            locations=master_countries["Country"],
            locationmode='country names',
            z=[0] * len(master_countries),
            zmin=0,
            zmax=1,
            colorscale=colorscale,
            marker_line_color='white',
            marker_line_width=0.5,
            customdata=[[0, 0, 0]] * len(master_countries),
            hovertemplate=(
                "<b>%{location}</b><br>"
                "Total: %{z}<br>"
                "Terrestrial: %{customdata[0]}<br>"
                "Freshwater: %{customdata[1]}<br>"
                "Marine: %{customdata[2]}"
                "<extra></extra>"
            ),
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
    
    # Create an empty figure
    fig = go.Figure()
    
    # Layer 1: Marine layer
    fig.add_trace(go.Choropleth(
        geojson=marine_geojson,
        featureidkey="properties.SOVEREIGN1",
        locations=full_country_data["Country"],
        z=full_country_data["Marine"],
        colorscale=marine_colorscale,
        zmin=0,
        zmax=max_marine,
        marker_line_width=0,
        hoverinfo="skip",
        name="",
        colorbar=dict(
            title="Marine Studies",
            thickness=15,
            len=0.4,
            x=1.02,
            y=0.9,
            yanchor="top",
        )
    ))
    
    # Layer 2: Base map
    fig.add_trace(go.Choropleth(
        locations=full_country_data["Country"],
        locationmode="country names",
        z=full_country_data["Studies"],
        zmin=0,
        zmax=max_studies,
        colorscale=colorscale,
        marker_line_color='white',
        marker_line_width=0.5,
        customdata=full_country_data[["Terrestrial", "Freshwater", "Marine"]],
        hovertemplate=(
            "<b>%{location}</b><br>"
            "Total: %{z}<br>"
            "Terrestrial: %{customdata[0]}<br>"
            "Freshwater: %{customdata[1]}<br>"
            "Marine: %{customdata[2]}"
            "<extra></extra>"
            ),
        colorbar=dict(
            title="Total Studies",
            thickness=15,
            thicknessmode="pixels",
            len=0.4, 
            x=1.02,
            y=0.1,
            yanchor="bottom"
        )
    ))
    
    # Layer 3: Dots for small countries
    fig.add_trace(go.Scattergeo(
        locations=small_country_data['Country'],
        locationmode="country names",
        customdata=small_country_data[["Terrestrial", "Freshwater", "Marine"]],
        text=small_country_data["Studies"],
        hovertemplate=(
            "<b>%{location}</b><br>"
            "Total: %{text}<br>"
            "Terrestrial: %{customdata[0]}<br>"
            "Freshwater: %{customdata[1]}<br>"
            "Marine: %{customdata[2]}"
            "<extra></extra>"
        ),
        marker=dict(
            size=6,
            color=small_country_data["Studies"],
            colorscale=colorscale,
            cmin=0,
            cmax=max_studies,
            showscale=False,
            line=dict(width=0.5, color="#636363")
        )
    ))
    
    fig.update_geos(
        showland=True,
        landcolor="#c4c4c4",
        showocean=True,
        oceancolor="#c6dbef",
        showlakes=True,
        lakecolor="#ffffff",
        showcountries=True,
        countrycolor="#ffffff",
        showcoastlines=True,
        coastlinecolor="#ffffff",
        projection_type="natural earth",
        bgcolor="#ffffff",
        showframe=False
    )
    
    fig.update_layout(
        height=500,
        margin={'r': 100, 't': 40, 'l': 0, 'b': 0},
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        # Sensitivity settings for mouse hover (adjust as needed)
        hoverdistance=2
    )
    
    return fig
