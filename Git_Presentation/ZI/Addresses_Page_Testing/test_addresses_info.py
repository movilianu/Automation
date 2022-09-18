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
"""
The following three arguments added to the options used for the chrome instance,
are to exclude the "Chrome is being controlled by automated testing" infobar.
"""
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-infobars")
# Globally defined variable for the chromedriver.exe file's path. Comment this out if needed. The test runs without it as well, it is a failsafe against possible issues.
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is made to test the main elements found on the Addresses page.
def test_sign_in_page_mandatory():
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
    assert (Text("If you would like to add a comment about your order, please write it in the field below.").exists())
    assert (Text("YOUR DELIVERY ADDRESS").exists())
    assert (Text("YOUR BILLING ADDRESS").exists())
    full_name_delivery_address = Text(above=S(locators.delivery_address_street)).value
    assert full_name_delivery_address == "Dan Movilianu"
    street_delivery_address = Text(below=S(locators.delivery_address_full_name), above=S(locators.delivery_address_city)).value
    assert street_delivery_address == "Street Zitec nr1"
    city_delivery_address = Text(below=S(locators.delivery_address_street), above=S(locators.delivery_address_country)).value
    assert city_delivery_address == "Bucharest, Rhode Island 55555"
    country_delivery_address = Text(below=S(locators.delivery_address_city), above=S(locators.delivery_address_phone_number)).value
    assert country_delivery_address == "United States"
    phone_number_delivery_address = Text(below=S(locators.delivery_address_country), above=S(locators.update_delivery_address_button)).value
    assert phone_number_delivery_address == "555-5123-1231"
    full_name_billing_address = Text(above=S(locators.billing_address_street)).value
    assert full_name_billing_address == "Dan Movilianu"
    street_billing_address = Text(below=S(locators.billing_address_full_name), above=S(locators.billing_address_city)).value
    assert street_billing_address == "Street Zitec nr1"
    city_billing_address = Text(below=S(locators.billing_address_street), above=S(locators.billing_address_country)).value
    assert city_billing_address == "Bucharest, Rhode Island 55555"
    country_billing_address = Text(below=S(locators.billing_address_city), above=S(locators.billing_address_phone_number)).value
    assert country_billing_address == "United States"
    phone_number_billing_address = Text(below=S(locators.billing_address_country), above=S(locators.update_billing_address_button)).value
    assert phone_number_billing_address == "555-5123-1231"
    kill_browser()
