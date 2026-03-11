print("Programa para calcular seu mês de trabalho.")
HT = int(input("Digite as horas trabalhadas no mês: "))
VH = float(input("Digite o valor da sua hora trabalhada: "))
PD = float(input("Digite o percentual de desconto do seu salário: "))

salBruto = HT * VH 
totalDesc = (PD / 100) * salBruto
SL = salBruto - totalDesc

print("Suas horas trabalhadas são: ", HT)
print("Seu salário bruto: ", salBruto)
print("O desconto do salário fica: ", totalDesc)
print("O salário liquido no final de tudo: ", SL)