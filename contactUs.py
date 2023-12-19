# main_script.py
# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time

from setUpDrive import setup_driver

driver = setup_driver()

# Replace these with actual values

# no sign in is needed fa malhash lazma

site_url = "https://confused-twist.demo.prestashop.com/en/contact-us"


def contact_us(email, message):
    driver.get(site_url)
    # to select the subject drop down btn
    subject_select = driver.find_element("id", "id_contact")
    subject_select.click()
    # writing email field
    email_field = driver.find_element("id", "email")
    email_field.send_keys(email)
    # writing in message field
    message_field = driver.find_element("id", "message")
    message_field.send_keys(message)
    # clicking on send button
    send_button = driver.find_element("class name", "btn-primary")
    send_button.click()

    time.sleep(2)


if __name__ == "__main__":
    # Replace these with actual values
    email = "a@a.com"
    message = "Our TA is the best!"
    contact_us(email, message)
