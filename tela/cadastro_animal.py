# -*- coding: utf-8 -*-

import os

from PIL import Image, ImageTk  # Importe as classes necessárias da biblioteca Pillow

import tkinter as tk
from tkinter import ttk

from tela.calendario import Calendario

from tela import dialogo

from classe.animal import Animal
from classe.animal import ESPECIES_LIST, SEXO_LIST

from database.database import Database

class Tela:
    def __init__(self):
        self.botao_calendario = None
        self.novo = None
        self.treeview = None
        self.bt_sair = None
        self.frame_campos = None
        self.bt_excluir = None
        self.db = Database()
        self.db.tabela = 'Animal'

        # Definições da Tela Principal
        self.bt_salvar = None
        self.bt_procurar = None
        self.sexo = None
        self.peso = None
        self.nome = None
        self.altura = None
        self.inativo = None
        self.especie = None
        self.codigo = None
        self.data_nascimento = None


        self.tela_principal = tk.Tk()
        self.tela_principal.title("PetShop")
        self.tela_principal.geometry("800x400")


        self.tela_principal.iconbitmap(self.obter_caminho_img("pet.ico"))

        # Frame principal

        self.frame_principal = ttk.Frame(self.tela_principal, padding=10)
        # self.frame_principal.grid(row=0, column=0, sticky="nsew")
        self.frame_principal.pack(fill="both", expand=True)

        # Configure a grade do frame principal
        self.frame_principal.grid_columnconfigure(0, weight=4)  # Coluna dos campos
        self.frame_principal.grid_columnconfigure(1, weight=1)  # Coluna dos botoes
        self.gera_campos_tela()
        self.tela_principal.mainloop()

    def gera_campos_tela(self):

        # Frame à esquerda - campos
        # Crie um estilo personalizado para a borda
        estilo_borda = ttk.Style()
        estilo_borda.configure("Borda.TFrame", borderwidth=3, relief="flat", background="#DCDCDC")

        self.frame_campos = ttk.Frame(self.frame_principal, width=20, style="Borda.TFrame", borderwidth=1, relief="solid")
        self.frame_campos.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)


        # Frame à direita - Botoes
        # Crie um estilo para o segundo frame
        estilo_borda2 = ttk.Style()
        estilo_borda2.configure("Borda2.TFrame", borderwidth=2, background="green")
        frame_botoes = ttk.Frame(self.frame_principal, width=10, style="Borda.TFrame", borderwidth=1, relief="solid")
        frame_botoes.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Campos da Tela
        fonte_menor = ("Helvetica", 11)
        self.cria_label(self.frame_campos, "Código:", linha=0, coluna=0, padx=3, pady=3, fonte_menor=fonte_menor)
        self.codigo = self.cria_entry(self.frame_campos, linha=0, coluna=1, padx=0, pady=0, tamanho=10)

        novo_codigo = self.db.get_proximo_codigo_animal(tabela='animal')
        self.codigo.insert(0, novo_codigo)
        self.codigo.configure(state='readonly')

        self.cria_label(self.frame_campos, "Espécie:   ", linha=0, coluna=3, padx=3, pady=3, fonte_menor=fonte_menor)
        self.especie = self.cria_combobox(self.frame_campos, ESPECIES_LIST, linha=0, coluna=4, padrao='Cachorro', padx=0, pady=0, tamanho=10)

        self.inativo = tk.IntVar()
        ttk.Checkbutton(self.frame_campos, text="Inativar", variable=self.inativo).grid(row=0, column=6, padx=15, pady=8, columnspan=2, sticky='w')

        self.cria_label(self.frame_campos, "Nome:  ", linha=1, coluna=0, padx=3, pady=3, fonte_menor=("Helvetica", 11))
        self.nome = self.cria_entry(self.frame_campos, linha=1, coluna=1, padx=3, pady=3, tamanho=33)

        self.cria_label(self.frame_campos, "Data Nasc:  ", linha=1, coluna=3, padx=2, pady=3, fonte_menor=("Helvetica", 11))
        self.data_nascimento = ttk.Entry(self.frame_campos, width=12)
        self.data_nascimento.grid(row=1, column=4, padx=1, pady=1)

        # Carrega a imagem de ícone de calendário
        imagem_calendario = Image.open(self.obter_caminho_img("calendario.png"))
        imagem_calendario = imagem_calendario.resize((20, 20), Image.ANTIALIAS)  # Redimensione a imagem

        # Crie um objeto PhotoImage usando a imagem carregada
        icon_calendario = ImageTk.PhotoImage(imagem_calendario)

        Calendar = Calendario(self.frame_campos, self.data_nascimento)

        self.botao_calendario = ttk.Button(self.frame_campos, image=icon_calendario, command=Calendar.abrir_calendario)
        self.botao_calendario.grid(row=1, column=5, padx=2, pady=2)

        # Salve uma referência ao objeto PhotoImage para evitar que ele seja coletado pelo garbage collector
        self.botao_calendario.image = icon_calendario

        self.cria_label(self.frame_campos, "Sexo:    ", linha=2, coluna=0, padx=3, pady=3, fonte_menor=("Helvetica", 11))
        self.sexo = self.cria_combobox(self.frame_campos, SEXO_LIST, linha=2, coluna=1, padrao='Macho')

        self.cria_label(self.frame_campos, "Altura:  ",  linha=2, coluna=2, padx=1, pady=1, fonte_menor=("Helvetica", 11))
        self.altura = self.cria_entry(self.frame_campos, linha=2, coluna=3, padx=1, pady=1, tamanho=8)

        self.cria_label(self.frame_campos, "Peso:    ", linha=2, coluna=4, padx=1, pady=1, fonte_menor=("Helvetica", 11))
        self.peso = self.cria_entry(self.frame_campos, linha=2, coluna=5, padx=1, pady=1, tamanho=8)

        self.novo = ttk.Button(frame_botoes, text="Novo", width=8, command=self.novo_cad)
        self.novo.grid(row=0, column=0, padx=2, pady=3, sticky="nsew", rowspan=1)  # rowspan define a altura dupla

        self.bt_salvar = ttk.Button(frame_botoes, text="Salvar", width=8, command=self.salvar)
        self.bt_salvar.grid(row=1, column=0, padx=2, pady=3, sticky="nsew", rowspan=1)  # rowspan define a altura dupla

        self.bt_procurar = ttk.Button(frame_botoes, text="Procurar", width=8, command=self.procurar)
        self.bt_procurar.grid(row=2, column=0, padx=2, pady=3, sticky="nsew", rowspan=1)  # rowspan define a altura dupla

        self.bt_excluir = ttk.Button(frame_botoes, text="Excluir", width=8, command=self.excluir)
        self.bt_excluir.grid(row=3, column=0, padx=2, pady=3, sticky="nsew", rowspan=1)  #   # rowspan define a altura dupla

        self.bt_sair = ttk.Button(frame_botoes, text="Sair", width=8, command=self.sair)
        self.bt_sair.grid(row=4, column=0, padx=2, pady=3, sticky="nsew", rowspan=1)  # rowspan define a altura dupla

        self.botao_calendario.bind("<Button-1>", self.on_botao_calendario_clicado)

    def on_botao_calendario_clicado(self, event):
        self.frame_principal


    def obter_caminho_img(self, nome):

        # Obtém o diretório atual do script (subpasta)
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        diretorio_raiz_projeto = os.path.dirname(diretorio_atual)
        imagem_calendario_path = os.path.join(diretorio_raiz_projeto, "imagens", nome)

        return imagem_calendario_path


    def cria_label(self, frame, texto, linha, coluna, coluna_tamanho=None, padx=None, pady=None, fonte_menor=None):
        label = ttk.Label(frame, text=texto, font=fonte_menor, borderwidth=1, relief="solid")
        label.grid(row=linha, column=coluna, sticky="w", columnspan=coluna_tamanho, padx=padx, pady=pady)

        return label

    def cria_entry(self, frame, linha, coluna, padx=None, pady=None, tamanho=None):
        entry = ttk.Entry(frame, width=tamanho)
        entry.grid(row=linha, column=coluna, sticky="w", padx=padx, pady=pady)

        return entry

    def cria_combobox(self, frame, opcoes, linha, coluna, padrao='', padx=None, pady=None, tamanho=None):
        cbbox = ttk.Combobox(frame, values=opcoes, width=tamanho)

        if padrao:
            cbbox.set(padrao)  # Defina "Masculino" como padrão

        cbbox.grid(row=linha, column=coluna, sticky="w", padx=padx, pady=pady)

        return cbbox

    def salvar(self):
        dados_da_tela = self.obter_dados_tela()

        from pprint import pprint as pp;
        pp(dados_da_tela)

        A = Animal()
        if not A.valida_campos(dados_da_tela):

            dialogo.DialogoAviso(A.erro)

            return

        dados_da_tela['inativo'] = bool(dados_da_tela['inativo'])

        cadastro_original_list = self.db.select("select * from animal where codigo = %s limit 1" % dados_da_tela['codigo'])

        if cadastro_original_list:
            cadastro_original_dict = cadastro_original_list[0]
            cadastro_original_dict.update(dados_da_tela)

            if not self.db.update('animal', cadastro_original_dict, dados_da_tela['codigo']):
                dialogo.DialogoAviso(self.db.erro)
                return False


        elif not self.db.insert(insert_dict=dados_da_tela):
            dialogo.DialogoAviso(self.db.erro)
            return False

        dialogo.DialogoAviso("Cadastro Salvo com Sucesso!")

        return True

    def procurar(self):
        # Crie uma nova janela para a busca
        janela_procurar = tk.Toplevel(self.tela_principal)
        janela_procurar.title("Procurar")

        # Crie um combobox com as opções "Código" e "Nome"
        combobox_opcoes = ttk.Combobox(janela_procurar, values=["", "codigo", "nome"])
        combobox_opcoes.grid(row=0, column=0, padx=10, pady=10)

        # Crie um entry para inserir o valor de busca
        entry_busca = ttk.Entry(janela_procurar)
        entry_busca.grid(row=0, column=1, padx=10, pady=10)

        # Crie um botão para iniciar a busca
        botao_buscar = ttk.Button(janela_procurar, text="Buscar", command=lambda: self.atualizar_lista_treeview(combobox_opcoes.get(), entry_busca.get()))
        botao_buscar.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Crie um Treeview para exibir a lista de cadastros
        self.treeview = ttk.Treeview(janela_procurar, columns=("Código", "Nome", "Espécie"), show="headings")
        self.treeview.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.treeview.heading("Código", text="Código")
        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Espécie", text="Espécie")

    def atualizar_lista_treeview(self, opcao, valor):

        if opcao == 'codigo':

            try:
                valor = int(valor)
            except:

                dialogo.DialogoAviso("Amigao, é codigo")
                return

            sql_base = 'SELECT codigo, nome, especie FROM animal where codigo = %s' % valor

        else:
            sql_base = "SELECT codigo, nome, especie FROM animal WHERE nome ILIKE '%s'" % str('%' + valor + '%')

        dados = self.db.select(sql_base)

        # Limpe a exibição atual do Treeview
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Adicione os dados à lista
        for registro in dados:
            self.treeview.insert("", "end", values=(registro['codigo'], registro['nome'], registro['especie']))

        # Associe um evento de clique na Treeview
        self.treeview.bind("<ButtonRelease-1>", self.pegar_dados_linha)


    def pegar_dados_linha(self, event):

        item_selecionado = self.treeview.selection()  # Obtém o item selecionado
        if item_selecionado:
            # Obtém os valores das colunas para o item selecionado
            valores = self.treeview.item(item_selecionado)['values']
            if valores:
                codigo, nome, especie = valores
                print(f"Código: {codigo}, Nome: {nome}, Espécie: {especie}")

                dados_list = self.db.select("select * from animal where codigo = %s limit 1" % codigo)

                print("Dados: %s" % dados_list)

                campo_list = [x for x in dados_list[0]]



                # Crie rótulos e campos de texto para cada chave-valor no dict
                for campo in campo_list:

                    if getattr(self, campo) and campo != 'inativo':
                        getattr(self, campo).delete(0, tk.END)  # Limpa o conteúdo atual, se houver
                        getattr(self, campo).insert(0, dados_list[0][campo])

        else:
            print("Selecione um registro")

    def excluir(self):

        codigo = self.codigo.get()

        if not self.db.select("select * from animal where codigo = %s" % codigo):
            dialogo.DialogoAviso("É necessário estar em um animal cadastrado para poder excluir!")
            return

        # self.db.delete("animal", )

    def novo_cad(self):
        pass


    def sair(self):
        print("Fechando tela: %s" % self.tela_principal.title())
        self.tela_principal.destroy()

    def obter_dados_tela(self):
        # Crie uma lista para armazenar os dados dos campos
        tela_dict = {}

        campo_list = ['nome', 'data_nascimento', 'sexo', 'inativo', 'peso', 'codigo', 'especie', 'altura']


        for campo in campo_list:
            if getattr(self, campo):
                tela_dict[campo] = getattr(self, campo).get()

        return tela_dict

if __name__ == '__main__':
    T = Tela()
