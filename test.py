# from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
# client = PIWebApiClient("https://ucd-pi-iis.ou.ad3.ucdavis.edu/piwebapi", useKerberos=False, username="username", password="password", verifySsl=True)
# print(client)

import csv
from datetime import datetime as dt

days = [0] * 7
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
with open('wifisample.csv') as samplefile:
    sample = csv.reader(samplefile)
    for row in sample:
        items = {}
        for label,col in zip(collabels,row):
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
        days[dayofweek] += items['Total_Count']

weekdays = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun'
]

for weekday,day in zip(weekdays,days):
    print(f'{weekday}: {day}')