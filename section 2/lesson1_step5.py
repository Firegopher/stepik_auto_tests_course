from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    treasure = browser.find_element_by_id('treasure')
    x = treasure.get_attribute('valuex')
    print(x)
    y = calc(x)
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    time.sleep(3)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    time.sleep(3)
    browser.quit()