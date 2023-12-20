# main_script.py

from sign_up_script import signIn
import time

# Replace these with actual values
username = "a@a.com"
password = "P,V2t@+%d^UnQBt"

driver = signIn(username, password)


def editEmail(newEmail):
    profile_page = driver.find_element("xpath", '//*[@id="identity-link"]')
    profile_page.click()

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
    print(save_button.text)
    save_button.click()

    time.sleep(2)


if __name__ == "__main__":
    # Replace these with actual values
    newEmail = "h@h.com"
    editEmail(newEmail)
