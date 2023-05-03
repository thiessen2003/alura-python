class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #property acessa diretamente o nome sem que haja a necessidad de colocar parenteses no código e nome se torna um atributo
    def nome(self):
        print("chamando @property nome")
        return self.__nome.title()

    @nome.setter
    def set_nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome