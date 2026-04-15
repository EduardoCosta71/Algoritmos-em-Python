s = float(input("Digite a distancia percorrida: "))
t = float(input("Digite a tempo do objeto: "))

if s > 0:
    v = s/t
    print("A velocidade percorrida é: ", v)
else:
    print("Erro, o valor de tempo deve ser positivo!")
    print("Tente Novamente")


