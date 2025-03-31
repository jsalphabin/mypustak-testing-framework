from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import DummyData, LocateById,LocateByXpath

def test_login_valid(setup_teardown,perform_login):
  """Test login with valid credentials"""
  perform_login(setup_teardown,DummyData.CORRECT_EMAIL, DummyData.CORRECT_PASSWORD)

  login_text = WebDriverWait(setup_teardown, 10).until(
      EC.visibility_of_element_located((By.XPATH, LocateByXpath.LOGIN_BTN))
  ).text
  assert login_text == 'Hi! Reader', "Login was unsuccessful!"

def test_login_invalid_password(setup_teardown,perform_login):
  """Test login with incorrect password"""
  perform_login(setup_teardown,DummyData.CORRECT_EMAIL, DummyData.INCORRECT_PASSWORD)

  error_message = WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.ID, LocateById.SNACKBAR_ID))).text
  assert "Entered email or password is incorrect" in error_message, "Incorrect password error not displayed!"

def test_login_empty_email(setup_teardown,perform_login):
    """Test login with empty email"""
    try:
        perform_login(setup_teardown,None, None)  # No password needed if email is empty
    except:
        error_message = WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.EMAIL_ERROR_XPATH))).text
        assert "Enter valid email" in error_message, "Empty email error not displayed!"

def test_login_incorrect_email(setup_teardown,perform_login):
  """Test login with invalid email"""
  try:
    perform_login(setup_teardown,DummyData.INCORRECT_EMAIL, None)  # No password needed if email is invalid
  except:
    error_message = WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.EMAIL_ERROR_XPATH))).text
    assert "Enter valid email" in error_message, "Invalid email error not displayed!"
