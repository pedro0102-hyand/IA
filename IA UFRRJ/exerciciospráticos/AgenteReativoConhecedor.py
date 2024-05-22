import random
import numpy as np
class Ambiente:
    def __init__(self):
        self.locais = np.array(["A", "B"])
        self.status = {local: "Limpo" for local in self.locais}
        self.local_agente = np.random.choice(self.locais)
        self.pontuacao = 0
    def sujeira(self, local):
        self.status[local] = "Sujo"
    def limpar(self, local):
        self.status[local] = "Limpo"
        self.pontuacao += 1
    def analisar(self):
        return self.local_agente, self.status[self.local_agente]
    def executar(self, acao):
        if acao == "Esquerda":
            self.local_agente = np.where(self.locais == self.local_agente, self.locais[0], self.local_agente)[0]
        elif acao == "Direita":
            self.local_agente = np.where(self.locais == self.local_agente, self.locais[1], self.local_agente)[0]
        elif acao == "Limpar":
            self.limpar(self.local_agente)
class AgenteReativoSimples:
    def __init__(self):
        pass
    def decidir(self, percepcao):
        local, status = percepcao
        if status == "Sujo":
            return "Limpar"
        elif local == "A":
            return "Direita"
        elif local == "B":
            return "Esquerda"
        else:
            return "NoOp"
class AgenteReativoSimplesConhecedor:
    def __init__(self,ambiente):
        self.ambiente=ambiente
    def decidir(self):
        local,status=self.ambiente.analisar()
        if status=="Sujo":
            return "Limpar"
        elif local=="A":
            return "Direita"
        elif local=="B":
            return "Esquerda"
        else:
            return "NoOp"
def simulacao():
    pontuacao_total_simples=0
    pontuacao_total_conhecimento=0
    num_configs=0
    for status_inicial in ["Limpo", "Sujo"]:
        for local_agente_inicial in ["A", "B"]:
            ambiente = Ambiente()
            ambiente.local_agente = local_agente_inicial
            ambiente.status = {"A": status_inicial, "B": status_inicial}
            if status_inicial == "Sujo":
                local_sujo = np.random.choice(ambiente.locais)
                ambiente.sujeira(local_sujo)
            agente_simples = AgenteReativoSimples()
            agente_conhecimento = AgenteReativoSimplesConhecedor(ambiente)
            print("\nConfiguração inicial:")
            print("Localização do Agente:", ambiente.local_agente)
            print("Status:", ambiente.status)
            for _ in range(1000):
                percepcao=ambiente.analisar()
                acao_simples=agente_simples.decidir(percepcao)
                acao_conhecimento=agente_conhecimento.decidir()
                ambiente.executar(acao_simples)
                ambiente.executar(acao_conhecimento)
            print("\nConfuguracao final:")
            print("Localizacao do Agente:",ambiente.local_agente)
            print("Status:",ambiente.status)
            print("Pontuacao Agente Simples:",ambiente.pontuacao)
            pontuacao_total_simples+=ambiente.pontuacao
            percepcao=ambiente.analisar()
            print("Pontuacao Agente Conhecimento:",sum(1 for status in ambiente.status.values() if status=="Limpo"))
            pontuacao_total_conhecimento+=sum(1 for status in ambiente.status.values() if status=="Limpo")
            num_configs+=1
            print("\nPontuação média Agente Simples:", pontuacao_total_simples / num_configs)
            print("Pontuacao media Agente Conhecimento :",pontuacao_total_conhecimento/num_configs)
simulacao()