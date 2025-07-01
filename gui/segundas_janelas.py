# Criação da Classe TopLevel... -->

import customtkinter as ctk

# Importando funções -->
from gui.func import combox_tela, combox_tema, botao_sair

class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, app):
        super().__init__()
        self.geometry("600x450")
        self.resizable(False, False)

        # Frames -->

        # Frame para título -->
        frame_titulo = ctk.CTkFrame(self, fg_color="transparent")
        frame_titulo.pack_configure(fill="x", anchor="center")

        label_titulo = ctk.CTkLabel(frame_titulo, text="Configurações do Sistema", font=("Arial", 16))
        label_titulo.pack(pady=20)

        # Frame para campos da configuração -->
        frame_opcoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_opcoes.pack_configure(fill="x", anchor="center")

        label_tema = ctk.CTkLabel(frame_opcoes, text="Tema do Sistema: ")
        label_tema.grid(row=0, column=0, padx= 20, pady=20)

        selecao_tema = ctk.CTkComboBox(
            frame_opcoes, 
            values=("System", "Dark", "Light"), 
            command=lambda valor: combox_tema(valor)
        )
        selecao_tema.grid(row=0, column=1, padx= 20, pady=20)
        

        label_tela = ctk.CTkLabel(frame_opcoes, text="Resulução do Sistema: ")
        label_tela.grid(row=1, column=0, padx= 20, pady=20)

        tamanho_tela = ctk.CTkComboBox(
            frame_opcoes, 
            values=("800x600", "1024x768", "1280x800"), 
            command=lambda valor: combox_tela(valor, self)
        )
        tamanho_tela.grid(row=1, column=1, padx= 20, pady=20)

        frame_rodape = ctk.CTkFrame(self, fg_color="transparent")
        frame_rodape.pack_configure(fill="x", anchor="center")

        botao_fechar_config = ctk.CTkButton(frame_rodape, text="Fechar", command=lambda:botao_sair(self))
        botao_fechar_config.grid(row=0, column=0, padx= 20, pady=20)




        



