from app import app
import time
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

def test_app_starts(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.get_logs() == [] or dash_duo.get_logs() is None


def test_title_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal(".navbar-brand", "What is the evidence on indirect drivers of biodiversity loss? A systematic map")

def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.multiple_click("#change_views_left",1)
    time.sleep(0.5)
    charts_button = dash_duo.driver.find_element(By.XPATH, "//*[text()='Charts']")
    charts_button.click()
    graph = dash_duo.find_element("#threat-chart_left")
    assert graph is not None

def test_layout_rendered(dash_duo):
    dash_duo.start_server(app)
    navbar = dash_duo.find_element(".navbar")
    assert navbar is not None
    # Main container exists
    main_container = dash_duo.find_element(".container-fluid")
    assert main_container is not None

def test_charts_exist(dash_duo):
    """Check that all main charts exist in layout"""
    dash_duo.start_server(app)
    dash_duo.multiple_click("#change_views_right",1)
    time.sleep(0.5)
    charts_button = dash_duo.driver.find_element(By.XPATH, "//*[text()='Charts']")
    charts_button.click()

    # Threat chart
    threat_chart = dash_duo.find_element("#threat-chart_right")
    assert threat_chart is not None

    # Study Design chart
    study_chart = dash_duo.find_element("#study-design-chart_right")
    assert study_chart is not None

    study_chart = dash_duo.find_element("#driver-sankey_right")
    assert study_chart is not None

    # Wordcloud chart
    wordcloud_chart = dash_duo.find_element("#wordcloud-chart_right")
    assert wordcloud_chart is not None

#Map exist test

def test_map_exists(dash_duo):
    dash_duo.start_server(app)

    dash_duo.wait_for_element("#world-map_left", timeout=10)
    map_element = dash_duo.find_element("#world-map_left")
    assert map_element is not None

# Map renders correctly test
def test_map_renders(dash_duo):
    dash_duo.start_server(app)

    # Set browser window size for headless rendering
    dash_duo.driver.set_window_size(1200, 800)

    # Wait for the element to exist
    dash_duo.wait_for_element("#world-map_left", timeout=10)

    map_element = None
    for _ in range(10):
        try:
            map_element = dash_duo.find_element("#world-map_left")
            # Check displayed and has non-zero size
            if map_element.is_displayed() and map_element.size['width'] > 0 and map_element.size['height'] > 0:
                break
        except StaleElementReferenceException:
            # Element can become stale while the map is re-rendering; ignore and retry
            pass
        time.sleep(0.5)
    else:
        assert False, "Map did not render properly"

    # Final assertions
    assert map_element.is_displayed()
    assert map_element.size['width'] > 0
    assert map_element.size['height'] > 0
# This test checks that the articles table renders with correct ID
def test_articles_table_renders(dash_duo):
    # Start the Dash app in the test server
    dash_duo.start_server(app)

    # Wait until the table element with id 'article_table' is in the DOM
    dash_duo.wait_for_element("#article_table_right")

    # Grab the table element
    table = dash_duo.find_element("#article_table_right")
    
    # Assert the table exists
    assert table is not None

    #check that it has rows (data)
    rows = dash_duo.find_elements("#article_table_right .dash-cell")
    assert len(rows) > 0

    # check column headers
    headers = dash_duo.find_elements("#article_table_right .column-header-name")
    header_texts = [h.text for h in headers]
    assert "Authors" in header_texts
    assert "Year" in header_texts
    assert "Title" in header_texts
