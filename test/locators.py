class Urls:
  LOGIN_URL = "https://www.mypustak.com/"

class DummyData:
  CORRECT_EMAIL = "jainam@gmail.com"
  INCORRECT_EMAIL = "jainam@gmail..com"
  CORRECT_PASSWORD = "jainam@jainam"
  INCORRECT_PASSWORD = "xyzabcd"

class LocateById:
  LOGIN_BUTTON_ID = "loginBtn"
  SNACKBAR_ID = "notistack-snackbar"

 

class LocateByClass:
  POPUP_LOGIN_CLASS = "WLoginNavbar_loginButton__M7mhW"

class LocateByXpath:
  SEARCH_BAR_XPATH = '//input[@id="gsearch"]'  # Adjust this if needed
  SEARCH_BUTTON_XPATH = '//button[@id="searchId"]'  # Adjust this if needed
  RESULT_TITLES_XPATH = '//*[contains(@class, "search-page")]/div/div/div/div/div/div[1]'  # Modify based on actual site structure
  ERROR_MESSAGE_XPATH='//*[contains(@class, "title-error")]'
  EMAIL_INPUT_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/div/input'
  PASSWORD_INPUT_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[2]/div/input'
  EMAIL_ERROR_XPATH = '//div[@class="WLoginNavbar_loginDialogRightDiv__x6Kbk"]/form/div/div[1]/div/p'
  ADD_TO_CART_XPATH="//div[contains(@class,'search-page')]//button[contains(., 'Add to Cart')][1]"
  ADD_TO_CART_FINAL_XPATH = "(//button[contains(@class, 'Product_productAddtoCarddiv__hWTQk')])[1]"
  BOOK_ADDED_TO_CART_XPATH="//span[contains(text(),'Book added to cart!')]"
  CART_ICON="//span[@id='cartIcon']"
  LOGIN_BTN='//button[@id="loginBtn"]/span'
  ADD_BUTTON='//*[@id="yousaved"]/div/div/button[2]'
  QUANTITY='//*[@id="yousaved"]/div/div/span[1]'
  ZERO_XPATH='/html/body/main/div[3]/div/div/div/div[1]/div[1]/div[1]/div[1]/span/text()[2]'