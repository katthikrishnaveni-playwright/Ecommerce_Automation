import os
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.logout_page import LogoutPage
from utilities.logger import LogGenerator


@pytest.mark.regression
def test_checkout(open_application):

    logger = LogGenerator.loggen()

    logger.info("********** Checkout Test Start **********")

    login_page = LoginPage(open_application)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    product_page = ProductPage(open_application)

    product_page.select_backpack()

    product_page.click_add_to_cart()

    product_page.back_to_products()

    cart_page = CartPage(open_application)

    cart_page.click_cart()

    assert open_application.url == (
        "https://www.saucedemo.com/cart.html"
    )

    assert cart_page.verify_backpack_in_cart()

    cart_page.click_checkout()

    checkout_page = CheckoutPage(open_application)

    checkout_page.enter_customer_details(
        "krishnaveni",
        "Test",
        "500090"
    )

    checkout_page.click_continue()

    assert open_application.url == (
        "https://www.saucedemo.com/checkout-step-two.html"
    )

    checkout_page.click_finish()

    order_confirmation_page = OrderConfirmationPage(open_application)

    assert order_confirmation_page.verify_order_success()

    logout_page = LogoutPage(open_application)

    logout_page.logout()

    assert open_application.url == (
        "https://www.saucedemo.com/"
    )

    logger.info("Checkout Test Passed")



