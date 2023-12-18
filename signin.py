# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://nondescript-loaf.demo.prestashop.com/en/login?back=https%3A%2F%2Fnondescript-loaf.demo.prestashop.com%2Fen%2Flogin%3Fback%3Dhttps%253A%252F%252Fnondescript-loaf.demo.prestashop.com%252Fen%252Flogin%253Fback%253Dhttps%25253A%25252F%25252Fnondescript-loaf.demo.prestashop.com%25252Fen%25252F%25253Fid_module_showcased%25253Dundefined")
driver.implicitly_wait(25)  # wait till the page load with max 30 sec

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
# now we have programmer that connect to URL , we can start get elements and manipulate it
# to select from drop down menu
# element = Select(driver.find_element("id", "testingDropdown"))
# element.select_by_value("Performance")

signinButton = driver.find_element("id", "submit-login")


emailFeild = driver.find_element("id","field-email")
passwordFeild = driver.find_element("id","field-password")
emailFeild.send_keys("a@a.com")
passwordFeild.send_keys("P,V2t@+%d^UnQBt")
signinButton.click()

# Wait for the alert to appear
time.sleep(2)  # Use WebDriverWait for a more robust solution
# element2.click()


# double click
# actions = ActionChains(driver)
# actions.double_click(element).perform()
#
#


# to click button

# element.click()

# Input data into the text field
# element.send_keys("Hello, World!")
# shopping cart =======================================
# order history
# browse deals

# how to wait for specific message like download competed
# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME, ''),  # Element filtration
#         'Complete!'  # The expected text|
#     )
# )
