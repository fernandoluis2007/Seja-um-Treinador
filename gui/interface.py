'''
from tkinter import *
from tkinter.ttk import * # Conjunto de widgets temáticos do Tk.
'''

import customtkinter as ctk

def fechar_janela(janela):
    janela.destroy()


def interface_grafica():

    janela = ctk.CTk()
    janela.geometry("600x450") # Tamanho da janela.
    janela.title("Simulador Treinador") # Título da janela.
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
    '''
    # Interfaçe Gráfica ->
    janela = Tk()
    janela.title("Dados do Técnico")

    # Widgets
    janela.

    janela.mainloop()
    
    '''