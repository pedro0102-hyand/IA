
class No:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
no1=No(5)
no2=No(10)
no3=No(15)
no1.proximo=no2
no2.proximo=no3
no_atual=no1
while no_atual:
    no_atual=no_atual.proximo