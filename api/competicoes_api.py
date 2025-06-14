#Fazer importação/consumir os dados da competição da API do Football_data.

import requests
import json

# Importar a função base request para consumir API.
from resquest_football_data import request_api, chamar_api_key

api_token= chamar_api_key()
# dados = request_api(api_token, 'competitions')

def obter_times_da_liga(api_token, liga, salvar_em=False):
    url_competitions = 'competitions'
    times_da_liga = request_api(api_token, f'{url_competitions}/{liga}', False)

    return times_da_liga

# chamando a função para acessar a API e consumi-lá e armazenar na pasta Data todos os .json de cada liga. 
'''
liga_world_cup = obter_times_da_liga(api_token, 'WC')
liga_champions_league = obter_times_da_liga(api_token, 'CL')
liga_aleman = obter_times_da_liga(api_token, 'BL1')
liga_horlandesa = obter_times_da_liga(api_token, 'DED')
liga_brasileira = obter_times_da_liga(api_token, 'BSA')
liga_espanhola = obter_times_da_liga(api_token, 'PD')
liga_francesa = obter_times_da_liga(api_token, 'FL1')
liga_inglesa_segunda_divisao = obter_times_da_liga(api_token, 'ELC')
liga_portuguesa = obter_times_da_liga(api_token, 'PPL')
liga_euro_copa = obter_times_da_liga(api_token, 'EC')
liga_italiana = obter_times_da_liga(api_token, 'SA')
liga_inglesa_primeira_divisao = obter_times_da_liga(api_token, 'PL')
'''







