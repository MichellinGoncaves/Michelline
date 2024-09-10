nome = input("digite seu nome:")
num = input("digite um numero:")
mes = int(input("digite o mes:"))

match mes:

    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("marco")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("dezembro")
    case _:
        print("invalido!")

