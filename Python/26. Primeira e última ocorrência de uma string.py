"""

Escreva um programa que leia uma frase pelo teclado e mostre:

--- Quantas vezes aparece a letra 'A'
--- Em que posição ela aparece na primeira vez
--- Em que posição ela aparece pela última vez

"""


print('Digite uma frase: ')
nome = str(input())

correcaoNome = nome.strip()

nome2 = correcaoNome.upper()
nome1 = nome2.count('A')

procuraNome = nome2.find('A')
nomeUltimo = nome2.rfind('A')

print(f'A letra A aparece {nome1} vezes')
print(f'A primeira letra A aparece na {procuraNome + 1}° casa')
print(f'A última letra A aparece na {nomeUltimo + 1}° casa')
