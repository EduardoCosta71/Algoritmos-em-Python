def parcela (valor, qtde, jur):
    jures= (jur/100) * valor
    res = (valor + jures) / qtde
    return (res)

valor = float(input("Digite o valor da compra: "))
juros = float(input("Digite o juros dessas parcelas: "))
qtdeparc = int(input("Digite quantas parcelas: "))

print("O valor das parcelas ficou: R$", parcela(valor, qtdeparc, juros))