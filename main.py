import requests
import json

# Teste ->
from api.jogadores_api import buscar_dados_jogador, calcular_over_jogador
from models.jogador import Jogador

# Busca os dados e estatísticas do jogador
dados, vitorias, derrotas, empates, time = buscar_dados_jogador(181439)

# Uma instância de Jogador
jogador_vitor_roque = Jogador("Vitor Roque", 181439, time, dados)

overall = calcular_over_jogador(vitorias, derrotas, empates)

