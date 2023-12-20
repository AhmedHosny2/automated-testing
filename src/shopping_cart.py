# main_script.py

# from sign_in_script import sign_in
from src.setUpDrive import setup_driver
from dotenv import load_dotenv
import time
import os


# Load environment variables from the .env file


def add_to_cart(driver, site_url, email, password, productName, quantity):
    # sign_in(driver, site_url, email, password)
    driver.get(site_url)
    driver.implicitly_wait(25)

    quantity -= 1
    clothes_button = driver.find_element("xpath", '//*[@id="category-3"]/a')
    clothes_button.click()
    # woman_section_button = driver.find_element("xpath",
    #                                            "//a[contains(@class, 'dropdown-item') and contains(@href, 'women')]")
    # woman_section_button.click()
    sweater_section_button = driver.find_element("xpath", f"//a[contains(@href, '{productName}')]")
    sweater_section_button.click();
    add_to_cart_button = driver.find_element("class name", "btn-primary")
    # quantity_wanted_field = driver.find_element("id", "quantity_wanted")
    # quantity_wanted_field.clear()
    # quantity_wanted_field.send_keys(quantity)

    quantity_wanted_field = driver.find_element("class name", "btn-touchspin")

    for _ in range(quantity):
        quantity_wanted_field.click()

    add_to_cart_button.click()
    check_out_button = driver.find_element("xpath",
                                           "//a[contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(@href, 'cart?action=show')]")
    check_out_button.click()
    one_pice_price_element = driver.find_element("class name", "price")
    total_price_element = driver.find_element("xpath",
                                              '//*[@id="main"]/div/div[1]/div/div[2]/ul/li/div/div[3]/div/div[2]/div/div[2]/span/strong')


    one_pice_price = float(one_pice_price_element.text[1:])
    total_price = float(total_price_element.text[1:])

    print(one_pice_price)
    print("*************")
    print(total_price)

    time.sleep(2)
    return one_pice_price, total_price


if __name__ == "__main__":
    load_dotenv()
    site_url = os.getenv("SITE_URL")
    print(site_url)
    email = "success@a.com"
    password = "P,V2t@+%d^UnQBt"
    quantity = 3
    productName = "sweater"
    # Replace these with actual values
    driver = setup_driver()
    add_to_cart(driver, site_url, email, password, productName, quantity)
