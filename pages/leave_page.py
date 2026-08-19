from pages.base_page import BasePage


class LeavePage(BasePage):

    TITLE = "h6"

    def page_loaded(self):
        return self.get_text(self.TITLE) == "Leave"
