import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

'''Данная фикстура применяется, если нужно провести тест на разных браузерах. По умолчанию установлен Chrome.
Для теста в Firefox необходимо передать параметр --browser_name=firefox. Оставляю ее в закомментированном виде,
Если установлен бразуер Firefox и есть geckodriver можно ее раскомментировать и проверить тест на браузере Firefox
предварительно закомментировав вторую фикстуру.'''

'''Сами драйвера для Chrome и Firefox добавлены в системны Path.'''

# # Фикстура открытия и закрытия браузера Chrome или Firefox
'''def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()'''


# Фикстура открытия и закрытия браузера Chrome
@pytest.fixture(scope='function')
def browser(request):
    print('\nstart browser for test..')
    browser = webdriver.Chrome() 
    yield browser
    print('\nquit browser..')
    browser.quit()
