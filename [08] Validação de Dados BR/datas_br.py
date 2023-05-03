from datetime import datetime

'''
%A	Dias da semana por extenso	Sunday, Monday, ...
%d	Dias do mês	01, 02, ..., 31
%m	Meses em formato de números	01, 02, ..., 12
%y	Ano em formato de 2 dígitos	99, 15
%Y	Ano em formato de 4 dígitos	1993, 2011
%H	Hora em formato decimal	00, 01, ..., 23
%M	Minuto em formato decimal	00, 01, ..., 59
%S	Segundo em formato decimal	00, 01, ..., 59
'''

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        mes_cadastro = self.momento_cadastro.month -1
        meses_do_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return meses_do_ano[mes_cadastro+1]

    def dia_semana(self):
        dia_semana = self.momento_cadastro.weekday()
        dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        return dias_da_semana[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro