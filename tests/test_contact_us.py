from src.contactUs import contact_us
from dotenv import load_dotenv
from src.setUpDrive import setup_driver
import os
import pytest
from selenium.common.exceptions import NoSuchElementException

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")
email = "a@sadfa.casdfom"
message = "best TA ever!"


def test_correct_contact_us():
    try:
        driver = setup_driver()
        success_alert = contact_us(driver, site_url, email, message)
        assert success_alert == "Your message has been successfully sent to our team."
    finally:
        driver.quit()


def test_empty_message():
    try:
        driver = setup_driver()
        success_alert = contact_us(driver, site_url, email, "")
        assert success_alert == "The message cannot be blank."
    finally:
        driver.quit()
