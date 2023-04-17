import csv
import json

with open('playgrounds.csv', mode='r', encoding='utf-8') as file:
    data_csv, temp = csv.DictReader(file, delimiter=';'), {}
    for row in data_csv:
        temp.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

with open('addresses.json', mode='w', encoding='utf-8') as save_file:
    json.dump(temp, save_file, indent='   ', ensure_ascii=False)

