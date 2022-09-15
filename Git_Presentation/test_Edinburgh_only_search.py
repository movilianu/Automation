from helium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
import pytest
import time
import config
import locators
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

def test_Edinburgh():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    time.sleep(2)
    click("Accept")
    click(S(locators.where_are_you_going))
    write("Edinburgh")
    time.sleep(2)
    assert Text("Edinburgh City Centre").exists()
    click ("Edinburgh City Centre")
    time.sleep(1)
    click (Text("14", to_right_of="13", to_left_of="15"))
    click (Text("25", to_right_of="24", to_left_of="17"))
    time.sleep(1)
    click ("Search")
    time.sleep(3)
    hover (Text("Kimpton - Charlotte Square, an IHG Hotel"))
    time.sleep(1)
    click (Text("Kimpton - Charlotte Square, an IHG Hotel"))
    time.sleep(2)
    assert (Text("38 Charlotte Square, Edinburgh, EH2 4HQ, United Kingdom – Excellent location - show map")).exists()
    time.sleep(1)
    hover (S(locators.first_image))
    click (S(locators.first_image))
    time.sleep(2)
    click (S(locators.first_image_choice_in_gallery))
    time.sleep(2)
    click (S(locators.back_to_gallery_button))
    time.sleep(1)
    click (S(locators.second_image_choice_in_gallery))
