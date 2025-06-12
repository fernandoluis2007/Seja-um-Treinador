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

liga_world_cup = obter_times_da_liga(api_token, 'WC')
liga_champions_league = obter_times_da_liga(api_token, 'CL')







