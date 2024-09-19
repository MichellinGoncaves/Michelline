v1 = int(input("digite um numero: "))
v2 = int(input("digite um numero: "))
v3 = int(input("digite um numero: "))
soma = v1 + v2

if v3<soma:
    soma = (v1+v2)
    print(f"a soma entre {v1} e {v2} e:{soma}")
else:
    print(f"a soma de {v3} é menor")