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