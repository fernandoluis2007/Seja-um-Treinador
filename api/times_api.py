#Fazer importação/consumir os dados dos times da API do Football_data.

import requests
import json

# Importar a função base request para consumir API.
from resquest_football_data import request_api, chamar_api_key

'''
api_token= chamar_api_key()
dados = request_api(api_token, 'competitions/WC/teams', False)
'''

# Função ler o arquivo .json -> e armazenar os times lidos dentro de uma lista:
def puxar_nome_times(pasta, arquivo): # O parâmetro é o nome do arquvio /-> ex: PL, WC, SA...
    nome_pasta = pasta
    nome_liga = arquivo
    lista_completa_times_liga = []

    with open(f'../data/competitions/{nome_pasta}/{nome_liga}.json', 'r', encoding='utf-8') as file:
        lista_times = json.load(file)
        try:
            for x in lista_times["teams"]: # Chave de acesso: ["teams"].
                lista_completa_times_liga.append(x["name"])
        except KeyError: # Quando tenta acessar uma chave inexistente em um dicionário.
            print("A chave 'teams' não existe no arquivo!")

    return lista_completa_times_liga

    

times_brasileirao = puxar_nome_times("BSA","teams")
times_bundelisga = puxar_nome_times("BL1", "teams")
times_champions_league = puxar_nome_times("CL", "teams")
times_eredivisie = puxar_nome_times("DED", "teams")
times_european_championship = puxar_nome_times("EC", "teams")
times_championship = puxar_nome_times("EC", "teams")
times_francesa = puxar_nome_times("FL1", "teams")
times_espanhola = puxar_nome_times("PD", "teams")
times_premier_league = puxar_nome_times("PL", "teams")
times_portuguesa = puxar_nome_times("PPL", "teams")
times_italiana = puxar_nome_times("SA", "teams")
selecoes = puxar_nome_times("WC", "teams")

print(times_brasileirao)
print(selecoes)


