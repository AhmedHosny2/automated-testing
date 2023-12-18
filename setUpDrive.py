# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time




def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver
