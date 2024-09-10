#Dados os valores de horarios abaixo, decifre a logica e faça um codigo para executar
#entrada 3:45|entrada 14:20|saida 6:05
#string
hora1 = int(input("digite hora1:"))
min1 = int(input("digite min1:"))
hora2 = int(input("digite hora2:"))
min2 = int(input("digite min2:"))
#comando
hora_restante = (min1+min2)//60
hora_final = (hora1+hora2) + hora_restante - 24
minuto_final = (min1+min2)%60
if hora_final <0:
    hora_final = hora_final *-1
if hora_final > 12:
    hora_final = hora_final-12
print(f"{hora_final}:{minuto_final}")