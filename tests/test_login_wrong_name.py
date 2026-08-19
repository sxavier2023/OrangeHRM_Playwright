from pages.login_page import LoginPage
from data.login_data import EMPTY_USERNAME


def test_valid_login(page):
    
    login  = LoginPage(page)
    
    login.open()
    
    login.login (EMPTY_USERNAME ["username"],EMPTY_USERNAME["password"])
    
    assert login.get_required_message() == "Required"
