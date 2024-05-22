from collections import defaultdict
class Grafo:
    def __init__(self):
        self.grafo=defaultdict(list)
    def adicionar_aresta(self,u,v):
        self.grafo[u].append(v)
    def busca_em_profundidade_util(self,vertice,visitados):
        visitados[vertice]=True
        print(vertice,end="")
        for vizinho in self.grafo[vertice]:
            if not visitados[vizinho]:
                self.busca_em_profundidade_util(vizinho,visitados)
    def busca_em_profundidade(self,inicio):
        visitados=[False]*(max(self.grafo)+1)
        self.busca_em_profundidade_util(inicio,visitados)