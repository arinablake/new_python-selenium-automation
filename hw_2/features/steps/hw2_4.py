from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS = (By.XPATH, "//span[@class='nav-line-2'][text()='& Orders']")
SIGNIN = (By.XPATH, "//form[@name='signIn']")


@given('Open https://www.amazon.com')
def open_amazon_help_page(context):
    context.driver.get('https://www.amazon.com')


@when('Click Orders')
def click_orders_button(context):
    amazon_orders_button = context.driver.find_element(*ORDERS)
    amazon_orders_button.click()

sleep(2)

@then('Verify Sign in page opened')
def check_page(context):
    assert 'Sign-In' in context.driver.find_element(*SIGNIN).text

sleep(1)

