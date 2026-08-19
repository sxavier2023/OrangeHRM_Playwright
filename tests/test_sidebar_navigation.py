from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.maintenance_page import MaintenancePage
from pages.side_bar_hamburger_page import SidebarComponent
from data.login_data import VALID_LOGIN

def test_dashboard_displayed(page):

    login = LoginPage(page)
    navigation = SidebarComponent(page)
    dashboard = DashboardPage(page)
    maintenance = MaintenancePage(page)
    

    login.open()

    login.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )
    assert dashboard.dashboard_is_displayed()

    menus = [
        navigation.ADMIN,
        navigation.PIM,
        navigation.PERFORMANCE,
        navigation.MY_INFO,
        navigation.DIRECTORY,
        navigation.DASHBOARD,
        navigation.MAINTENANCE,
        navigation.TIME,
        navigation.RECRUITMENT,
        navigation.BUZZ,
    ]

    for menu in menus:
        navigation.open_menu(menu)
        if menu == navigation.MAINTENANCE:
            maintenance.verify_admin_password(VALID_LOGIN["password"])
        navigation.wait(3)