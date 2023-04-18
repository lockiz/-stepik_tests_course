from zipfile import ZipFile


with ZipFile('test.zip') as zip_file:
    info = zip_file.namelist()
    print(info)

