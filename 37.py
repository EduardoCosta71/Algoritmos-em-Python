#Percorrendo por indice
frutas = ["banana", "maça", "pera", "banana"]

fru = input("Adcione uma fruta: ")
frutas.append(fru)

for i in range(len(frutas)):
    print(i,frutas[i])
    
print("Frutas indice 4: ", frutas[4])
    

        