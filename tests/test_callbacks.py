import pytest

from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
import dash




def test_update_dashboard_callback(
    trigger,
    n_clicks,
    continent_filter,
    world_map,
    threat_chart,
    study_design_chart,
    wordcloud_chart,
):
    def run_callback(
        trigger,
        n_clicks,
        continent_filter,
        world_map,
        threat_chart,
        study_design_chart,
        wordcloud_chart,
    ):
        context_value.set(AttributeDict(**{"triggered_inputs": [trigger]}))
        return callbacks.display(
            n_clicks, continent_filter, world_map, threat_chart, study_design_chart, wordcloud_chart
        )
    tx = copy_context()
    output = ctx.run(
            run_callback,
            trigger,
            n_clicks,
            continent_filter,
            world_map,
            threat_chart,
            study_design_chart,
            wordcloud_chart,
        )
    assert output == expected_output








# def register_callbacks(app):
#     """
#     Register all dashboard callbacks.
#     Call this function from app.py after layout is set.
#     """
    
#     @app.callback(
#         [
#             Output('result-counter', 'children'),
#             Output('world-map', 'figure'),
#             Output('threat-chart', 'figure'),
#             Output('study-design-chart', 'figure'),
#             Output('wordcloud-chart', 'figure'),
#         ],
#         [
#             Input('apply-filters-btn', 'n_clicks')
#         ],
#         [
#             Input('continent-filter', 'value'),
#             Input('ecoregion-filter', 'value'),
#             Input('study-design-filter', 'value'),
#             Input('threat-category-filter', 'value')
#         ],
#         prevent_initial_call=False
#     )
#     def update_dashboard(n_clicks, continent, ecoregions, study_designs, threat_category):
#         """
#         Main callback to filter data and update all visualizations.
#         Triggered by Apply Filters button click.
#         """


#         # Apply filters
#         filtered_df = filter_ridley_data(
#         # filtered_df = filter_grossi_data(
#             continent=continent,
#             ecoregions=ecoregions,
#             study_designs=study_designs,
#             threat_category=threat_category
#         )
        
#         # Create result counter text
#         total_articles = len(df_ridley)
#         # total_articles = len(df_grossi)
#         filtered_count = len(filtered_df)
#         counter_text = f"Showing {filtered_count} of {total_articles} articles"
        
#         # Generate visualizations
#         map_fig = create_world_map(filtered_df)
#         threat_fig = create_threat_distribution_chart(filtered_df)
#         design_fig = create_study_design_chart(filtered_df)
#         wordcloud_fig = create_wordcloud_chart()
        
#         return counter_text, map_fig, threat_fig, design_fig, wordcloud_fig
    
#     @app.callback(
#         [
#             Output('continent-filter', 'value'),
#             Output('ecoregion-filter', 'value'),
#             Output('study-design-filter', 'value'),
#             Output('threat-category-filter', 'value'),
#             Output('year-range-slider', 'value'),
#         ],
#         Input('reset-filters-btn', 'n_clicks'),
#         prevent_initial_call=True
#     )
#     def reset_all_filters(n_clicks):
#         """
#         Reset all filters to their default values when the Reset Filters button is clicked.
#         """
#         defaults = reset_filters()
#         return (
#             defaults['continent-filter'],
#             defaults['ecoregion-filter'],
#             defaults['study-design-filter'],
#             defaults['threat-category-filter'],
#             defaults['year-range-slider'],
#         )

#     @app.callback(
#         Output('article_table','data'),
#         Input('searchbar','value'),
#         Input('year-range-slider', 'value')
#     )
#     def update_search_bar(search_value, year_range):
#         filtered_df = ridley_bib_table.copy()

#         # Filter by year range
#         if year_range:
#             filtered_df = filtered_df[
#                 (filtered_df['Year'] >= year_range[0]) &
#                 (filtered_df['Year'] <= year_range[1])
#             ]

#         # Filter by search text
#         if search_value:
#             filtered_df = filtered_df[filtered_df.apply(
#                 lambda row: row.astype(str).str.contains(search_value, case=False).any(),
#                 axis=1
#             )]

#         return filtered_df.to_dict('records')