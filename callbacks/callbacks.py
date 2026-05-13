""" Dashboard callbacks - interactive functionality
Define Input/Output callbacks for chart updates, data filtering, and user interactions """
# pylint: disable=unused-argument
# Pre-made packages
from dash import Input, Output, State, ctx, clientside_callback, ClientsideFunction, ALL
from dash.exceptions import PreventUpdate


# local packages
from utils.data_loader import df

from layout.components.search_and_filters import reset_filters
from callbacks.callbacks_functions import (change_views,
                                            update_map,
                                            update_article_table,
                                            update_charts)


def register_callbacks(app):

    # Clientside: scroll charts container to the clicked chart card
    app.clientside_callback(
        """
        function(n_clicks_list, btn_ids) {
            const triggered = dash_clientside.callback_context.triggered;
            if (!triggered || triggered.length === 0) return dash_clientside.no_update;
            const prop = triggered[0].prop_id;
            if (!prop) return dash_clientside.no_update;
            // find the button element that was clicked via data attributes
            const btns = document.querySelectorAll('.chart-nav-pill');
            let scrollContainerId = null;
            let targetId = null;
            btns.forEach(function(btn) {
                if (btn.getAttribute('data-target') && prop.includes(btn.getAttribute('data-target'))) {
                    scrollContainerId = btn.getAttribute('data-scroll');
                    targetId = 'anchor-' + btn.getAttribute('data-target');
                }
            });
            // fallback: parse from prop_id JSON
            if (!targetId) {
                try {
                    const idx = JSON.parse(prop.split('.')[0]);
                    const side = idx.side;
                    const i = idx.index;
                    const charts = ['threat-chart_','driver-sankey_','study-design-chart_','wordcloud-chart_'];
                    targetId = 'anchor-' + charts[i] + side;
                    scrollContainerId = 'charts-scroll-' + side;
                } catch(e) { return dash_clientside.no_update; }
            }
            const container = document.getElementById(scrollContainerId);
            const target = document.getElementById(targetId);
            if (container && target) {
                container.scrollTo({ top: target.offsetTop - container.offsetTop, behavior: 'smooth' });
                // highlight active pill
                document.querySelectorAll('.chart-nav-pill').forEach(b => b.classList.remove('active'));
                const activeSide = scrollContainerId ? scrollContainerId.replace('charts-scroll-','') : '';
                document.querySelectorAll('.chart-nav-pill').forEach(function(b) {
                    if (b.getAttribute('data-target') === targetId.replace('anchor-','') ) {
                        b.classList.add('active');
                    }
                });
            }
            return dash_clientside.no_update;
        }
        """,
        Output('charts-scroll-left', 'data-active', allow_duplicate=True),
        Input({'type': 'chart-nav-btn', 'side': ALL, 'index': ALL}, 'n_clicks'),
        State({'type': 'chart-nav-btn', 'side': ALL, 'index': ALL}, 'id'),
        prevent_initial_call=True,
    )

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
    def update_article_table_right(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
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
            Output('threat-chart_left', 'figure'),
            Output('study-design-chart_left', 'figure'),
            Output('wordcloud-chart_left', 'figure'),
            Output('driver-sankey_left', 'figure'),
        ],
        filter_inputs,
    )
    def update_charts_left(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        return update_charts(df,
                        continent,
                        ecoregions,
                        study_designs,
                        threat_category,
                        year_range,
                        search_value)

    @app.callback(
        [
            Output('threat-chart_right', 'figure'),
            Output('study-design-chart_right', 'figure'),
            Output('wordcloud-chart_right', 'figure'),
            Output('driver-sankey_right', 'figure'),
        ],
        filter_inputs,
    )
    def update_charts_right(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        return update_charts(df,
                        continent,
                        ecoregions,
                        study_designs,
                        threat_category,
                        year_range,
                        search_value)

    @app.callback(
        [
            Output('result-counter_right', 'children'),
            Output('world-map_right', 'figure'),
        ],
        filter_inputs,
    )
    def update_map_right(n_clicks, continent, ecoregions, study_designs, threat_category, year_range, search_value):
        return update_map(df,
                        continent,
                        ecoregions,
                        study_designs,
                        threat_category,
                        year_range,
                        search_value)

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
            Output('searchbar', 'value', allow_duplicate=True),
        ],
        Input('reset-filters-btn', 'n_clicks'),
        prevent_initial_call=True
    )
    def reset_all_filters(n_clicks):
        """
        Reset all filters to their default values when the Reset Filters button is clicked. Also clears the searchbar and map selections.
        """
        defaults = reset_filters()
        return (
            defaults['continent-filter'],
            defaults['ecoregion-filter'],
            defaults['study-design-filter'],
            defaults['threat-category-filter'],
            defaults['year-range-slider'],
            "",
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
    
    @app.callback(
        Output("searchbar", "value", allow_duplicate=True),
        Input("world-map_left", "clickData"),
        State("searchbar", "value"),
        prevent_initial_call=True
    )
    def update_search_map_left(click_data, current_search):
        if not click_data:
            raise PreventUpdate
        
        try:
            clicked_country = click_data["points"][0]["location"]
            if current_search == clicked_country:
                return ""
            else:
                return clicked_country
        except (KeyError, IndexError):
            raise PreventUpdate

    @app.callback(
        Output("searchbar", "value", allow_duplicate=True),
        Input("world-map_right", "clickData"),
        State("searchbar", "value"),
        prevent_initial_call=True
    )
    def update_search_map_right(click_data, current_search):
        if not click_data:
            raise PreventUpdate

        try:
            clicked_country = click_data["points"][0]["location"]
            if current_search == clicked_country:
                return ""
            else:
                return clicked_country
        except (KeyError, IndexError):
            raise PreventUpdate

    @app.callback(
        [
            Output("left-collapse", "is_open"),
            Output("right-collapse", "is_open"),
            Output("left-col", "className"),
            Output("right-col", "className"),
            Output("toggle-left-btn", "children"),
            Output("toggle-right-btn", "children"),
        ],
        [
            Input("toggle-left-btn", "n_clicks"),
            Input("toggle-right-btn", "n_clicks"),
        ],
        [
            State("left-collapse", "is_open"),
            State("right-collapse", "is_open"),
        ],
        prevent_initial_call=True,
    )
    def toggle_panels(n_left, n_right, left_open, right_open):
        triggered = ctx.triggered_id
        if triggered == "toggle-left-btn":
            left_open = not left_open
        elif triggered == "toggle-right-btn":
            right_open = not right_open

        if left_open and right_open:
            left_class, right_class = "col-6", "col-6"
        elif left_open and not right_open:
            left_class, right_class = "col-12", "col-12 d-none"
        elif not left_open and right_open:
            left_class, right_class = "col-12 d-none", "col-12"
        else:
            # both collapsed — restore both
            left_open, right_open = True, True
            left_class, right_class = "col-6", "col-6"

        left_label = "▼ Hide" if left_open else "▶ Show"
        right_label = "▼ Hide" if right_open else "▶ Show"
        return left_open, right_open, left_class, right_class, left_label, right_label

    @app.callback(
        Output("filter-collapse", "is_open"),
        Output("toggle-filter-btn", "children"),
        Input("toggle-filter-btn", "n_clicks"),
        State("filter-collapse", "is_open"),
        prevent_initial_call=True,
    )
    def toggle_filter(n_clicks, is_open):
        new_state = not is_open
        label = "▼ Hide Filters" if new_state else "▶ Show Filters"
        return new_state, label
