# from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
# client = PIWebApiClient("https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi", useKerberos=False, username="username", password="password", verifySsl=True)
# print(client)

import csv
from datetime import datetime as dt

collabels = [
    'Num',
    'UFL',
    'TimeStamp',
    'Year',
    'Month',
    'Day',
    'Hour',
    'Minute',
    'Wifi Access Points',
    'UFL Building',
    'Total_Count',
    'SomeNum',
    'Zero'
]
weekdays = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun'
]
def plabel(labels, data):
    for label,d in zip(labels,data):
        print(f'{label} : {d:,}')

import sys
import itertools as it
days = [0] * 7
hours = [0] * 24
minutes = [0] * 6
for counter in it.count(1):
    if counter % 10000 == 0:
        print(f'Checked {counter} lines.   ', end='\r')
    row = sys.stdin.readline()
    if not row:
        break
    items = {}
    for label,col in zip(collabels,row.split(',')):
        try:
            items[label] = int(col)
        except ValueError:
            items[label] = col
    rowtime = dt(
        items['Year'],
        items['Month'],
        items['Day'],
        items['Hour'],
        items['Minute'],
    )
    dayofweek = rowtime.weekday()
    hour = rowtime.hour
    minute = rowtime.minute // 10
    total = items['Total_Count']
    days[dayofweek] += total
    hours[hour] += total
    minutes[minute] += total

print(f'Checked {counter} lines.')

plabel(weekdays, days)
print()
plabel([f'{n}:00' for n in range(24)], hours)
print()
plabel([f'0:{n}0' for n in range(6)], minutes)
