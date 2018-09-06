# coding=utf-8

import ConfigParser
import os
import time
from selenium import webdriver

class TestReadConfig(object):
    """
    这是一个读取配置文件的类
    """
    def get_value(self):
        """
        读取config.ini文件的值
        :return:
        """
        root_dir = os.path.dirname(os.path.abspath('.'))      #获取当前项目的根目录相对路径
        print root_dir

        config = ConfigParser.ConfigParser()
        file_path = root_dir + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        url = config.get("testServer", "URL")

        if browser == "Chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get(url)
        time.sleep(5)
        driver.quit()

        print browser,url

trc = TestReadConfig()
trc.get_value()