class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = nome
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def set_nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__ome = nome
        self.ano = nome
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like(self):
        self.likes += 1
