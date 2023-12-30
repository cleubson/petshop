import tkinter as tk
from tkinter import ttk

class SuaClasse:
    def __init__(self):
        self.tela_principal = tk.Tk()
        self.tela_principal.title("Sua Aplicação")
        self.tela_principal.geometry('400x300')

        # Crie um Treeview para exibir a lista de cadastros
        self.treeview = ttk.Treeview(self.tela_principal, columns=("Código", "Nome", "Espécie"), show="headings")
        self.treeview.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Espécie", text="Espécie")

        # Adicione alguns dados fictícios para demonstração
        dados = [
            {'codigo': 1, 'nome': 'Bruno', 'especie': 'Cachorro'},
            {'codigo': 2, 'nome': 'Maria', 'especie': 'Gato'},
        ]

        # Adicione os dados à lista
        for registro in dados:
            self.treeview.insert("", "end", values=(registro['codigo'], registro['nome'], registro['especie']))

        # Associe um evento de clique na Treeview
        self.treeview.bind("<ButtonRelease-1>", self.pegar_dados_linha)

        self.tela_principal.mainloop()

    def pegar_dados_linha(self, event):
        item_selecionado = self.treeview.selection()  # Obtém o item selecionado
        if item_selecionado:
            # Obtém os valores das colunas para o item selecionado
            valores = self.treeview.item(item_selecionado)['values']
            if valores:
                codigo, nome, especie = valores
                print(f"Código: {codigo}, Nome: {nome}, Espécie: {especie}")

if __name__ == "__main__":
    app = SuaClasse()
