from cpf import CPF
from validate_docbr import CPF
from validate_docbr import CNPJ

exemplo_cpnj = "13254678410913"
cnpj = CNPJ()
cpf = CPF()
print(cpf.validate("12345123454"))
print(cnpj.validate(exemplo_cpnj))

