# set up the programmer

# main_script.py
# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

from src.setUpDrive import setup_driver
from dotenv import load_dotenv
import time
import os


def browse_deals(driver, site_url):
    driver.get(site_url + "prices-drop")
    driver.implicitly_wait(25)
    page_title = driver.find_element("id", "js-product-list-header")
    print(page_title.text)
    time.sleep(2)
    return page_title.text


if __name__ == "__main__":
    load_dotenv()
    site_url = os.getenv("SITE_URL")
    driver = setup_driver()
    browse_deals(driver, site_url)
