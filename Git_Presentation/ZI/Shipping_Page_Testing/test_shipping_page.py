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
    time.sleep(2)
    # Advance to the Shipping page
    click ("Proceed to checkout")
    # Ensure the user arrived at the Shipping page
    assert (Text("My carrier Delivery next day!").exists())
    assert (Text("Choose a shipping option for this address: movx93@yahoo.com"))
    assert (Text("$2.00").exists())
    assert (Text("Terms of service").exists())
    assert (Text("I agree to the terms of service and will adhere to them unconditionally. (Read the Terms of Service)").exists())
    # Ensure the checkbox is not ticked and it has proper functionality
    click ("Proceed to checkout")
    time.sleep(2)
    assert (Text("You must agree to the terms of service before continuing.").exists())
    click(S(locators.close_popup))
    time.sleep(2)
    # Tick the checkbox
    checkbox = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH , "//*[@type='checkbox']")))
    checkbox.click()
    # Read the terms and conditions
    terms_of_service = driver.find_element_by_link_text('(Read the Terms of Service)')
    click (terms_of_service)
    time.sleep(2)
    assert (Text("Use this website for all our practices of automation scripts. We (seleniumframework.com) have gone a long way to invest in creating this website and providing excellent experience for you to have a practice platform").exists())
    click(S(locators.close_popup))
    # Ensure the functionality of the ticked checkbox
    click ("Proceed to checkout")
    wait_until(lambda: not Text("You must agree to the terms of service before continuing.").exists())
    kill_browser()
