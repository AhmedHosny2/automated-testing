from src.sign_up_script import sign_up
from src.setUpDrive import setup_driver
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")

# Common metadata for tests
register_url = site_url + "registration"
gender_type = "male"
first_name = "Ahmed"
last_name = "Yehia"
password = "P,V2t@+%d^UnQBt"
agree_tac = True
agree_customer_privacy = True


def test_successful_sign_up():
    email = "success@a.com"
    driver = setup_driver()

    try:
        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac,
                agree_customer_privacy)
        assert driver.current_url == site_url
    finally:
        driver.quit()


def test_failed_sign_up_missing_agreement():
    email = "failed1@a.com"
    agree_customer_privacy = False
    driver = setup_driver()

    try:
        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac,
                agree_customer_privacy)
        assert driver.current_url != site_url
    finally:
        driver.quit()


def test_failed_sign_up_invalid_email():
    email = "invalid_email"
    driver = setup_driver()

    try:
        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac,
                agree_customer_privacy)
        assert driver.current_url != site_url
    finally:
        driver.quit()


def test_failed_sign_up_existing_email():
    email = "success@a.com"
    driver = setup_driver()

    try:
        # Assuming successful sign-up (this can be a precondition or a separate test)
        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac,
                agree_customer_privacy)

        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac,
                agree_customer_privacy)
        assert driver.current_url != site_url
    finally:
        driver.quit()
