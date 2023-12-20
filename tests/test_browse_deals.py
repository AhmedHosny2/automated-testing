from src.browse_deals import browse_deals
from dotenv import load_dotenv
from src.setUpDrive import setup_driver
import os
import pytest
from selenium.common.exceptions import NoSuchElementException

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")


def test_correct_deal_browsing():
    try:
        driver = setup_driver()
        newEmail = "h@h.com"
        page_title = browse_deals(driver, site_url)
        assert page_title == "PRICES DROP"
    finally:
        driver.quit()
