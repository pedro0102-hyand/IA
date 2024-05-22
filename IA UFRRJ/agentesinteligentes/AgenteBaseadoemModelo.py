import random
class AgenteBaseadoModelo:
    def __init__(self):
        self.modelo={}
        def atualizar_modelo(self,estado,acao,resultado,novo_estado):
            if estado not in self.modelo:
                self.modelo[estado]={}
                if acao not in self.modelo[estado]:
                    self.modelo[estado][acao]={}
                self.modelo[estado][acao][resultado]=novo_estado
        def planejar(self,estado_atual,objetivo):
            estado=estado_atual
            plano=[]
            while estado != objetivo :
                if estado not in self.modelo or 'Mover para frente' not in self.modelo[estado]:
                    return None
                acoes_possiveis=list(self.modelo[estado]['Mover para frente'].keys())
                proximo_estado=self.modelo[estado]['Mover para frente'][random.choice(acoes_possiveis)]
                plano.append('Mover para frente')
                estado=proximo_estado
            return plano
agente=AgenteBaseadoModelo()
plano=agente.planejar('Estado A','Estado Final')

#agente inteligente baseado em modelo
#realiza percepcoes e análises mais precisas sobre o ambiente em que está
#possui um modelo que permite analisar e recolher iteracoes passadas
#pode prever acoes e análises futuras
#práticos em ambientes flexíveis e instáveis
#adapta suas acoes conforme analisa o ambiente
#podem planejar e adaptar eventos futuros