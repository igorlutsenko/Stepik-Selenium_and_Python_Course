import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LINKS = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope="function")
def driver():
    print("\nBrowser opened!")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('link', LINKS)
def test_open_link(driver, link):
    driver.get(link)
    time.sleep(1)
    form = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-type='string-quiz']>textarea")))
    form.send_keys(str(math.log(int(time.time()))))
    time.sleep(1)
    btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "submit-submission ")))
    btn.click()
    time.sleep(1)
    feedback = driver.find_element_by_class_name("smart-hints__hint ").text
    assert feedback == "Correct!"

