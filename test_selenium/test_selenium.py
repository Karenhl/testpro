"""
__author__ = 'karen'
__time__ = '2021/7/12 下午3:19'
"""

import selenium
from selenium import webdriver


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    # driver.close()

