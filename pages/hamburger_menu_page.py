from pages.base_page import Page
from selenium.webdriver.common.by import By


class HamburgerMenuPage(Page):
    AM_LINK = (By.CSS_SELECTOR, "#hmenu-content > ul.hmenu.hmenu-visible > li:nth-child(3) > a")
    LINKS = (By.CSS_SELECTOR, ".hmenu-item[href*='music']")

    def open_music(self):
        self.click(*self.AM_LINK)

    def check_number(self, num: int):
        self.wait_for_element_appear(*self.LINKS)
        self.verify_number(num, *self.LINKS)
