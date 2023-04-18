import json
import csv
from datetime import datetime

with open('exam_results.csv', mode='r', encoding='UTF-8') as csv_file:
    data = sorted(list(csv.DictReader(csv_file)), key=lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d \
    %H:%M:%S'))

    temp = {}
    for row in data:
        if temp.get(row['email'], 0) == 0:
            temp[row['email']] = {
                'name': row['name'],
                'surname': row['surname'],
                'best_score': int(row['score']),
                'date_and_time': row['date_and_time'],
                'email': row['email']
            }
        else:
            if int(temp[row['email']]['best_score']) <= int(row['score']):
                temp[row['email']]['best_score'] = int(row['score'])
                temp[row['email']]['date_and_time'] = row['date_and_time']

with open('best_scores.json', mode='w', encoding='UTF-8') as save_file:
    json.dump(sorted(list(temp.values()), key=lambda x: x['email']), save_file, indent=3)
