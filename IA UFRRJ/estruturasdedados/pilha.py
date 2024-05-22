class Pilha:
    def __init__(self):
        self.itens=[]
    def vazia(self):
        return len(self.iens)==0
    def empilhar(self,item):
        self.itens.append(item)
    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            raise IndexError("A pilha está vazia")
    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None
    def tamanho(self):
        return len(self.itens)
pilha=Pilha()
item_removido=pilha.desempilhar()