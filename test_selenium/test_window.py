"""
__author__ = 'karen'
__time__ = '2021/7/13 下午2:11'
"""
import time

from testpro.test_selenium.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        # print(self.driver.window_handles)
        self.driver.switch_to_window(self.driver.window_handles[-1])

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('17783456710')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('17783456710')
        time.sleep(3)

        self.driver.switch_to_window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys('17783456710')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys('17783456710')
        time.sleep(2)
