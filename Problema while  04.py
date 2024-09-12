n = int(input("digite um valor: "))
opcao = 1
while opcao != 2:
    while n <= 0:
    n = int(input("invalido, digite um valor: "))
    print(f"O valor é inteiro")
    for x in range (1,n,+1):
        print(x, and = " ")
    opcao:int(input("\n digite 1 para seguir :\n"
                    "ou 2 para não quero"))
    print("")