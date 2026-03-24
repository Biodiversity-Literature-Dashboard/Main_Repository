# Dashboard callbacks - interactive functionality
# Define Input/Output callbacks for chart updates, data filtering, and user interactions

# Pre-made packages
from dash import Input, Output, State


# local packages
from utils.data_loader import df_ridley, filter_data
# from utils.data_loader import df_grossi, filter_grossi_data
from layout.components.search_and_filters import reset_filters
from layout.components.charts import create_threat_distribution_chart, create_study_design_chart, create_wordcloud_chart
from layout.components.maps import create_world_map
from sections.dataframes import ridley_bib_table
from layout.components.tables import articles_datatable


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
            Output('wordcloud-chart', 'figure'),
            Output('article_table', 'data'),
        ],
        [
            Input('apply-filters-btn', 'n_clicks'),
            Input('continent-filter', 'value'),
            Input('ecoregion-filter', 'value'),
            Input('study-design-filter', 'value'),
            Input('threat-category-filter', 'value'),
            Input('year-range-slider', 'value'),
            Input('searchbar', 'value')
        ],
        prevent_initial_call=False
    )
    def update_dashboard(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        """
        Main callback to filter data and update all visualizations.
        Triggered by Apply Filters button click.
        """

        filtered_df = df_ridley.copy()

        # Apply filters
        filtered_df = filter_data(
            df=filtered_df,
            continent=continent,
            ecoregions=ecoregions,
            study_designs=study_designs,
            threat_category=threat_category
        )

        # Filter by year range
        if year_range:
            filtered_df = filtered_df[
                (filtered_df['Year'] >= year_range[0]) &
                (filtered_df['Year'] <= year_range[1])
            ]

        # Filter by search text
        if search_value:
            filtered_df = filtered_df[filtered_df.apply(
                lambda row: row.astype(str).str.contains(search_value, case=False, na=False).any(),
                axis=1
            )]
        
        # Create result counter text
        total_articles = len(df_ridley)
        # total_articles = len(df_grossi)
        filtered_count = len(filtered_df)
        counter_text = f"Showing {filtered_count} of {total_articles} articles"
        
        # Generate visualizations
        map_fig = create_world_map(filtered_df)
        threat_fig = create_threat_distribution_chart(filtered_df)
        design_fig = create_study_design_chart(filtered_df)
        wordcloud_fig = create_wordcloud_chart(filtered_df)

        table_df = filtered_df[['Authors', 'Year', 'Title']]
        
        return counter_text, map_fig, threat_fig, design_fig, wordcloud_fig, table_df.to_dict('records')
    
    @app.callback(
        [
            Output('continent-filter', 'value'),
            Output('ecoregion-filter', 'value'),
            Output('study-design-filter', 'value'),
            Output('threat-category-filter', 'value'),
            Output('year-range-slider', 'value'),
        ],
        Input('reset-filters-btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def reset_all_filters(n_clicks):
        """
        Reset all filters to their default values when the Reset Filters button is clicked.
        """
        defaults = reset_filters()
        return (
            defaults['continent-filter'],
            defaults['ecoregion-filter'],
            defaults['study-design-filter'],
            defaults['threat-category-filter'],
            defaults['year-range-slider'],
        )
    @app.callback(
        Output("info-modal", "is_open"),
        [
            Input("info-button", "n_clicks"),
            Input("close-info", "n_clicks")
        ],
        [
            State("info-modal", "is_open")
        ]
    )
    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open