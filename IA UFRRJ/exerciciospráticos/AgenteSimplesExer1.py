import random
import numpy
import numpy as np 
class Ambiente :
    def __init__(self):
        self.locais=np.array(["A","B"])
        self.status={local: "Limpo" for local in self.locais}
        self.local_agente=np.random.choice(self.locais)
        self.pontuacao=0
    def sujeira(self,local):
        self.status[local]="Sujo"
    def limpar(self,local):
        self.status[local]="Limpo"
        self.pontuacao+=1
    def analisar(self):
        return self.local_agente,self.status[self.local_agente]
    def executar(self,acao):
        if acao=="Esquerda":
            self.local_agente=np.where(self.locais==self.local_agente,self.locais[0],self.local_agente)[0]
        elif acao=="Direita":
            self.local_agente=np.where(self.locais==self.local_agente,self.locais[1],self.local_agente)[0]
        elif acao=="Aspirar":
            if self.status[self.local_agente]=="Sujo":
                self.limpar(self.local_agente)
class AgenteReativoSimples:
    def __init__(self):
        pass
    def decidir(self,percepcao):
        local,status=percepcao
        if status=="Sujo":
            return "Aspirar"
        elif local=="A":
            return "Direita"
        elif local=="B":
            return "Esquerda"
        else:
            return "NoOp"
def simulacao():
    ambiente=Ambiente()
    agente=AgenteReativoSimples()
    pontuacao_total=0
    num_configs=0
    for status_inicial in ["Limpo","Sujo"]:
        for local_agente_inicial in ["A","B"]:
            ambiente.local_agente=local_agente_inicial
            ambiente.status={"A":status_inicial,"B":status_inicial}
            if status_inicial=="Sujo":
                local_sujo=np.random.choice(ambiente.locais)
                ambiente.sujeira(local_sujo)
            print("\nConfiguracao Inicial:")
            print("Localizacao do Agente:",ambiente.local_agente)
            print("Status:",ambiente.status)
            for _ in range(1000):
                percepcao=ambiente.analisar()
                acao=agente.decidir(percepcao)
                ambiente.executar(acao)
            print("\nConfiguracao Inicial:")
            print("Localizacao do Agente:",ambiente.local_agente)
            print("Status:",ambiente.status)
            print("Pontuacao:",ambiente.pontuacao)
            pontuacao_total=pontuacao_total+ambiente.pontuacao
            num_configs=num_configs+1
    print("\n Pontuacao média:",pontuacao_total/num_configs)
simulacao()
