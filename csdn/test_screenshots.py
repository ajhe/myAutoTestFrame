# coding=utf-8

from test_page.basepage import BasePage
from selenium import webdriver
import time


class TestScreenshot(object):
    """
    截图调用
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    bp = BasePage(driver)
    def get_screenshots(self):
        """
        开始截图
        :return:
        """
        self.bp.open_url("http://www.qq.com")
        time.sleep(3)
        self.bp.test_screenshot()
        self.bp.quit_brower()


myscreen = TestScreenshot()
myscreen.get_screenshots()

