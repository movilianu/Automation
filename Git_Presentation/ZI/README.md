This file contains details of what the thought process behind the tests is.
The tests were created using Python, Selenium and Helium.

The latter is a Python library based off of Selenium-Python. While it does the same things (mostly),
it helps keep the code shorter, cleaner and tighter thus makes it easier to read and maintain.

While against best practice when it comes to combining libraries in one framework,
Selenium is also used in some tests for proving knowledge if nothing else.
----------------------------------------
You will notice that some tests like:
test_select_item_main_page_option_one.py
&
test_select_item_main_page_option_two.py
do almost the same thing from their title but they are written differently as to shown the different
patterns that one may use to tackle an issue. The first one is excruciatingly easy to both write, read and follow.
The second one does the same thing but it is definitely not as user-friendly.
----------------------------------------
Not only that, but you will notice different approaches both in how the elements are interacted with
as well as how the webdriver is accessed.

Ex. 1
# Driver is declared locally in the test as a path.

driver = webdriver.Chrome(executable_path=r'C:\Testing\Automation\Automation\Lib\chromedriver', options=options)

def example_how_the_instance_is_started_1():
    set_driver(driver)
    get_driver()
    go_to(config.url)

vs.

Ex. 2
# Driver variable is not defined since it is supposedly already defined by adding chromedriver to the environmental path in the local machine

def example_how_the_instance_is_started_2():
    start_chrome(config.url, headless=False)

For other comments reasoning the inserted line of code or argument, you may see them in the tests themselves.
