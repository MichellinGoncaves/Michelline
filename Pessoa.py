class Pessoa():
    def __init__(self,nome, peso, idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.andando=False
        self.comendo=False
        self.dormindo=False
    def comer(self):
        if self.comendo==False:
            if self.andando==False:
                if self.dormindo==False:
                    print(f"{self.nome} já foi comer")
                    self.comendo=True
                else:
                    print(f"{self.nome} não pode comer pois já esta dormindo")
            else:
                print(f"{self.nome} não pode comer pois já esta andando")
        else:
            print(f"{self.nome} Já está comendo")
    def andar (self):
        if self.andando==False:
            if self.comendo==False:
                if self.dormindo==False:
                    print(f"{self.nome} já foi comer")
                    self.andando=True
                else:
                    print(f"{self.nome} não pode comer pois já esta dormindo")
            else:
                print(f"{self.nome} não pode comer pois já esta andando")
        else:
            print(f"{self.nome} Já está comendo")
    def dormir(self):
        if self.dormindo==False:
            if self.andando==False:
                if self.comendo==False:
                    print(f"{self.nome} já foi comer")
                    self.dormindo=True
                else:
                    print(f"{self.nome} não pode comer pois já esta dormindo")
            else:
                print(f"{self.nome} não pode dormir pois já esta andando")
        else:
            print(f"{self.nome} Já está comendo")


class Animal:
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
        self.comer=False

    def comer(self):
        self.comer=True
        print(f"{self.nome} está comendo!")

class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"{self.nome} foi miar!")

class Cachorro(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)

    def comer(self):
        self.comer=True
        print(f"{self.nome} está comendo!")

    def late(self):
        print(f"{self.nome} faz AuAu!")

class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def mugi(self):
        print(f"{self.nome} faz MUUUUU!")

class Coelho(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def gruindo(self):
        print(f"{self.nome} faz nhec! nhec!")



class Atleta:
    def __init__(self,nome, peso):
        self.nome=nome
        self.peso=peso
        self.aposentado=False
        self.aquecido=False

    def aposentar (self):
        if self.aposentado == False:
            print(f"{self.nome} está aposentado")
        else:
            print(f"{self.nome} está aposentado")
            self.aposentado=True

    def aquecer (self):
        if self.aquecido == False:
            print(f"{self.nome} está aquecido")
        else:
            print(f"{self.nome} nao está aquecido ")
            self.aposentado=True

class corredor(Atleta):
    def __init__(self,nome, peso):
        super().__init__(nome,peso)
    def correr(self):
        if
        print(f"{self.nome} foi correr!")





