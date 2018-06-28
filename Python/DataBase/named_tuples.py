# -*-coding:utf-8-*-
"""定义必需的名称元组"""

import collections

# 用于MySQL的服务信息
MySQL = collections.namedtuple('MySQL', ['host', 'user', 'password', 'port', 'charset', 'schema'])
