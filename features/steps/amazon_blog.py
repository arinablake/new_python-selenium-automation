from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


BLOG_LINK = (By.XPATH, "//a[text()='See daily updates at blog.aboutamazon.com']")
BLOG_HEADLINE = (By.CSS_SELECTOR, '.ArticlePage-headline')
BLOG_MENU = (By.CSS_SELECTOR, '.ArticlePage-header-menuToggle')
BLOG_MENU_CLOSE = (By.CSS_SELECTOR, '.ArticlePage-header-menuClose')


@when('Store original windows')
def store_original_window(context):
    context.init_window = context.driver.current_window_handle


@when('Click on blog link “See daily updates at blog.aboutamazon.com”')
def click_blog_link(context):
    blog_link = context.driver.find_element(*BLOG_LINK)
    blog_link.click()
    context.all_windows = context.driver.window_handles


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.switch_to.window(context.all_windows[1])


@then('Amazon {expected} is opened')
def verify_blog(context, expected):
    actual = context.driver.find_element(*BLOG_HEADLINE).text
    assert expected in actual, f'Expected text {expected}, but got {actual}'


@then('User can open and close Blog menu')
def blog_menu(context):
    blog_menu_link = context.driver.find_element(*BLOG_MENU)
    blog_menu_link.click()
    blog_menu_close = context.driver.find_element(*BLOG_MENU_CLOSE)
    blog_menu_close.click()


@then('User can close new window and switch back to original')
def close_and_go_back(context):
    context.driver.close()
    context.driver.switch_to.window(context.init_window)