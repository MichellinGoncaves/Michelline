peso = float(input("digite seu peso: "))
altura = float(input("digite sua aultura: "))
imc = peso/(altura**2)
if imc < 18.5:
    print(f"seu peso é: abaixo do peso.")
elif imc >= 18.6 and imc < 25.0:
    print(f"seu peso é: peso ideal, parabéns!")
elif imc <= 25.0 and imc < 30.0:
    print(f"seu peso é: levemente acima do peso.")
elif imc <= 30.0 and 35.0:
    print(f"seu peso é: obesidade grau I.")
elif imc <= 35.0 and 40.0:
    print(f"seu peso é: obesidade grau II(severa)")
elif imc > 40:
    print(f"seu peso é: obesidade grau III(mórbida)")


