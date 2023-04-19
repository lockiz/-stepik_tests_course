from zipfile import ZipFile
import json


def is_correct_json(file_json):
    try:
        return json.load(file_json)
    except (json.decoder.JSONDecodeError, UnicodeDecodeError):
        return False


with ZipFile('data.zip', mode='r') as zip_file:
    result = []
    for name_file in zip_file.infolist():
        if name_file.filename.split('.')[-1] == 'json':
            with zip_file.open(name_file, mode='r') as file:
                data = is_correct_json(file)
                if data and data['team'] == 'Arsenal':
                    result.append(f"{data['first_name']} {data['last_name']}")

    print(*sorted(result), sep='\n')
