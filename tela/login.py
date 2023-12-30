# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.senha = None
        self.usuario = None
        self.login_ok = False


    def monta_tela(self):
        # Criar a janela de login
        self.janela = tk.Tk()
        self.janela.title("Tela de Login")
        self.janela.geometry('250x150')

        # Rótulo e entrada para o nome de usuário
        rotulo_usuario = tk.Label(self.janela, text="Usuário:", relief="solid", borderwidth=1, justify='left')
        rotulo_usuario.grid(row=0, column=0, sticky="nsew", pady=2, padx=2)

        self.usuario = tk.Entry(self.janela, relief="solid", borderwidth=1, justify='left')
        self.usuario.grid(row=0, column=1, pady=2, padx=2)

        # Rótulo e entrada para a senha
        rotulo_senha = tk.Label(self.janela, text="Senha:", relief="solid", borderwidth=1)
        rotulo_senha.grid(row=1, column=0, sticky="nsew", pady=2, padx=2)

        self.senha = tk.Entry(self.janela, show="*", relief="solid", borderwidth=1)  # Opcionalmente, ocultar a senha
        self.senha.grid(row=1, column=1)

        # Botão de login
        botao_login = tk.Button(self.janela, text="Login", command=self.verificar_credenciais, relief="solid", borderwidth=1)
        botao_login.grid(row=4, column=1, pady=2, padx=2)

        # Iniciar a interface gráfica
        self.janela.mainloop()

    # Função para verificar as credenciais
    def verificar_credenciais(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        # Verificar as credenciais (usaremos credenciais fixas como exemplo)
        if usuario == "b" and senha == "1":
            # messagebox.showinfo("Login bem-sucedido", "Bem-vindo, " + usuario + "!")
            self.janela.destroy()
            self.login_ok = True

        else:
            messagebox.showerror("Login falhou", "Credenciais inválidas. Tente novamente.")
            self.login_ok = False

        return False

    def valida_login(self):

        self.monta_tela()

        if not self.login_ok:
            return False

        return True


if __name__ == '__main__':
    Login()


