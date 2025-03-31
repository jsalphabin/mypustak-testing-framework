import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Urls, DummyData, LocateById,LocateByClass,LocateByXpath

@pytest.fixture(scope='function',autouse=True)
def setup_teardown():
    """Fixture to set up and tear down WebDriver."""
    global driver
    driver = webdriver.Chrome()
    driver.get(Urls.LOGIN_URL)
    driver.maximize_window()
    yield
    driver.quit()

def perform_login(email, password):
   
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

def add_to_cart():
   add_to_cart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.ADD_TO_CART_XPATH)))
   add_to_cart.click()
   time.sleep(2)
   add_to_cart_final = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.ADD_TO_CART_FINAL_XPATH)))
   add_to_cart_final.click()

def perform_search():
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

  
  search_bar.clear()
  search_bar.send_keys("Computer")

  search_button.click()
   
def login_and_search():
  perform_login(DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
  time.sleep(2)
  perform_search()


def verify_cart():
   added_to_cart=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.BOOK_ADDED_TO_CART_XPATH))).text
   assert "Book added to cart!" in added_to_cart,"Book not added to cart"

def click_on_cart():
   cart=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.CART_ICON)))
   cart.click()

def click_on_add_button():
   qunatity_before=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.QUANTITY))).text
   time.sleep(2)
   add_button=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.ADD_BUTTON)))
   add_button.click()
   time.sleep(2)
   qunatity_after=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.QUANTITY))).text
   assert int(qunatity_after)==int(qunatity_before)+1

def check_if_zero():
   zero=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,LocateByXpath.ZERO_XPATH)))
   assert zero.text=='My Cart (0)'

def test_login_valid():
  """Test login with valid credentials"""
  perform_login(DummyData.CORRECT_EMAIL, DummyData.CORRECT_PASSWORD)

  login_text = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, LocateByXpath.LOGIN_BTN))
  ).text
  assert login_text == 'Hi! Reader', "Login was unsuccessful!"

def test_login_invalid_password():
  """Test login with incorrect password"""
  perform_login(DummyData.CORRECT_EMAIL, DummyData.INCORRECT_PASSWORD)

  error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, LocateById.SNACKBAR_ID))).text
  assert "Entered email or password is incorrect" in error_message, "Incorrect password error not displayed!"

def test_login_empty_email():
    """Test login with empty email"""
    try:
        perform_login(None, None)  # No password needed if email is empty
    except:
        error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.EMAIL_ERROR_XPATH))).text
        assert "Enter valid email" in error_message, "Empty email error not displayed!"

def test_login_incorrect_email():
  """Test login with invalid email"""
  try:
    perform_login(DummyData.INCORRECT_EMAIL, None)  # No password needed if email is invalid
  except:
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.EMAIL_ERROR_XPATH))).text
    assert "Enter valid email" in error_message, "Invalid email error not displayed!"

@pytest.mark.parametrize("search_query, expected_result", [
    ("Computer", "Computer"),  # Test Search 1: Searching for "Computer"
    ("", ""),  # Test Search 2: Clicking search without input
    ("TABLET and AnDroid","tablet and android")
])

def test_search_functionality(search_query, expected_result):
  """Generic test function for different search cases"""
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

  # Enter search query (if provided)
  search_bar.clear()
  search_bar.send_keys(search_query)

  # Click search button
  search_button.click()

  # Wait for results to load
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)))

  # Fetch all displayed book titles
  book_titles = driver.find_elements(By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)
  
  # Validate results based on the search case
  if search_query == "Computer":
      assert any(expected_result in title.text for title in book_titles), "Relevant books not found!"
  elif search_query == "":
      assert len(book_titles) > 0, "No books found when searching without input!"
  elif search_query=="Tablet" or search_query=="Android":
     assert any(expected_result in title.text for title in book_titles), "Relevant books not found!"
  else:
      assert len(book_titles) > 0, "Unfortunately the page you are looking for has been moved or deleted"

  print(f"Search test passed for query: {search_query}")


@pytest.mark.parametrize("search_query, expected_behavior", [
    ("#", "#"),  # Test Search 3: Special characters
    ("!@#$%^&*()_+", "Unfortunately the page you are looking for has been moved or deleted")  # Test Search 4: All special characters
])
def test_special_character_search( search_query, expected_behavior):
  """Test search functionality with special characters"""
  search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

  search_bar.clear()
  search_bar.send_keys(search_query)
  search_button.click()

  try:
      # Check for error message
      error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.ERROR_MESSAGE_XPATH)))
      assert error_message.text, f"Error displayed: {error_message.text}"
      print(f"✅ Search '{search_query}' caused an expected error: {error_message.text}")
  except:
      # If no error message appears, check if results are displayed
      book_titles = driver.find_elements(By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)
      if book_titles:
          print(f"✅ Search '{search_query}' returned some results.")
      else:
          print(f"❌ No books found for search '{search_query}', and no error message shown.")
          driver.save_screenshot(f"screenshot_{search_query}.png")
      assert len(book_titles) > 0, f"No books found for special character search: {search_query}"



def test_cart_1():
   perform_login(DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(5)
   click_on_cart()
   check_if_zero()

def test_cart_2():
   perform_login(DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   perform_search()
   time.sleep(2)
   add_to_cart()
#    time.sleep(1)
   verify_cart()

def test_cart_3():
   perform_login(DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   perform_search()
   time.sleep(2)
   add_to_cart()
   time.sleep(1)
   verify_cart()
   click_on_cart()
   click_on_add_button()
# def test_add_to_cart():
#   login_and_search()
#   add_single_product_to_cart()

def test_cart_4():
   perform_login(DummyData.CORRECT_EMAIL,DummyData.CORRECT_PASSWORD)
   time.sleep(2)
   click_on_cart()
