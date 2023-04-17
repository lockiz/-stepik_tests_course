import json


with open('countries.json', mode='r', encoding='utf-8') as file:
    data, temp = json.load(file), {}
    for row in data:
        temp.setdefault(row['religion'], [])
        temp[row['religion']].append(row['country'])

with open('religion.json', mode='w', encoding='utf-8') as save_file:
    json.dump(temp, save_file, indent='   ')
