from zipfile import ZipFile
import os

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']


with ZipFile('files.zip', mode='w') as zip_file:
    for file in file_names:
        if os.path.getsize(file) <= 100:
            zip_file.write(file)

print(os.path.getsize('files.zip'))
