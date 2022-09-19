from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import config
import locators
options = webdriver.ChromeOptions()
"""
The following three arguments added to the options used for the chrome instance,
are to exclude the "Chrome is being controlled by automated testing" infobar.
"""
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-infobars")
# Globally defined variable for the chromedriver.exe file's path. Comment this out if needed. The test runs without it as well, it is a failsafe against possible issues.
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is fairly complex, it is not an easy read but it is more stable and should technically require less maintenance.
# This test is not written in a best practice manner since it is meant to show knowledge of testing techniques.
# This test replicates how to check for a part of the proper flow when having UNSTABLE data in the testing environment
def test_select_the_first_option():
    start_chrome(config.url, headless=False)
    # The time package is used here to avoid failed assertions (ergo failed test) because of page loading time.
    time.sleep(5)
     # Identifying the login button and interacting with it
    click(S(locators.sign_in))
    # Adding the data in the login fields
    write(config.username, into=S(locators.email))
    write(config.password, into=S(locators.password))
    # Clicking the log in button
    click(Text("Sign in", below="Forgot your password?"))
    # Interact with the main logo element to return to the first page since this is the fastest way to reach a product
    click(S(locators.logo_image))
    # Once the main page is accessed add the first item to the cart whatever it may be.
    add_to_cart = Text("Add to cart", below="Blouse")
    click (add_to_cart)
    # Continue the flow by advancing to the checkout summary page.
    time.sleep(3)
    click ("Proceed to checkout")
        # Ensure there are items from the cart in the Summary page
    wait_until(lambda: not Text("Your shopping cart is empty.", below="Summary").exists())
    totalAmount = Text(to_right_of=S(locators.total_text_cell), below=S(locators.vat_value)).value
    assert totalAmount != "$00.00"
    # Proceed to the next page
    click ("Proceed to checkout")
    # Choosing to assert texts like "YOUR DELIVERY ADDRESS" or "YOUR BILLING ADDRESS" is a good way of knowing that the flow continued properly adn the user is on the correct page.
    # since the strings themselves did not exist in the pages prior to the current one
    assert Text("YOUR DELIVERY ADDRESS").exists()
    assert Text("YOUR BILLING ADDRESS").exists()
    # Advance to the Shipping page
    click ("Proceed to checkout")
    # Ensure the user is on the Shipping page
    assert (Text("My carrier Delivery next day!")).exists()
    # Tick the checkbox
    click(S(locators.checkbox))
    # Press the Proceed to Checkout button.
    click ("Proceed to checkout")
    # The following assertion is a great example of how one can test that two strings exist while technically only testing for one of them and at the same time ensure we've reached the correct page.
    assert (Text("Pay by bank wire",above="Pay by check")).exists()
    # Proceed by choosing one of the payment options.
    click(S(".bankwire"))
    # Ensure the user is on the last page of the flow
    assert (Text("BANK-WIRE PAYMENT.")).exists()
    # Press the confirmation button
    click("I confirm my order")
    # Ensure the text detailing the completion of the flow exists
    assert (Text("Your order on My Store is complete.")).exists()
    kill_browser()
