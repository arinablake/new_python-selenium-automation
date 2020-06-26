from selenium.webdriver.common.by import By
from behave import given, when, then

CHECK_WF_PAGE = (By.CSS_SELECTOR, '.wfm-sales-item-card__regular-price')
WF_NAME = (By.CSS_SELECTOR, '.wfm-sales-item-card__product-name')


@given('Open Amazon Whole Foods deals page')
def open_amazon_wf_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify, every product on the page has a text {expected}')
def check_wf_page(context, expected):
    actual = context.driver.find_element(*CHECK_WF_PAGE).text
    assert expected in actual, f'Expected text {expected}, but got {actual}'


@then('Verify, every product on the page has a product name')
def check_wf_name(context):
    wf_names = context.driver.find_elements(*WF_NAME)
    for pr_name in wf_names:
        print(pr_name.text)
        assert len(pr_name.text) > 0
