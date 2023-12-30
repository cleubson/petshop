# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class MinhaAplicacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Minha Aplicação")

        self.botao_aviso = tk.Button(self.janela, text="Mostrar Aviso", command=self.mostrar_aviso)
        self.botao_aviso.pack(pady=20)

    def mostrar_aviso(self):
        # Bloqueie a tela principal
        self.janela.wait_window(self.mostrar_aviso_modal())

    def mostrar_aviso_modal(self):
        janela_aviso = tk.Toplevel(self.janela)
        janela_aviso.title("Aviso")
        janela_aviso.geometry("300x150")

        label_aviso = tk.Label(janela_aviso, text="Isso é um aviso!")
        label_aviso.pack(pady=20)

        botao_fechar = tk.Button(janela_aviso, text="Fechar Aviso", command=janela_aviso.destroy)
        botao_fechar.pack()

        # Espere até que a janela de aviso seja fechada
        janela_aviso.wait_window()

if __name__ == "__main__":
    root = tk.Tk()
    app = MinhaAplicacao(root)
    root.mainloop()
