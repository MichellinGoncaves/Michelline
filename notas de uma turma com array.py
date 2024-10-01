arraynotas = [0,0,0,0,0]
soma= 0
media = 0
cont= 0
tam=len(arraynotas)
for i in range(tam):
    arraynotas[i]=float(input("digite uma nota: "))

for x in range(tam):
    soma = soma+arraynotas[i]
    media = soma/tam

for r in range(tam):
    if arraynotas[x]>media:
        con=cont+1
print(f"A media da turma é {media} e {cont} alunos ficaram abaixo da media")
