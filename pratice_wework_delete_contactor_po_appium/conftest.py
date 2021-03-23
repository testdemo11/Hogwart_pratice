# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import logging

logger = logging.getLogger()
fh = logging.FileHandler('../report/report.log', encoding='utf-8', mode='a')
formatter = logging.Formatter('%(asctime).19s%(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.INFO)

# logging.basicConfig(level=logging.INFO,
#                     #日志格式，时间，代码所在文件夹，代码行号，日志级别名字，日志信息
#                     format='%(asctime).19s%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     #日志时间
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     #日志存放目录以及日志文件名，目录必须存在
#                     filename='../report/report.log',
#                     #打开日志方式
#                     filemode='w',
#                     )
