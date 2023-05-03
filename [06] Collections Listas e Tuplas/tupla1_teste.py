#BASIC NOTES: Tuplas são imutáveis, entretanto
#podemos inseri-las em listas | somente seus valores internos são imutáveis
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]

usuarios.append(('Paulo', 39, 1979))

#um for desta maneira desempacota tuplas
for nome, idade, ano in usuarios:
    print(nome, idade, ano)

#o _ ignora o elemento
for nome, _, _ in usuarios:
    print(nome, idade, ano)

