# main_script.py

# from sign_in_script import sign_in
import time
from src.setUpDrive import setup_driver
from dotenv import load_dotenv
import time
import os


# Replace these with actual values
# username = "a@a.com"
# password = "P,V2t@+%d^UnQBt"

# driver = sign_in(username, password)


def editEmail(driver, site_url, email, password, newEmail):
    # first sign in
    driver.get(site_url + "login")
    driver.implicitly_wait(25)

    signin_button = driver.find_element("id", "submit-login")
    email_field = driver.find_element("id", "field-email")
    password_field = driver.find_element("id", "field-password")

    email_field.send_keys(email)
    password_field.send_keys(password)
    signin_button.click()

    # then edit the email
    account_management = driver.find_element("class name", 'account')
    account_management.click()

    persnola_info = driver.find_element("id", 'identity-link')
    persnola_info.click()
    email_feild = driver.find_element("id", "field-email")
    email_feild.clear()
    email_feild.send_keys(newEmail)
    password_field = driver.find_element("id", "field-password")
    password_field.send_keys(password)
    agree_tac_checkbox = driver.find_element("name", "psgdpr")
    agree_customer_privacy_checkbox = driver.find_element("name", "customer_privacy")
    agree_tac_checkbox.click()

    agree_customer_privacy_checkbox.click()
    save_button = driver.find_element("class name", "btn-primary")
    save_button.click()
    new_email_feild = driver.find_element("id", "field-email")
    success_alert = driver.find_element("xpath", '//*[@id="notifications"]/div/article/ul/li')
    print(success_alert.text)
    time.sleep(2)

    return new_email_feild.get_attribute("value") , success_alert.text


if __name__ == "__main__":
    load_dotenv()
    site_url = os.getenv("SITE_URL")
    print(site_url)
    email =  "h@h.com"
    password = "P,V2t@+%d^UnQBt"
    driver = setup_driver()
    newEmail = "success@a.com"
    editEmail(driver, site_url, email, password, newEmail)
