import random
class AgenteBaseadoObjeto:
    def __init__(self,nome,posicao):
        self.nome=nome
        self.posicao=posicao
    def mover_frente(self):
        self.posicao[0]=self.posicao[0]+1
    def mover_tras(self):
        self.posicao[0]=self.posicao[0]-1
    def virar_esquerda(self):
        self.posicao[1]-=1
    def virar_direita(self):
        self.posicao[1]+=1
    def aleatorio(self):
        acao=random.choice([self.mover_frente,self.mover_tras,self.virar_esquerda,self.virar_direita])
        acao()
agente=AgenteBaseadoObjeto()
for _ in range(5):
    agente.aleatorio()

#agente reativo baseado em objeto
#opera baseado em metas e objetivos
#busca alcancar metas especificas dadas as circunstancias do ambiente
#toma acoes baseadas na capacidade de maximizar seus objetivos
#avalia como suas acoes podem contribuir para realizar um objetivo
