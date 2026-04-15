resp = "Sim"

while (resp == "Sim" or resp == "yes" or resp == "sim" or resp == "s" or resp == "y"):
     peso = float(input("Digite o peso da pessoa, em KG: "))
     altura = float(input("Digite sua altura em M: "))
     
     if (peso > 0 and altura > 0.10 and altura <2.5):
         imc = peso / altura **2
         print("O IMC é {:.2f} kg/m2: ".format(imc))
         if imc > 17:
           print("Muito abiaxo do peso")
         elif imc >= 17 and imc < 18.5:
            print("Abaixo do peso normal") 
         elif imc  <= 18.5 and imc < 25:
            print("Peso dentro do normal") 
         elif imc <= 25 and imc < 30:
            print("Acima do peso normal")
         elif imc <= 30:
            print("Muito acima do peso")
         else: 
            print("vá ao medico urgente!")
         
resp = input("Deseja continuar (Sim ou Não): ")
while (resp!="Sim" and resp!="Não"):
  print("Resposta inválida. Por favor, digite 'Sim ou Nao'.")
  resp = input("Deseja continuar Sim ou Não?")