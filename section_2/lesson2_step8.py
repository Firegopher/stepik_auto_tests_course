from selenium import webdriver
import os 
import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
try:
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Пупкин')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Вася')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('1@1.1')
    current_dir = os.path.abspath(os.path.dirname('selenium_course'))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '.txt')           # добавляем к этому пути имя файла 
    file_input = browser.find_element_by_id('file')
    file_input.send_keys(file_path)
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()
finally:
    time.sleep(5)
    browser.quit()