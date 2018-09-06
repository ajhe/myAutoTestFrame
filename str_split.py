# coding=utf-8

from selenium import webdriver
import time

class StrSplit(object):
    """
    这是一个字符串切割的列子类
    """
    def get_search_result(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

        driver.get("https://www.baidu.com")
        time.sleep(2)
        driver.find_element_by_id('kw').send_keys("selenium")
        driver.find_element_by_id('su').click()
        print driver.current_url
        time.sleep(2)
        result_str = driver.find_element_by_xpath("//*/div[@class='nums']").text
        print result_str

        result_str_split1 = result_str.split(u'约')[1]               #这里中文记得加上U，表示Unicode编码
        finall_result = result_str_split1.split(u'个')[0]

        print finall_result
        driver.quit()


strSplit = StrSplit()
strSplit.get_search_result()