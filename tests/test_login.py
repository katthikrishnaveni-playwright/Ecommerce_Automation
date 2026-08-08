import pytest
import allure
from pages.login_page import LoginPage
from utilities.logger import LogGenerator
from utilities.excel_reader import ExcelReader


test_data = ExcelReader.get_data(
    "testdata/LoginData.xlsx",
    "Sheet1"
)


@allure.epic("Ecommerce Automation")
@allure.feature("Login Module")
@allure.story("Valid and Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify login functionality using multiple users from Excel")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username,password", test_data)
def test_login(open_application, username, password):

    logger = LogGenerator.loggen()

    with allure.step("Start Login Test"):
        logger.info("********** Login Test Start **********")

    login_page = LoginPage(open_application)

    with allure.step(f"Login with Username: {username}"):
        login_page.login(username, password)

    logger.info(f"Login Attempt with {username}")

    if username == "locked_out_user":

        with allure.step("Verify Locked User Error Message"):

            expected_error = "Epic sadface: Sorry, this user has been locked out."

            actual_error = login_page.get_error_message()

            assert actual_error == expected_error

            logger.info("Locked User Validation Passed")

    else:

        with allure.step("Verify Successful Login"):
            assert open_application.url == "https://www.saucedemo.com/inventory.html"
            logger.info("Login Successful")

    logger.info("********** Login Test Completed **********")