from zipfile import ZipFile
from datetime import datetime


with ZipFile('workbook.zip', mode='r') as zip_file:
    data = sorted(zip_file.infolist(), key=lambda x: x.filename.split('/')[-1])

    for file in data:
        if not file.is_dir():
            print(file.filename.split('/')[-1])
            print(f"  Дата модификации файла: {str(datetime(*file.date_time))}")
            print(f"  Объем исходного файла: {file.file_size} байт(а)")
            print(f"  Объем сжатого файла: {file.compress_size} байт(а)")
            print()
