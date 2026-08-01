from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page




        # Customer details
        self.first_name = page.locator(
            "#first-name"
        )

        self.last_name = page.locator(
            "#last-name"
        )

        self.postal_code = page.locator(
            "#postal-code"
        )

        # Continue button
        self.continue_button = page.get_by_role(
            "button",
            name="Continue"
        )


        # finish button
        self.finish_button = page.get_by_role(
            "button",
            name="finish"
        )


    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def click_finish(self):
        self.finish_button.click()


    def verify_order_success(self):
        return self.page.get_by_text(
            "Thank you for your order!"
        )






