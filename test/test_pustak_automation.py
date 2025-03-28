import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BAR_XPATH = '//input[@id="gsearch"]'  # Adjust this if needed
SEARCH_BUTTON_XPATH = '//button[@id="searchId"]'  # Adjust this if needed
RESULT_TITLES_XPATH = '//*[contains(@class, "search-page")]/div/div/div/div/div/div[1]'  # Modify based on actual site structure
ERROR_MESSAGE_XPATH='//*[contains(@class, "title-error")]'

# Constants
LOGIN_URL = "https://www.mypustak.com/"
CORRECT_EMAIL = "jainam@gmail.com"
INCORRECT_EMAIL = "jainam@gmail..com"
CORRECT_PASSWORD = "jainam@jainam"
INCORRECT_PASSWORD = "xyzabcd"

# Element Selectors
LOGIN_BUTTON_ID = "loginBtn"
POPUP_LOGIN_CLASS = "WLoginNavbar_loginButton__M7mhW"
EMAIL_INPUT_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/div/input'
PASSWORD_INPUT_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[2]/div/input'
SNACKBAR_ID = "notistack-snackbar"
EMAIL_ERROR_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/p'


@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
  """Fixture to set up and tear down WebDriver."""
  global driver
  driver = webdriver.Chrome()
  driver.get(LOGIN_URL)
  driver.maximize_window()
  yield
  driver.quit()


def perform_login(email, password):
   
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, LOGIN_BUTTON_ID))).click()
  if email:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, EMAIL_INPUT_XPATH)))
    email_input.clear()
    email_input.send_keys(email)

  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, POPUP_LOGIN_CLASS))).click()

  if password:
      password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, PASSWORD_INPUT_XPATH)))
      password_input.clear()
      password_input.send_keys(password)

      WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, POPUP_LOGIN_CLASS))).click()

def perform_search():
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON_XPATH)))

  
  search_bar.clear()
  search_bar.send_keys("Computer")

  search_button.click()
   
def login_and_search():
  perform_login(CORRECT_EMAIL,CORRECT_PASSWORD)
  time.sleep(2)
  perform_search()

#def add_single_product_to_cart():
   

def test_login_valid():
  """Test login with valid credentials"""
  perform_login(CORRECT_EMAIL, CORRECT_PASSWORD)

  login_text = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//button[@id="loginBtn"]/span'))
  ).text
  assert login_text == 'Hi! Reader', "Login was unsuccessful!"

def test_login_invalid_password():
  """Test login with incorrect password"""
  perform_login(CORRECT_EMAIL, INCORRECT_PASSWORD)

  error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, SNACKBAR_ID))).text
  assert "Entered email or password is incorrect" in error_message, "Incorrect password error not displayed!"

def test_login_empty_email():
  """Test login with empty email"""
  try:
    perform_login(None, None)  # No password needed if email is empty
  except:
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, EMAIL_ERROR_XPATH))).text
    assert "Enter valid email" in error_message, "Empty email error not displayed!"

def test_login_incorrect_email():
  """Test login with invalid email"""
  try:
    perform_login(INCORRECT_EMAIL, None)  # No password needed if email is invalid
  except:
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, EMAIL_ERROR_XPATH))).text
    assert "Enter valid email" in error_message, "Invalid email error not displayed!"

@pytest.mark.parametrize("search_query, expected_result", [
    ("Computer", "Computer"),  # Test Search 1: Searching for "Computer"
    ("", ""),  # Test Search 2: Clicking search without input
])

def test_search_functionality(search_query, expected_result):
  """Generic test function for different search cases"""
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON_XPATH)))

  # Enter search query (if provided)
  search_bar.clear()
  search_bar.send_keys(search_query)

  # Click search button
  search_button.click()

  # Wait for results to load
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, RESULT_TITLES_XPATH)))

  # Fetch all displayed book titles
  book_titles = driver.find_elements(By.XPATH, RESULT_TITLES_XPATH)
  
  # Validate results based on the search case
  if search_query == "Computer":
      assert any(expected_result in title.text for title in book_titles), "Relevant books not found!"
  elif search_query == "":
      assert len(book_titles) > 0, "No books found when searching without input!"
  else:
      assert len(book_titles) > 0, "Unfortunately the page you are looking for has been moved or deleted"

  print(f"Search test passed for query: {search_query}")


@pytest.mark.parametrize("search_query, expected_behavior", [
    ("#", "Unfortunately the page you are looking for has been moved or deleted"),  # Test Search 3: Special characters
    ("!@#$%^&*()_+", "Unfortunately the page you are looking for has been moved or deleted")  # Test Search 4: All special characters
])
def test_special_character_search( search_query, expected_behavior):
  """Test search functionality with special characters"""
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SEARCH_BUTTON_XPATH)))

  search_bar.clear()
  search_bar.send_keys(search_query)
  search_button.click()

  try:
      # Check for error message
      error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, ERROR_MESSAGE_XPATH)))
      assert error_message.text, f"Error displayed: {error_message.text}"
      print(f"✅ Search '{search_query}' caused an expected error: {error_message.text}")
  except:
      # If no error message appears, check if results are displayed
      book_titles = driver.find_elements(By.XPATH, RESULT_TITLES_XPATH)
      if book_titles:
          print(f"✅ Search '{search_query}' returned some results.")
      else:
          print(f"❌ No books found for search '{search_query}', and no error message shown.")
          driver.save_screenshot(f"screenshot_{search_query}.png")
      assert len(book_titles) > 0, f"No books found for special character search: {search_query}"

def test_add_to_cart():
  login_and_search()
  add_single_product_to_cart()
