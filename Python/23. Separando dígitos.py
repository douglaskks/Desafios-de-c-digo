"""
Faça um proframa que leia um numerode 0 a 9999 e mostre na tela
cada um dos dígitos separados.

Ex: digite um número: 1234

Unidade: 4
Dezena:  3
Centena: 2
Milhar:  1

"""

print('Digite um número: ')
numero = int(input())

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
