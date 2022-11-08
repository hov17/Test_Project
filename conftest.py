import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


'''Данная фикстура применяется, если нужно провести тест на разных браузерах. По умолчанию установлен Chrome.
Для теста в Firefox необходимо передать параметр --browser_name=firefox'''

'''Сами драйвера для Chrome и Firefox добавлены в системны XPATH, поэтому я не передаю путь к ним в самой фикстуре.'''


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
