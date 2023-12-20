# main_script.py
# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

from src.setUpDrive import setup_driver
from dotenv import load_dotenv
import time
import os


# Replace these with actual values

# no sign in is needed fa malhash lazma


def contact_us(driver, site_url, email, message):
    driver.get(site_url + "contact-us")
    driver.implicitly_wait(25)

    # to select the subject drop down btn
    subject_select = driver.find_element("id", "id_contact")
    subject_select.click()
    # writing email field
    email_field = driver.find_element("id", "email")
    email_field.send_keys(email)
    # writing in message field
    message_field = driver.find_element("id", "contactform-message")
    message_field.send_keys(message)
    # clicking on send button
    send_button = driver.find_element("name", "submitMessage")
    send_button.click()
    try:
        success_alert = driver.find_element("xpath", '//*[@id="content"]/section/form/div/ul/li')
        print(success_alert.text)
        time.sleep(2)
        return success_alert.text
    except:
        pass


if __name__ == "__main__":
    # Replace these with actual values
    load_dotenv()
    site_url = os.getenv("SITE_URL")
    driver = setup_driver()
    email = "a@sadfa.casdfom"
    message = ""
    contact_us(driver,site_url, email, message)
