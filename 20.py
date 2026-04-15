N = int(input("Quantas pessoas serão processadas? "))
for i in range(N): # repete para i=0, i=1, i=2, i=3 (para quatro pessoas)
    peso = float(input("\nDigite o peso da pessoa, em Kg: "))
    altura = float(input("Digite a estatura da pessoa, em m: "))
    if(peso > 0 and altura > 0.10 and altura < 2.5):
        imc = peso / altura**2
        print("O IMC é ", imc, " Kg/m²")
    else:
        print("Verifique por favor, valor digitados errados!")
print ("\nAté logo!")   