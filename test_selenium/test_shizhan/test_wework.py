"""
__author__ = 'karen'
__time__ = '2021/7/13 下午4:37'
"""
from time import sleep

import yaml
from selenium import webdriver


class TestWeWork:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)

    def test_cookie(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        print(self.driver.get_cookies())
        with open('cookies.yml', 'w', encoding='UTF-8') as f:
            yaml.dump(self.driver.get_cookies(), f)

        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?')
        with open('cookies.yml', encoding='utf-8') as f:
            cookies =  yaml.safe_load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
