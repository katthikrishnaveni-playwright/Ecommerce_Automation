from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        self.page = page

        # Locators
        self.username_textbox = page.locator("#user-name")
        self.password_textbox = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def enter_username(self, username):

        self.username_textbox.fill(username)

    def enter_password(self, password):

        self.password_textbox.fill(password)

    def click_login(self):

        self.login_button.click()

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()