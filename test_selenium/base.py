"""
__author__ = 'karen'
__time__ = '2021/7/13 下午2:12'
"""
import os
import sys
from time import sleep

from selenium import webdriver


class Base():
    def setup(self):
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Safari()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        sleep(2)
        self.driver.quit()
        # pass