"""

Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre:

-- A média de idade do grupo
-- Qual é o nome do homem mais velho
-- Quantas mulheres tem menos de 20 anos

"""
media = 0
homemVelho = 0
mulheresVinte = 0
somaIdade = 0
idadeVelha = 0
mulherNome = 0
mulherNova = 0

for i in range(1, 5):
    print('==' * 10)
    print(f'{i}° Pessoa')

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    somaIdade += idade

    if i == 1 and sexo == 'M':
        homemVelho = nome
        idadeVelha = idade
    if sexo == 'M' and idade > idadeVelha:
        homemVelho = nome
        idadeVelha = idade

    if sexo == 'F' and idade < 20:
        mulheresVinte = idade
        mulherNome = nome
        mulherNova += 1

mediaIdade = somaIdade / 4

print(f'A idade média de do grupo de pessoas é {mediaIdade} Anos')
print(f'O homem mais velho se chama {homemVelho} e ele têm {idadeVelha} Anos')
print(f'E no grupo tem {mulherNova} mulheres com menos de 20 Anos')

