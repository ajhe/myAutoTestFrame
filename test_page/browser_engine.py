# coding=utf-8

from selenium import webdriver
from random import randint

class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根本浏览器类型控制启动不同的浏览器
    """
    def __init__(self,driver):
        """
        定义构造函数
        :param driver:
        """
        self.driver = driver
    browser_list = ['Firefox', 'Chrome']
    browser_type = browser_list[randint(0,1)]

    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Firefox
        :return driver:
        """
        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'Chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(10)

        return driver
