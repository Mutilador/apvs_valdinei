import json,copy
from pprint import pprint

json_marcas = {}

with open('../static/json/car_master_resumed.json') as f:
    data = json.load(f)

for key,marca in data.items():
    print(key)
    print(marca)
    break