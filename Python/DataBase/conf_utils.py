# -*- coding:utf-8-*-
"""读取配置文件"""

import configparser

from named_tuples import MySQL


class ConfigReader:
    # path为配置文件的完整路径
    def __init__(self, path):
        if path is None or len(path) < 1:
            raise ValueError('The config ini file path required')
        else:
            self.conf = configparser.ConfigParser()
            self.conf.read(path)

    # 取得MySQL服务连接信息
    def get_mysql_info(self):
        host = self.conf.get('MySQL', 'host')
        user = self.conf.get('MySQL', 'user')
        pswd = self.conf.get('MySQL', 'password')
        port = self.conf.get('MySQL', 'port')
        charset = self.conf.get('MySQL', 'charset')
        schema = self.conf.get('MySQL', 'schema')
        return MySQL(host, user, pswd, int(port), charset, schema)
