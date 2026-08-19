from pages.base_page import BasePage


class MaintenancePage(BasePage):

    TITLE = "h6"
    PASSWORD = "input[name='password']"
    CONFIRM = "button[type='submit']"
    CANCEL = "button.oxd-button--ghost"

    def page_loaded(self):
        return self.get_text(self.TITLE) == "Maintenance"

    def admin_access_form_visible(self):
        return self.is_visible(self.PASSWORD)

    def verify_admin_password(self, password):
        self.fill(self.PASSWORD, password)
        self.click(self.CONFIRM)
