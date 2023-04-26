class ContaCorrete:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return (f"[>>>Código {self.codigo} Saldo {self.saldo}<<<]")
