# -*- coding: iso-8859-1 -*-

import psycopg2
from pprint import pprint as pp

class Database:
    def __init__(self, user='postgres', password='postgres', database='petshop', port=5432, host='localhost'):
        self.erro = ''
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.host = host
        self.conn = None
        self.tabela = None

    def get_proximo_codigo_animal(self, tabela):
        self.connect()
        cur = self.conn.cursor()

        query = 'SELECT MAX(codigo) FROM %s' % tabela

        cur.execute(query)
        max_codigo = cur.fetchone()[0] or 0  # Obtém o maior código

        self.disconnect()

        return max_codigo + 1


    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host,
                                         database=self.database,
                                         user=self.user,
                                         password=self.password,
                                         port=self.port)

        except Exception as e:
            print(str(e))

    def disconnect(self):

        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(str(e))

    def insert(self, table=None, insert_dict={}):

        if not table and not self.tabela:
            self.erro = 'Tabela não informada'
            return False


        if not insert_dict:
            self.erro = 'Informações de insert faltantes'
            return False


        self.connect()
        cur = self.conn.cursor()

        campo_list = []
        valor_list = []

        for campo, valor in insert_dict.items():

            if not valor:
                continue

            campo_list.append(campo)

            if type(valor) not in [int, float]:
                valor_list.append("'" + str(valor) + "'")
            else:
                valor_list.append(valor)

        print('Colunas: %s' % campo_list)
        print('Valores: %s' % valor_list)

        sql = "INSERT INTO %s (%s) VALUES (%s)" % (self.tabela or table,
                                                   ", ".join(campo_list),
                                                   ", ".join(valor_list))

        try:
            cur.execute(sql)
            self.conn.commit()

        except Exception as e:
            print(sql)
            print(e)
            self.erro = '%s'[:10] % e

        self.disconnect()

        return True

    def update(self, tabela, update_dict, pkey):
        self.connect()
        cur = self.conn.cursor()

        # Crie as listas para as colunas e valores a serem atualizados
        coluna_list = []
        valor_list = []

        coluna_valor = ''
        for coluna, valor in update_dict.items():
            if valor is not None:  # Ignorar valores em branco

                coluna_list.append(coluna)

                if type(valor) not in [int, float]:
                    valor_list.append("'" + str(valor) + "'")

                    coluna_valor += ' %s=%s,' % (coluna, "'" + str(valor) + "'")
                else:
                    coluna_valor += ' %s=%s,' % (coluna, valor)

        coluna_valor = coluna_valor[:-1]

        # forcoluna_list
        sql = "update %s set %s where codigo = %s"
        sql_completo =  sql % (tabela, coluna_valor, pkey)


        print("query bugada: %s" % sql_completo)

        # Execute a consulta SQL com os valores
        cur.execute(sql_completo)

        # Faça o commit da transação
        self.conn.commit()

        self.disconnect()

        return True

    def select(self, query):
        self.connect()
        cur = self.conn.cursor()
        cur.execute(query)

        registro_dict = {}

        retorno_list = cur.fetchall()

        result_dict_list = []
        coluna_list = []
        for coluna in cur.description:
            coluna_list.append(coluna.name)

        for retorno in retorno_list:
            for col, ret in zip(coluna_list, retorno):
                registro_dict[col] = ret

            result_dict_list.append(registro_dict.copy())

        self.disconnect()

        return result_dict_list

    def delete(self, table, condicao):
        self.connect()
        cur = self.conn.cursor()

        # Construa a consulta DELETE
        query = f"DELETE FROM {table} WHERE {condicao}"

        # Execute a consulta DELETE
        cur.execute(query)

        # Commit a transação
        self.conn.commit()

        self.disconnect()

        return True

if __name__== '__main__':
    d = Database(user='postgres', password='postgres', database='nfe')
    d.select('select * from empresa_local')
    d.insert('teste', {'teste': 1})
