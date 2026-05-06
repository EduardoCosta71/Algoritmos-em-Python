#Remove todos os dados da lista "REPETIDOS"
nomes = ["Ana", "Carlos", "Ana", "Giovanna", "Ana"]

while "Ana" in nomes:
    nomes.remove("Ana")
    
print(nomes)