from selenium import webdriver
from math import log, sin
from time import sleep


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

value = browser.find_element_by_id("input_value").text
form = browser.find_element_by_id("answer")
form.send_keys(calc(value))

checkbox = browser.find_element_by_id("robotCheckbox")
checkbox.click()
browser.execute_script('button = document.getElementsByTagName("button")[0]; button.scrollIntoView();')

radio = browser.find_element_by_id("robotsRule")
radio.click()
sleep(1)

button = browser.find_element_by_tag_name("button")


button.click()
assert True
