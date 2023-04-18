from zipfile import ZipFile


with ZipFile('workbook.zip', mode='r') as zip_file:
    original, compress = 0, 0
    for i in zip_file.infolist():
        original += i.file_size
        compress += i.compress_size

    print(f'Объем исходных файлов: {original} байт(а)')
    print(f'Объем сжатых файлов: {compress} байт(а)')
