from src.edit_email_script import editEmail
from dotenv import load_dotenv
from src.setUpDrive import setup_driver
import os
import pytest
from selenium.common.exceptions import NoSuchElementException

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")
email = "h@h.com"
password = "P,V2t@+%d^UnQBt"


def test_correct_new_email():
    try:
        driver = setup_driver()
        newEmail = "h@h.com"
        resultedEmail, success_alert = editEmail(driver, site_url, "success@a.com", password, newEmail)
        assert success_alert == "Information successfully updated."

        assert resultedEmail == newEmail


    finally:
        driver.quit()


# test no new email
@pytest.mark.xfail(raises=NoSuchElementException)
def test_no_new_email():
    try:
        driver = setup_driver()
        newEmail = ""
        resultedEmail, success_alert = editEmail(driver, site_url, email, password, newEmail)
        assert success_alert != "Information successfully updated."
    finally:
        driver.quit()


# test invalid new email
@pytest.mark.xfail(raises=NoSuchElementException)
def test_invalid_new_email():
    try:
        driver = setup_driver()
        newEmail = "invalid_email"
        resultedEmail, success_alert = editEmail(driver, site_url, email, password, newEmail)
        assert success_alert != "Information successfully updated."


    finally:
        driver.quit()


# test no password
@pytest.mark.xfail(raises=NoSuchElementException)
def test_no_password():
    try:
        driver = setup_driver()
        newEmail = "l@l.com"
        password = ""
        resultedEmail, success_alert = editEmail(driver, site_url, email, password, newEmail)
        assert success_alert != "Information successfully updated."

    finally:
        driver.quit()
