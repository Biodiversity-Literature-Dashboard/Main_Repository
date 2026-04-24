import pandas as pd

from callbacks.callbacks_functions import (
    apply_filters,
    year_range_filter,
    search_value_filter,
    update_article_table,
    update_map,
    change_views,
)
from utils.data_loader import df


# --- apply_filters ---

def test_apply_filters_no_filters_returns_full_df():
    result = apply_filters(df, 'all', ['Terrestrial', 'Marine', 'Freshwater'],
                           ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    assert len(result) == len(df)


def test_apply_filters_with_continent_reduces_rows():
    result = apply_filters(df, 'Africa', ['Terrestrial', 'Marine', 'Freshwater'],
                           ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    assert isinstance(result, pd.DataFrame)
    assert len(result) < len(df)


# --- year_range_filter ---

def test_year_range_filter_restricts_to_range():
    result = year_range_filter([2010, 2015], df)
    assert result['Year'].between(2010, 2015).all()


def test_year_range_filter_none_returns_unchanged():
    result = year_range_filter(None, df)
    assert len(result) == len(df)


# --- search_value_filter ---

def test_search_value_filter_none_returns_unchanged():
    result = search_value_filter(None, df)
    assert len(result) == len(df)


def test_search_value_filter_no_match_returns_empty():
    result = search_value_filter("xyzzy_no_match_9999", df)
    assert len(result) == 0


# --- update_article_table ---

def test_update_article_table_returns_data_and_tooltips():
    # Returns (list_of_records, list_of_tooltip_dicts) — both must be lists of equal length
    data, tooltips = update_article_table(df, 'all', ['Terrestrial', 'Marine', 'Freshwater'],
                                          ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    assert isinstance(data, list)
    assert isinstance(tooltips, list)
    assert len(data) == len(tooltips)


def test_update_article_table_records_have_required_keys():
    data, _ = update_article_table(df, 'all', ['Terrestrial', 'Marine', 'Freshwater'],
                                   ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    assert all({'Authors', 'Year', 'Title'}.issubset(row.keys()) for row in data)


# --- update_map ---

def test_update_map_returns_counter_text_and_figure():
    counter, fig = update_map(df, 'all', ['Terrestrial', 'Marine', 'Freshwater'],
                              ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    assert "Showing" in counter and "of" in counter


def test_update_map_filtered_count_less_than_total_when_continent_selected():
    counter, _ = update_map(df, 'Africa', ['Terrestrial', 'Marine', 'Freshwater'],
                            ['Observational', 'Experimental', 'S_Review'], 'all', None, None)
    shown = int(counter.split("Showing ")[1].split(" of")[0])
    assert shown < len(df)


# --- change_views ---

def test_change_views_returns_component_for_all_valid_views():
    assert change_views("Charts", "left") is not None
    assert change_views("Article_Table", "right") is not None
    assert change_views("Map", "left") is not None


def test_change_views_unknown_view_defaults_by_side():
    # unknown view: left side falls back to map_view, right side to table_view
    assert change_views("Unknown", "left") is not None
    assert change_views("Unknown", "right") is not None
