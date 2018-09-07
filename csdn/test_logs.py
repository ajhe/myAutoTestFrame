# coding=utf-8

import time
from selenium import webdriver
#from test_page.logger import Logger
from test_page.logger import TestLogger

#mylogger = Logger(logger='TestMyLog').getlog()
mylogger = TestLogger(logger='MyTestLogger').getlogger()

class TestMyLog(object):

    def print_log(self):

        driver = webdriver.Firefox()
        mylogger.info(u"打开浏览器")
        #driver.maximize_window()
        #mylogger.debug(u"最大化浏览器异常")
        driver.implicitly_wait(10)

        driver.get("https://www.baidu.com")
        mylogger.info(u"打开百度首页")
        time.sleep(2)
        mylogger.info(u"暂停2秒")
        driver.quit()
        mylogger.info(u"关闭并退出浏览器")


testlog = TestMyLog()
testlog.print_log()