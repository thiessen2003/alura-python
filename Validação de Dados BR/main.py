import requests

from acesso_cep import BuscaEndereco

cep = "90450210"
objeto_cep = BuscaEndereco(cep)
objeto_cep.acessa_via_cep()

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)
