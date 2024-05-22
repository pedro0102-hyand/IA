class Lista:
    def __init__(self):
        self.itens=[]
    def vazia(self):
        return len(self.itens)==0
    def adicionar(self,item):
        self.itens.append(item)
    def remover(self,item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            raise ValueError("O item nao está na lista")
    def tamanho(self):
        return len(self.itens)
    def __str__(self):
        return str(self.itens)
lista=Lista()
lista.adicionar(10)