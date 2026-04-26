"Functions for callbacks"
from utils.data_loader import filter_data
from layout.layoutviews import map_view, charts_view, table_view
from layout.components.maps import create_world_map
from layout.components.charts import create_threat_distribution_chart, create_study_design_chart, create_wordcloud_chart, create_driver_sankey
from utils.data_loader import df_threats
from utils.dataframes import ridley_driver_lookup


def apply_filters(df,continent, ecoregions,study_designs,threat_category,year_range,search_value):        
    filtered_df = df.copy()

    # Apply filters
    filtered_df = filter_data(
        dataframe=filtered_df,
        continent=continent,
        ecoregions=ecoregions,
        study_designs=study_designs,
        threat_category=threat_category
    )

    # Filter by year range
    filtered_df = year_range_filter(year_range, filtered_df)

    # Filter by search text
    filtered_df = search_value_filter(search_value, filtered_df)

    return filtered_df

def update_article_table(df, continent, ecoregions, study_designs, threat_category, year_range, search_value):
    """
    Main callback to filter data and update all visualizations.
    Triggered by Apply Filters button click.
    """

    filtered_df = apply_filters(df,continent,ecoregions,study_designs,threat_category,year_range,search_value)

    # Build article table only
    table_df = filtered_df[['ArticleID', 'Authors', 'Year', 'Title']].copy()
    table_df['ArticleID'] = table_df['ArticleID'].astype(str)

    table_df = table_df.merge(
        ridley_driver_lookup,
        on='ArticleID',
        how='left'
    )

    table_df = table_df[
        [
            'Authors',
            'Year',
            'Title',
            'Georef_ind_driver_clean',
            'Direct_driver_clean',
            'Indirect_driver_clean'
        ]
    ]

    # Create tooltip data for the Title column only
    tooltip_data = [
        {
            'Title': {'value': row['Title'], 'type': 'text'} 
        } for _, row in table_df.iterrows()
    ]
    return [table_df.to_dict('records'), tooltip_data]

def update_map(df, continent, ecoregions, study_designs, threat_category, year_range, search_value):
    filtered_df = apply_filters(df,
                    continent,
                    ecoregions,
                    study_designs,
                    threat_category,
                    year_range,
                    search_value)

    # Create result counter text
    total_articles = len(df)
    filtered_count = len(filtered_df)
    counter_text = f"Showing {filtered_count} of {total_articles} articles"

    # Generate visualizations
    map_fig = create_world_map(filtered_df)

    return counter_text, map_fig

def update_charts(df, continent, ecoregions, study_designs, threat_category, year_range, search_value):

    filtered_df = apply_filters(df,
                        continent,
                        ecoregions,
                        study_designs,
                        threat_category,
                        year_range,
                        search_value)

    # Generate visualizations
    threat_fig    = create_threat_distribution_chart(filtered_df)
    design_fig    = create_study_design_chart(filtered_df)
    wordcloud_fig = create_wordcloud_chart(filtered_df)
    sankey_fig    = create_driver_sankey(filtered_df, df_threats)

    return threat_fig, design_fig, wordcloud_fig, sankey_fig


def year_range_filter(year_range, filtered_df):
    if year_range:
        filtered_df = filtered_df[
            (filtered_df['Year'] >= year_range[0]) &
            (filtered_df['Year'] <= year_range[1])
        ]
    return filtered_df

def search_value_filter(search_value,filtered_df):
    if search_value:
        filtered_df = filtered_df[filtered_df.apply(
            lambda row: row.astype(str).str.contains(search_value, case=False, na=False).any(),
            axis=1
        )]
    return filtered_df

def change_views(view,side):
    if view == "Charts":
        return charts_view(side, selected_view=view)
    if view == "Article_Table":
        return table_view(side, selected_view=view)
    if view == "Map":
        return map_view(side, selected_view=view)
    if side == "right":
        return table_view(side, selected_view="Article_Table")
    if side == "left":
        return map_view(side, selected_view="Map")