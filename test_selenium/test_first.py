"""
__author__ = 'karen'
__time__ = '2021/7/12 下午4:28'
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, 'kw').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.ID, 'su').click()
        self.driver.find_element(By.LINK_TEXT, '霍格沃兹测试学院 - 主页').click()
        self.driver.get_screenshot_as_png()
