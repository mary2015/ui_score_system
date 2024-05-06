import time

import pytest
from selenium.webdriver.common.by import By

from constants import Constants
from pages.login_page import LoginPage


@pytest.mark.usefixtures("driver")
class TestLoginPage:

    def test_login(self, driver):
        page = LoginPage()
        page.login(driver, Constants.USER_NAME, Constants.PASSWORD)
        id, displayName, username = page.home_page(driver)
        assert id == "00ugstdr23VVGx0So5d7"
        assert displayName == "rongyao ma"
        assert username == "rongyaoma2020@gmail.com"
        page.sign_out(driver)
