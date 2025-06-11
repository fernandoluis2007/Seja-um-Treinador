#Fazer importação/consumir os dados dos times da API do Football_data.

import requests
import json

# Importar a função base request para consumir API.
from resquest_football_data import request_api, chamar_api_key

api_token= chamar_api_key()
dados = request_api(api_token, 'teams/')