valorHora = float(input("Digite o valor da sua hora de trabalho: \n"))
horasMes = float(input("Digite o total de horas trabalhadas no mês: \n"))

valorPagar = valorHora * horasMes
aumento = (10 * valorPagar) / 100
pagamentoAumentado = valorPagar + aumento

print(f"O valor a ser pago com 10% acrescidos será de R${pagamentoAumentado}")