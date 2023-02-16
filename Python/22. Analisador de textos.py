"""
Crie um programa que leia o nome completode uma pessoa e mostra:

-- O nome com todas as letras maiúsculas e minúsculas
-- Quantas letras ao todo (sem considerar espaços)
-- quantas letras tem o primeiro nome

"""

print('Digite seu nome completo: ')
listNome = str(input())

listNome1 = listNome.upper()
listNome2 = listNome.lower()
listNome3 = listNome.strip()
listNome4 = len(listNome3) - listNome.count(' ')
listNome5 = listNome.find(' ')

print(f'Seu nome em maiúsculas é {listNome1}')
print(f'Seu nome em minúsculas é {listNome2}')
print(f'O total de letras de seu nome é {listNome4}')
print(f'O seu primeiro nome tem {listNome5} letras')