from selenium import webdriver
import math
from time import sleep


def calc(x):
    return math.log(abs(12 * math.sin(int(x))))


URL = "http://suninjuly.github.io/alert_accept.html"

driver = webdriver.Chrome()
driver.get(URL)

btn = driver.find_element_by_tag_name("button")
btn.click()

accept = driver.switch_to.alert
accept.accept()

value = driver.find_element_by_id("input_value").text
form = driver.find_element_by_id("answer")
btn = driver.find_element_by_xpath("//button[@type='submit']")
form.send_keys(str(calc(value)))
btn.click()

sleep(5)

driver.quit()

