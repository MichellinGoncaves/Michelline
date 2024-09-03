nota1 = float(input("informar 1 nota"))
nota2 = float(input("informar 2 nota"))
nota3 = float(input("informar 3 nota"))
media = (nota1 + nota2 + nota3)/3
if media >=7:
    print(f"voce foi aprovado,parabens!")
    print(f"{media}")
if media >=4:
    print(f"voce esta recuperacao")
else:
    print(f"voce infelizmento foi reprovado")
    print(f"{media}")