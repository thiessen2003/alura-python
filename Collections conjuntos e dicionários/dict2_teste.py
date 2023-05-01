from collections import defaultdict, Counter

class Conta:
    def __init__(self):
        print("Imprimindo uma conta.")

#Toda vez que não der para achar uma conta específica, defaultdict chama o Conta como valor default
contas = defaultdict(Conta)

#Cria uma conta nova
contas[16]

print(contas[16])

