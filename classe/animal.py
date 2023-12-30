# -*- coding: utf-8 -*-

SEXO = {
    'M' : 'Macho',
    'F' : 'Femea'
}

SEXO_LIST = ['Macho', 'Femea']
ESPECIES_LIST = ['Cachorro', 'Gato']

class Animal:
    def __init__(self):
        self.nome = ''
        self.data_nasc = ''
        self.sexo = 'M'
        self.inativo = ''
        self.peso = ''
        self.codigo = ''
        self.especie = ''
        self.altura = ''

        self.erro = ''
        self.atributo_obrigatorio_list = ['codigo', 'nome', 'sexo', 'especie']


    def get_som_emitido(self, som):
        return som

    def valida_campos(self, campos_dict):

        for atributo in self.atributo_obrigatorio_list:

            if not campos_dict.get(atributo):

				            self.erro = 'Necessário informar o campo %s' % atributo

				            return False
        return True

class Gato(Animal):
    def __init__(self):
        Animal.get_som_emitido('Mia')

class Cachorro(Animal):
    def __init__(self):
        Animal.get_som_emitido('Late')