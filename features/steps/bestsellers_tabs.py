from selenium.webdriver.common.by import By
from behave import given, when, then


BESTSELLERS_LOCATOR = (By.CSS_SELECTOR,"#nav-xshop a[href*='bestsellers']")
TABS = (By.CSS_SELECTOR, "#zg_tabs a")


@when('Click bestsellers link')
def bestsellers_link(context):
    bestsellers = context.driver.find_element(*BESTSELLERS_LOCATOR)
    bestsellers.click()


@then('Verify that there are {expected} links on amazon bestsellers page')
def tabs(context, expected):
    actual = context.driver.find_elements(*TABS)
    assert int(expected) == len(actual), f'Expected number {expected}, but got {actual}'

