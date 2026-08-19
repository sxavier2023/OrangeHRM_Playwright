import os
import time

import pytest
from playwright.sync_api import sync_playwright

from config import SCREENSHOT_DIR


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs["page"]
        except Exception:
            return
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        path = os.path.join(SCREENSHOT_DIR, f"{timestamp}_{item.name}.png")
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        page.screenshot(path=path)
        try:
            import pytest_html

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(path))
            report.extra = extra
        except Exception:
            pass