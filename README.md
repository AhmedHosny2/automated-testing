Automated Testing with Selenium

This repository contains a Selenium script for automated testing on a website using Python.
Prerequisites

Before running the script, make sure you have the following installed:

    Python (version 3.x)
    Selenium package

You can install the Selenium package using the following command:

bash

pip install selenium

Additionally, download the appropriate WebDriver executable (geckodriver for Firefox or chromedriver for Chrome) and ensure it is available in your system's PATH.
Setup

Clone this repository:

bash

git clone https://github.com/yourusername/automated-testing.git
cd automated-testing

Run the setup.py script to perform the initial setup:

bash

python setup.py

This script will set up the necessary dependencies and run the sign-up process once.
Running Tests

To run specific tests, you can execute the corresponding Python script. Tests that require a sign-in will automatically perform the sign-in process before executing.

Example:

To run the shopping cart test:

bash

python shopping_cart_test.py

Notes

    Make sure to customize the WebDriver setup in the setup_driver() function in setup.py according to your browser preference.
    If you encounter any issues, check the error messages in the console for details.

Feel free to contribute or report issues!