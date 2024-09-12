negativo = 0
rep = 0
opcao = 1
while opcao != 2 and rep <= 3:
    neg = 0
    for x in range (2):
        valor = int(input("digite um valor: "))
    if valor < 0:
        negativo = negativo + 1
    print(negativo)
    opcao = int(input("Deseja repetir? 1 sim ou 2 não: "))
if opcao == 2:
    print(f"processo finalizado")
    rep = rep + 1