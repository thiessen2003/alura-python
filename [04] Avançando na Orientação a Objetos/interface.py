from abc import ABC # abstract base classes
#métodos abstratos são utilizados principalmente para delimitar métodos abstratos na
#classe mãe que devem ser obrigatoriamente herdados e aplicados diferentemente nas classes filhas

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao

    def __len__(self):
        return len(self.descricao)

lista = MinhaListagem('Nova_lista')
print(lista)
