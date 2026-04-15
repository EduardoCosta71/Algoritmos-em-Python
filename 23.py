def parcela (valor, qtde):
    juros = valor*0.05
    res = (valor + juros) / qtde
    return (res)

valor = float(input("Digite o valor da compra: "))
qtdeparc = int(input("Digite quantas parcelas: "))
print("O valor das parcelas ficou: R$", parcela(valor, qtdeparc))