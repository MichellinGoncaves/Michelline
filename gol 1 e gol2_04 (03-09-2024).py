time1 = input("digite o nome do time 1")
gols1 = int(input(f"informe quantos gols{time1}"))

time2 = input("digite o nome do time 2")
gols2 = int(input(f"informe quantos gols {time2}"))

if gols1==gols2:
    print("empate")
else:
    if gols1 > gols2:
        print(f"{time2} vencedor")
