from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):

    USERNAME = "input[name='username']"
    PASSWORD = "input[name='password']"
    LOGIN = "button[type='submit']"
    ERROR_MESSAGE = ".oxd-alert-content-text"
    REQUIRED_MESSAGE = ".oxd-input-field-error-message"

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN)    
    def invalid_login(self):
        return self.is_visible(self.ERROR_MESSAGE)
    def required_message(self):
        return self.is_visible(self.REQUIRED_MESSAGE)
    def get_required_message(self):
        return self.get_text(self.REQUIRED_MESSAGE)
    def get_invalid_message(self):
        return self.get_text(self.ERROR_MESSAGE)