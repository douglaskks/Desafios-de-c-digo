"""

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos

"""

listaPeso = []

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    listaPeso.append(peso)

listaPeso.sort()
print(f'O maior peso lido foi {listaPeso[4]}Kg')
print(f'O menor peso lido foi {listaPeso[0]}Kg')
