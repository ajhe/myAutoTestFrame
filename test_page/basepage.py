# coding=utf-8

class BasePage(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """
    def __init__(self,driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver

    def back(self):
        """
        浏览器后退按钮
        :return:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :return:
        """
        self.driver.forward()

    def open_url(self,url):
        """
        打开url网址
        :param url:
        :return:
        """
        self.driver.get(url)

    def quit_brower(self):
        """
        关闭并停止浏览器服务
        :return:
        """
        self.driver.quit()