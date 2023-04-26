class ContaCorrete:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return (f"[>>>Código {self.codigo} Saldo {self.saldo}<<<]")

conta_do_gui = ContaCorrete(15)
conta_da_dani = ContaCorrete(47855)
contas = [conta_da_dani, conta_do_gui]

for conta in contas:
    print(conta)
