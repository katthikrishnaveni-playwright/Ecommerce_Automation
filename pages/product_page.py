from playwright.sync_api import Page


class ProductPage:


    def __init__(self, page: Page):
        self.page = page



        self.backpack_product = page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        )


        self.add_to_cart_button = page.locator(
            "#add-to-cart"
        )


        self.back_to_products_button = page.locator(
            "#back-to-products"
        )

    def select_backpack(self):
        self.backpack_product.click()

    def click_add_to_cart(self):
        self.add_to_cart_button.click()

    def back_to_products(self):
        self.back_to_products_button.click()

