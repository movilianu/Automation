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

# This test is made to test if the Sign In step of the checkout process is forced if the user is not already logged in.
def test_sign_in_page_mandatory():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    time.sleep(5)
    # Add to cart an item
    add_to_cart = Text("Add to cart", below="Blouse")
    click (add_to_cart)
    # Continue the flow by advancing to the checkout summary page.
    time.sleep(3)
    click ("Proceed to checkout")
    # Ensure the Summary page appears and has the proper title and information added.
    assert (Text("Your shopping cart", above="SHOPPING-CART SUMMARY").exists())
    # Ensure that pressing the proceed to checkout button takes the user to the Address page
    click ("Proceed to checkout")
    # Add the proper inputs in the sign in fields and sign in
    # Adding the data in the login fields
    usernameInputField = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.ID , "email")))
    usernameInputField.click()
    usernameInputField.send_keys("movilianu" + "@" + "gmail.com")
    driver.find_element_by_id("passwd").send_keys("Test123!")
    # Clicking the log in button
    signInButton = driver.find_element_by_name("SubmitLogin")
    signInButton.click()
    assert (Text("Choose a delivery address:").exists())
    assert (Text("If you would like to add a comment about your order, please write it in the field below.").exists())
    kill_browser()
