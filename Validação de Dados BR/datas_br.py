from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        mes_cadastro = self.momento_cadastro.month -1
        meses_do_ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        return meses_do_ano[mes_cadastro+1]

    def dia_semana(self):
        dia_semana = self.momento_cadastro.weekday()
        dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        return dias_da_semana[dia_semana]