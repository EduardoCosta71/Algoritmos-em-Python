def velocidade (s,t):
    if t > 0:
        v = s/t
        return (v)
    else:
        return (0)
    
s = float(input("Digite a distancia percorrida pelo objeto, em KM: "))
t = float(input("Digite o tempo percorrido pelo obejto: "))
res = velocidade (s,t)

if res !=0:
    print("A velocidade do objeto é: ", res, "Km/H")
else:
    print("voce digitou zero no tempo")