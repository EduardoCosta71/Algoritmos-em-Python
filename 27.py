#Criamos uma lista com valores fixos, visualizamos a lista,
#visualizamos o primeiro e o ultimo valor elemento da lista,
#somamos os valores da lista e visualizamos o elementos nas posições pares.

lista = [4.0, 9.2, 3.1, 9.1, 1.5, 3.2, 2.6]

print("A lista criada é: ", lista)
print("O 1° elemento da lista é:", lista[0])
print("O último elemento da lista é: ", lista[len(lista)-1])

soma = 0
for i in range(len(lista)):
    soma += lista[i]
    
print("A soma dos elementos da lista é: ", soma)

print("Os elementos nas posições pares da lista são: ")
for i in range(0,len(lista),2):
    print(list[i])