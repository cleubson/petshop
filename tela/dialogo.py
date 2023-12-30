# -*- coding: utf-8 -*-

import os

import tkinter as tk
from tkinter import ttk

class DialogoAviso(tk.Toplevel):
    def __init__(self, msg):
        super().__init__()

        self.title("Aviso")
        self.geometry("300x150")

        # Obtém o diretório atual do script (subpasta)
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        # Suba um nível para obter o diretório do projeto
        diretorio_raiz_projeto = os.path.dirname(diretorio_atual)

        # Agora você pode construir caminhos relativos a partir do diretório raiz
        caminho_relativo_para_icone = os.path.join(diretorio_raiz_projeto, "imagens", "pet.ico")

        self.iconbitmap(caminho_relativo_para_icone)

        label = ttk.Label(self, text=msg, wraplength=250)
        label.pack(padx=20, pady=20)

        ok_button = ttk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)


if __name__ == "__main__":
    pass



