# -*-coding:utf-8 -*-

"""This module is used to upload data(普通版)"""

import pymysql
import pandas as pd


def read_excel(file_path):
    """
    读取数据
    :param file_path:  string
            excel path
    :return:
    data: DataFrame
    tips: 若数据没有文件头，添加参数head=None,index_col可以指定索引列
    """
    file_data = pd.read_excel(file_path)
    return file_data


def connect_database(host='localhost', db='custom', user='root', password='root', charset='utf8'):
    """创建数据库连接，并返回连接对象"""
    conn = pymysql.connect(host=host, db=db, user=user, passwd=password, charset=charset)
    return conn


def create_table(cursor):
    """
    创建数据表，ID自增
    :param cursor: Cursor
    :return: None
    """
    sql = '''
            CREATE TABLE IF NOT EXISTS student  
            (
            S_NUM VARCHAR (30) NOT NULL,
            PRIMARY KEY (S_NUM)
            )DEFAULT CHARSET=utf8;
          '''
    cursor.execute(sql)
    conn.commit()


def insert_table(cursor, series):
    """
    插入数据
    :param cursor: Cursor
    :param series: Series
        DataFrame中的一列，这里指的是S_NUM列
    :return: None
    """
    for i in range(len(series)):
        item = series[i]
        values = (
            item,
        )
        sql = "REPLACE INTO student(S_NUM) VALUES(%s)"
        cursor.execute(sql, values)
    conn.commit()


if __name__ == '__main__':
    db_settings = {
        'host': 'localhost',
        'db': 'test',
        'user': 'root',
        'password': '777888',
        'charset': 'utf8'
    }
    conn = connect_database(**db_settings)
    cursor = conn.cursor()
    create_table(cursor)

    data = read_excel('student_num.xlsx')
    insert_table(cursor, data['S_NUM'])
    conn.close()
