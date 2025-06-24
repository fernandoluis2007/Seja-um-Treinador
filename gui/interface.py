from tkinter import *
import tkinter as tk
from tkinter.ttk import * # Conjunto de widgets temáticos do Tk.


def fechar_janela(janela):
    janela.destroy()


def interface_grafica():

    janela = Tk()
    janela.geometry("400x250") # Tamanho da janela.
    janela.title("Simulador Treinador") # Título da janela.

    label = tk.Label(janela, text="Bem vindo ao Simulador de treinador!")
    label.grid(column=0, row=0)

    botao_sair = tk.Button(janela, text="Sair", command=lambda: fechar_janela(janela))
    # Função anônima que só será executada quando o botão for clicado.
    botao_sair.grid(column=0, row=1)


    janela.mainloop()
    '''
    # Interfaçe Gráfica ->
    janela = Tk()
    janela.title("Dados do Técnico")

    # Widgets
    janela.

    janela.mainloop()
    
    '''