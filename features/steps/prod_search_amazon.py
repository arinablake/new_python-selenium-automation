from behave import given, when, then


@when('Search for {search_word}')
def input_search(context, search_word):
    context.app.top_nav_menu.search_word(search_word)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.results_page.verify_found_results_text(search_word)


@when('Select {alias} department')
def select_department(context, alias):
    context.app.top_nav_menu.select_department(alias)


@then('{selected_dep} department is selected')
def verify_selected_department(context, selected_dep):
    context.app.top_nav_menu.verify_selected_department (selected_dep)
