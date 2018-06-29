import json,copy
from pprint import pprint

json_marcas = {}

with open('../static/json/master.json') as f:
    data = json.load(f)


for car in data:
    json_marcas[car['marca']] = {}

count = 0

json_final = copy.deepcopy(json_marcas)

for car in data:
    if car['marca'] in json_marcas.keys():
        json_marcas[car['marca']][count] = {'modelo':car['modelo'],'anomodelo':car['anomodelo'],'combustivel':car['combustivel'],'tipoveiculo':car['tipoveiculo'],'valor':car['valor'].split(" ")[1]}
        count += 1


modelo = ""
count2 = 0
for carro in json_marcas:
    for key,id in json_marcas[carro].items():
        if modelo != id['modelo']:
            anos = {}
            valores = {}
            modelo = id['modelo']
            count2 = 0

        if modelo != "":
            anos[count2] = id ['anomodelo']
            valores[count2] = id['valor']
            count2 += 1

        json_final[carro][modelo] = {'anomodelo':anos,'combustivel':id['combustivel'],'tipoveiculo':id['tipoveiculo'],'valor':valores}




json_data = json.dumps(json_final)

arq = open('../static/json/car_master_resumed.json', 'w')
arq.write(json_data)
arq.close()