import pytest
from selenium import webdriver


class TestMain():

    def setup_method(self):
        print("\nStart browser")
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        print("\nQuit browser")
        self.driver.quit()

    def test_link1(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")

        first_name = self.driver.find_element_by_css_selector('.first_block > .first_class > input')
        first_name.send_keys("Ivan")
        second_name = self.driver.find_element_by_css_selector('.first_block > .second_class > input')
        second_name.send_keys("Petrov")
        email = self.driver.find_element_by_css_selector('.first_block > .third_class > input')
        email.send_keys("petrov@yandex.ru")

        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text = self.driver.find_element_by_tag_name("h1").text

        assert welcome_text == "Поздравляем! Вы успешно зарегистировались!"

    def test_link2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")

        first_name = self.driver.find_element_by_css_selector('.first_block > .first_class > input')
        first_name.send_keys("Ivan")
        second_name = self.driver.find_element_by_css_selector('.first_block > .second_class > input')
        second_name.send_keys("Petrov")
        email = self.driver.find_element_by_css_selector('.first_block > .third_class > input')
        email.send_keys("petrov@yandex.ru")

        button = self.driver.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text = self.driver.find_element_by_tag_name("h1").text

        assert welcome_text == "Поздравляем! Вы успешно зарегистировались!"

