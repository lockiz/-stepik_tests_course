import csv


def condense_csv(filename, id_name):
    with open(file=filename, mode='r', encoding='utf-8') as file:
        data = csv.reader(file)

        temp, temp_list = {}, []
        for row in data:
            if temp.get(id_name, False) == row[0]:
                temp[row[1]] = row[2]
            else:
                if any(temp):
                    temp_list.append(temp.copy())
                    temp.clear()
                temp[id_name] = row[0]
                temp[row[1]] = row[2]
        else:
            temp_list.append(temp)

    with open('condensed.csv', mode='w', encoding='utf-8') as save_file:
        writer = csv.DictWriter(save_file, fieldnames=temp_list[0].keys(), delimiter=',')
        writer.writeheader()
        writer.writerows(temp_list)


condense_csv('file.csv', id_name='ID')