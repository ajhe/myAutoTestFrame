# coding=utf-8


from test_page.browser_engine import BrowserEngine

class TestBrowserEngine(object):

    def open_browser(self):
        browserengine = BrowserEngine(self)
        driver = browserengine.get_browser()
        print browserengine.browser_type

tbe = TestBrowserEngine()
tbe.open_browser()
