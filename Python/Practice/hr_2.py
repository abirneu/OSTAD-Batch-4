import calendar as c
import datetime as d
input_date= input().split()
day = d.datetime(int(input_date[2]),int(input_date[0]), int(input_date[1]))
print(c.day_name[day.weekday()].upper())