from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from src.sign_up_script import sign_up
from src.setUpDrive import setup_driver

def test_sign_up():
    gender_type = "male"
    first_name = "Ahmed"
    last_name = "Yehia"
    email = "f@a.com"
    password = "P,V2t@+%d^UnQBt"
    agree_tac = True
    agree_customer_privacy = True

    site_url = "https://unwieldy-order.demo.prestashop.com/en/"
    register_url = site_url+"registration"
    driver = setup_driver()

    try:
        sign_up(driver, register_url, gender_type, first_name, last_name, email, password, agree_tac, agree_customer_privacy)
        assert driver.current_url == site_url
    finally:
        driver.quit()
