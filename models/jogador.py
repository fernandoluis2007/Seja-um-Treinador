
class Jogador():
    def __init__(self, nome=str, id_jogador=int, time=str, partidas=dict | list, overall= None):
        self.nome = nome
        self.id = id_jogador
        self.time = time
        self.partidas = partidas
        self.overall = None


    def __str__(self):
        messagem = (
            f"Nome do Jogador: {self.nome}\n"
            f"Id do jogador: {self.id}\n"
            f"Time do jogador: {self.time}\n"
            f"Overall do jogador: {self.overall}"
        )
        return messagem


vitor_roque = Jogador("Vitor Roque", 181439, "SE Palmeiras", None)

