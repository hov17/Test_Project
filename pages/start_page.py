import allure
from selenium.webdriver import Keys
from base.base_page import BasePage
from utilities.locators import StartPageLocators
from utilities.logger import Logger


class StartPage(BasePage):
    # Метод для ввода информации в строке поиска
    def entering_information_in_the_search_field(self, text):
        with allure.step('Entering information in the search field'):
            Logger.add_start_step(method='entering_information_in_the_search_field')
            iframe = self.browser.find_element(*StartPageLocators.SEARCH_FIELD_FRAME)
            self.browser.switch_to.frame(iframe)
            assert self.is_element_present(*StartPageLocators.SEARCH_FIELD), 'Search field is missing!'
            self.browser.find_element(*StartPageLocators.SEARCH_FIELD).send_keys(text)
            assert self.is_element_present(*StartPageLocators.SUGGEST_LIST), 'Suggest list is missing!'
            self.browser.find_element(*StartPageLocators.SEARCH_FIELD).send_keys(Keys.RETURN)
            Logger.add_end_step(self.browser.current_url, method='entering_information_in_the_search_field')

    # Метод перехода на страницу с изображениями
    def go_to_page_with_images(self):
        with allure.step('Go to Image page'):
            Logger.add_start_step(method='go_to_page_with_images')
            iframe = self.browser.find_element(*StartPageLocators.SEARCH_FIELD_FRAME)
            self.browser.switch_to.frame(iframe)
            assert self.is_element_present(*StartPageLocators.SEARCH_FIELD), 'Search field is missing!'
            self.browser.find_element(*StartPageLocators.SEARCH_FIELD).click()
            assert self.is_element_present(*StartPageLocators.IMAGE_ICON), 'Image icon link is missing!'
            self.browser.find_element(*StartPageLocators.IMAGE_ICON).click()
