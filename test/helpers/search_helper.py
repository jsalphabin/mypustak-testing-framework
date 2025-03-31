from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import LocateByXpath

class SearchHelper:
  @staticmethod
  def perform_search(driver):
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, LocateByXpath.SEARCH_BAR_XPATH)))
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

    
    search_bar.clear()
    search_bar.send_keys("Computer")

    search_button.click()
