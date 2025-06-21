# API -> https://www.api-football.com/news/post/how-to-get-all-fixtures-data-from-one-league, será usada para os dados dos jogadores.

# Biblotecas para requisasão
import requests
import json
import os

# Importar do Dotenv, para usar o Token que está no .env do projeto e acessa-lá.
from dotenv import load_dotenv

# Importando a função de resgatar o valor da key de acesso.
def chamar_api_key():
    load_dotenv()
    chave_api_token = os.getenv('API_TOKEN')
    return chave_api_token

api_token_key = chamar_api_key()

url = "http://api.football-data.org/v4/persons/16271/matches"

# Informações de autenticação
headers = {
    "X-Auth-Token" : api_token_key
}

params = {
    "limit" : 2,
    "withStats" : "True"
}

r = requests.get(url, headers=headers, params=params)
dados = r.json()
print(json.dumps(dados, indent=2))


