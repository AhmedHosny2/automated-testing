# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time
from setUpDrive import setup_driver



def login_to_site(driver, site_url, username, password):
    driver.get(site_url)
    driver.implicitly_wait(25)

    signin_button = driver.find_element("id", "submit-login")
    email_field = driver.find_element("id", "field-email")
    password_field = driver.find_element("id", "field-password")

    email_field.send_keys(username)
    password_field.send_keys(password)
    signin_button.click()

    time.sleep(2)


def signIn(username, password):
    driver = setup_driver()
    login_to_site(driver,
                  "https://unkempt-coil.demo.prestashop.com/en/login?back=https%3A%2F%2Funkempt-coil.demo.prestashop.com%2Fen%2Flogin%3Fback%3Dhttps%253A%252F%252Funkempt-coil.demo.prestashop.com%252Fen%252Fregistration" ,
                 username, password)
    return driver


if __name__ == "__main__":
    # Replace these with actual values
    username = "a@a.com"
    password = "P,V2t@+%d^UnQBt"
    signIn(username, password)
