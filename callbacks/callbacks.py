""" Dashboard callbacks - interactive functionality
Define Input/Output callbacks for chart updates, data filtering, and user interactions """
# pylint: disable=unused-argument
# Pre-made packages
from dash import Input, Output, State


# local packages
from utils.data_loader import df

from layout.components.search_and_filters import reset_filters
from layout.components.charts import create_threat_distribution_chart, create_study_design_chart, create_wordcloud_chart
from callbacks.callbacks_functions import apply_filters,change_views, update_map, update_article_table


def register_callbacks(app):
    """
    Register all dashboard callbacks.
    Call this function from app.py after layout is set.
    """
    filter_inputs = [
            Input('apply-filters-btn', 'n_clicks'),
            Input('continent-filter', 'value'),
            Input('ecoregion-filter', 'value'),
            Input('study-design-filter', 'value'),
            Input('threat-category-filter', 'value'),
            Input('year-range-slider', 'value'),
            Input('searchbar', 'value')
        ]

    @app.callback(
        [
            Output('article_table_left', 'data'),
            Output('article_table_left', 'tooltip_data'),
        ],
        filter_inputs,
        prevent_initial_call=False
    )
    def update_article_table_left(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        """
        Main callback to filter data and update all visualizations.
        Triggered by Apply Filters button click.
        """

        return update_article_table(df, 
                            continent, 
                            ecoregions, 
                            study_designs, 
                            threat_category, 
                            year_range, 
                            search_value)
    @app.callback(
        [
            Output('article_table_right', 'data'),
            Output('article_table_right', 'tooltip_data'),
        ],
        filter_inputs,
        prevent_initial_call=False
    )
    def update_article_table_left(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        """
        Main callback to filter data and update all visualizations.
        Triggered by Apply Filters button click.
        """

        return update_article_table(df, 
                            continent, 
                            ecoregions, 
                            study_designs, 
                            threat_category, 
                            year_range, 
                            search_value)
    @app.callback(
        [
        Output('threat-chart', 'figure'),
        Output('study-design-chart', 'figure'),
        Output('wordcloud-chart', 'figure'),
        ],
        filter_inputs,
    )
    def update_charts(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):

        filtered_df = apply_filters(df,
                            continent,
                            ecoregions,
                            study_designs,
                            threat_category,
                            year_range,
                            search_value)

        # Generate visualizations
        threat_fig = create_threat_distribution_chart(filtered_df)
        design_fig = create_study_design_chart(filtered_df)
        wordcloud_fig = create_wordcloud_chart(filtered_df)

        return threat_fig, design_fig, wordcloud_fig
    @app.callback(
        [           
            Output('result-counter_right', 'children'),
            Output('world-map_right', 'figure'),
        ],
        filter_inputs,
    )

    def update_map_right(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        return update_map(df,continent, ecoregions, study_designs, threat_category, year_range, search_value)

    @app.callback(
        [            
            Output('result-counter_left', 'children'),
            Output('world-map_left', 'figure'),
        ],
        filter_inputs,
    )

    def update_map_left(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        return update_map(df,
                    continent,
                    ecoregions,
                    study_designs,
                    threat_category,
                    year_range,
                    search_value)

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
    @app.callback(
        Output("left_view","children"),
        Input("change_views_left","value")
    )
    def change_views_left(change_views_left):
        return change_views(change_views_left,"left")
    @app.callback(
        Output("right_view","children"),
        Input("change_views_right","value")
    )
    def change_views_right(change_views_right):
        return change_views(change_views_right,"right")
