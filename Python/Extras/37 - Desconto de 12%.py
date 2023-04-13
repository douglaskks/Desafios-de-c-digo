valor = float(input("Digite o valor do produto: \n"))

desconto = (12 * valor) / 100
valorReal = valor - desconto

print(f"O produto no valor de R${valor} com desconto ficará R${valorReal}")