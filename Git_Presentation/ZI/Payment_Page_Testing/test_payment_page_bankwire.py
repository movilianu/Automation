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

# This test is made to test the redirect as in the .

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
    # Proceed to the Payment Page
    checkbox = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH , "//*[@type='checkbox']")))
    checkbox.click()
    click ("Proceed to checkout")
    # Ensure the user arrived on the Payment page
    assert (Text("PLEASE CHOOSE YOUR PAYMENT METHOD").exists())
    # Choose bankwire and check the flow
    click (S(locators.pay_by_bank_wire))
    time.sleep(2)
    assert (Text("BANK-WIRE PAYMENT.").exists())
    assert (Text("You have chosen to pay by bank wire. Here is a short summary of your order:").exists())
    assert (Text("- The total amount of your order comes to: $29.00 (tax incl.)").exists())
    assert (Text("- We allow the following currency to be sent via bank wire: Dollar").exists())
    assert (Text("- Bank wire account information will be displayed on the next page.").exists())
    assert (Text('- Please confirm your order by clicking "I confirm my order.".').exists())
    click ("I confirm my order")
    # Ensure the functionality for the button worked and the flow continued
    assert (Text("Your order on My Store is complete.").exists())
    assert (Text("Please send us a bank wire with").exists())
    assert (Text("Your order will be sent as soon as we receive payment.").exists())
    customer_support = driver.find_element_by_xpath('//html/body/div/div[2]/div/div[3]/div/div/a')
    customer_support.click()
    time.sleep(4)
    assert (Text("CUSTOMER SERVICE - CONTACT US").exists())
    kill_browser()
