import os
import time

import pytest
from playwright._impl._errors import TimeoutError as PlaywrightTimeout

from pages.login_page import LoginPage
from pages.side_bar_hamburger_page import SidebarComponent
from pages.buzz_page import BuzzPage
from data.login_data import VALID_LOGIN

POST_TEXT = "Hello from Playwright"
VIDEO_URL = "https://www.youtube.com/watch?v=tgbNymZ7vqY"
PIC_PATH = os.path.join(
    os.path.dirname(__file__), "..", "utils", "test_pic.png"
)

POST_API = "/api/v2/buzz/posts"
MODAL_RETRIES = 4


def _open_buzz(page):
    login = LoginPage(page)
    navigation = SidebarComponent(page)
    buzz = BuzzPage(page)

    login.open()
    login.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    navigation.open_menu(navigation.BUZZ)
    assert buzz.page_loaded()
    return buzz


def _unique_text(prefix):
    return f"{prefix} {int(time.time() * 1000)}"


def _assert_post_created(page, click_action, timeout=20000):
    with page.expect_response(
        lambda r: r.request.method == "POST" and POST_API in r.url,
        timeout=timeout,
    ) as info:
        click_action()
    assert info.value.status < 400


def _post_with_media(page, buzz, open_modal, fill_body):
    for attempt in range(MODAL_RETRIES):
        open_modal()
        if not buzz.modal_visible():
            buzz.wait(1)
            continue
        try:
            fill_body()
            _assert_post_created(page, buzz.click_modal_post, timeout=15000)
            assert buzz.wait_for_modal_closed(timeout=10000)
            return
        except PlaywrightTimeout:
            buzz.wait(1)
    pytest.fail(
        "Could not complete the post: the demo's share modal kept closing "
        "before submit. This is an environment issue, not a locator problem."
    )


def test_post_only_text(page):
    buzz = _open_buzz(page)
    text = _unique_text(POST_TEXT)

    buzz.type_status(text)

    _assert_post_created(page, buzz.click_post)
    buzz.wait(2)
    buzz.take_screenshot("buzz_post_only_text")


def test_post_text_with_pic(page):
    buzz = _open_buzz(page)
    text = _unique_text(POST_TEXT)

    buzz.type_status(text)

    _post_with_media(
        page,
        buzz,
        open_modal=buzz.click_share_photos,
        fill_body=lambda: buzz.upload_photo(PIC_PATH),
    )
    buzz.wait(2)
    buzz.take_screenshot("buzz_post_text_with_pic")


def test_post_text_with_video(page):
    buzz = _open_buzz(page)
    text = _unique_text(POST_TEXT)

    buzz.type_status(text)

    def fill_video():
        buzz.enter_video_url(VIDEO_URL)
        buzz.wait(3)

    _post_with_media(
        page,
        buzz,
        open_modal=buzz.click_share_video,
        fill_body=fill_video,
    )
    buzz.wait(2)
    buzz.take_screenshot("buzz_post_text_with_video")


def test_post_only_pic(page):
    buzz = _open_buzz(page)
    buzz.wait(2)

    _post_with_media(
        page,
        buzz,
        open_modal=buzz.click_share_photos,
        fill_body=lambda: buzz.upload_photo(PIC_PATH),
    )
    buzz.wait(2)
    buzz.take_screenshot("buzz_post_only_pic")


def test_post_only_video(page):
    buzz = _open_buzz(page)
    buzz.wait(2)

    def fill_video():
        buzz.enter_video_url(VIDEO_URL)
        buzz.wait(3)

    _post_with_media(
        page,
        buzz,
        open_modal=buzz.click_share_video,
        fill_body=fill_video,
    )
    buzz.wait(2)
    buzz.take_screenshot("buzz_post_only_video")


def test_post_empty_negative(page):
    requests = []
    page.on("request", lambda req: requests.append(req))

    buzz = _open_buzz(page)
    buzz.wait(2)
    before = buzz.post_count()

    buzz.click_post()

    buzz.wait(3)
    assert buzz.post_count() == before
    assert not any(
        req.method == "POST" and POST_API in req.url
        for req in requests
    )
    buzz.take_screenshot("buzz_post_empty_negative")