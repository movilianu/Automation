from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import config
import locators
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is made to test what happens when the user is on the Addresses page, decides to make a new address but then quits mid-way.
def test_addresses_changing_delivery_billing_address_return_to_addresses():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    time.sleep(5)
    # Add to cart an item
    add_to_cart = Text("Add to cart", below="Blouse")
    click (add_to_cart)
    # Continue the flow by advancing to the checkout addresses page.
    time.sleep(3)
    click ("Proceed to checkout")
    assert (Text("Your shopping cart", above="SHOPPING-CART SUMMARY").exists())
    click ("Proceed to checkout")
        # Add the proper inputs in the sign in fields and sign in
    usernameInputField = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.ID , "email")))
    usernameInputField.click()
    usernameInputField.send_keys("movilianu" + "@" + "gmail.com")
    driver.find_element_by_id("passwd").send_keys("Test123!")
        # Clicking the log in button
    signInButton = driver.find_element_by_name("SubmitLogin")
    signInButton.click()
    # Ensure the user arrived on the Addresses page
    assert (Text("Choose a delivery address:").exists())
    time.sleep(4)
    # Check that the Update buttons work as intended
    # First is the delivery update button
        # Because of lack of time, only the mobile phone update will be tested.
        # Normally, all fields should be tested with the documentation of limits and requirements as reference.
    delivery_billing_address_checkbox = driver.find_element_by_id('addressesAreEquals')
    if delivery_billing_address_checkbox.is_selected():
        click(delivery_billing_address_checkbox)
    time.sleep(2)
    assert (S(locators.add_a_new_address_button).exists())
    click (S(locators.add_a_new_address_button))
    time.sleep(2)
    click (S(locators.back_to_your_addresses_button))
    assert (Text("Be sure to update your personal information if it has changed.").exists())
    kill_browser()
