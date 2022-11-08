import allure
from base.base_page import BasePage
from utilities.locators import MainPageLocators
from utilities.logger import Logger


class MainPage(BasePage):
    # Метод перехода по первой ссылке в результате поиска
    def go_to_first_link(self):
        with allure.step('Go to first link'):
            Logger.add_start_step(method='go_to_first_link')
            assert self.is_element_present(*MainPageLocators.SEARCHING_RESULTS), 'Searching results is missing!'
            self.browser.find_element(*MainPageLocators.FIRST_LINK).click()
            Logger.add_end_step(self.browser.current_url, method='go_to_first_link')
