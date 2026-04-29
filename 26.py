senha = [123]
usuario = ["Admin"]

print(" =========== == Logue no sistema! == ============")

while True:
    senha = int(input("Digite a senha: "))
    usuario = input("Digite o usuario: ")
    
    if senha == 123 and usuario == "Admin":
        print("Bem-vindo!")
        break
        
    else:
        print("Senha ou Usuario errada, Tente novamente!")
        