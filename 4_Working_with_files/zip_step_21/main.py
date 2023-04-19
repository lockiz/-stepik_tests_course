from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name, mode='r') as zip_file:
        if len(args) == 0:
            zip_file.extractall()
        else:
            for name_file in args:
                zip_file.extract(name_file)
