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
from layout.layoutviews import map_view, charts_view, table_view


def register_callbacks(app):
    """
    Register all dashboard callbacks.
    Call this function from app.py after layout is set.
    """
    
    @app.callback(
        [
<<<<<<< 61-again-work-on-the-map-view-once-more
            Output('result-counter', 'children'),
            Output('world-map', 'figure'),
            Output('threat-chart', 'figure'),
            Output('study-design-chart', 'figure'),
            Output('wordcloud-chart', 'figure'),
=======
            Output('article_table', 'data'),
            Output('article_table', 'tooltip_data'),
>>>>>>> Development
        ],
        [
            Input('apply-filters-btn', 'n_clicks'),
            Input('continent-filter', 'value'),
            Input('ecoregion-filter', 'value'),
            Input('study-design-filter', 'value'),
            Input('threat-category-filter', 'value'),
<<<<<<< 61-again-work-on-the-map-view-once-more
            Input('world-map', 'clickData'),
        ],
        prevent_initial_call=False
    )
    def update_dashboard(n_clicks, continent, ecoregions, study_designs, threat_category, click_data):
=======
            Input('year-range-slider', 'value'),
            Input('searchbar', 'value')
        ],
        prevent_initial_call=False
    )
    def update_article_table(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
>>>>>>> Development
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
        
        # Generate visualizations

        table_df = filtered_df[['Authors', 'Year', 'Title']]
        # Create tooltip data for the Title column only
        tooltip_data = [
            {
                'Title': {'value': row['Title'], 'type': 'text'}  # shows title as tooltip when hovering over Title cell
            } for _, row in table_df.iterrows()
        ]
        return [table_df.to_dict('records'), tooltip_data]
    @app.callback(
        [
        Output('threat-chart', 'figure'),
        Output('study-design-chart', 'figure'),
        Output('wordcloud-chart', 'figure'),
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
    )
    def update_charts(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):

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
        
        # Generate visualizations
        threat_fig = create_threat_distribution_chart(filtered_df)
        design_fig = create_study_design_chart(filtered_df)
        wordcloud_fig = create_wordcloud_chart(filtered_df)
        
        return threat_fig, design_fig, wordcloud_fig
    @app.callback(
        [            
            Output('result-counter', 'children'),
            Output('world-map', 'figure'),
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
    )
    def update_map(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
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
        
        # Apply map click filtering
        if click_data:
            try:
                country_clicked = click_data["points"][0].get("location")
                if country_clicked:
                    filtered_df = filtered_df[filtered_df["Country"] == country_clicked]
            except (KeyError, IndexError):
                pass

        # Create result counter text
        total_articles = len(df_ridley)
        filtered_count = len(filtered_df)
        counter_text = f"Showing {filtered_count} of {total_articles} articles"
        
        # Generate visualizations
        map_fig = create_world_map(filtered_df)
        
        return counter_text, map_fig

    @app.callback(
        [
            Output('continent-filter', 'value'),
            Output('ecoregion-filter', 'value'),
            Output('study-design-filter', 'value'),
            Output('threat-category-filter', 'value'),
            Output('year-range-slider', 'value'),
            Output('world-map', 'clickData'),
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
            None, # Clear map click data
        )
    @app.callback(
<<<<<<< 61-again-work-on-the-map-view-once-more
        Output('article_table','data'),
        Input('searchbar','value'),
        Input('year-range-slider', 'value'),
        Input("world-map", "clickData"),
    )
    def update_search_bar(search_value, year_range, click_data):
        filtered_df = ridley_bib_table.copy()

        # Filter by year range
        if year_range:
            filtered_df = filtered_df[
                (filtered_df['Year'] >= year_range[0]) &
                (filtered_df['Year'] <= year_range[1])
            ]

        # Filter by search text
        if search_value:
            filtered_df = filtered_df[filtered_df.apply(
                lambda row: row.astype(str).str.contains(search_value, case=False).any(),
                axis=1
            )]
            
        # Filter by clicked country on the map
        if click_data:
            try:    
                country_clicked = click_data["points"][0].get("location")
                if country_clicked:
                    filtered_df = filtered_df[filtered_df["Country"] == country_clicked]
            except (KeyError, IndexError):
                pass

        return filtered_df.to_dict('records')
=======
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
    def change_views_left(change_views):
        if change_views == "Charts":
            return charts_view("left")
        if change_views == "Map":
            return map_view("left")
        return table_view("left")
    @app.callback(
        Output("right_view","children"),
        Input("change_views_right","value")
    )
    def change_views_right(change_views):
        if change_views == "Charts":
            return charts_view("right")
        if change_views == "Article_Table":
            return table_view("right")
        return map_view("right")
>>>>>>> Development
