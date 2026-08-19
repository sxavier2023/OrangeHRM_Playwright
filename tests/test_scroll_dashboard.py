from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.login_data import VALID_LOGIN

def test_dashboard_displayed(page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.open()

    login.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )
    dashboard.dashboard_is_displayed()

    dashboard.scroll_to_text("Employee Distribution by Sub Unit")
    dashboard.scroll_to_text("Employee Distribution by Location")

    assert dashboard.widget_visible(dashboard.EMPLOYEE_LOCATION)
    widgets = [
        dashboard.TIME_AT_WORK,
        dashboard.MY_ACTIONS,
        dashboard.EMPLOYEE_DISTRIBUTION,
        dashboard.EMPLOYEE_LOCATION,
        
    ]

    for widget in widgets:
        assert dashboard.widget_visible(widget)