# -*- coding=utf-8 -*-
import datetime


def date_range(begin_date, end_date):
    dates = []
    dt = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    date = begin_date[:]
    while date <= end_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def week_range(begin_date, end_date):
    week = set()
    for date in date_range(begin_date, end_date):
        week.add(datetime.date(int(date[0:4]), int(date[5:7]), int(date[8:10])).isocalendar()[0:2])

    week_list = []
    for year_week in sorted(list(week)):
        week_list.append(str(year_week[0]) + '#' + str(year_week[1]))
    return week_list


if __name__ == '__main__':
    for week in week_range('2016-10-01', '2017-01-01'):
        print(week)
