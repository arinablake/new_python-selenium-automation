from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SC_LOCATOR = (By.CSS_SELECTOR, "#nav-cart")
CHECK_PAGE = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")


@given('Open Amazon page')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')


@when('Click Shopping cart button')
def click_sc_button(context):
    amazon_sc_button = context.driver.find_element(*SC_LOCATOR)
    amazon_sc_button.click()
    sleep(1)


@then('Verify {expected} text present')
def check_page(context, expected):
    actual = context.driver.find_element(*CHECK_PAGE).text
    assert expected in actual, f'Expected text {expected}, but got {actual}'
    sleep(1)

