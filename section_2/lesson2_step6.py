from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin((int(x))))))
try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    browser.execute_script("window.scrollBy(0, 100);")
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    time.sleep(3)
    browser.quit()
