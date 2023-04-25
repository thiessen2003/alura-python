url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
print(url)

#Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#Busca o valor de um paramêtro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor) #indice_valor representa a partir de qual ponto você quer buscar o caractere desejado
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]