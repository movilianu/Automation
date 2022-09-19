This file contains details of what the thought process behind the tests is.
The tests were created using Python, Selenium and Helium.

The latter is a Python library based off of Selenium-Python. While it does the same things (mostly),
it helps keep the code shorter, cleaner and tighter thus makes it easier to read and maintain.

While against best practice when it comes to combining libraries in one framework,
Selenium is also used in some tests for adding stability and completion.
----------------------------------------
I recommend starting by reading the tests:
test_select_item_main_page_option_one.py
&
test_select_item_main_page_option_two.py
They are found in the same folder as this REDME.md file and do almost the same thing but they are written differently as to show the various
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

End to End flows for puchasing:
test_e2e_flow_first.py
test_e2e_flow_second.py

Summary Page testing:
- Ensuring general data and values are present and correct on the Summary page
test_summary_page_text_assertions.py
- Ensuring that if the user interacts with a soon-to-be bought item, the behaviour is as expected
test_summary_page_redirect_shopping_cart_product_name.py
test_summary_page_redirect_shopping_cart_product_color_size.py
test_summary_page_redirect_description_name.py
test_summary_page_redirect_description_color_size.py
- Ensuring that the values and buttons in the Quantity area are present and function properly
test_summary_page_quantity_interaction.py
- Ensuring that deletion from both the Summary page as well as the shopping cart exists and has proper functionality
test_summary_page_delete_from_page.py
test_summary_page_delete_from_cart.py
- Ensuring the checkout cart is available and has proper data in the summary page
test_summary_page_checkout_cart.py

Sign In Page testing:
- Ensuring the user is forced to log in before they reach the Addresses page if they have not signed in yet
test_sign_in_page_mandatory.py
- Ensuring the Sign In page does not appear as a requirement in the shopping process if they have already signed in before proceeding further than the Summary page
test_sign_in_page_skip.py

Addresses Page testing:
- Ensuring the user's data is added in the page and it correctly shows itself
test_addresses_info.py
- Ensuring that the user can update and change their data and it reflects properly in the page as well as testing related elements (buttons, texts, values, etc.)
test_addresses_updates.py
- Ensuring users can add addresses, change them, use different ones and that elements related to them exist and function properly (selectors, buttons, input fields, values, etc.)
test_addresses_changing_delivery_billing_same_different_addresses.py
test_addresses_changing_delivery_billing_address_add_new_address.py
test_addresses_changing_delivery_billing_address_return_to_addresses.py

Shipping Page testing :
- Ensuring all elements are present, interactable and have proper behavior (texts, checkboxes, links, buttons, terms and conditions)
test_shipping_page.py

Payment Page testing:
While it could have been broken down into multiple smaller tests (as best practice indicates), it was 2AM when I was writing them and I really needed to sleep so apologise for the cramming of code into only two tests.
- Ensuring the user can use the cheque payment option and that both the data, flow and elements are properly present
test_payment_page_cheque.py
- Ensuring the user can use the bankwire payment option and that both the data, flow and elements are properly present
test_payment_page_cheque.py
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
- retesting the data and redirects in the Payment page. This was not done because the steps are almost identical with the testing done for the summary page.The only thing different is that the user has to advance to the page by clicking Proceed for 4 times.
