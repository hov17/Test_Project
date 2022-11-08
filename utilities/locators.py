from selenium.webdriver.common.by import By


class StartPageLocators():
    SEARCH_FIELD_FRAME = (By.XPATH, '//iframe[@class="dzen-search-arrow-common__frame"]')
    SEARCH_FIELD = (By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    SUGGEST_LIST = (By.XPATH, '//ul[@class="mini-suggest__popup-content"]')
    IMAGE_ICON = (By.XPATH, '//div[@class="desktop-services"]/ul/li[4]/a')


class MainPageLocators():
    SEARCHING_RESULTS = (By.XPATH, '//div[@class="content__left"]')
    FIRST_LINK = (By.XPATH, '//span[@class="OrganicTitleContentSpan organic__title"]')


class ImagesPageLocators():
    FIRST_CATEGORY = (By.XPATH, '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    FIRST_IMAGE_IN_LIST = (By.XPATH, '//div[@class="serp-controller__content"]/div/div[1]')
    NAME_OF_IMAGE = (By.XPATH, '//div[@class="MMOrganicSnippet"]/div[1]/a')
    FORWARD_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-LayoutScene > .MediaViewer_theme_fiji-ButtonNext')
    BACK_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-LayoutScene > .MediaViewer_theme_fiji-ButtonPrev')
    CLOSE_BUTTON = (By.XPATH, '//div[@class="MMViewerModal-Close"]')
