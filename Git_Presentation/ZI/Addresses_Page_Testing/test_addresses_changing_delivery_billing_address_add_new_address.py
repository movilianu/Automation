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
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is made to test the behavior of adding a new address on the Addresses page.
# This function can have ascii_lowercase replaced with digits and then numbers will be shown, or concatenated and have both shown
def random_char(y):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(y))

def test_addresses_changing_delivery_billing_address_add_new_address():
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
    click(S(locators.delivery_input_field_mobile_phone))
    write("555-1234-1234")
    # Ensure the user has to fill all mandatory fields and can not advance otherwise
    click("Save")
    assert (Text("There are 5 errors").exists())
    time.sleep(4)
    # Add a new First Name
    click(S(locators.delivery_input_first_name))
    press(CONTROL + "a")
    press(DELETE)
    write("Automation" + random_char(3))
    # Add a new Last Name
    click(S(locators.delivery_input_last_name))
    press(CONTROL + "a")
    press(DELETE)
    write("Automation" + random_char(3))
    # Add a random street address
    click(S(locators.delivery_input_street_address))
    write(random_char(10))
    # Add a city
    click(S(locators.delivery_input_city))
    write(random_char(5))
    # Add a State
    select_state = Select(driver.find_element_by_id('id_state'))
    select_state.select_by_value('1')
    # Add an alias email
    click(S(locators.delivery_input_alis_email))
    write("Automation" + random_char(3) + "@" + "gmail.com")
    # Now we click the save button so that we may easily obtain the values added in the fields until now
    click("Save")
    # Puttin the values in variables for later use. Also printing the values to ensure manipulation if needed.
    new_first_name = driver.find_element_by_id("firstname").get_attribute('value')
    print(new_first_name)
    new_last_name = driver.find_element_by_id("lastname").get_attribute('value')
    print(new_last_name)
    new_street_address = driver.find_element_by_id("address1").get_attribute('value')
    print(new_street_address)
    new_state = driver.find_element_by_id("id_state").get_attribute('value')
    print(new_state)
    new_city = driver.find_element_by_id("city").get_attribute('value')
    print(new_city)
    new_alias = driver.find_element_by_id("alias").get_attribute('value')
    print(new_alias)
    # Saving to ensure the error message updates
    click("Save")
    # Checking the error message
    assert (Text("There is 1 error")).exists()
    assert (Text("The Zip/Postal code you've entered is invalid. It must follow this format: 00000")).exists()
    # Adding the zip Postal Code
    click(S(locators.delivery_input_zip_code))
    write("12345")
    # Save and return to the Addresses page
    click("Save")
    # Ensure the newly added data is present as the billing data
    new_billing_first_name = Text(below=S(locators.your_billing_address_header), above=S(locators.billing_address_street)).value
    assert new_billing_first_name == new_first_name + ' ' + new_last_name
    new_billing_street_address = Text(below=S(locators.billing_address_full_name), above=S(locators.billing_address_city)).value
    assert new_billing_street_address == new_street_address
    new_billing_city_state_and_zip_code = Text(below=S(locators.billing_address_street), above=S(locators.billing_address_country)).value
    assert new_billing_city_state_and_zip_code == new_city + ',' + ' ' + 'Alabama' + ' ' + '12345'
    new_billing_country = Text(below=S(locators.billing_address_city), above=S(locators.billing_address_phone_number)).value
    assert new_billing_country == "United States"
    new_billing_phone_number = Text(below=S(locators.billing_address_country), above=S(locators.update_billing_address_button)).value
    assert new_billing_phone_number == "555-1234-1234"
    kill_browser()
