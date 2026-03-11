print("RESTAURANTE ComaBEm - SEJA BEM VINDO")
print("Digite abaixo o valor total da sua conta de hoje (Considerando o 10% do garçom): ")
conta = float(input("Valor: "))

resultado = conta * 0.10
liquido = conta + resultado

print("O valor total foi de: ", liquido)
print("Gorjeta: ", resultado)