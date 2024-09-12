aluno = int(input("digite o numero de alunos: "))
x = 0
while x <= aluno+1:
    nota = float(input("Digte a nota do aluno"))
    somanota = nota+somanota
    x = x+1
mediafinal = somanota/aluno
print(f"A menida desse aluno é: {mediafinal:.2f}")