valorProduto = float(input("Digite o valor do Produto: \n"))

desconto = (valorProduto * 10) / 100
parcelas = valorProduto / 3
valorDescontado = valorProduto - desconto
comissaoVista = (valorDescontado * 5) / 100
comissaoParcelada = (valorProduto * 5) / 100

print(f"O total a ser pago com 10% de desconto é R${valorDescontado}\n")
print(f"O valor do parcelamento em 3X sem Juros é R${round(parcelas, 2)}\n")
print(f"O valor da comissão do vendedor se vender a vista será de R${comissaoVista}\n")
print(f"O valor da comissão do vendedor se vender parcelado será de R${comissaoParcelada}\n")