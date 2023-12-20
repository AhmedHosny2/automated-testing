# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time
from setUpDrive import setup_driver


def browse_deals():
    site_url = "https://miniature-debt.demo.prestashop.com/en/prices-drop"
    driver = setup_driver()
    driver.implicitly_wait(25)
    time.sleep(2)


if __name__ == "__main__":
    # Replace these with actual values
    browse_deals()
