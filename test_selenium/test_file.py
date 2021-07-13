"""
__author__ = 'karen'
__time__ = '2021/7/13 下午2:58'
"""
import time

from testpro.test_selenium.base import Base


class TestFileupload(Base):
    def test_file_upload(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="form"]/span[1]/span[2]').click()
        # self.driver.switch_to_frame()
        self.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').\
            send_keys('/Users/karen/PycharmProjects/excise2021/testpro18/testpro/test_selenium/test.png')
        time.sleep(4)