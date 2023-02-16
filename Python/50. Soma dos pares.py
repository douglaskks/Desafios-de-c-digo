"""

Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o
valor digitado for ímpar, desconsidere-o.

"""

soma = 0
contagem = 0

for i in range(1, 7, 1):
    entrada = int(input(f'Digite o {i}° valor: '))
    if entrada % 2 == 0:
        soma = soma + entrada
        contagem = contagem + 1

print(f'Você digitou {contagem} números pares e o resultado da sua soma é {soma}')
