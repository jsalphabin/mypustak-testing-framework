from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import LocateByClass, LocateById, LocateByXpath

class LoginHelper:
  @staticmethod
  def perform_login(driver,email, password):
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, LocateById.LOGIN_BUTTON_ID))).click()
    if email:
      email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.EMAIL_INPUT_XPATH)))
      email_input.clear()
      email_input.send_keys(email)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, LocateByClass.POPUP_LOGIN_CLASS))).click()

    if password:
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.PASSWORD_INPUT_XPATH)))
        password_input.clear()
        password_input.send_keys(password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, LocateByClass.POPUP_LOGIN_CLASS))).click()
