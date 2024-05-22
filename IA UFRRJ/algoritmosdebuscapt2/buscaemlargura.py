from collections import deque
def bfs(grafo,inicio):
    visitados=set()
    fila=deque([inicio])
    while fila:
        vertice=fila.popleft()
        if vertice not in visitados:
            print(vertice,end='')
            visitados.add(vertice)
            fila.extend(grafo[vertice]-visitados)
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}
print("BFS comecando de A:")
bfs(grafo,'A')

