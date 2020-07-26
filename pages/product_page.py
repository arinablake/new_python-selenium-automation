from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Product(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, '#nav-subnav > a:nth-child(7)')
    DEALS = (By.CSS_SELECTOR, '.mega-menu')

    def hover_new_arvls(self):
        new_arvls_btn = self.find_element(*self.NEW_ARRIVALS)
        self.actions.move_to_element(new_arvls_btn).perform()

    def verify_deals_tooltip(self):
        self.wait_for_element_appear(*self.DEALS)