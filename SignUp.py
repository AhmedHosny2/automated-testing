from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from setUpDrive import setup_driver


def sign_up_to_site(driver, site_url, gender_type, first_name, last_name, email, password, agree_tac,
                    agree_customer_privacy):
    driver.get(site_url)
    driver.implicitly_wait(25)

    gender_select = driver.find_element("id", f"field-id_gender-{1 if gender_type == 'male' else 2}")
    first_name_field = driver.find_element("id", "field-firstname")
    last_name_field = driver.find_element("id", "field-lastname")
    email_field = driver.find_element("id", "field-email")
    password_field = driver.find_element("id", "field-password")
    agree_tac_checkbox = driver.find_element("name", "psgdpr")
    agree_customer_privacy_checkbox = driver.find_element("name", "customer_privacy")

    gender_select.click()
    first_name_field.send_keys(first_name)
    last_name_field.send_keys(last_name)
    email_field.send_keys(email)
    password_field.send_keys(password)

    if agree_tac:
        agree_tac_checkbox.click()

    if agree_customer_privacy:
        agree_customer_privacy_checkbox.click()

    # save_button = driver.find_element("css selector", "button[data-link-action='save-customer']")
    # save_button = driver.find_element("css selector", "button[data-link-action='save-customer']")

    save_button = driver.find_element("class name", "btn-primary")
    print(save_button.text)
    save_button.click()

    time.sleep(2)


def signUp(gender_type, first_name, last_name, email, password, agree_tac, agree_customer_privacy):
    driver = setup_driver()
    sign_up_to_site(driver,
                    "https://unkempt-coil.demo.prestashop.com/en/registration", gender_type, first_name, last_name,
                    email, password, agree_tac, agree_customer_privacy)
    return driver


if __name__ == "__main__":
    # Replace these with actual values
    gender_type = "male"  # or "Mrs" or "Miss"
    first_name = "Ahmed"
    last_name = "Yehia"
    email = "a@a.com"
    password = "P,V2t@+%d^UnQBt"
    agree_tac = True
    agree_customer_privacy = True

    signUp(gender_type, first_name, last_name, email, password, agree_tac, agree_customer_privacy)
