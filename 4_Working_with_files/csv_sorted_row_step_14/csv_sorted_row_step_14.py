import csv


with open(file='deniro.csv', mode='r', encoding='utf-8') as deniro:
    data = csv.reader(deniro)

    input_user_row = int(input()) - 1

    sort_iterable = sorted(data, key=lambda row: int(row[input_user_row]) if row[input_user_row].isdigit() else row[input_user_row])

    for rows in sort_iterable:
        print(','.join(rows))

