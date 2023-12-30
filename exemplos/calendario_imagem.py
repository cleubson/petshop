# -*- coding: utf-8 -*-

import os

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importe as classes necessárias da biblioteca Pillow


class SuaClasse:
    def __init__(self):
        self.tela_principal = tk.Tk()
        self.tela_principal.title("Tela com Ícone de Calendário")

        # Obtém o diretório atual do script (subpasta)
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_raiz_projeto = os.path.dirname(diretorio_atual)
        imagem_calendario_path = os.path.join(diretorio_raiz_projeto, "imagens", "calendario.png")

        # Carregue a imagem de ícone de calendário
        imagem_calendario = Image.open(imagem_calendario_path)
        imagem_calendario = imagem_calendario.resize((24, 24), Image.ANTIALIAS)  # Redimensione a imagem

        # Crie um objeto PhotoImage usando a imagem carregada
        icon_calendario = ImageTk.PhotoImage(imagem_calendario)

        # Crie o botão com o ícone
        botao_calendario = ttk.Button(self.tela_principal, image=icon_calendario, command=self.abrir_calendario)
        botao_calendario.pack()

        # Salve uma referência ao objeto PhotoImage para evitar que ele seja coletado pelo garbage collector
        botao_calendario.image = icon_calendario

    def abrir_calendario(self):
        # Implemente aqui a lógica para abrir o calendário
        pass


if __name__ == "__main__":
    app = SuaClasse()
    app.tela_principal.mainloop()
