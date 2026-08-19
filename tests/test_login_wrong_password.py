from pages.login_page import LoginPage
from data.login_data import INVALID_PASSWORD


def test_valid_login(page):
    
    login  = LoginPage(page)
    
    login.open()
    
    login.login (INVALID_PASSWORD ["username"],INVALID_PASSWORD["password"])
    
    assert login.get_invalid_message() == "Invalid credentials"

    login.take_screenshot("login_wrong_password_error")