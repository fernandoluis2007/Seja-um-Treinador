#Fazer importação/consumir os dados dos times da API do Football_data.

import requests
import json

# Importar a função base request para consumir API.
from resquest_football_data import request_api, chamar_api_key
'''

api_token= chamar_api_key()
dados = request_api(api_token, 'teams')

'''
# Ler o arquivo .json ->
with open('../data/competitions/BSA.json', 'r', encoding='utf-8') as file:
    times_brasileiro = json.load(file)
    for x in times_brasileiro["seasons"]:
        if x["winner"] != None:
            dados = x["winner"]
            for time in dados:
                print(dados["id"], dados["tla"], dados["name"])
        

#
#for time in times_brasileiro['']
#           print(f'Nome Clube: {times_brasileiro["name"]}\n Id do clube: {times_brasileiro["id"]}')
#

            




# Armazenar os arquvios lidos do .json ->
def armazenar_times_lista(id_time, nome, tla, fundado_em, estadio, endereco):
    dicionario_times_brasileiro = {
        'id': [id_time],
        'nome': [nome],
        'sigla': [tla],
        'fundado': [fundado_em],
        'estadio': [estadio],   
        'endereco': [endereco]
    }

    # f-strings, para retornar os dados do time ->
    mensagem = (
        f'Id do clube: {id_time}\n'
        f'Nome do clube: {nome}\n'
        f'Sigla do clube: {tla}\n'
        f'Clube fundado em: {fundado_em}\n'
        f'Estádio do clube: {estadio}\n'
        f'Endereço do Clube: {endereco}\n'
    )

    return mensagem