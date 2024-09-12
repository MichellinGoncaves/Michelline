#Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive)
#considere que N será sempre maoir que ZERO.
n = int(input("digite um valor: "))
n = 0
while n <= 0:
    n = int(input("invalido, digite um valor: "))
    print(f"O valor é inteiro")
for x in range (1,n,+1):
    print(x, end = " ")
