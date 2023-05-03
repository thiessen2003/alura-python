import re

#Explicação caracteres regex
# [] = define um range ou um grupo de caracteres | [0-9]; [a-z]; [abc]
# * = Marca nenhuma, uma ou mais ocorrência | sol*
# {} = Quantidade de repetições de uma ocorrência definida | [abc]{5}
# \d = Qualquer número de 0 até 9 | \d{3,4}
# \w = Qualquer número de 0 até 9, letra de a até z ou o _underline | \w{10}
# | = um ou outro | @|$
# () = Captura e agrupa | (\w{4})

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aabbcc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta.group())