import re

#Regular expressions or regex são basicamente formas de pré-descrever padrões de dados a serem encontrados em um código
#Vamos supor que em uma texto quero detectar a parte que descreve idades que possuam dois digitos
#A regex para isso seria algo assim [123456789][0123456789]


endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

#? significa que esse caractere em específico pode aparecer uma ou nenhuma vez | os {} indicam quantas vezes aquele padrao deve aparecer
#0-9 significa de 0 até 9
#no lugar do ? podemos colocar {0,1} para dizer que um elemento aparece de 0 até 1 vez
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)