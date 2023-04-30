usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

set_usuarios_data_science = {15, 23, 43, 56}
set_usuarios_machine_learning = {13, 23, 56, 42}

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

#quando há uma lista de elementos na qual não queremos pegar elementos repetidos, normalmente utilizamos um set | além disso, sets são mutáveis

#Conjuntos não aceitam elementos repetidos e não possuem indexação | Mesmo assim, sets continuam sendo iteráveis | Para operações de conjuntos, podemos utilizar o elementou
# ou ( | ) como extend | o mesmo se aplica para a operação and ( & )
print(set(assistiram))

print(set_usuarios_data_science | set_usuarios_machine_learning)

print(set_usuarios_data_science - set_usuarios_machine_learning)

print(set_usuarios_data_science & set_usuarios_machine_learning)

print(set_usuarios_data_science ^ set_usuarios_machine_learning) #elementos que aparecem em só um dos conjuntos

set_usuarios_data_science.add(95)

set_nova_lista_de_usuarios = frozenset(set_usuarios_machine_learning)

#Implementação com strings e texto
meu_texto = "Olá, meu nome é Gabriel e tenho 20 anos."
palavras_do_texto = meu_texto.split()
print(set(palavras_do_texto))