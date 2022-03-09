from selenium import webdriver
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

browser.find_element_by_css_selector("button.btn").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector("span#input_value.nowrap")
x = x_element.text
y = calc(x)
result = browser.find_element_by_css_selector("input#answer.form-control").send_keys(y)
browser.find_element_by_css_selector("button.btn").click()