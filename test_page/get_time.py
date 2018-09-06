# coding=utf-8

import time

class GetTime(object):
    """
    获取当前时间的类
    """

    def get_system_time(self):
        print (time.time())               #time.time()获取从1970年到现在的时间间隔，单位为秒
        print (time.localtime())          #当前时间
        new_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        print new_time

getTime = GetTime()
getTime.get_system_time()