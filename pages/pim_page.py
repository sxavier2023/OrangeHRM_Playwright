from pages.base_page import BasePage


class PimPage(BasePage):

    TITLE = ".oxd-topbar-header-breadcrumb-module"

    EMPLOYEE_LIST_TAB = (
        "a.oxd-topbar-body-nav-tab-item:text-is('Employee List')"
    )
    ADD_EMPLOYEE_TAB = (
        "a.oxd-topbar-body-nav-tab-item:text-is('Add Employee')"
    )
    REPORTS_TAB = "a.oxd-topbar-body-nav-tab-item:text-is('Reports')"

    ADD_EMPLOYEE_FORM = ".orangehrm-employee-form"
    EMPLOYEE_TABLE = ".oxd-table-body .oxd-table-card"

    def page_loaded(self):
        return self.get_text(self.TITLE) == "PIM"

    def click_employee_list(self):
        self.click(self.EMPLOYEE_LIST_TAB, no_wait_after=True)

    def click_add_employee(self):
        self.click(self.ADD_EMPLOYEE_TAB, no_wait_after=True)

    def click_reports(self):
        self.click(self.REPORTS_TAB, no_wait_after=True)

    def wait_for_employee_list(self, timeout=15000):
        self.page.wait_for_selector(self.EMPLOYEE_TABLE, timeout=timeout)

    def on_employee_list(self):
        return (
            self.page.url.split("/")[-2:] == ["pim", "viewEmployeeList"]
            and self.page.locator(self.EMPLOYEE_TABLE).count() > 0
        )

    def on_add_employee(self):
        return (
            self.page.url.split("/")[-2:] == ["pim", "addEmployee"]
            and self.is_visible(self.ADD_EMPLOYEE_FORM)
        )

    def on_reports(self):
        return (
            self.page.url.split("/")[-2:]
            == ["pim", "viewDefinedPredefinedReports"]
            and self.page.locator(self.EMPLOYEE_TABLE).count() > 0
        )

    def employee_row_count(self):
        return self.page.locator(self.EMPLOYEE_TABLE).count()