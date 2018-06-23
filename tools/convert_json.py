import json
from pprint import pprint

json_marcas = {}

with open('../static/json/master.json') as f:
    data = json.load(f)

for car in data:
    json_marcas[car['marca']] = {}


for car in data:
    if car['marca'] in json_marcas.keys():
        json_marcas[car['marca']][car['modelo']] = {'anomodelo':car['anomodelo'],'combustivel':car['combustivel'],'tipoveiculo':car['tipoveiculo'],'valor':car['valor'].split(" ")[1]}


#{'modelo': car['modelo'], 'anomodelo':car['anomodelo'],'combustivel':car['combustivel'],'tipoveiculo':car['tipoveiculo'],'valor':car['tipoveiculo']}
json_data = json.dumps(json_marcas)

arq = open('../static/json/car_master_resumed.json', 'w')
arq.write(json_data)
arq.close()