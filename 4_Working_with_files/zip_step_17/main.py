from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip', mode='r') as zip_file:
    t = datetime.strptime('2021-11-30 14:22:00', '%Y-%m-%d %H:%M:%S')
    for file in sorted(list(zip_file.infolist()), key=lambda x: x.filename.split('/')[-1]):
        if (not file.is_dir()) and (datetime(*file.date_time) >= t):
            print(file.filename.split('/')[-1])
