import pytest
from pages.login_page import LoginPage
from utilities.logger import LogGenerator


@pytest.mark.smoke
def test_login(open_application):

    logger = LogGenerator.loggen()

    logger.info("********** Login Test Start **********")

    login_page = LoginPage(open_application)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    logger.info("Login Successful")

    assert open_application.url == (
        "https://www.saucedemo.com/inventory.html"
    )

    logger.info("Login Test Passed")






