# Biblotecas para requisasão
import requests
import json
import os

# 
from functools import lru_cache
from collections import Counter

# Importando a função de resgatar o valor da key de acesso.
from resquest_football_data import chamar_api_key
api_token_key = chamar_api_key()


# @lru_cache -> Memoriza o resultado de uma função com base nos argumentos.
@lru_cache(maxsize=128) # Pode guardar até 128 chamadas diferentes.
def buscar_dados_jogador(id_jogador: int):
    url = f"http://api.football-data.org/v4/persons/{id_jogador}/matches"

    # Informações de autenticação
    headers = {
        "X-Auth-Token" : api_token_key
    }

    params = {
        "limit" : 38, # Buscar nas últimas 38 partidas do jogador
        "withStats" : "True" # Com os status da partida
    }

    try:
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            dados = r.json()
            print(json.dumps(dados, indent=2))

            vitorias = 0
            derrotas = 0
            empate = 0
            time_do_jogador = vereficar_time_jogador(dados)
            
            for jogos in dados["matches"]:
                resultado_jogo = jogos["score"]["winner"]
                casa = jogos["homeTeam"]["name"]
                visitante = jogos["awayTeam"]["name"]

                if time_do_jogador in [casa, visitante]:
                    if resultado_jogo == "DRAW":
                        empate += 1
                    elif (resultado_jogo == "AWAY_TEAM" and visitante == time_do_jogador) or (resultado_jogo == "HOME_TEAM" and casa == time_do_jogador):
                        vitorias += 1
                    else:
                        derrotas += 1 

            print(f"\nTime identificado: {time_do_jogador}")
            print(f"Vitórias: {vitorias}, Empates: {empate}, Derrotas: {derrotas}")
        else:
            print(f"Erro.")
            return dados

    except requests.RequestException as e:
        print(f"Falha na Requesitação: {e}")
        return {}



def vereficar_time_jogador(data):
    contagem_times = Counter()

    for jogo in data["matches"]:
        casa = jogo["homeTeam"]["name"]
        visitante = jogo["awayTeam"]["name"]
        contagem_times[casa] += 1
        contagem_times[visitante] += 1

    time_mais_frequente = contagem_times.most_common(1)[0][0]
    return time_mais_frequente

jogador_vitor_roque = buscar_dados_jogador(181439)