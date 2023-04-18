import json


with open('food_services.json', mode='r', encoding='UTF-8') as json_file:
    rows = sorted(list(json.load(json_file)), key=lambda x: int(x['SeatsCount']))
    result = {}
    for row in rows:
        result[row['TypeObject']] = {
            'name': row['Name'],
            'SeatsCount': str(row['SeatsCount'])
        }

    for key, val in sorted(result.items()):
        print(key, ', '.join(list(val.values())), sep=': ')
