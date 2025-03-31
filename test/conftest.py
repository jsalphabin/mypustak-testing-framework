import pytest
from selenium import webdriver

from locators import Urls

@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
    """Fixture to set up and tear down WebDriver."""
    driver = webdriver.Chrome()
    driver.get(Urls.LOGIN_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
