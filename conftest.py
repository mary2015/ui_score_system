import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from constants import Constants


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(Constants.BASE_URL)
    driver.implicitly_wait(3)
    return driver
