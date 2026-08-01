from playwright.sync_api import Page


class LogoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

    def click_logout(self):
        self.menu_button.click()
        self.logout_button.click()
