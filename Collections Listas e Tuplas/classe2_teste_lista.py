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

    #lt = less than
    def __lt__(self, outro):
        return self._saldo < outro._saldo
#isinstance() verifica a hierarquia de classes também