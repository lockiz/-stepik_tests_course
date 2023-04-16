import json


def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False
