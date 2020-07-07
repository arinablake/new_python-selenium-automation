from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TABS = (By.CSS_SELECTOR, "#zg_tabs a")
BANNER_TEXT = (By.CSS_SELECTOR, "#zg_banner_text")


@then('Verify that each tab has a matching banner')
def matching_banners(context):
    tab_titles = context.driver.find_elements(*TABS)

    for x in range(len(tab_titles)):
        tab_to_click = context.driver.find_elements(*TABS)[x]
        tab_text = tab_to_click.text
        tab_to_click.click()
        context.driver.wait.until(EC.visibility_of_element_located(BANNER_TEXT))
        banner_text = context.driver.find_element(*BANNER_TEXT).text
        assert tab_text in banner_text, f'Expected {tab_text} to be in {banner_text}'
