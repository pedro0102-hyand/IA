class Fila:
    def __init__(self):
        self.itens=[]
    def vazia(self):
        return len(self.itens)==0
    def enfileirar(self,item):
        self.itens.append(item)
    def desenfileirar(self):
        if not  self.vazia():
            return self.itens.pop(0)
        else:
            raise IndexError("A fila está vazia")
    def tamanho(self):
        return len(self.itens)
    def __str__(self):
        return str(self.itens)
fila=Fila()
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
item_removido=fila.desenfileirar()
