"""
__author__ = 'karen'
__time__ = '2021/7/13 下午1:48'
"""
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_form(self):
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys('user')
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys('password')
        self.driver.find_element_by_xpath('//*[@class="custom-control-label"]').click()
        self.driver.find_element_by_xpath('//input[@value="登录"]').click()
        sleep(3)

    def teardown(self):
        self.driver.quit()