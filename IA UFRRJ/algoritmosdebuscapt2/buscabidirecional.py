def busca_bidirecional(grafo,inicio,objetivo):
    visitados_inicio=set()
    visitados_objetivo=set()
    fila_inicio=[inicio]
    fila_objetivo=[objetivo]
    while fila_inicio and fila_objetivo:
        vertice_atual_inicio=fila_inicio.pop(0)
        visitados_inicio.add(vertice_atual_inicio)
        if vertice_atual_inicio in visitados_objetivo:
            return True
        for vizinho in grafo[vertice_atual_inicio]:
            if vizinho not in visitados_inicio:
                fila_inicio.append(vizinho)
        vertice_atual_objetivo=fila_objetivo.pop(0)
        visitados_objetivo.add(vertice_atual_objetivo)
        if vertice_atual_objetivo in visitados_inicio:
            return True
        for vizinho in grafo[vertice_atual_objetivo]:
            if vizinho not in visitados_objetivo:
                fila_objetivo.append(vizinho)
    return False