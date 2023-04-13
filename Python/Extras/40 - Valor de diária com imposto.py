diasTrabalhados = int(input("Total de dias trabalhados: "))

totalReceber = diasTrabalhados * 30
desconto = (totalReceber * 8) / 100
totalReceber = totalReceber - desconto
print(f"O total a ser pago com desconto de 8% do imposto será de R${totalReceber}")