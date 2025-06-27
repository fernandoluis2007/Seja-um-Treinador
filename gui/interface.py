'''
from tkinter import *
from tkinter.ttk import * # Conjunto de widgets temáticos do Tk.
'''

import customtkinter as ctk

from gui.segundas_janelas import ToplevelWindow

# Variáveis de Cores, Funções, Caminhos e etc... ->




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inicio - Seja um Treinador")
        self.geometry("600x450") # Tamanho da janela.
        self.resizable(False, False) # Redimensionar da Página pelo usuário é cancelada.
        self.iconbitmap("gui\img\logo\Seja_Um_Treinador_Icon.ico") # Icone da janela.
        self._set_appearance_mode("system") # Defalut.
    
        # Frame do Título -->
        frame_titulo = ctk.CTkFrame(self, fg_color="transparent", )
        frame_titulo.pack(fill="x", pady=10)


        titulo_frame = ctk.CTkLabel(frame_titulo, text="Bem vindo ao Simulador de treinador!")
        titulo_frame.pack(pady= 10)

        # Frame dos Botões -->
        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(fill="both", expand=True, pady=40) # fill="both", O frame dos botões se expande na vertical e horizontal.
                                                    # expand=True, Permite que ele ocupe o espaço extra da janela.


        botao_iniciar = ctk.CTkButton(frame_botoes, text="Iniciar", command="", anchor="center")
        botao_iniciar.pack(pady=20)

        botao_config = ctk.CTkButton(frame_botoes, text="Configurações", command=self.configuracoes_programa, anchor="center")
        botao_config.pack(pady=20)

        botao_sair = ctk.CTkButton(frame_botoes, text="Sair", command=lambda:finalizar_programa(self), anchor="center")
        botao_sair.pack(pady=20)

        def finalizar_programa(self):
            self.destroy()
        
    def configuracoes_programa(self):
        ToplevelWindow(self)



'''
def fechar_janela(janela):
    janela.destroy()


def interface_grafica():

    janela = ctk.CTk()
    janela.geometry("600x450") # Tamanho da janela.
    janela.title("Simulador Treinador") # Título da janela.
    janela.resizable(True, True)
    janela.grid_columnconfigure(0, weight=1)


    label = ctk.CTkLabel(janela, text="Bem vindo ao Simulador de treinador!")
    label.grid(column=0, row=0, padx=20, pady=20)

    botao_iniciar = ctk.CTkButton(janela, text="Iniciar")
    botao_iniciar.grid(column=0, row=1, padx=20, pady=20)

    botao_config = ctk.CTkButton(janela, text="Configurações")
    botao_config.grid(column=0, row=2, padx=20, pady=20)

    botao_sair = ctk.CTkButton(janela, text="Sair", command=lambda: fechar_janela(janela))
    # Função anônima que só será executada quando o botão for clicado.
    botao_sair.grid(column=0, row=3, padx=20, pady=20)



    janela.mainloop()

def janela_config():
    pass
    
'''