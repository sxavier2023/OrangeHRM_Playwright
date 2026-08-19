from pages.base_page import BasePage


class AdminPage(BasePage):

    # =========================
    # Page
    # =========================

    TITLE = ".oxd-topbar-header-breadcrumb-module"

    # =========================
    # Add User
    # =========================

    ADD_USER_BUTTON = "button:has-text('Add')"

    # =========================
    # Dropdowns
    # =========================

    USER_ROLE_DROPDOWN = (
        "div.oxd-input-group"
        ":has(label:has-text('User Role'))"
        " .oxd-select-text"
    )

    STATUS_DROPDOWN = (
        "div.oxd-input-group"
        ":has(label:has-text('Status'))"
        " .oxd-select-text"
    )

    # =========================
    # Input fields
    # =========================

    EMPLOYEE_NAME = "input[placeholder='Type for hints...']"

    USERNAME = (
        "div.oxd-input-group"
        ":has(label:has-text('Username'))"
        " input"
    )

    PASSWORD = (
        "div.oxd-input-group"
        ":has(label:text-is('Password'))"
        " input"
    )

    CONFIRM_PASSWORD = (
        "div.oxd-input-group"
        ":has(label:text-is('Confirm Password'))"
        " input"
    )

    # =========================
    # Buttons
    # =========================

    SAVE_BUTTON = "button:has-text('Save')"

    CANCEL_BUTTON = "button:has-text('Cancel')"

    # =========================
    # Page validation
    # =========================

    def page_loaded(self):
        return self.get_text(self.TITLE) == "Admin"

    # =========================
    # Add User
    # =========================

    def click_add_user(self):
        self.click(self.ADD_USER_BUTTON)

    # =========================
    # Dropdown actions
    # =========================

    def select_user_role(self, role):
        self.click(self.USER_ROLE_DROPDOWN)
        self.page.get_by_role("option", name=role).click()

    def select_status(self, status):
        self.click(self.STATUS_DROPDOWN)
        self.page.get_by_role("option", name=status).click()

    # =========================
    # Input actions
    # =========================

    def enter_employee_name(self, employee_name):
        self.fill(self.EMPLOYEE_NAME, employee_name)

    def enter_username(self, username):
        self.fill(self.USERNAME, username)

    def enter_password(self, password):
        self.fill(self.PASSWORD, password)

    def enter_confirm_password(self, password):
        self.fill(self.CONFIRM_PASSWORD, password)

    # =========================
    # Button actions
    # =========================

    def click_save(self):
        self.click(self.SAVE_BUTTON)

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)