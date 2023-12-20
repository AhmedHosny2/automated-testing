import math

from src.shopping_cart import add_to_cart
from dotenv import load_dotenv
from src.setUpDrive import setup_driver
import os

# Load environment variables from the .env file
load_dotenv()
site_url = os.getenv("site_url")
email = "success@a.com"
password = "P,V2t@+%d^UnQBt"
quantity = 3
productName = "sweater"


def test_correct_shopping_cart_creation():
    try:
        driver = setup_driver()
        individual_price, total_price = add_to_cart(driver, site_url, email, password, productName, quantity)
        assert driver.current_url == site_url + "cart?action=show" and math.fabs(
            total_price - individual_price * quantity) <= 0.02
    finally:
        driver.quit()

def test_negative_quantity():
    try:
        driver = setup_driver()
        individual_price, total_price = add_to_cart(driver, site_url, email, password, productName, -10)
        assert driver.current_url == site_url + "cart?action=show" and math.fabs(
            total_price - individual_price * 1) <= 0.02
    finally:
        driver.quit()

def test_zero_quantity():
    try:
        driver = setup_driver()
        individual_price, total_price = add_to_cart(driver, site_url, email, password, productName, 0)
        assert driver.current_url == site_url + "cart?action=show" and math.fabs(
            total_price - individual_price * 1) <= 0.02
    finally:
        driver.quit()

