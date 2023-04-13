valorPremio = float(input("Digite o valor do prêmio: \n"))
primeiraPorcentagem = (46 * valorPremio) / 100
segundaPorcentagem = (32 * valorPremio) / 100
terceiraPorcentagem = (22 * valorPremio) / 100

somaPorcentagem = primeiraPorcentagem + segundaPorcentagem + terceiraPorcentagem

print(f"O primeiro ganhador recebrá um total de R${primeiraPorcentagem}\n")
print(f"O segundo ganhador recebrá um total de R${segundaPorcentagem}\n")
print(f"O terceiro ganhador recebrá um total de R${terceiraPorcentagem}\n")
print("\n")
print(f"Totalizando um prêmio de R${somaPorcentagem}")