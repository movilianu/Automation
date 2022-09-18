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
# This test replicates how to check for a part of the proper flow when having UNSTABLE data in the testing environment
def test_select_the_first_option():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    # The time package is used here to avoid failed assertions (ergo failed test) because of page loading time.
    time.sleep(5)
     # Identifying the login button and interacting with it
    # Once the main page is accessed add the first item to the cart whatever it may be.
    driver.find_elements_by_xpath("//a[@title='Add to cart']")[1].click()
    # Continue the flow by advancing to the checkout summary page.
    click (Text("Proceed to checkout"))
    # Choosing to assert texts like "In stock" or "SHOPPING-CART SUMMARY" is a good way of knowing that the flow continued properly
    # since the strings themselves did not exist in the pages prior to the current one
    assert (Text("SHOPPING-CART SUMMARY")).exists()
    assert (Text("In stock")).exists()
    click (Text("Proceed to checkout"))
# Ensure specific elements are present at this point of the checkout flow if the user is not logged in
    assert (Text("ALREADY REGISTERED?")).exists()
    assert (Text("Please enter your email address to create an account.")).exists()
    # The following two assertions are great examples of how one can test that two strings exist while technically only testing for one of them
    assert (Text("Sign in", to_left_of="Address")).exists()
    assert (Text("Shipping", to_left_of="Payment")).exists()
    kill_browser()
