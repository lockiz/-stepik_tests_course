import json
import csv
from datetime import datetime

with open('exam_results.csv', mode='r', encoding='UTF-8') as csv_file:
    rows = sorted(list(csv.DictReader(csv_file)), key=lambda x: datetime.strptime(x['date_and_time'], '%Y-%m-%d \
    %H:%M:%S'))

    temp = {}
    for row in rows:
        print(row['email'])
        print(sorted(rows, key=lambda x: x['email'] == row['email']))
        break


# with open('best_scores.json', mode='w', encoding='UTF-8') as save_file:
#     json.dump(sorted(list(temp.values()), key=lambda x: x['email']), save_file, indent=3)
