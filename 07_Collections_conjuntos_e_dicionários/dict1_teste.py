from collections import defaultdict, Counter

aparicoes_no_texto = {"Gabriel": 3, "cachorro": 2, "meu": 4, "o":7}

print(aparicoes_no_texto["Gabriel"])
print(aparicoes_no_texto.get("xpto", 0)) #pega o valor do índice específico, e caso não encontre nada, retorna 0

aparicoes_no_texto["Gabriel"] = 2
del aparicoes_no_texto["cachorro"]

for elemento in aparicoes_no_texto.keys():
    print(elemento)

for elemento in aparicoes_no_texto.values():
    print(elemento)

#Retorna tuplas de tamanho 2
for elemento, valor in aparicoes_no_texto.items():
    print(elemento, "=", valor)

#=======================================================================================================
meu_texto = "Bem vindo meu nome é Gabriel e tenho 20 anos e gosto do meu peixe o nome dele é Nemo"
texto = meu_texto.lower()

#podemos usar o defaultdict também, para o qual podemos assinalar valores padrão, como o próprio int
aparicoes = defaultdict(int)

#É possível escrever esse for assim, pois o defacultdict permite que o valor 0 seja assinalado automaticamente caso uma valor não seja encontrado na iteração
for palavra in texto.split():
    aparicoes[palavra] += 1

aparicoes_mais_faceis_de_contas = Counter(meu_texto.split())
print(aparicoes_mais_faceis_de_contas)