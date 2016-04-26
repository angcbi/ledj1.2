# -*- coding:utf-8 -*-

import  logging
from datetime import datetime


logname = datetime.strftime(datetime.now(), '%Y%m%d') + '.log'
#
# logging.basicConfig(filename=logname,
#                     filemode='a',
#                     level=logging.DEBUG,
#                     format='[%(asctime)s] %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )


# def init():
#     log = logging.getLogger()
#     hdlr = logging.FileHandler(logname)
#     formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s %(message)s')
#     hdlr.setFormatter(formatter)
#     log.addHandler(hdlr)
#     log.setLevel(logging.DEBUG)
#     return log

