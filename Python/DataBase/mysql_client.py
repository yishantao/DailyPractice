# -*-coding:utf-8 -*-
"""MySQL操作函数集"""

import pymysql
from conf_utils import ConfigReader


# MySQL获取数据库连接
def connect():
    cr = ConfigReader('db.ini')
    conf = cr.get_mysql_info()
    return pymysql.connections.Connection(host=conf.host, port=conf.port, user=conf.user, password=conf.password,
                                          database=conf.schema, charset=conf.charset)


connect()
