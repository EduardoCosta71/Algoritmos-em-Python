#Cria listas com dados de automoveis digitados pelo usuario

continua = 's'
placas = []
precos = []
marcas = []
modelos = []

while (continua == 's' or continua == 'S'):
    pl = input('Digite a placa: ')
    placas.append(pl)
    
    pr = float(input('Digite o preço: '))
    precos.append(pr)
    
    mar = input('Digite a marca: ')
    marcas.append(mar)
    
    mo = input('Digite o modelo: ')
    modelos.append(mo)
    
    continua = input('Desejar continuar?? (s/n)')
    
    print('Placas', placas, 'Preços', precos, 'Marcas', marcas, 'Modelos', modelos )
    
 