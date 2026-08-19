from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.side_bar_hamburger_page import SidebarComponent
from data.login_data import VALID_LOGIN

def test_dashboard_displayed(page):

    login = LoginPage(page)
    sidebar = SidebarComponent(page)
    dashboard = DashboardPage(page)

    login.open()

    login.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )
    dashboard.dashboard_is_displayed()
    


    