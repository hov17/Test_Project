import allure
from pages.images_page import ImagesPage
from pages.main_page import MainPage
from pages.start_page import StartPage

'''В задании указан сайт yandex.ru. При переходе на него идет авторедирект на Дзен, из-за этого немного отличается
 отображение элементов на сайте. Буду использовать сайт указанный в задании c редиректом на Дзен.'''


@allure.description('Yandex search test')
def test_yandex_search(browser):
    url = 'https://yandex.ru/'
    page = StartPage(browser, url, timeout=10)
    page.open()
    page.entering_information_in_the_search_field('Тензор')
    page.window_handles(1)
    page = MainPage(browser, browser.current_url, timeout=10)
    page.go_to_first_link()
    page.window_handles(2)
    page.is_url_address_correct('https://tensor.ru/')


# В данном тесте не смог реализовать пункт 6 из задания - "Проверить, что название категории отображается в поле
# поиска" - так как в HTML коде страницы не отображается значение введенное в строку поиска
@allure.description('Yandex images test')
def test_yandex_images(browser):
    url = 'https://yandex.ru/'
    page = StartPage(browser, url, timeout=10)
    page.open()
    page.go_to_page_with_images()
    page.window_handles(1)
    page.is_url_address_correct('https://yandex.ru/images/')
    page = ImagesPage(browser, browser.current_url, timeout=10)
    page.go_to_first_category()
    page.images_check()
