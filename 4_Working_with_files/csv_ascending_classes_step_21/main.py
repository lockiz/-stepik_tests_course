import csv

with open('student_counts.csv',  mode='r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    data_list = list(data)
    sort_column = sorted(data.fieldnames[1:], key=lambda item: (int(item.split('-')[0]), item.split('-')[1]))
    sort_column = ['year'] + sort_column


with open('sorted_student_counts.csv',  mode='w', encoding='utf-8') as save_file:
    writer = csv.DictWriter(save_file, fieldnames=sort_column, delimiter=',')
    writer.writeheader()
    writer.writerows(data_list)
