import json


with open('food_services.json', mode='r', encoding='UTF-8') as json_file:
    rows = json.load(json_file)
    areas, institution = {}, {}

    for row in rows:
        areas.setdefault(row['District'], 0)
        areas[row['District']] += 1
        if row['IsNetObject'] == 'да':
            institution.setdefault(row['OperatingCompany'], 0)
            institution[row['OperatingCompany']] += 1

print(*max(areas.items(), key=lambda x: x[1]), sep=': ')
print(*max(institution.items(), key=lambda x: x[1]), sep=': ')
