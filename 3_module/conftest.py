import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
        help='Choose browser')


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print(f'\nStart {browser_name}')
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        print(f'\nStart {browser_name}')
        driver = webdriver.Firefox()
    else:
        print(f'Browser {browser_name} is not implemented yet')
    yield driver
    print(f'\nQuit {browser_name}')
    driver.quit()
