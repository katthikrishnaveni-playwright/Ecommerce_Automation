from playwright.sync_api import Page




class CartPage:

    def __init__(self, page: Page):
        self.page = page

        # Cart icon
        self.cart_button = page.locator(
            "a.shopping_cart_link"
        )


        self.backpack_product = page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        )



        # Checkout button
        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )


    def click_cart(self):
        self.cart_button.click()

    def verify_backpack_in_cart(self):
        return self.backpack_product.is_visible()

    def click_checkout(self):
        self.checkout_button.click()