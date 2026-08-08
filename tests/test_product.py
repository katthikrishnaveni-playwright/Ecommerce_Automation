import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utilities.logger import LogGenerator


@pytest.mark.smoke
@pytest.mark.regression
def test_select_product(open_application):

    logger = LogGenerator.loggen()

    logger.info("********** Product Test Start **********")

    login_page = LoginPage(open_application)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("Login Successful")

    product_page = ProductPage(open_application)

    product_page.select_backpack()

    logger.info("Backpack Selected")

    product_page.click_add_to_cart()

    logger.info("Product Added To Cart")

    product_page.back_to_products()

    logger.info("Returned To Product Page")

    assert open_application.url == (
        "https://www.saucedemo.com/inventory.html"
    )

    logger.info("Product Test Passed")
