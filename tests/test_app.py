def test_app_starts(dash_duo):
    from app import app
    dash_duo.start_server(app)
    assert dash_duo.get_logs() == []


def test_title_present(dash_duo):
    from app import app
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal(".navbar-brand", "Interactive Biodiversity Dashboard")


def test_graph_exists(dash_duo):
    from app import app
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#threat-chart")
    assert graph is not None

def test_layout_rendered(dash_duo):
    from app import app
    dash_duo.start_server(app)
    navbar = dash_duo.find_element(".navbar")  # change if class is different
    assert navbar is not None
    # Main container exists
    main_container = dash_duo.find_element(".container-fluid")
    assert main_container is not None
# ----------------------------
# Graphs exist test
# ----------------------------
def test_charts_exist(dash_duo):
    """Check that all main charts exist in layout"""
    from app import app
    dash_duo.start_server(app)

    # Threat chart
    threat_chart = dash_duo.find_element("#threat-chart")
    assert threat_chart is not None

    # Study Design chart
    study_chart = dash_duo.find_element("#study-design-chart")
    assert study_chart is not None

    # Wordcloud chart
    wordcloud_chart = dash_duo.find_element("#wordcloud-chart")
    assert wordcloud_chart is not None