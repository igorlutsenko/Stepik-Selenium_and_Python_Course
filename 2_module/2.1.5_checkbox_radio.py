from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()
driver.get(link)

value = driver.find_element_by_id("input_value").text
print(value)
answer = calc(value)
print(answer)
field = driver.find_element_by_id("answer")

field.send_keys(answer)
time.sleep(1)

checkbox = driver.find_element_by_id("robotCheckbox")
checkbox.click()
radio = driver.find_element_by_id("robotsRule")
radio.click()
time.sleep(1)
button = driver.find_element_by_xpath("//button[text()='Отправить']")
button.click()

time.sleep(20)
driver.quit()