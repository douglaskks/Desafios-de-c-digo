"""

Escreva um programa que leia um número n inteiro qualquer e
mostra na tela os n primeiros elementos de uma sequência de
Fibonacci.

Ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

"""
f1 = 0
f2 = 1
contador = 3

termos = int(input('Quantos termos você quer mostrar? '))
print(f'{f1} -> {f2}', end=' -> ')
while contador <= termos:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=' -> ')
    contador += 1
print('FIM')
