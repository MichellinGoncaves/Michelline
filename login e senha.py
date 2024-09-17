usuario = 'mi'
senha = '4321'
cont = 1

entrada = input("digite seu usuario: ")
senha_saida = input("digite sua senha: ")

if entrada == usuario and senha_saida == senha:
    print("Seja bem vinda mi!:)")

else:
    print("Voce errou mi, tente mais uma vez")
    while cont <= 2:
        entrada =input("digite seu usuario: ")
        senha_saida = input("digite sua senha: ")
        cont = cont + 1
        if entrada == usuario and senha_saida == senha:
            print("Seja bem vinda mi! :)")
            break
    else:
       print("voce errou! ")
    if cont  >=3:
       print("Voce excedeu, voce esta bloqueada!")