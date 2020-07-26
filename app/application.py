from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
# from pages.search_results_page import SearchResults
from pages.main_page import MainPage
from pages.results_page import ResultsPage
from pages.hamburger_menu_page import HamburgerMenuPage
from pages.product_page import Product

class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        # self.search_results_page = SearchResults(self.driver)
        self.main_page = MainPage(self.driver)
        self.results_page = ResultsPage(self.driver)
        self.hamburger_menu_page = HamburgerMenuPage(self.driver)
        self.product_page = Product(self.driver)
