"""
__author__ = 'karen'
__time__ = '2021/7/13 下午2:28'
"""
from time import sleep

from selenium.webdriver import ActionChains

from testpro.test_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        ele1 = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        ele2 = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele1, ele2).perform()
        sleep(3)
        self.driver.switch_to_alert().accept()
        sleep(3)
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()

