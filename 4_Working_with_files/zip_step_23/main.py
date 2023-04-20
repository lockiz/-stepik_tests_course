from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size == 0:
        return ''
    if size < 1000:
        return f' {size} B'
    elif 1000 <= size < 1000000:
        return f' {round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f' {round(size / 1048576)} MB'
    else:
        return f' {round(size / 1073741824)} GB'


with ZipFile('Desktop.zip', mode='r') as zip_file:
    for file in zip_file.namelist():
        row = [c for c in file.split('/') if c]
        indent = ((len(row) - 1) * 2)
        print(f"{' ' * indent}{row[-1]}{convert_bytes(zip_file.getinfo(file).file_size)}")

