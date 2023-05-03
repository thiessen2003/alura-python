from functools import total_ordering

@total_ordering
#O módulo total_ordering da biblioteca functools permite que a partir das dunder functions _eq__ e __lt__, todas outras operações de comparação e etc sejam realizadas, tal como a operação <= e =>
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return (f"[>>>Codigo {self._codigo} Saldo {self._saldo}<<<]")

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    #lt = less than | permite utilizar o sorted com a ordem natural dos objetos
    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

#isinstance() verifica a hierarquia de classes também