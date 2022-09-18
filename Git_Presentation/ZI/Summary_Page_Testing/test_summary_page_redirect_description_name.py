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

# This test is made to test the Summary page's Description redirect when the user clicks on a product's name in it
def test_summary_page_redirect_description_name():
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
    # Testing the product's Description redirect
    # Click on the item and make sure it redirects properly by ensuring the existance of elements not found in the Summary page but on the product's page
    blouse_name = Text("Blouse", below="Description")
    click(blouse_name)
    assert (S(locators.social_media_area).exists())
    assert (Text("REVIEWS").exists())
    # Check that on the product's page the cart contains the added product
    hover(S(locators.shopping_cart))
    shopping_cart_style_before = driver.find_element_by_xpath("//html/body/div/div[1]/header/div[3]/div/div/div[3]/div/div")
    shopping_cart_style_before_style_value = shopping_cart_style_before.value_of_css_property("display")
    print(shopping_cart_style_before_style_value)
    assert shopping_cart_style_before_style_value == "block"
    total_price_in_cart = Text(below=S(locators.tax_cost_in_cart), to_right_of=S(locators.total_header_in_cart)).value
    total_price_in_cart == "$29.00"
    # Return to the Summary page and ensure data is still there properly assigned
    click(S(locators.check_out_button))
    assert (Text("Your shopping cart", above="SHOPPING-CART SUMMARY").exists())
    hover(S(locators.shopping_cart))
    total_price_cell_below_tax = Text(below=S(locators.tax_cost_cell), to_right_of=S(locators.total_final_header_below_tax)).value
    total_price_in_cart = Text(below=S(locators.tax_cost_in_cart), to_right_of=S(locators.total_header_in_cart)).value
    assert total_price_cell_below_tax == total_price_in_cart
    kill_browser()
