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

# This test is made to test the Summary page
def test_summary_page_checkout_cart():
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
    # Ensure the cart has the proper properties when the user is not interacting with it
    shopping_cart_style_before = driver.find_element_by_xpath("//html/body/div/div[1]/header/div[3]/div/div/div[3]/div/div")
    shopping_cart_style_before_style_value = shopping_cart_style_before.value_of_css_property("display")
    print(shopping_cart_style_before_style_value)
    assert shopping_cart_style_before_style_value == "none"
    # Ensure the cart has the proper properties when the user is interacting with it
    hover(S(locators.shopping_cart))
    shopping_cart_style_before = driver.find_element_by_xpath("//html/body/div/div[1]/header/div[3]/div/div/div[3]/div/div")
    shopping_cart_style_before_style_value = shopping_cart_style_before.value_of_css_property("display")
    print(shopping_cart_style_before_style_value)
    assert shopping_cart_style_before_style_value == "block"
    # Ensure the cart's data reflects the summary page's data
    total_price_cell_below_tax = Text(below=S(locators.tax_cost_cell), to_right_of=S(locators.total_final_header_below_tax)).value
    total_price_in_cart = Text(below=S(locators.tax_cost_in_cart), to_right_of=S(locators.total_header_in_cart)).value
    assert total_price_cell_below_tax == total_price_in_cart
    # Leave the page and then return to ensure cart stays the same -
    # This part would normally be in a different test since it is already getting cluttered but it is easier for you to follow the line of thought this way.
    click(S(locators.logo_image))
    time.sleep(3)
    hover(S(locators.shopping_cart))
    click(S(locators.check_out_button))
    assert (Text("Your shopping cart", above="SHOPPING-CART SUMMARY").exists())
    hover(S(locators.shopping_cart))
    total_price_cell_below_tax = Text(below=S(locators.tax_cost_cell), to_right_of=S(locators.total_final_header_below_tax)).value
    total_price_in_cart = Text(below=S(locators.tax_cost_in_cart), to_right_of=S(locators.total_header_in_cart)).value
    assert total_price_cell_below_tax == total_price_in_cart
    """
    Normally the redirect of the items in the cart when the user clicks them to their product page would be tested as well
    but for that, the test_summary_page_redirect_shopping_cart.py test has been created since this redirect is also found in the summary page as well.
    """
    kill_browser()
