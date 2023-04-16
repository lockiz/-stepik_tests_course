import csv


def condense_csv(filename, id_name):
    with open(file=filename, mode='r', encoding='utf-8') as file:
        temp = {}
        for object_id, property_obj, value_obj in csv.reader(file):
            if object_id not in temp:
                temp[object_id] = {id_name: object_id, property_obj: value_obj}
            else:
                temp[object_id][property_obj] = value_obj

    with open('condensed.csv', mode='w', encoding='utf-8') as save_file:
        writer = csv.DictWriter(save_file, fieldnames=temp[object_id].keys(), delimiter=',')
        writer.writeheader()
        for key, val in temp.items():
            writer.writerow(val)


condense_csv('file.csv', id_name='ID')
