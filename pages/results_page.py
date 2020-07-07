from pages.base_page import Page
from selenium.webdriver.common.by import By


class ResultsPage(Page):
    SIGN_IN = (By.XPATH, "//form[@name='signIn']")
    CHECK_PAGE = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")
    RESULTS_HEADER = (By.CSS_SELECTOR, "span.a-color-state.a-text-bold")

    def verify_found_results_text(self, expected_text: str):
        self.verify_text(expected_text, *self.RESULTS_HEADER)

    def verify_result(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGN_IN)

    def check_cart(self, expected_text: str):
        self.verify_text(expected_text, *self.CHECK_PAGE)


