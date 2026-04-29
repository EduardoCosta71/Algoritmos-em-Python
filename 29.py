#Cria/processa lista com dados de automoveis (dadso fixos, para teste)

placas = ['ADC 1233', 'DFE 2341', 'EER 3456', 'JKI 3054', 'OEDD 7832']
preco = [25000, 75000, 50000, 230232, 15000]
marcas = ['Fiat', 'Ford', 'Fiat', 'Audi', 'VW']
modelos = ['Uno', 'Focus', 'Palio', 'A6', 'Fusca']

print('Dados Cadastrados')
print(placas, '\n,', preco, '\n', marcas, '\n', modelos , '\n')

#calcular a media de preços do carro digitado pelo usuario
soma = 0
qtde = 0

mped = input('Digite uma marca para a pesquisa: ')
for i in range (len(placas)):
    if (marcas[i] == mped):
        soma += preco[i]
        qtde = qtde + 1
print("A média de preço dos carros da marca", mped, "é", soma/qtde, "\n")

#Listar os carros com preço abaixo de R$ 55.000,00
print("Carros com o preço abaixo de 55000 ")
for i in range(len(placas)):
    if (preco[i]  >55000):
        print(placas[i], preco[i], marcas[i], modelos[i])
        
#determinar o carro mais barato
menor = 999999999
pos = 0
for i in range(len(placas)):
    if (preco[i] < menor):
        menor = preco[i]
        pos = i
print("O carro mais barato é: ", 
      placas[pos], "R$", preco[pos], marcas[pos], modelos[pos])