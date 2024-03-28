import dash.testing.wait as wait
from selenium.webdriver.common.by import By

def header_test(dash_duo):
    dash_duo.start_server(app)

    if_header = dash_duo.find_element('h1')
    assert if_header.text == "Visualization of Sales"

def visual_test(dash_duo):
    dash_duo.start_server(app)

    if_visual = dash_duo.find_element('#sales')
    assert visual_test

def region_test(dash_duo):
    dash_duo.start_server(app)

    if_region = dash_duo.find_element('#Select-Region')
    assert if_region