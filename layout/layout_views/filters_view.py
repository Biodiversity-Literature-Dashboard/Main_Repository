from layout.components.search_and_filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter, year_range_slider
from dash import html
import dash_bootstrap_components as dbc


def filters_view():
        filters_container = dbc.Card([
                dbc.CardHeader("Filters", style={"fontWeight": "bold"}),
                dbc.CardBody([
                    # Continent filter
                    html.Label("Continent/Ocean:", className="fw-bold mb-2"),
                    continent_filter,
                    
                    # Ecoregion filter (checkboxes - can select multiple)
                    html.Label("Ecoregion:", className="fw-bold mb-2 mt-3"),
                    ecoregion_filter,
                    
                    # Study Design filter (checkboxes)
                    html.Label("Study Design:", className="fw-bold mb-2 mt-3"),
                    study_design_filter,
                    
                    # Threat Category filter
                    html.Label("Threat Category:", className="fw-bold mb-2 mt-3"),
                    threat_category_filter,

                    # Year range filter (filters articles table)
                    html.Label("Publication Year (Articles Table):", className="fw-bold mb-2 mt-3"),
                    year_range_slider,

                    # Apply button (will wire up in callbacks later)
                    html.Hr(),
                    dbc.Button("Apply Filters", id="apply-filters-btn", color="primary", className="w-100 mt-2"),
                    #reset button
                    dbc.Button("Reset Filters", id="reset-filters-btn", color="secondary", className="w-100 mt-2", n_clicks=0)
                ])
            ], className="h-100")
        return filters_container

filters_view = filters_view()
