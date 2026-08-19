from pages.login_page import LoginPage
from pages.side_bar_hamburger_page import SidebarComponent
from pages.admin_page import AdminPage

from data.login_data import VALID_LOGIN


def test_add_admin_user(page):

    login = LoginPage(page)
    navigation = SidebarComponent(page)
    admin = AdminPage(page)

    # 1. Login
    login.open()

    login.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # 2. Open Admin
    navigation.open_menu(navigation.ADMIN)

    # 3. Verify Admin page
    assert admin.page_loaded()

    # 4. Click Add
    admin.click_add_user()

    # 5. Select User Role
    admin.select_user_role("Admin")

    # 6. Select Status
    admin.select_status("Enabled")

    # 7. Fill user details
    admin.enter_employee_name("John Doe")
    admin.enter_username("john.doe")

    admin.enter_password("Password123!")
    admin.enter_confirm_password("Password123!")

    # 8. Save
    admin.click_save()