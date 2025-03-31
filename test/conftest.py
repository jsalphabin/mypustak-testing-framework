import pytest
from selenium import webdriver
from helpers.login_helper import LoginHelper
from helpers.search_helper import SearchHelper
from helpers.cart_helper import CartHelper
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

@pytest.fixture
def perform_search():
    def _search(driver):
        return SearchHelper.perform_search(driver)
    return _search

@pytest.fixture
def add_to_cart():
    def _cart(driver):
        return CartHelper.add_to_cart(driver)
    return _cart

@pytest.fixture
def verify_cart():
    def _cart(driver):
        return CartHelper.verify_cart(driver)
    return _cart

@pytest.fixture
def click_on_cart():
    def _cart(driver):
        return CartHelper.click_on_cart(driver)
    return _cart

@pytest.fixture
def click_on_add_button():
    def _cart(driver):
        return CartHelper.click_on_add_button
    return _cart

@pytest.fixture
def check_if_zero():
    def _cart(driver):
        return CartHelper.check_if_zero(driver)
    return _cart
