# Dashboard callbacks - interactive functionality
# Define Input/Output callbacks for chart updates, data filtering, and user interactions

from dash import Input, Output
from utils.data_loader import df_grossi, filter_grossi_data
from visualizations.charts import create_world_map, create_threat_distribution_chart, create_study_design_chart
from sections.dataframes import ridley_bib_table
from visualizations.tables import articles_datatable


def register_callbacks(app):
    """
    Register all dashboard callbacks.
    Call this function from app.py after layout is set.
    """
    
    @app.callback(
        [
            Output('result-counter', 'children'),
            Output('world-map', 'figure'),
            Output('threat-chart', 'figure'),
            Output('study-design-chart', 'figure'),
        ],
        [
            Input('apply-filters-btn', 'n_clicks')
        ],
        [
            Input('continent-filter', 'value'),
            Input('ecoregion-filter', 'value'),
            Input('study-design-filter', 'value'),
            Input('threat-category-filter', 'value')
        ],
        prevent_initial_call=False
    )
    def update_dashboard(n_clicks, continent, ecoregions, study_designs, threat_category):
        """
        Main callback to filter data and update all visualizations.
        Triggered by Apply Filters button click.
        """


        # Apply filters
        filtered_df = filter_grossi_data(
            continent=continent,
            ecoregions=ecoregions,
            study_designs=study_designs,
            threat_category=threat_category
        )
        
        # Create result counter text
        total_articles = len(df_grossi)
        filtered_count = len(filtered_df)
        counter_text = f"Showing {filtered_count} of {total_articles} articles"
        
        # Generate visualizations
        map_fig = create_world_map(filtered_df)
        threat_fig = create_threat_distribution_chart(filtered_df)
        design_fig = create_study_design_chart(filtered_df)
        
        return counter_text, map_fig, threat_fig, design_fig
    
    @app.callback(
        Output('article_table','data'),
        Input('searchbar','value')
    )

    def update_search_bar(search_value):
        if not search_value:
            filtered_df = ridley_bib_table.to_dict('records')
        else:
            # Case-insensitive search across all columns
            filtered_df = ridley_bib_table[ridley_bib_table.apply(
                lambda row: row.astype(str).str.contains(search_value, case=False).any(),
                axis=1
            )].to_dict('records')
        
        return filtered_df
