class No:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
class ListaEncadeada:
    def __init__(self):
        self.primeiro=None
    def inserir_inicio(self,dado):
        novo_no=No(dado)
        novo_no.proximo=self.primeiro
        self.primeiro=novo_no
    def imprimir(self):
        atual=self.primeiro
        while atual:
            atual=atual.proximo
lista=ListaEncadeada()
lista.inserir_inicio(10)
lista.imprimir()