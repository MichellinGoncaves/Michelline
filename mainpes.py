class Cachorro:
    def __init__(self,nome,comida,sono):
        self.nome=nome
        self.comida=comida
        self.sono=sono

    def comer(self):
        print(self.comida)
        self.comida-=1

    def dormir(self):
        self.sono = False

Cachorro1=Cachorro("dog",100,14)
Cachorro1.comer()
Cachorro1.dormir()
