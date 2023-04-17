import json
import sys


data = json.load(sys.stdin)
for key, val in data.items():
    if type(val) == list:
        print(f'{key}: {", ".join([str(i) for i in val])}')
    else:
        print(f'{key}: {val}')
