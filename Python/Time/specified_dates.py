# -*- coding=utf-8 -*-
import datetime


def date_range(begin_date, end_date):
    """
    :param begin_date:  起始日期，string
    :param end_date:    结束日期，string
    :return: dates: 指定日期范围内日期列表，元素类型string
    """
    dates = []
    dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(days=1)
        date = dt.strftime("%Y-%m-%d")
    return dates


if __name__ == '__main__':
    for date in date_range('2016-10-01', '2017-01-01'):
        print(date)
