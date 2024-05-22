class No:
    def __init__(self,chave):
        self.esquerda=None
        self.direita=None
        self.valor=chave
def inserir(raiz,chave):
    if raiz is None:
        return No(chave)
    else:
        if raiz.valor<chave:
            raiz.direira=inserir(raiz.direita,chave)
        else:
            raiz.esquerda=inserir(raiz.esquerda,chave)
    return raiz
def percorrer_em_ordem(raiz):
    if raiz:
        percorrer_em_ordem(raiz.esquerda)
        print(raiz.valor)
        percorrer_em_ordem(raiz.direita)
if __name__=="__main__":
    raiz=No(50)
    raiz=inserir(raiz,20)
    raiz=inserir(raiz,40)
    raiz=inserir(raiz,50)
    percorrer_em_ordem(raiz)
