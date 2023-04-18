import json
from datetime import datetime, timedelta

start = datetime.strptime("10:00", '%H:%M')
temp = []

with open('pools.json', mode='r', encoding='UTF-8') as file:
    data = json.load(file)
    for row in data:
        dates = [datetime.strptime(time, '%H:%M') for time in row['WorkingHoursSummer']['Понедельник'].split('-')]
        if (dates[0] == start) and ((dates[1] - dates[0]) >= timedelta(hours=2)):
            temp.append(row)

result = max(temp, key=lambda x: [x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']])
print(f"{result['DimensionsSummer']['Length']}x{result['DimensionsSummer']['Width']}")
print(result['Address'])
