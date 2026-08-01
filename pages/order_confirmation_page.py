from playwright.sync_api import Page

class OrderConfirmationPage:

    def __init__(self, page: Page):
        self.page = page

        self.success_message = page.locator(
            '[data-test="complete-header"]'
        )

    def verify_order_success(self):
        return (
            self.success_message.text_content()
            == "Thank you for your order!"
        )