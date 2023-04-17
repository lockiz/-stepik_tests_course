import json


with open('data1.json', 'r', encoding='utf-8') as file_1, open('data2.json', 'r', encoding='utf-8') as file_2:
    data_1, data_2 = json.load(file_1), json.load(file_2)
    data_1.update(data_2)

with open('data_merge.json', mode='w', encoding='utf-8') as save_file:
    json.dump(data_1, save_file, indent='   ')
