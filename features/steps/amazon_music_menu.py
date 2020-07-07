from behave import given, when, then


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.main_page.click_h_menu()


@when('Click on Amazon Music menu item')
def click_cart(context):
    context.app.hamburger_menu_page.open_music()


@then('{num} menu items are present')
def verify_list_number(context, num):
    context.app.hamburger_menu_page.check_number(num)
