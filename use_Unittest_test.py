# coding=utf-8


from selenium import webdriver
import time
import unittest

class TestUnittest(unittest.TestCase):
    """
    继承unittest,利用TestCase模块
    """

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.baidu.com")
        time.sleep(2)

    def tearDown(self):
        """
        测试固件的tearDown()的代码，主要是测试结束准备工作
        :return:
        """
        self.driver.quit()


    def test_search(self):
        """
        test开头，是测试用例，必须test开头定义函数
        :return:
        """

        self.driver.find_element_by_id('kw').send_keys("selenium")
        time.sleep(1)
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        try:
            assert "selenium" in self.driver.title
            print ("Test pass")
        except Exception as e:
            print ("Test Fail", format(e))

if __name__ == '__main__':
    unittest.main()