from pages.login_page import LoginPage
from data.login_data import VALID_LOGIN
from pages.dashboard_page import DashboardPage
def test_valid_login(page):
    
    login  = LoginPage(page)
    dashboard = DashboardPage(page)
    login.open()
    
    login.login(VALID_LOGIN["username"],VALID_LOGIN["password"])
    
    assert dashboard.dashboard_is_displayed()

    dashboard.take_screenshot("login_valid_dashboard")
    