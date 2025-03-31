import pytest
from selenium import webdriver
from Helpers.LoginHelper import LoginHelper
from locators import Urls

@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
    """Fixture to set up and tear down WebDriver."""
    driver = webdriver.Chrome()
    driver.get(Urls.LOGIN_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def perform_login():
    def _login(driver, email, password):
        return LoginHelper.perform_login(driver, email, password)
    return _login  
