"""

Escreva um programa que leia a velocidade de um carro.
ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado.

A multa vai custar R$7,00 por cada km acima do limite

"""


print('Digite a velocidade do carro: ')
velocidade = float(input())

if velocidade > 80:
    valorPagar = (velocidade - 80) * 7

    print('Multado!!')
    print('Você ultrapassou o limite de 80km/h')
    print(f'Você pagará R${valorPagar} de multa!')

else:
    print('Tenha um bom dia, Dirija com segurança!')
