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

# This test is made to test the quantity textfield and its buttons in the Summary page
def test_summary_page_quantity_interaction():
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
    assert (Text("Qty", to_left_of="Total").exists())
    # Take the value from the quantity input field
    quantity_input_field_value_first_iteration = TextField(to_right_of=S(locators.unit_price_cell), below=S(locators.quantity_column_header_cell)).value
    assert quantity_input_field_value_first_iteration == "1"
    # Ensure the adding of quantity works
    time.sleep(1)
    click(S(locators.add_quantity))
    time.sleep(2)
    quantity_input_field_value_second_iteration = TextField(to_right_of=S(locators.unit_price_cell), below=S(locators.quantity_column_header_cell)).value
    assert quantity_input_field_value_second_iteration == "2"
    # Ensure the total value changes properly after quantity has been changed.
    # There are other changes in the page that take place but because of time sensitivity I will not check all of them, though normally I would.
    total_price_cell_below_tax = Text(below=S(locators.tax_cost_cell), to_right_of=S(locators.total_final_header_below_tax)).value
    assert total_price_cell_below_tax == "$56.00"
    # Ensure the Unit Price remained the same
    unit_price_amount_cell = Text(below=S(locators.unit_price_column_header), to_right_of=S(locators.availability_cell)).value
    assert unit_price_amount_cell == "$27.00"
    # Ensure the removal of quantity works
    time.sleep(1)
    click(S(locators.remove_quantity))
    time.sleep(2)
    quantity_input_field_value_third_iteration = TextField(to_right_of=S(locators.unit_price_cell), below=S(locators.quantity_column_header_cell)).value
    assert quantity_input_field_value_third_iteration == "1"
    # Ensure the total value changes properly after quantity has been changed.
    total_price_cell_below_tax = Text(below=S(locators.tax_cost_cell), to_right_of=S(locators.total_final_header_below_tax)).value
    assert total_price_cell_below_tax == "$29.00"
    # Ensure the Unit Price remained the same
    unit_price_amount_cell = Text(below=S(locators.unit_price_column_header), to_right_of=S(locators.availability_cell)).value
    assert unit_price_amount_cell == "$27.00"
    kill_browser()
