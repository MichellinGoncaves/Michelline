#Ler o numero de alunos existentes em uma turma e, após isto, ler as notas destes alunos, calcular e escrever
#a media aritimeticas desses notas lidas

aluno = int(input("digite o numero de alunos: "))
somanota = 0
for i in range(aluno):
    nota = float(input("Digte a nota do aluno"))
    somanota = nota+somanota
mediafinal = somanota/aluno
print(f"A menida desse aluno é: {mediafinal:.2f}")