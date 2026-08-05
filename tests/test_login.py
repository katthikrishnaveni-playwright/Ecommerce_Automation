import pytest
from pages.login_page import LoginPage
from utilities.logger import LogGenerator
from utilities.excel_reader import ExcelReader


test_data = ExcelReader.get_data(
    "testdata/LoginData.xlsx",
    "Sheet1"
)


@pytest.mark.smoke
@pytest.mark.parametrize("username,password", test_data)
def test_login(open_application, username, password):

    logger = LogGenerator.loggen()

    logger.info("********** Login Test Start **********")

    login_page = LoginPage(open_application)

    login_page.login(username, password)

    logger.info(f"Login Attempt with {username}")

    if username == "locked_out_user":

        expected_error = "Epic sadface: Sorry, this user has been locked out."

        actual_error = login_page.get_error_message()

        assert actual_error == expected_error
        logger.info("Locked User Validation Passed")

    else:

        assert open_application.url == "https://www.saucedemo.com/inventory.html"

        logger.info("Login Successful")




