# calculadora de desconto simples

valor_compra = float(input("digite o valor de compra: "))
desconto = float(input("diga o desconto aplicado: (ex: 10% = 10) "))


def calcular_desconto(valor, desconto):
    return valor * (desconto / 100)  # transforma % em decimal e aplica


valor_desconto = calcular_desconto(valor_compra, desconto)
valor_final = valor_compra - valor_desconto
print(f"o valor final da compra e: r$ {valor_final:.2f}")
