from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name ul[role="radiogroup"] li')
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {productid} page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@when('Hover over New Arrivals')
def hover_new_arvls(context):
    context.app.product_page.hover_new_arvls()

@then('User can see the deals')
def verify_deals_tooltip(context):
    context.app.product_page.verify_deals_tooltip()
