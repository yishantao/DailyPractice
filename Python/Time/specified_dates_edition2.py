import datetime

start = '2016-06-01'
end = '2017-01-01'

date_start = datetime.datetime.strptime(start, '%Y-%m-%d')
date_end = datetime.datetime.strptime(end, '%Y-%m-%d')

while date_start < date_end:
    date_start += datetime.timedelta(days=1)
    print(date_start.strftime('%Y-%m-%d'))
