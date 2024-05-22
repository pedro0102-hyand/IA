from queue import PriorityQueue
def busca_estrela(grafo,inicio,objetivo,heuristica):
    visitados=set()
    caminho=[]
    fila_prioridade=PriorityQueue()
    fila_prioridade.put((0,inicio))
    while not fila_prioridade.empty():
        custo,vertice_atual=fila_prioridade.get()
        if vertice_atual==objetivo:
            caminho.append(vertice_atual)
            return caminho
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            caminho.append(vertice_atual)
            for vizinho in grafo[vertice_atual]:
                if vizinho not in visitados:
                    custo_vizinho=custo+1
                    fila_prioridade.put((custo_vizinho+heuristica(vizinho,objetivo),vizinho))
    return None