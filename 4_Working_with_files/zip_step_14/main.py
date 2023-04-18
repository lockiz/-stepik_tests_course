from zipfile import ZipFile

with ZipFile('workbook.zip', 'r') as zip_file:
    print(sum(not file.is_dir() for file in zip_file.infolist()))
