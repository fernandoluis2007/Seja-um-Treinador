import requests
import json

from tkinter import*

# Teste ->
from api.jogadores_api import buscar_dados_jogador, calcular_over_jogador
from models.jogador import Jogador
from gui.interface import App

# Busca os dados e estatísticas do jogador
dados, vitorias, derrotas, empates, time = buscar_dados_jogador(181439)

# Uma instância de Jogador
jogador_vitor_roque = Jogador("Vitor Roque", 181439, time, dados)

overall = calcular_over_jogador(vitorias, derrotas, empates)

if __name__ == "__main__":
    app = App()
    app.mainloop()