#Exemplo de comando if-elif-else no python
x = float(input("Digite o valor de X: "))

if x >= 0 and x <= 10:
    print("O valor digitado se encontrar entre 0 a 10")
    
elif x > 10 and x <= 20:
    print("O valor digitado esta entre 10 a 20")
    
elif x > 20 and x <= 30:
    print("O valor se encontra entre 20 e 30")
    
elif x > 30 and x <= 40:
    print("O valor se encontra entre 30 e 40")
    
elif x > 40 and x <= 50:
    print("O valor se encontra entre 40 e 50")
    
elif x > 50 and x <= 60:
    print("O valor se encontra entre 50 e 60")
    
else:
    print("O valor de x é negativo ou maior que 60")