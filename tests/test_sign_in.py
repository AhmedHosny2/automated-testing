from src.sign_in_script import sign_in
from dotenv import load_dotenv
from src.setUpDrive import setup_driver
import os

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")
email = "success@a.com"
password = "P,V2t@+%d^UnQBt"


def test_incorrect_password():
    try:
        driver = setup_driver()
        incorrect_password = "incorrect_password"
        sign_in(driver, site_url, email, incorrect_password)
        assert driver.current_url != site_url
    finally:
        driver.quit()


def test_successful_login():
    try:
        driver = setup_driver()
        sign_in(driver, site_url, email, password)
        assert driver.current_url == site_url
    finally:
        driver.quit()


def test_empty_fields():
    try:
        driver = setup_driver()
        sign_in(driver, site_url, "", "")
        assert driver.current_url != site_url
    finally:
        driver.quit()


def test_invalid_email_format():
    try:
        driver = setup_driver()
        sign_in(driver, site_url, "invalid_email", "")
        assert driver.current_url != site_url
    finally:
        driver.quit()
