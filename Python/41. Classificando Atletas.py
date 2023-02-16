"""

A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de uma atleta e mostre sua categoria,
de acordo com a idade.

-- até 9 Anos (MIRIM)
-- até 14 Anos (INFANTIL)
-- Até 19 Anos (JÙNIOR)
-- Até 25 Anos (SÊNIOR)
-- Acima (MASTER)

"""

anoNascimento = int(input('Digite seu ano de nascimento: '))

idade = 2017 - anoNascimento

if idade <= 9:
    print(f'O atleta tem {idade} Anos')
    print(f'Classificação: MIRIM ')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade} Anos')
    print('classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'O atleta tem {idade} Anos')
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print(f'O atleta tem {idade} Anos')
    print('Classificação: SÊNIOR')
elif idade > 25:
    print(f'O atleta tem {idade} Anos')
    print('Classificação: MASTER')
