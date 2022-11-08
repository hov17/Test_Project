from base.base_page import BasePage
from utilities.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_first_link(self):
        # assert self.is_element_present(*MainPageLocators.SEARCHING_RESULTS), 'Searching results is missing!'
        self.browser.find_element(*MainPageLocators.FIRST_LINK).click()
        # return MainPage(browser=self.browser, url=self.browser.current_url, timeout=10)
