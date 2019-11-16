# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （Jackson)
# created:  2019.11.16

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

import logging

logging. basicConfig(level=logging.DEBUG, filename='my.log',
                     format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging. getLogger(__name__)

msg = 'Debug information...'
logger.debug(msg)

msg = '调试'
logger.debug(msg)

msg = '预期'
logger.info(msg)

msg = '现在没问题'
logger. warning(msg)

msg = '严重问题'
logger. error(msg)

msg = '致命性问题'
logger. critical(msg)


def mylog(level, msg):
    if level == 'D':
        logger. debug(msg)
    elif level == 'I':
        logger. info(msg)
    return 
