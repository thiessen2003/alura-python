from datetime import date

class Funcionario:
    def __init__(self, nome, data_de_nascimento, salario):
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        ano_atual = date.today().year
        return ano_atual - int(self._data_de_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:

