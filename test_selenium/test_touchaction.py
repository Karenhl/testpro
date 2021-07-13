"""
__author__ = 'karen'
__time__ = '2021/7/13 下午1:25'
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_scrollbotoom(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        search_button = self.driver.find_element_by_xpath('//*[@id="su"]')
        touch_action = TouchActions(self.driver)
        touch_action.tap(search_button)
        touch_action.perform()
        touch_action.scroll_from_element(self.driver.find_element_by_xpath('//*[@id="kw"]'), 0, 10000).perform()
        sleep(2)

