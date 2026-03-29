from utils.data_loader import filter_data
from layout.layoutviews import map_view, charts_view, table_view



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
        return charts_view(side)
    if view == "Article_Table":
        return table_view(side)
    if view == "Map":
        return map_view(side)
    if side == "right":
        return map_view(side)
    if side == "left":
        return table_view(side)
