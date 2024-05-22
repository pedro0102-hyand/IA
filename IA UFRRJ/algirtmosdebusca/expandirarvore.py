class No:
    def __init__(self,chave):
        self.esquerda=None
        self.direita=None
        self.valor=chave
def expandir_arvore(raiz):
    if raiz is None:
        return
    if raiz.esquerda is None and raiz.direita is None:
        raiz.esquerda=No(raiz.valor *2)
        raiz.direita=No(raiz.valor *2+1)
    else:
        expandir_arvore(raiz.esquerda)
        expandir_arvore(raiz.direita)
def imprimir_arvore(raiz):
    if raiz:
        print(raiz.valor)
        imprimir_arvore(raiz.esquerda)
        imprimir_arvore(raiz.direita)
if __name__=="__main__":
    raiz=No(1)
    expandir_arvore(raiz)
    imprimir_arvore(raiz)