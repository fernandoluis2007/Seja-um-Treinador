#Fazer importação/consumir da API do Football_data.
# arquivo base para as importações.

import requests
import json

# Importar do Dotenv, para usar o Token que está no .env do projeto e acessa-lá.
from dotenv import load_dotenv
import os


# Variável base para armazenar o link da API.
base_url = 'https://api.football-data.org/v4'

def request_api(api_token, path):

    url = f'{base_url}/{path}'

    herdears = {
        'X-Auth-Token': api_token
    }

    try:
        # Estou mandando uma requisição e me identificando com esse token autorizado.
        requesicao = requests.get(url, headers=herdears)
        if requesicao.status_code == 200:
            dados = requesicao.json()


            with open(f'data/{path}.json', 'w', encoding='utf-8') as file:
                json.dump(dados, file, indent=2, ensure_ascii=False)
                # Indenta o JSON com 2 espaços (melhora a leitura).
                # ensure_ascii=False	Permite acentos e caracteres especiais corretamente.
            
            return dados
        else:
            print(f'Erro: [{requesicao.status_code}] -> {requesicao.text}')
            return{}

    except requests.RequestException as e:
        print(f"[FALHA DE CONEXÃO] {e}")
        return{}

def chamar_api_key():
    load_dotenv()
    chave_api_token = os.getenv('API_TOKEN')
    return chave_api_token