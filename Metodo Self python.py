
'''metodo mostra acao
atributo caracterisca, variavel
herença herda acoes e caracteristicas, pode receber os dois'''

'''class Pessoa: (METODTODO ESPECIAL CHAMADO CONTRUTOR)
    def__init__(self,nome,peso,idade,comendo=false):
        self.nome - ATRIBUTO = n é argumento
        self.peso
        self.idade'''

class Pessoa:
    def __init__(self,n,p,i,andar,comendo,dormindo):
        self.nome=n
        self.peso=p
        self.idade=i
        self.andar=andar
        self.comendo=comendo
        self.dormindo=dormindo

    def andar(self):
        if self.andar == False:
            print("Foi comer!")
            self.andar=True
        else:
            print("Já está comendo!")

    def parar(self):
        if self.andar:
            self.andar = False

    def comer(self):
        if self.comer == False:
            print("Foi comer!")
            self.comer=True


        print("Foi comer")

    def dormir (self):
        print("Foi dormir")

p1=Pessoa('MICHELLNE',50,12)
