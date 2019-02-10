def createdata():
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
    from sys import stdin
    from datetime import datetime
    from collections import defaultdict
    buildings = defaultdict(lambda: [0] * (7 * 24 * 6))
    import itertools as it
    for counter in it.count(1):
        if counter % 10000 == 0:
            print(f'Checked {counter} lines.   ', end='\r')
        row = stdin.readline()
        if not row:
            break
        items = {}
        for label,col in zip(collabels,row.split(',')):
            try:
                items[label] = int(col)
            except ValueError:
                items[label] = col
        rowtime = datetime(
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
        build = items['UFL Building']
        buildings[build][dayofweek * 24 * 6 + hour * 6 + minute] += total

    print(f'Checked {counter} lines.')
    return dict(buildings)

import pickle
import os
try:
    with open('pkl/buildings.pkl', 'rb') as f:
        buildings = pickle.load(f)
except FileNotFoundError:
    if not os.path.exists('pkl'):
        os.mkdir('pkl')
    with open('pkl/buildings.pkl', 'wb') as f:
        buildings = createdata()
        pickle.dump(buildings, f)

def indextotime(index):
    minute = index % 6
    hour = (index // 6) % 24
    day = index // (24 * 6)
    return day, hour, minute * 10

import json

with open('data.json', 'wb') as datafile:
    json.dump(buildings, datafile)