# coding=utf-8

import  time
from selenium import webdriver
from test_page.basepage import BasePage

class BaiduSearch(object):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    bp = BasePage(driver)

    def open_baidu(self):
        self.bp.open_url("https://www.baidu.com")
        time.sleep(2)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        self.bp.back()
        self.bp.forward()
        self.bp.quit_brower()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()