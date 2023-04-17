import csv
import json


with open('students.json', mode='r', encoding='UTF-8') as file:
    data, student = sorted(json.load(file), key=lambda x: x['name']), list()
    for row in data:
        if (int(row['age']) >= 18) and (int(row['progress']) >= 75):
            student.append({'name': row['name'],  'phone': row['phone']})

with open('data.csv', mode='w', encoding='UTF-8') as save_file:
    writer = csv.DictWriter(save_file, fieldnames=['name', 'phone'])
    writer.writeheader()
    writer.writerows(student)
