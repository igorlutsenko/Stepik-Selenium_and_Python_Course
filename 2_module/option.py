from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

URL = 'http://suninjuly.github.io/selects1.html'

driver = webdriver.Chrome()
driver.get(URL)

num1 = driver.find_element_by_id("num1").text
num2 = driver.find_element_by_id("num2").text
result = int(num1) + int(num2)

select = Select(driver.find_element_by_tag_name("select"))
select.select_by_visible_text(str(result))
sleep(2)

button = driver.find_element_by_xpath("//button[text()='Отправить']")
button.click()
sleep(6)
driver.quit()