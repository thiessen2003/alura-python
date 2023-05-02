from validate_docbr import CPF

class Cpf:
    def __init__(self, documento):
        self.documento = str(documento)
        documento = str(documento)
        if self.cpf_eh_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!!")

    def __str__(self):
        return self.formata_cpf()

    def cpf_eh_valido(self, valor_cpf):
        if len(valor_cpf) == 11:
            validador = CPF()
            return validador.validate(valor_cpf)
        else:
            raise ValueError("Quantidade de digitos inválida.")

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask((self.cpf))