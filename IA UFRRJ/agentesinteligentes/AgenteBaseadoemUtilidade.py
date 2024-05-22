class AgenteBaseadoUtilidade:
    def __init__(self):
        self.utilidadade_total=0
    def calcular_utilidade(self,estado):
        if estado=='Estado A':
            return 10
        elif estado=='Estado B':
            return 20
        elif estado=='Estado C':
            return 30
        else:
            return 0
    def escolher_acao(self,possiveis_acoes):
        melhor_acao=None
        melhor_utilidade=float('-inf')
        for acao in possiveis_acoes:
            utilidade_acao=self.calcular_utilidade(acao)
            if utilidade_acao>melhor_utilidade:
                melhor_acao=acao
                melhor_utilidade=utilidade_acao
        return melhor_acao
agente=AgenteBaseadoUtilidade()
possiveis_acoes=['Estado A','Estado B','Estado C','Estado D']
melhor_acao=agente.escolher_acao(possiveis_acoes)

#agente reativo baseado em utilidade
#busca realizar acoes que possam maximizar seu desempenho
#realiza avaliacao e comparacao de alternativas afim de encontrar o mais maximizavel
#utilizado quando há incertezas sobre a natureza do ambiente
