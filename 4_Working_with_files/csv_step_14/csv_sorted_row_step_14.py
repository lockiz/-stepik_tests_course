import requests
import csv

path_file = '4_Working_with_files/csv_step_14/deniro.csv'

with open(file=path_file, mode='r', encoding='utf-8') as deniro:
    print(deniro.read())

