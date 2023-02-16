"""

Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de 3 e que se encontram
no intervalo de 1 a 500

"""

soma = 0
contagem = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        soma = soma + i
        contagem = contagem + 1

print(f'A soma de todos os {contagem} números é {soma}')
