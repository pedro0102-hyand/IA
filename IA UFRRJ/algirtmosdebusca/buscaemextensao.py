class No:
    def __init__(self,chave):
        self.chave=chave
        self.esquerda=None
        self.direita=None
def busca_em_extensao(raiz):
    if raiz is None:
        return
    fila=[]
    fila.append(raiz)
    while fila:
        no_atual=fila.pop(0)
        print(no_atual.chave)
        if no_atual.esquerda:
            fila.append(no_atual.esquerda)
        if no_atual.direita:
            fila.append(no_atual.direita)
if __name__=="__main__":
    raiz=No(1)
    raiz.esquerda=No(2)
    raiz.direita=No(3)
    busca_em_extensao(raiz)
