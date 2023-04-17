import json

with open('people.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    keys = list(max(data, key=lambda x: len(x)).keys())
    temp = []
    for row in data:
        for i in keys:
            row.setdefault(i, None)
        temp.append(row)

with open('updated_people.json', mode='w', encoding='utf-8') as save_file:
    json.dump(temp, save_file, indent='   ', sort_keys=True)

