import os

# 封装资源路径前缀
import logging
import logging.handlers
import time

BASE_URL = "http://182.92.81.159/api/sys/"

# 获取项目绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))


def my_log_config():
    # 2.
    # 获取日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 3.
    # 设置日志处理器(控制输出目标)
    to1 = logging.StreamHandler()  # 默认控制台
    filename = PRO_PATH + "/log/myAuto" + time.strftime("%Y%m%d%H%M%S") + ".log"
    to2 = logging.handlers.TimedRotatingFileHandler(filename=filename, when="h", interval=10, backupCount=20,
                                                    encoding="utf-8")
    # 4.
    # 设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 5.
    # 组织上述对象
    to1.setFormatter(formatter)
    to2.setFormatter(formatter)
    logger.addHandler(to1)
    logger.addHandler(to2)


TOKEN = None
