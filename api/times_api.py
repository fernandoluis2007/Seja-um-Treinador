#Fazer importação/consumir os dados dos times da API do Football_data.

import requests
import json

# Importar a função base request para consumir API.
from resquest_football_data import request_api, chamar_api_key

'''
api_token= chamar_api_key()
dados = request_api(api_token, 'competitions/BSA/teams', False)
'''


# Armazenar os nomes dos times, dos arquvios lidos do .json ->
lista_completa_times_br = []

# Ler o arquivo .json -> e armazenar os times lidos dentro de uma lista:
with open('../data/competitions/teams.json', 'r', encoding='utf-8') as file:
    times_brasileiro = json.load(file)
    lista_completa_times_br = []
    for x in times_brasileiro["teams"]: # Chave de acesso: ["teams"].
        lista_completa_times_br.append(x["name"])
        
print(lista_completa_times_br)
# Teste --> print(lista_completa_times_br).

# lista_completa_times_br.append(x["name"])
       
