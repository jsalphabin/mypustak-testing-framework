import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Urls, DummyData, LocateById,LocateByXpath


@pytest.mark.parametrize("search_query, expected_result", [
    ("Computer", "Computer"),  # Test Search 1: Searching for "Computer"
    ("", ""),  # Test Search 2: Clicking search without input
    ("TABLET and AnDroid","tablet and android")
])

def test_search_functionality(setup_teardown,search_query, expected_result):
  """Generic test function for different search cases"""
  search_bar = WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(setup_teardown, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

  # Enter search query (if provided)
  search_bar.clear()
  search_bar.send_keys(search_query)

  # Click search button
  search_button.click()

  # Wait for results to load
  WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)))

  # Fetch all displayed book titles
  book_titles = setup_teardown.find_elements(By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)
  
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
def test_special_character_search(setup_teardown ,search_query, expected_behavior):
  """Test search functionality with special characters"""
  search_bar = WebDriverWait(setup_teardown, 10).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.SEARCH_BAR_XPATH)))
  search_button = WebDriverWait(setup_teardown, 10).until(EC.element_to_be_clickable((By.XPATH, LocateByXpath.SEARCH_BUTTON_XPATH)))

  search_bar.clear()
  search_bar.send_keys(search_query)
  search_button.click()

  try:
      # Check for error message
      error_message = WebDriverWait(setup_teardown, 5).until(EC.presence_of_element_located((By.XPATH, LocateByXpath.ERROR_MESSAGE_XPATH)))
      assert error_message.text, f"Error displayed: {error_message.text}"
      print(f"✅ Search '{search_query}' caused an expected error: {error_message.text}")
  except:
      # If no error message appears, check if results are displayed
      book_titles = setup_teardown.find_elements(By.XPATH, LocateByXpath.RESULT_TITLES_XPATH)
      if book_titles:
          print(f"✅ Search '{search_query}' returned some results.")
      else:
          print(f"❌ No books found for search '{search_query}', and no error message shown.")
          setup_teardown.save_screenshot(f"screenshot_{search_query}.png")
      assert len(book_titles) > 0, f"No books found for special character search: {search_query}"

