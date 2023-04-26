#BASE DE TESTES PARA LISTAS. REFERÊNCIA DE DOCUMENTAÇÃO https://docs.python.org/3/tutorial/datastructures.html
idade1 = 12
idade2 = 10
idade3 = 30
idade4 = 47
idade5 = 23


idades = [idade1, idade2, idade3, idade4, idade5]

idades.append(2)
idades.remove(47) #remove a primeira aparição
idades.insert(0, 109) #insere na posição específica
idades.extend([28, 67]) #permite inserir uma lista de números, algo que o append não faz

if 47 in idades:
    print("Está")
else:
    print("Não está")

#List comprehension: para somar 1 a cada idade, há uma sintaxe simplificada
idades_no_ano_que_vem = [(idade+1) for idade in idades]
