from selenium import webdriver
import unittest
import time 
browser = webdriver.Chrome()
class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element_by_xpath('//div/input[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//div/input[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('//div/input[@placeholder="Input your email"]')
        input3.send_keys("88005553535")
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration 1 fail")
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        input1 = browser.find_element_by_xpath('//div/input[@placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath('//div/input[@placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath('//div/input[@placeholder="Input your email"]')
        input3.send_keys("88005553535")
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration 2 fail")
        time.sleep(5)
        browser.quit()
if __name__ == "__main__":
    unittest.main()
