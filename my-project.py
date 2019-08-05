import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

import pdb
import time


class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Yutyp\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.delete_all_cookies()

    def test_language(self):
        self.driver.get('https://www.google.com/')
        language = self.driver.find_elements_by_css_selector('#SIvCob > a:nth-child(1)')
        text1 = language[0].text
        language[0].click()
        language = self.driver.find_elements_by_css_selector('#SIvCob > a:nth-child(1)')
        text2 = language[0].text
        self.assertNotEqual(text2, text1)

    def test_city(self):
        self.driver.get('https://www.google.com/maps')
        search = self.driver.find_elements_by_css_selector('#searchboxinput')
        search[0].send_keys('Em Hamoshavot Road, בני ברק')
        from selenium.webdriver.common.keys import Keys
        search[0].send_keys(Keys.ENTER);
        city = self.driver.find_elements_by_css_selector('h2 span[dir="ltr"]')
        name = city[0].text
        self.assertEqual('Em Hamoshavot Road', name)

if __name__ == '__main__':
    unittest.main()
