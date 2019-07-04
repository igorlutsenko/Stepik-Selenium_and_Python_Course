import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


URL = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(URL)

book = driver.find_element_by_id("book")

value = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
book.click()

val = driver.find_element_by_id("input_value").text
form = driver.find_element_by_id("answer")
btn = driver.find_element_by_id("solve")

form.send_keys(calc(val))
btn.click()

