from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    x = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    y = int(num2.text)
    z = x + y
    print(z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()