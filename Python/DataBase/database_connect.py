# -*- coding:utf-8 -*-
import pymysql


def db_connect():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "777888", "test")
    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    # 使用execute()方法执行SQL查询
    cursor.execute('SELECT VERSION()')
    # 使用fetchone()方法获取单条数据
    data = cursor.fetchone()
    print(data)
    db.close()


def create_table():
    db = pymysql.connect("localhost", "root", "777888", "test")
    cursor = db.cursor()
    # 使用execute方法执行SQL，如果表存在就删除
    cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(20) NOT NULL,
    AGE INT,
    SEX CHAR(1),
    CREATE_TIME DATETIME)
    """
    try:
        cursor.execute(sql)
        print('CREATE TABLE SUCCESS.')
    except Exception as e:
        print('CREATE TABLE FAILED,CASE:%s' % e)
    finally:
        # 关闭数据库连接
        db.close()


import datetime


def insert_record():
    db = pymysql.connect("localhost", "root", "777888", "test")
    cursor = db.cursor()
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME,AGE,SEX,CREATE_TIME)VALUES('%s',%d,'%c','%s')" % (
        'xiao', 22, 'M', datetime.datetime.now())
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        print('INSERT INTO MySQL FAILED,CASE:%s' % e)
        # 如果发生错误就回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


def query_data():
    db = pymysql.connect("localhost", "root", "777888", "test")
    cursor = db.cursor()
    sql = "SELECT * FROM EMPLOYEE WHERE AGE>%d" % 15
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            first_name = row[0]
            age = row[1]
            print(first_name, age)
    except Exception as e:
        print('ERROR,CASE:%s' % e)
    finally:
        # 关闭数据库连接
        db.close()


def update_data():
    db = pymysql.connect("localhost", "root", "777888", "test")
    cursor = db.cursor()
    sql = "UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%s'" % 'M'
    try:
        cursor.execute(sql)
        db.commit()
        print('UPDATE SUCCESS!')
    except Exception as e:
        print('ERROR,CASE:%s' % e)
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


def delete_record():
    db = pymysql.connect("localhost", "root", "777888", "test")
    cursor = db.cursor()
    sql = "DELETE FROM EMPLOYEE WHERE AGE>%d" % 23
    try:
        cursor.execute(sql)
        db.commit()
        print('DELETE SUCCESS!')
    except Exception as e:
        print('ERROR,CASE:%s' % e)
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


delete_record()
