# coding=utf-8

import logging
import os.path
import time

'''
class Logger(object):
    """
    保存日志的类
    """

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件将
            日志存入指定的文件中
        :param logger:
        :return None:
        """

        #创建一个logger
        self.logger  = logging.getLogger(logger)    #实例化一个logger
        self.logger.setLevel(logging.DEBUG)         #定义日志级别

        #创建一个handler,用于写入日志文件
        rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))    #获取当前时间，以201809051831的格式
        log_path = os.path.dirname(os.getcwd()) + "/Logs/"             #获取当前Logs文件夹路径
        log_name = log_path + rq + '.log'                             #log文件路径
        fh = logging.FileHandler(log_name)                           #建立一个log文件
        fh.setLevel(logging.INFO)                                    #定义级别

        #再创建一个handler，用于输出控制台
        ch = logging.StreamHandler()                                #实例化一个控制台输出的handler
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger
'''
class TestLogger(object):
    """
    默写
    """

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = root_path + '/Logs/'
        now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        log_file_path = log_path + now_time + '.log'
        fileHandler = logging.FileHandler(log_file_path)
        fileHandler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fileHandler.setFormatter(formatter)

        controlHandler = logging.StreamHandler()
        controlHandler.setLevel(logging.INFO)
        controlHandler.setFormatter(formatter)

        self.logger.addHandler(fileHandler)
        self.logger.addHandler(controlHandler)

    def getlogger(self):
        return self.logger


