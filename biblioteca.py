'''with open("teste1.txt", "a") as arquivo:
     arquivo.write(f"{texto}")

with open("teste1.txt", "r") as arquivo2:
        texto2 = arquivo2.read()
        print(texto2)'''


def Cadastrar(texto):
    with open("teste1.txt", "a") as arquivo:
     arquivo.write(f"{texto}")

def Mostrar():
    with open("teste1.txt", "r") as arquivo2:
        texto2 = arquivo2.read()
        print(texto2)


def pesquisar(texto):
    cont=0
    with open ("Texto2.txt","r") as arquivo:
        for i in arquivo:
            if texto in i:
                cont+=1
    print(cont)