# # set up the programmer using chrome
#
from selenium import webdriver

from selenium.webdriver.chrome.options import Options




def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver

#using fire fox

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
#
# def setup_driver():
#     # Set up Firefox options
#     firefox_options = Options()
#     # Add any additional options if needed
#
#     # Create a Firefox WebDriver instance
#     driver = webdriver.Firefox(options=firefox_options)
#     return driver
