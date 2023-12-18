# main_script.py

from signin import signIn
import time

# Replace these with actual values
username = "a@a.com"
password = "P,V2t@+%d^UnQBt"

driver = signIn(username, password)


def add_to_cart(productName, quantity):
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
    time.sleep(2)


if __name__ == "__main__":
    # Replace these with actual values
    url = "https://nondescript-loaf.demo.prestashop.com/en/women/2-9-brown-bear-printed-sweater.html#/1-size-s"
    quantity = 3
    productName = "sweater"
    add_to_cart(productName, quantity)
