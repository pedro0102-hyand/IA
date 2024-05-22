class No:
    def __init__(self,chave):
        self.esquerda=None
        self.direita=None
        self.chave=chave
def busca_em_profundidade(raiz):
        if raiz is None:
            return
        
        print(raiz.chave)

        busca_em_profundidade(raiz.esquerda)
        busca_em_profundidade(raiz.direita)

if __name__=="__main__" :
     raiz=No(1)
     raiz.esquerda=No(2)
     raiz.direita=No(3)
     raiz.esquerda.esquerda=No(4)
     raiz.esquerda.direita=No(5)
     raiz.direita.esquerda=No(6)
     raiz.direita.direita=No(7)
     busca_em_profundidade(raiz)
