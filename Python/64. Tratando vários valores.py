"""

Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)

"""
soma = entrada = 0
soma2 = 0
soma2 += 1
soma = soma + entrada

entrada = int(input('Digite um número [999 para parar] '))
while entrada != 999:
    soma += entrada
    soma2 += 1
    entrada = int(input('Digite um número [999 para parar] '))
print(f'Você digitou {soma2 - 1} números e a soma entre eles foi {soma}')
