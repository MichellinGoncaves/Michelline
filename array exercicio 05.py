array1 = [0]*10
array2 = [0]*10
tam=len (array1)

for a in range(tam):
    array1[a]=int(input("digite uma nota: "))
mult = int(input("digite o multiplicador: "))

for i in range(tam):
    array2[i] = array1[i]*mult

print(array1)
print(mult)
print(array2)


