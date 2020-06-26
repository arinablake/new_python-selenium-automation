from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name ul[role="radiogroup"] li')
COLOR_TITLE_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon Jeans {productid} page')
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@when('Check every color has matching description')
def color_description(context):
    jeans_colors = context.driver.find_elements(*COLOR_BUTTON_LOCATOR)
    color_title = context.driver.find_element(*COLOR_TITLE_LOCATOR)
    for jeans_color in jeans_colors:
        jeans_color.click()
        # print(color_title.text)
        # print(jeans_color.get_attribute('title'))
        assert color_title.text in jeans_color.get_attribute('title'), f"Expected {color_title.text} in {jeans_color.get_attribute('title')}"
