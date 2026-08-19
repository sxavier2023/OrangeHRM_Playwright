from pages.base_page import BasePage


class BuzzPage(BasePage):

    TITLE = ".oxd-topbar-header-breadcrumb-module"

    POST_INPUT = "textarea.oxd-buzz-post-input"
    POST_BUTTON = ".orangehrm-buzz-create-post button[type='submit']"

    SHARE_PHOTOS_BUTTON = "button.oxd-glass-button:has-text('Share Photos')"
    SHARE_VIDEO_BUTTON = "button.oxd-glass-button:has-text('Share Video')"

    MODAL = ".orangehrm-dialog-modal"
    PHOTO_INPUT = MODAL + " input[type='file']"
    VIDEO_URL_INPUT = (
        MODAL
        + " div.oxd-input-group:has(label:has-text('Video URL')) textarea"
    )
    MODAL_POST_BUTTON = MODAL + " button[type='submit']"

    def page_loaded(self):
        return self.get_text(self.TITLE) == "Buzz"

    def type_status(self, text):
        self.fill(self.POST_INPUT, text)

    def click_post(self):
        self.click(self.POST_BUTTON)

    def click_share_photos(self):
        self.click(self.SHARE_PHOTOS_BUTTON)

    def click_share_video(self):
        self.click(self.SHARE_VIDEO_BUTTON)

    def modal_visible(self):
        return self.is_visible(self.MODAL)

    def upload_photo(self, file_path):
        self.page.locator(self.PHOTO_INPUT).set_input_files(file_path)

    def enter_video_url(self, url):
        self.fill(self.VIDEO_URL_INPUT, url)

    def click_modal_post(self):
        self.click(self.MODAL_POST_BUTTON)

    def post_count(self):
        return self.page.locator(
            ".orangehrm-buzz-newsfeed .orangehrm-buzz-post"
        ).count()

    def wait_for_post(self, text, timeout=15000):
        self.page.wait_for_selector(
            f".orangehrm-buzz-newsfeed .orangehrm-buzz-post:has-text('{text}')",
            timeout=timeout,
        )
        return True

    def wait_for_modal_closed(self, timeout=15000):
        self.page.wait_for_selector(
            self.MODAL, state="detached", timeout=timeout
        )
        return True