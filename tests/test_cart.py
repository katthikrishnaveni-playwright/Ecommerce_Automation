import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.logger import LogGenerator

@pytest.mark.smoke
@pytest.mark.regression
def test_cart(open_application):

    logger = LogGenerator.loggen()

    logger.info("********** Cart Test Start **********")

    login_page = LoginPage(open_application)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("Login Successful")

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

    logger.info("Cart Test Passed")