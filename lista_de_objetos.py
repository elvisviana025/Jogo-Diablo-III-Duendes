from collections.abc import MutableSequence
from random import randint


class Lista_de_objetos(MutableSequence):
    def __init__(self, nome, lista_de_objetos):
        self._nome = nome
        self._lista_de_objetos = lista_de_objetos

    def __getitem__(self, key): # TORNA LISTA ITERÁVEL
        return self._lista_de_objetos[key]

    def __setitem__(self, key, valor): # ATRIBUI VALOR
        self._lista_de_objetos[key] = valor

    def __delitem__(self, key): # REMOVE ITEM DA LISTA
        del self._lista_de_objetos[key]

    def __len__(self): # RETORNA O TAMANHO
        return len(self._lista_de_objetos)

    def insert(self, key, valor): # INSERIR ITEM NA LISTA
        self._lista_de_objetos.insert(key, valor)

    def imprimir_objetos(self):
        for objeto in self:
            print(objeto)

    def sortear_objeto(self):
        return self.__getitem__(randint(0, (self.__len__() - 1)))
