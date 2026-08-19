from pages.login_page import LoginPage
from pages.side_bar_hamburger_page import SidebarComponent
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from data.login_data import VALID_LOGIN


def test_pim_tabs_navigation(page):

    login = LoginPage(page)
    navigation = SidebarComponent(page)
    dashboard = DashboardPage(page)
    pim = PimPage(page)

    # 1. Login
    login.open()
    login.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    assert dashboard.dashboard_is_displayed()

    # 2. Open PIM from the sidebar
    navigation.open_menu(navigation.PIM)
    assert pim.page_loaded()

    # 3. Employee List is the default tab after clicking PIM
    pim.wait_for_employee_list()
    assert pim.on_employee_list()
    pim.take_screenshot("pim_default_employee_list")

    # 4. Click Add Employee
    pim.click_add_employee()
    pim.wait(2)
    assert pim.on_add_employee()
    pim.take_screenshot("pim_add_employee")

    # 5. Click Reports
    pim.click_reports()
    pim.wait(2)
    assert pim.on_reports()
    pim.take_screenshot("pim_reports")

    # 6. Click back to Employee List
    pim.click_employee_list()
    pim.wait(2)
    assert pim.on_employee_list()
    pim.take_screenshot("pim_back_employee_list")