from zipfile import ZipFile


with ZipFile('workbook.zip', mode='r') as zip_file:
    files_compress = list()

    for file in zip_file.infolist():
        if not file.is_dir():
            files_compress.append((file.filename.split('/')[-1], (file.compress_size / file.file_size) * 100))

    print(min(files_compress, key=lambda file_info: file_info[1])[0])
