opcao = 1
while opcao != 2:
    n1 = float(input("digite o 1 nota: "))
    while n1 < 0 or n1 >10:
        n1 = float(input("digite o 1 nota: "))
        print("nota não existe")
    n2 = float(input("digite o 2 nota: "))
    while n2 < 0 or n2 >10:
        n2 = float(input("digite o 2 nota: "))
        print("nota não existe")
        opcao:int(input("\n digite 1 para sim :\n"
                        "ou 2 para não"))
        print("")

    media = (n1+n2)/2
    print(media)
