This file contains details of what the thought process behind the tests is.
The tests were created using Python, Selenium and Helium.

The latter is a Python library based off of Selenium-Python. While it does the same things (mostly),
it helps keep the code shorter, cleaner and tighter thus makes it easier to read and maintain.

While against best practice when it comes to combining libraries in one framework,
Selenium is also used in some tests for adding stability and completion.
----------------------------------------
You will notice that some tests like:
test_select_item_main_page_option_one.py
&
test_select_item_main_page_option_two.py
do almost the same thing from their title but they are written differently as to show the different
patterns that one may use to tackle an issue. The second one is excruciatingly easy to both write, read and follow.
The first one does the same thing but it is definitely not as user-friendly.
----------------------------------------
Not only that, but you will notice different approaches both in how the elements are interacted with
as well as how the webdriver is accessed. Again, this is done to showcase different writing techniques or combinations.

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
----------------------------------------
The following presents what the written tests do.
For a more accurate completion, the data is predetermined and more easily tested.
Of course if needed, the syntax can be changed so that elements are found as a list or dictionary and selected as needed. (see test_e2e_flow_first.py for such an example).


----------------------------------------
Aditional tests that were not created because of lack of time:
- out of stock products and their behavior in the processing phase
- extreme quantities of a product in the processing order phase
- multiple product interactions with the processing order phase
- editing user's information (name, street, location, phone number, email address, etc.) while the user is in the process of purchasing - this would need testing at every
 point of the checkout phase (Summary, Address, Shipping, Payment)
- processing flow and the interaction with every element or way that the user may leave the page and then return (ex. clicking the savings banner, opening a new tab and redirecting to the same shop while closing the old tab and then refreshing the new one, searching for different products, searching for the same products, contacting support, etc.)
- creating a new registered user while purchasing
- deep css value analysis depending on states (it is done once in the test_e2e_flow_first.py test and once more in the test_summary_page_checkout_cart.py test)
