from helium import *
# from selenium import webdriver
# import pytest
driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=get_driver())
#driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

def test_login():
    #start_chrome("www.google.com")
    set_driver(driver)
    get_driver()
    go_to("www.google.ro")
    kill_browser()


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
    start_chrome("www.google.com")
