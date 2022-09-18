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
    set_driver(driver)
    get_driver()
    go_to(config.url)
    # The time package is used here to avoid failed assertions (ergo failed test) because of page loading time.
    time.sleep(5)
     # Identifying the login button and interacting with it
    loginButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH , "//*[@class='login']")))
    loginButton.click()
    # Adding the data in the login fields
    usernameInputField = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.ID , "email")))
    usernameInputField.click()
    usernameInputField.send_keys("movilianu" + "@" + "gmail.com")
    driver.find_element_by_id("passwd").send_keys("Test123!")
    # Clicking the log in button
    signInButton = driver.find_element_by_name("SubmitLogin")
    signInButton.click()
    # Interact with the main logo element to return to the first page since this is the fastest way to reach a product
    driver.find_element_by_xpath("//html/body/div/div[1]/header/div[3]/div/div/div[1]/a/img").click()
    # Once the main page is accessed add the first item to the cart whatever it may be.
    driver.find_elements_by_xpath("//a[@title='Add to cart']")[1].click()
    # Continue the flow by advancing to the checkout summary page.
    time.sleep(3)
    driver.find_element_by_xpath("//html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span").click()
        # Ensure there are items from the cart in the Summary page
    wait_until(lambda: not Text("Your shopping cart is empty.", below="//html/body/div/div[2]/div/div[3]/div/ul/li[1]/span").exists())
    totalAmount = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.XPATH , "//html/body/div/div[2]/div/div[3]/div/div[2]/table/tfoot/tr[7]/td[2]/span"))).get_attribute("innerHTML")
    if totalAmount != "$00.00":
        time.sleep(1)
    else:
        print("Amount is 0, check what happened. It should not have been.")
        kill_browser()
    # Proceed to the next page
    driver.find_element_by_xpath("//html/body/div/div[2]/div/div[3]/div/p[2]/a[1]").click()
    # Choosing to assert texts like "YOUR DELIVERY ADDRESS" or "YOUR BILLING ADDRESS" is a good way of knowing that the flow continued properly adn the user is on the correct page.
    # since the strings themselves did not exist in the pages prior to the current one
    yourDeliveryAddress = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.XPATH , "//html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[1]/ul/li[1]/h3"))).get_attribute("innerHTML")
    if yourDeliveryAddress == "Your delivery address":
        time.sleep(1)
    else:
        print("Missing header for Delivery Address section. Please investigate!")
        kill_browser()
    yourBillingAddress = WebDriverWait(driver,4).until(EC.presence_of_element_located((By.XPATH , "//html/body/div/div[2]/div/div[3]/div/form/div/div[2]/div[2]/ul/li[1]/h3"))).get_attribute("innerHTML")
    if yourBillingAddress == "Your billing address":
        time.sleep(1)
    else:
        print("Missing header for Billing Address section. Please investigate!")
        kill_browser()
    # Advance to the Shipping page
    driver.find_element_by_name("processAddress").click()
    # Ensure the user is on the Shipping page
    assert (Text("My carrier Delivery next day!")).exists()
    # Tick the checkbox
    checkbox = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH , "//*[@type='checkbox']")))
    checkbox.click()
    # Press the Proceed to Checkout button.
    driver.find_element_by_name("processCarrier").click()
    # The following assertion is a great example of how one can test that two strings exist while technically only testing for one of them and at the same time ensure we've reached the correct page.
    assert (Text("Pay by bank wire",above="Pay by check")).exists()
    # Proceed by choosing one of the payment options.
    driver.find_element_by_class_name("bankwire").click()
    # Ensure the user is on the last page of the flow
    assert (Text("BANK-WIRE PAYMENT.")).exists()
    # Press the confirmation button
    driver.find_element_by_xpath("//html/body/div/div[2]/div/div[3]/div/form/p/button").click()
    # Ensure the text detailing the completion of the flow exists
    assert (Text("Your order on My Store is complete.")).exists()
    # Ensure the styling is correct for the present flow
    borderColor = driver.find_element_by_id("step_end")
    if borderColor.value_of_css_property('border-right-color') != "rgba(81, 174, 92, 1)":
        print(borderColor.value_of_css_property('border-right-color') + "is the border color. Something went wrong, see why the colors do not match!")
        kill_browser()
    else:
        time.sleep(1)
    kill_browser()
