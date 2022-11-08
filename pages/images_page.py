import allure
from base.base_page import BasePage
from utilities.locators import ImagesPageLocators
from utilities.logger import Logger


class ImagesPage(BasePage):
    # Метод для открытия первой категории в изображениях
    def go_to_first_category(self):
        with allure.step('Go to first category'):
            Logger.add_start_step(method='go_to_first_category')
            self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()
            Logger.add_end_step(self.browser.current_url, method='go_to_first_category')

    # Метод проверки изображений
    def images_check(self):
        with allure.step('Images check'):
            Logger.add_start_step(method='images_check')
            self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE_IN_LIST).click()
            assert self.is_element_present(*ImagesPageLocators.CLOSE_BUTTON), 'First image does not open!'
            first_image_name_1 = self.browser.find_element(*ImagesPageLocators.NAME_OF_IMAGE).text
            self.browser.find_element(*ImagesPageLocators.FORWARD_BUTTON).click()
            second_image_name = self.browser.find_element(*ImagesPageLocators.NAME_OF_IMAGE).text
            assert first_image_name_1 != second_image_name, 'Second image does not open!'
            self.browser.find_element(*ImagesPageLocators.BACK_BUTTON).click()
            first_image_name_2 = self.browser.find_element(*ImagesPageLocators.NAME_OF_IMAGE).text
            assert first_image_name_1 == first_image_name_2, 'First image is incorrect!'
            Logger.add_end_step(self.browser.current_url, 'images_check')

