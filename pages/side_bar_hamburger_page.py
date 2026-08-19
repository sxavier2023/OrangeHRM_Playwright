from pages.base_page import BasePage


class SidebarComponent(BasePage):

    SEARCH_BOX = "input[placeholder='Search']"

    ADMIN = "span.oxd-main-menu-item--name:text-is('Admin')"
    PIM = "span.oxd-main-menu-item--name:text-is('PIM')"
    PERFORMANCE = "span.oxd-main-menu-item--name:text-is('Performance')"
    MY_INFO = "span.oxd-main-menu-item--name:text-is('My Info')"
    DIRECTORY = "span.oxd-main-menu-item--name:text-is('Directory')"
    DASHBOARD = "span.oxd-main-menu-item--name:text-is('Dashboard')"
    MAINTENANCE = "span.oxd-main-menu-item--name:text-is('Maintenance')"
    TIME = "span.oxd-main-menu-item--name:text-is('Time')"
    RECRUITMENT = "span.oxd-main-menu-item--name:text-is('Recruitment')"
    BUZZ = "span.oxd-main-menu-item--name:text-is('Buzz')"
    MENU_TOGGLE = "button.oxd-main-menu-button"

    def search_is_displayed(self):
        return self.is_visible(self.SEARCH_BOX)

    def search(self, text):
        self.fill(self.SEARCH_BOX, text)

    def get_search_text(self):
        return self.page.locator(self.SEARCH_BOX).input_value()

    def open_menu(self, menu):
        self.page.locator(menu).click(no_wait_after=True)

    def menu_is_displayed(self, title):
        return self.get_text("h6") == title