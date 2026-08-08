import os
import pytest
import allure
from playwright.sync_api import sync_playwright


# -----------------------------
# Playwright Fixture
# -----------------------------
@pytest.fixture
def open_application():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        yield page

        browser.close()


# -----------------------------
# Allure Screenshot Hook
# -----------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    if report.when == "call" and report.failed:

        page = item.funcargs.get("open_application")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            try:
                page.screenshot(path=screenshot_path)

                allure.attach.file(
                    screenshot_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

            except Exception as e:
                print(f"Screenshot failed: {e}")