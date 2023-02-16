"""

Desenvolva um programa que leia o primeiro termo e a
razao de uma PA. No final, mostre os 10 primeiros termos dessa
progressão

"""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
termo1 = 0

for i in range(termo, termo + 10, 1):

    print(f'{termo1}', end=' ├ ')
    termo1 = termo1 + razao

