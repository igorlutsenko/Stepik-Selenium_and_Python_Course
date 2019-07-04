from selenium import webdriver
from time import sleep
import os


current_dir = os.path.abspath(os.path.dirname('file.txt'))
file_path = os.path.join(current_dir, 'file.txt')


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

first_name = browser.find_element_by_css_selector('[name="firstname"]')
second_name = browser.find_element_by_css_selector('[name="lastname"]')
email = browser.find_element_by_css_selector('[name="email"]')

first_name.send_keys("Igor")
second_name.send_keys("Lutsenko")
email.send_keys("igor@smth.com")


file = browser.find_element_by_id("file")
file.send_keys(file_path)


button = browser.find_element_by_tag_name("button")
button.click()

