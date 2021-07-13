"""
__author__ = 'karen'
__time__ = '2021/7/12 下午4:54'
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        # 隐式等待
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="有新帖的话题"]').click()
        # 强制等待
        # time.sleep(3)

        # 显示等待
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]'))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()

    def teardown(self):
        self.driver.quit()