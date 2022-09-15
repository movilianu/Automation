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
    go_to("https://www.booking.com/hotel/gb/the-principal-edinburgh-charlotte-square.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaMABiAEBmAEJuAEXyAEM2AEB6AEB-AELiAIBqAIDuALgsNKYBsACAdICJGRkNDFhNDdkLWE5YjYtNDc0MC04YTAwLTE5YmNlMzZkMGZkNtgCBuACAQ&sid=01e77df9b8479ef78f053f26f1f23d1d&atlas_src=sr_iw_title;checkin=2022-09-14;checkout=2022-09-25;dest_id=17250;dest_type=district;dist=0;group_adults=2;group_children=0;highlighted_blocks=21753843_222132351_2_2_0;no_rooms=1;room1=A%2CA;sb_price_type=total;type=total;ucfs=1&")
    time.sleep(3)
    click("Accept")
    assert (Text("38 Charlotte Square, Edinburgh, EH2 4HQ, United Kingdom – Excellent location - show map")).exists()
    press(PAGE_DOWN)
    time.sleep(1)
    press(PAGE_DOWN)
    time.sleep(1)
    click (S(locators.select_room))
    press(ARROW_DOWN)
    press(ENTER)
    time.sleep(0.6)
    hover (S(locators.I_will_reserve_button))
