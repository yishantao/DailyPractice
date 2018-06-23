# -*-coding:utf-8 -*-

"""This module is used to upload data"""

import pandas as pd

from twisted.internet import reactor
from twisted.enterprise import adbapi


def read_excel(file_path):
    file_data = pd.read_excel(file_path)
    return file_data


def connect_database(db='test', host='localhost', user='root', passwd='777888'):
    db_pool = adbapi.ConnectionPool('pymysql', host=host, db=db, user=user, passwd=passwd, charset='utf8')
    return db_pool


def create_table(tx):
    sql = '''
            CREATE TABLE IF NOT EXISTS student  
            (
            ID INT PRIMARY KEY AUTO_INCREMENT,
            S_NUM VARCHAR (30) NOT NULL
            )DEFAULT CHARSET=utf8;
          '''
    tx.execute(sql)


def insert_table(tx, series):
    for i in range(len(series)):
        item = series[i]
        values = (
            item,
        )
        sql = "REPLACE INTO student(S_NUM) VALUES(%s)"
        tx.execute(sql, values)


if __name__ == '__main__':
    database_pool = connect_database()
    database_pool.runInteraction(create_table)

    data = read_excel('student_num.xlsx')
    database_pool.runInteraction(insert_table, data['S_NUM'])
    # 使用reactor.callLater函数定时执行函数，第一个参数为等待的秒数，第二个参数为需要调用的函数
    # reactor.callLater(2, reactor.stop)
    # reactor.run()

"""说明：其实可以不用这么写，我写的时候考虑数据量庞大的话可以使用多线程机制；虽然在Python中多线程机制有点鸡肋，
但Twisted提供了以异步方式多线程访问数据库的模块adbapi，我觉得使用该模块可以显著提高程序访问数据库的效率；
数据数据量很小的话，建议把多线程机制去除。
第一次运行没数据；第二次运行才有数据；好久没用了，机制都搞不清了，吃完饭改"""
