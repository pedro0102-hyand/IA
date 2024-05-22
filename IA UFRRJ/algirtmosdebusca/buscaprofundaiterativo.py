class No:
    def __init__(self,chave):
        self.chave=chave
        self.direita=None
        self.esquerda=None
def busca_aprofundamento_iterativo(raiz,alvo):
    profundidade_maxima=0
    while True:
        resultado=busca_em_profundidade_limitada(raiz,alvo,profundidade_maxima)
        if resultado is not None:
            return resultado
        profundidade_maxima+=1
def busca_em_profundidade_limitada(no,alvo,profundidade_maxima):
    return busca_recursiva(no,alvo,profundidade_maxima,0)
def busca_recursiva(no,alvo,profundidade_maxima,profundidade_atual):
    if profundidade_atual>profundidade_maxima:
        return None
    if no.chave==alvo:
        return no
    if no.esquerda is not None:
        resultado_esquerda=busca_recursiva(no.esquerda,alvo,profundidade_maxima,profundidade_atual+1)
        if resultado_esquerda is not None:
            return resultado_esquerda
        if no.direita is not None:
            resultado_direita=busca_recursiva(no.direita,alvo,profundidade_maxima,profundidade_atual+1)
            if resultado_direita is not None:
                return resultado_direita
            return None