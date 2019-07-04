import unittest
from selenium import webdriver
import time


class TestMain(unittest.TestCase):

    def test_link1(self):
        driver = webdriver.Chrome()

        driver.get("http://suninjuly.github.io/registration1.html")

        first_name = driver.find_element_by_css_selector('.first_block > .first_class > input')
        first_name.send_keys("Ivan")

        second_name = driver.find_element_by_css_selector('.first_block > .second_class > input')
        second_name.send_keys("Petrov")

        email = driver.find_element_by_css_selector('.first_block > .third_class > input')
        email.send_keys("petrov@yandex.ru")

        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text = driver.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

    def test_link2(self):
        driver = webdriver.Chrome()

        driver.get("http://suninjuly.github.io/registration2.html")

        first_name = driver.find_element_by_css_selector('.first_block > .first_class > input')
        first_name.send_keys("Ivan")

        second_name = driver.find_element_by_css_selector('.first_block > .second_class > input')
        second_name.send_keys("Petrov")

        email = driver.find_element_by_css_selector('.first_block > .third_class > input')
        email.send_keys("petrov@yandex.ru")

        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)

        welcome_text = driver.find_element_by_tag_name("h1").text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")


if __name__ == "__main__":
    unittest.main()
