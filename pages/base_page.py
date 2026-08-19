import os

from config import SCREENSHOT_DIR


class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, selector, no_wait_after=False):
        self.page.locator(selector).click(no_wait_after=no_wait_after)

    def fill(self, selector, text):
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        return self.page.locator(selector).text_content()

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def open(self, url):
        self.page.goto(url)

    def scroll_to_text(self, text):
        self.page.locator(f"text={text}").scroll_into_view_if_needed()

    def scroll_to(self, selector):
        self.page.locator(selector).scroll_into_view_if_needed()

    def wait(self, seconds):
        self.page.wait_for_timeout(seconds * 1000)

    def take_screenshot(self, name):
        path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.page.screenshot(path=path)
        return path