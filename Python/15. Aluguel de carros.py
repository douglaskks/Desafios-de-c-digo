#Escreva um programa que pergunte a quantidade de km percorridos por um carro
#alugado e a quantidae de dias pelos quais ele foi alugado. Calcule o preço a paga,
#sabendo que o carro custa R$60,00 por dia e R$0.15 por km rodado

print('Quantos dias o carro ficou alugado? ')
diasAluguel = int(input())

print('Quantos Km rodados? ')
kmRodado = float(input())

calculoAluguel = diasAluguel * 60
calculoKm = kmRodado * 0.15
valorTotal = calculoAluguel + calculoKm

print(f'O total a pagar é R${valorTotal}')
