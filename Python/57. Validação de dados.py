"""

Faça um programa que leia o sexo de uma pessoa, mas
só aceite os valores 'M' ou 'F'. Caso esteja errado, peça
a digitação novamente até ter um valor correto

"""

sexo = str(input('Digite seu sexo: [M/F] '))

while sexo not in 'MmFf':
    sexo = str(input('Dádos inválidos. Por favor digite seu sexo: [M/F] '))

if sexo in 'Mm' or sexo in 'Ff':
    print(f'Sexo {sexo} cadastrado com sucesso')
