from selenium.webdriver.common.by import By


class StartPageLocators():
    SEARCH_FIELD_FRAME = (By.XPATH, '//iframe[@class="dzen-search-arrow-common__frame"]')
    SEARCH_FIELD = (By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    SUGGEST_LIST = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')


class MainPageLocators():
    SEARCHING_RESULTS = (By.XPATH, '//div[@class="content__left"]')
    FIRST_LINK = (By.XPATH, '//span[@class="OrganicTitleContentSpan organic__title"]')
