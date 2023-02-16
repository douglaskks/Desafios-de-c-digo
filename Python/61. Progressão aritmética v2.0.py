"""

Refaça o desafio 051, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura while

"""
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 10

while contador > 0:
    print(f'{termo}', end=' -> ')
    termo += razao
    contador -= 1
print('FIM')
