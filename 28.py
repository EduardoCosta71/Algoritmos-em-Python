#Criamos uma lista com os valores digitados pelo usuario, visualizamos
#a lista e somamos todos seus valores.

continua = 's'
lista = []
while (continua == 's' or continua == 'S'):
    n = float(input("Digite os valores para criar a lista: "))
    lista.append(n)
    
    continua = input("Deseja continuar? (s/n)")
    
print("A lista com os elementos digitados é: ", lista)

soma = 0 
for i in range(len(lista)):
    soma += lista[i]
    
print("A soma dos elementos da lista é: ", soma)