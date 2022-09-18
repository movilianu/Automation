from helium import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument(r"--user-data-dir=C:\\Users\\movil\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 4")
#options.add_argument(r'--profile-directory=Profile 4')
#options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f"user-data-dir=C:\\Users\\movil\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("profile-directory=Default")
import pytest
import time
import config
import locators
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

def test_Edinburgh():
    set_driver(driver)
    get_driver()
    go_to(config.url)
    time.sleep(5)
    click(S(locators.where_are_you_going))
    write("Edinburgh")
    time.sleep(2)
    assert Text("Edinburgh City Centre").exists()
    click ("Edinburgh City Centre")
    time.sleep(0.7)
    click (S(locators.date_picker))
    time.sleep(0.6)
    click (S(locators.the_25th))
    time.sleep(0.4)
    click (S(locators.the_30th))
    time.sleep(1)
    click ("Search")
    time.sleep(4)
    click (S(".map_full_overlay__close"))
    hover ("Kimpton - Charlotte Square, an IHG Hotel")
    time.sleep(1)
    click ("Kimpton - Charlotte Square, an IHG Hotel")
    time.sleep(2)
    assert (Text("38 Charlotte Square, Edinburgh, EH2 4HQ, United Kingdom – Excellent location - show map")).exists()
    time.sleep(5)
    click (S(locators.first_image))
    time.sleep(2)
    click (S(locators.first_image_choice_in_gallery))
    time.sleep(2)
    click (S(locators.back_to_gallery_button))
    time.sleep(1)
    click (S(locators.second_image_choice_in_gallery))
    time.sleep(2)
    click (S(locators.next_image_button))
    time.sleep(1)
    click (S(locators.next_image_button))
    time.sleep(2)
    click (S(locators.back_to_gallery_button))
    time.sleep(2)
    press(PAGE_DOWN)
    time.sleep(3)
    press(PAGE_DOWN)
    time.sleep(3)
    click (S(locators.close_gallery))
    time.sleep(2)
    assert (Text("38 Charlotte Square, Edinburgh, EH2 4HQ, United Kingdom – Excellent location - show map")).exists()
    press(PAGE_DOWN)
    time.sleep(1)
    press(PAGE_DOWN)
    time.sleep(1)
    click (S(locators.select_room))
    time.sleep(1)
    press(ARROW_DOWN)
    press(ENTER)
    time.sleep(0.6)
    hover (S(locators.I_will_reserve_button))