"""
__author__ = 'karen'
__time__ = '2021/7/13 下午2:40'
"""
from testpro.test_selenium.base import Base


class Test12306(Base):
    def test12306(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script('document.getElementById("train_date").removeAttribute("readonly");'
                                   'document.getElementById("train_date").setAttribute("value","2021-7-17")')
        data = self.driver.execute_script('retrun document.getElementById("train_date")')