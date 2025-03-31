from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import LocateByXpath
import time


class CartHelper:
  @staticmethod  
  def add_to_cart(driver):
    add_to_cart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.ADD_TO_CART_XPATH)))
    add_to_cart.click()
    time.sleep(2)
    add_to_cart_final = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.ADD_TO_CART_FINAL_XPATH)))
    add_to_cart_final.click()
  
  @staticmethod
  def verify_cart(driver):
    added_to_cart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.BOOK_ADDED_TO_CART_XPATH))).text
    assert "Book added to cart!" in added_to_cart,"Book not added to cart"
  
  @staticmethod
  def click_on_cart(driver):
    cart=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.CART_ICON)))
    cart.click()

  @staticmethod
  def click_on_add_button(driver):
    qunatity_before=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.QUANTITY))).text
    time.sleep(2)
    add_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.ADD_BUTTON)))
    add_button.click()
    time.sleep(2)
    qunatity_after=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.QUANTITY))).text
    assert int(qunatity_after)==int(qunatity_before)+1

  @staticmethod
  def check_if_zero(driver):
    zero=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.ZERO_XPATH)))
    assert zero.text=='My Cart (0)'