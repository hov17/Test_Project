import allure
from pages.main_page import MainPage
from pages.start_page import StartPage

'''В задании указан сайт yandex.ru. При переходе на него идет авторедирект на дзен. Буду использовать его, 
как указано в задании. Сам сайт Яндекса теперь открывается по ссылке https://ya.ru/. Можно указать его в url.'''


@allure.description('Test go to Tensor website')
def test_go_to_tensor_website(browser):
    url = 'https://yandex.ru/'
    page = StartPage(browser, url, timeout=10)
    page.open()
    page.entering_information_in_the_search_field('Тензор')
    page.window_handles(1)
    page = MainPage(browser, browser.current_url, timeout=10)
    page.go_to_first_link()
    page.window_handles(2)
    page.is_url_address_correct('https://tensor.ru/')
