from pages.base_page import BasePage

class HeaderComponent(BasePage):

    PROFILE = ".oxd-userdropdown-tab"
    PROFILE_IMAGE = ".oxd-userdropdown-img"
    USERNAME = ".oxd-userdropdown-name"

    UPGRADE_BUTTON = ".orangehrm-upgrade-button"
    HELP_BUTTON = "button[title='Help']"

    def profile_visible(self):
        return self.is_visible(self.PROFILE_IMAGE)

    def get_username(self):
        return self.get_text(self.USERNAME)

    def upgrade_button_visible(self):
        return self.is_visible(self.UPGRADE_BUTTON)

    def help_button_visible(self):
        return self.is_visible(self.HELP_BUTTON)

    def open_profile_menu(self):
        self.click(self.PROFILE)

    def click_help(self):
        self.click(self.HELP_BUTTON)

    def click_upgrade(self):
        self.click(self.UPGRADE_BUTTON)