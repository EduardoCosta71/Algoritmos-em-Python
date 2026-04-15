import math
def func_calc (angulo):
  print("Seno: ", math.sin(angulo))
  print("Cosseno: ", math.cos(angulo))
  print("Tagente: ", math.tan(angulo))
  
ang = float(input("Digite o valor do angulo: "))
ang = ang * math.pi/180
func_calc(ang)