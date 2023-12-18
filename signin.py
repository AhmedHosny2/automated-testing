# set up the programmer

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
import time


def setup_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    return driver


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
                  "https://nondescript-loaf.demo.prestashop.com/en/login?back=https%3A%2F%2Fnondescript-loaf.demo.prestashop.com%2Fen%2Flogin%3Fback%3Dhttps%253A%252F%252Fnondescript-loaf.demo.prestashop.com%252Fen%252Flogin%253Fback%253Dhttps%25253A%25252F%25252Fnondescript-loaf.demo.prestashop.com%25252Fen%25252F%25253Fid_module_showcased%25253Dundefined",
                  username, password)
if __name__ == "__main__":
    # Replace these with actual values
    username = "a@a.com"
    password = "P,V2t@+%d^UnQBt"
    signIn(username, password)