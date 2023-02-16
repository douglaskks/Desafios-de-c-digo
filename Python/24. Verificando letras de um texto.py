"""

Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome 'SANTO'

"""

cidade = str(input('Digite a cidade que você nasceu: '))
cidade1 = cidade.upper()
cidade2 = cidade1.split()

print(cidade2)
print(cidade2[0] == 'SANTO')