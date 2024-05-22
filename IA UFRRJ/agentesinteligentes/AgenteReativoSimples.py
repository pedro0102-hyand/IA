import random
class AgenteReativoSimples:
    def __init__(self):
        self.actions=['Mover para Frente','Mover para trás','Virar a esquerda','virar para a direita']
        def reagir(self,percepcao):
            if percepcao=='Obstáculo a frente':
                return 'Mover para trás'
            else:
                return random.choice(['Mover para frente','Virar a esquerda','Virar pra a direita'])
            agente=AgenteReativoSimples()
            percepcoes=['Nada','Obstáculo a frente','Nada','Nada']
            for percpecao in percepcoes:
                acao=agente.reagir(percepcao)


#exemplo de agente reativo simples
#realiza acoes com base na percepcao imediata do ambiente
#nao realiza acoes mais complexas
# incapaz de prever futuras e possíeis acoes
#nao possui histórico de interacoes passadas
#lida apenas com situacoes específicas
#eficientes em ambientes estáticos e simples

