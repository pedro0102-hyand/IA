def busca_gulosa(grafo,inicio,objetivo,heuristica):
    visitados=set()
    caminho=[]
    fila_prioridade=[(heuristica(inicio,objetivo),inicio)]
    while fila_prioridade:
        _, vertice_atual=fila_prioridade.pop(0)
        if vertice_atual==objetivo:
            caminho.append(vertice_atual)
            return caminho
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            caminho.append(vertice_atual)
            for vizinho in grafo[vertice_atual]:
                if vizinho not in visitados:
                    fila_prioridade.append((heuristica(vizinho,objetivo,vizinho)))
        fila_prioridade.sort(key=lambda x:x[0])
    return None