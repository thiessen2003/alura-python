from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2003_deve_retornar_22(self):
        entrada = '13/03/2003' #Given | Serve para dar o contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)