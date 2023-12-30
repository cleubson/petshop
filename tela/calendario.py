# -*- coding: utf-8 -*-

import tkinter as tk
from tkcalendar import Calendar

class Calendario:
    def __init__(self, janela, data):
        self.Calendario = Calendar
        self.janela = janela
        self.data = data

        self.cal_popup = None

    def selecionar_data(self):
        self.data_selecionada = self.data.get_date()
        print("Data selecionada:", self.data_selecionada)


    def abrir_calendario(self):
        self.top = tk.Toplevel(self.janela)
        self.top.title("Calendário")

        # Crie um objeto Calendar no topo (popup)
        self.cal_popup = self.Calendario(self.top, selectmode="day", locale="pt_BR", date_pattern="dd/mm/yyyy")
        self.cal_popup.pack(padx=10, pady=10)

        # Quando o usuário selecionar uma data no calendário, atualize o campo de data
        self.cal_popup.bind("<<CalendarSelected>>", lambda e: self.atualizar_data(self.cal_popup.get_date()))



    def atualizar_data(self, data):
        self.data.delete(0, tk.END)  # Limpe o campo de data atual
        self.data.insert(0, data)  # Insira a nova data

        self.top.destroy()  # Feche a janela do calendário

