import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Urls, DummyData, LocateById,LocateByXpath


def test_cart_1(setup_teardown,perform_login,click_on_cart,check_if_zero):
   perform_login(setup_teardown,DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(5)
   click_on_cart()
   check_if_zero()

def test_cart_2(setup_teardown,perform_login,perform_search,add_to_cart,verify_cart):
   perform_login(setup_teardown,DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   perform_search()
   time.sleep(2)
   add_to_cart()
#    time.sleep(1)
   verify_cart()

def test_cart_3(setup_teardown,perform_login,perform_search,add_to_cart,verify_cart,click_on_cart,click_on_add_button):
   perform_login(setup_teardown,DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   perform_search()
   time.sleep(2)
   add_to_cart()
   time.sleep(1)
   verify_cart()
   click_on_cart()
   click_on_add_button()

def test_cart_4(setup_teardown,perform_login,click_on_cart):
   perform_login(setup_teardown,DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   click_on_cart()
