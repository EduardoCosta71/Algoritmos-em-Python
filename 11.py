print("IMC")
peso = float(input("Digite seu Peso: "))
alt = float(input("Digite sua Altura: "))

soma = peso / (alt **2)

print("IMC: ", soma)
print("Muito abaixo do peso: ", soma < 17)
print("Abaixo do peso norma: ", soma >= 17 and soma < 18.5)
print("Peso dentro do Normal: ", soma >= 18.5 and soma < 25)
print("Acima do Peso normal: ", soma >= 25 and soma < 30)
print("Muito acima do peso: ", soma >= 30)