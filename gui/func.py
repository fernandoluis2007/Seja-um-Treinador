# Arquivo para Funções da Interface -->
import customtkinter as ctk

# Configurações -->
def combox_tema(escolha):
    print(f"Tema alterado: {escolha}")
    ctk.set_appearance_mode(escolha)
        
def combox_tela(escolha):
    print(f"Tamanho de Tela alterado: {escolha}")
    app.geometry(escolha)


