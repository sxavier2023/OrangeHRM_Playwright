from pages.base_page import BasePage

class DashboardPage(BasePage):
    
    DASHBOARD_TITLE = ".oxd-topbar-header-breadcrumb-module"

    HELP = "button[title='Help']"
    STOPWATCH = "button:has(i.bi-stopwatch)"

    TIME_AT_WORK = "text=Time at Work"
    MY_ACTIONS = "text=My Actions"
    QUICK_LAUNCH = "text=Quick Launch"
    BUZZ_LATEST = "text=Buzz Latest Posts"
    EMPLOYEES_ON_LEAVE = "text=Employees on Leave Today"
    EMPLOYEE_DISTRIBUTION = "text=Employee Distribution by Sub Unit"
    EMPLOYEE_LOCATION = "text=Employee Distribution by Location"
    LOGO = "img[alt='client brand banner']"
    SEARCH_INPUT = "input[placeholder='Search']"

    def logo_is_displayed(self):
        return self.is_visible(self.LOGO)

    def dashboard_is_displayed(self):
        return self.get_text(self.DASHBOARD_TITLE) == "Dashboard"

    def widget_visible(self, widget):
        return self.is_visible(widget)
    
    def scroll_to_employee_distribution(self):
        self.page.locator(self.EMPLOYEE_DISTRIBUTION).scroll_into_view_if_needed()

    def scroll_to_employee_location(self):
        self.page.locator(self.EMPLOYEE_LOCATION).scroll_into_view_if_needed()
        
    def search_is_displayed(self):
        return self.is_visible(self.SEARCH_INPUT)

    def search(self, text):
        self.fill(self.SEARCH_INPUT, text)

    def get_search_value(self):
        return self.page.locator(self.SEARCH_INPUT).input_value()
    