import csv


with open('prices.csv', mode='r', encoding='utf-8') as file:
    reader = sorted(list(csv.DictReader(file, delimiter=';')), key=lambda item: item['Магазин'], reverse=True)
    min_value = int(reader[0][list(reader[0].keys())[1]])
    for row in reader:
        for key, val in row.items():
            if val.isdigit() and (int(val) < min_value):
                min_value = int(val)

    for row in reader:
        for key, val in row.items():
            if val.isdigit() and int(val) == int(min_value):
                print(f"{key}: {row['Магазин']}")
                exit()

