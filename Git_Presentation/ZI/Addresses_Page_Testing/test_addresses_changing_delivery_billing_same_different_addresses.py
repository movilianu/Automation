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
import random
import string
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-infobars")
# Globally defined variable for the chromedriver.exe file's path. Comment this out if needed. The test runs without it as well, it is a failsafe against possible issues.
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is made to test the behavior of adding a new address on the Addresses page.
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
    time.sleep(4)
    # Ensure only the delivery address is present
    wait_until(lambda: not Text("Choose a billing address:").exists())
    # Uncheck the checkbox
    delivery_billing_address_checkbox = driver.find_element_by_id('addressesAreEquals')
    if delivery_billing_address_checkbox.is_selected():
        click(delivery_billing_address_checkbox)
    time.sleep(2)
    # Ensure the Delivery email is the same as the user's initial address
    assert (Text("Choose a billing address:").exists())
    select_delivery_email = Select(driver.find_element_by_id('id_address_delivery'))
    select_delivery_email.select_by_visible_text('movx93@yahoo.com')
    select_delivery_email.select_by_value('747232')
    delivery_email = driver.find_element_by_id("id_address_delivery").get_attribute('value')
    print(delivery_email + " is the recorded delivery email value")
    assert delivery_email == "747232"
    # Ensure the billing address is different than the user's delivery address
    select_billing_email = Select(driver.find_element_by_id('id_address_invoice'))
    select_billing_email.select_by_visible_text('Automationogt@gmail.com')
    select_billing_email.select_by_value('747430')
    billing_email = driver.find_element_by_id("id_address_invoice").get_attribute('value')
    print(billing_email + " is the recorded billing email value")
    assert billing_email == "747430"
    # Ensure the user is able to switch between the available addresses for both delivery and billing.
    select_delivery_email = Select(driver.find_element_by_id('id_address_delivery'))
    select_delivery_email.select_by_visible_text('Automationogt@gmail.com')
    select_delivery_email.select_by_value('747430')
    delivery_email = driver.find_element_by_id("id_address_delivery").get_attribute('value')
    print(delivery_email + " is the recorded delivery email value")
    assert delivery_email == "747430"
    select_billing_email = Select(driver.find_element_by_id('id_address_invoice'))
    select_billing_email.select_by_visible_text('movx93@yahoo.com')
    select_billing_email.select_by_value('747232')
    billing_email = driver.find_element_by_id("id_address_invoice").get_attribute('value')
    print(billing_email + " is the recorded billing email value")
    assert billing_email == "747232"
    # Disable the different delivery and billing addresses by re-checking the checkbox for the same address
    click(delivery_billing_address_checkbox)
    # Ensure the different billing address does not exist anymore
    wait_until(lambda: not Text("Choose a billing address:").exists())
    full_name_delivery_address = Text(above=S(locators.delivery_address_street), below=S(locators.your_delivery_address_header)).value
    full_name_billing_address = Text(above=S(locators.billing_address_street), below=S(locators.your_billing_address_header)).value
    assert full_name_delivery_address == full_name_billing_address
    street_delivery_address = Text(below=S(locators.delivery_address_full_name), above=S(locators.delivery_address_city)).value
    street_billing_address = Text(below=S(locators.billing_address_full_name), above=S(locators.billing_address_city)).value
    assert street_delivery_address == street_billing_address
    city_delivery_address = Text(below=S(locators.delivery_address_street), above=S(locators.delivery_address_country)).value
    city_billing_address = Text(below=S(locators.billing_address_street), above=S(locators.billing_address_country)).value
    assert city_delivery_address == city_billing_address
    country_delivery_address = Text(below=S(locators.delivery_address_city), above=S(locators.delivery_address_phone_number)).value
    country_billing_address = Text(below=S(locators.billing_address_city), above=S(locators.billing_address_phone_number)).value
    assert country_delivery_address == country_billing_address
    phone_number_delivery_address = Text(below=S(locators.delivery_address_country), above=S(locators.update_delivery_address_button)).value
    phone_number_billing_address = Text(below=S(locators.billing_address_country), above=S(locators.update_billing_address_button)).value
    assert phone_number_delivery_address == phone_number_billing_address
    kill_browser()
