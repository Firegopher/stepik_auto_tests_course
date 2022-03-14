import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

@pytest.fixture(scope = "function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.mark.parametrize('something', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepik_lesson6_test(browser, something):
    link = f'https://stepik.org/lesson/{something}/step/1'
    browser.get(link) 
    browser.find_element(By.TAG_NAME, "textarea").click()
    answer = math.log(int(time.time()))
    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    Answer = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert Answer == "Correct!", Answer

