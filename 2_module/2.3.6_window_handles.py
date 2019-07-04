from selenium import webdriver
import math
from time import sleep


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


URL = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
driver.get(URL)

btn = driver.find_element_by_tag_name("button")
btn.click()

driver.switch_to.window(driver.window_handles[1])

value = driver.find_element_by_id("input_value").text
form = driver.find_element_by_id("answer")
btn = driver.find_element_by_tag_name("button")

form.send_keys(calc(value))
btn.click()

sleep(5)

driver.quit()
