from helium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time
import config
import locators
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-infobars")
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

# This test is made to test the Summary page's cart deletion when the user clicks on the delete button in the cart
def test_summary_page_delete_from_cart():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    time.sleep(5)
    add_to_cart = Text("Add to cart", below="Blouse")
    click (add_to_cart)
    # Continue the flow by advancing to the checkout summary page.
    time.sleep(3)
    click ("Proceed to checkout")
    # Ensure the page appears and has the proper title and information added.
    assert (Text("Your shopping cart", above="SHOPPING-CART SUMMARY").exists())
    # Use the delete button to remove the added product from the cart and ensure its functionality
    hover(S(locators.shopping_cart))
    time.sleep(2)
    click(S(locators.cart_delete_product_button))
    time.sleep(10)
    assert (Text("Your shopping cart is empty.").exists())
    kill_browser()
