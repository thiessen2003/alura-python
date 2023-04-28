from abc import ABCMeta, abstractmethod
from classe2_teste_lista import ContaSalario

class Conta(metaclass = ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return (f"[>>>Código {self.codigo} Saldo {self.saldo}<<<]")

    @abstractmethod
    def passa_o_mes(self):
        pass

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento():
    pass

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

def extrai_saldo(conta):
    return conta._saldo


#Teste herança
conta_do_gui = ContaSalario(15)
conta_da_dani = ContaSalario(47855)
contas = [conta_da_dani, conta_do_gui]
contas_imutaveis = (conta_do_gui, conta_da_dani)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
novas_contas = [conta16, conta17]

#Teste ordenamento
conta_do_gabriel = ContaSalario(22)
conta_do_gabriel.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(20)

conta_do_mauricio = ContaSalario(34)
conta_do_mauricio.deposita(250)

contas_ordenamento = [conta_do_mauricio, conta_da_daniela, conta_do_gabriel]

#Dessa forma, a função reduz os objetos a algo comparável
for conta in sorted(contas_ordenamento, key=extrai_saldo): #ou key=attrgetter("_saldo")
    print(conta)

#Teste iteração
for conta in novas_contas:
    conta.passa_o_mes()


for conta in contas:
    print(conta)

print(contas_imutaveis[0])

