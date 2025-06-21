from ..api.jogadores_api import buscar_dados_jogador, vereficar_time_jogador

class Jogador():
    def __init__(self, nome=str, id_jogador=int, time=str, partidas=dict | list):
        self.nome = nome
        self.id = id_jogador
        self.time = time
        self.partidas = partidas
        

    def __str__(self):
        messagem = (
            f"Nome do Jogador: {self.nome}\n"
            f"Id do jogador: {self.id}\n"
            f"Time do jogador: {self.time}"
        )
        return messagem
    
    def calcular_overall():
        buscar_dados_jogador()
    

vitor_roque = Jogador("Vitor Roque", 181439, "SE Palmeiras", None)
over_jogador = vitor_roque.calcular_overall()
print(over_jogador)

