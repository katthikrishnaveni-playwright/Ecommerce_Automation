import os
import pytest
from playwright.sync_api import Playwright


# Existing fixture (already unna code)
@pytest.fixture
def open_application(page):
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()


# Screenshot on Failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("open_application")

        if page:

            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = (
                f"reports/screenshots/{item.name}.png"
            )

            page.screenshot(path=screenshot_path)