"""
__author__ = 'karen'
__time__ = '2021/7/13 上午10:13'
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_click(self):
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        elemennet_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        elemennet_double_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        elemennet_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(elemennet_click)
        action.double_click(elemennet_double_click)
        action.context_click(elemennet_right_click)
        action.perform()

    def test_moveto(self):
        self.driver.get('https://www.baidu.com')
        elem = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(elem)
        action.perform()
        time.sleep(3)

    def test_drag_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        drag_elem = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        drop_elem = self.driver.find_element_by_xpath('//*[@class="item"][1]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_elem, drop_elem)
        action.perform()

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys('tom').pause(2)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()
