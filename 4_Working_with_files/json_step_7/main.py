import json

actions = {
    str: lambda x: x + "!",
    int: lambda x: x + 1,
    bool: lambda x: not x,
    list: lambda x: x + x,
    dict: lambda x: x.update({"newkey": None}) or x
}

with open('data.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)
    data_dict = [actions[type(i)](i) for i in data if i != None]

with open('updated_data.json', mode='w', encoding='utf-8') as save_file:
    json.dump(data_dict, save_file, indent='   ')
