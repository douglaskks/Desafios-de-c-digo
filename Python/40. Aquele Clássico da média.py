"""

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atinginda:

-- média abaixo de 5.0 (Reprovado)
-- média entre 5.- e 6.9 (Recuperação)
-- média 7 ou superior (Aprovado)

"""

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'A média do aluno ficou {media}!')
    print(f'Portanto o aluno foi reprovado!')
elif media >= 5 and media < 7:
    print(f'A média do aluno ficou {media}!')
    print('Portanto o aluno vai pra recuperação"')
elif media >= 7:
    print(f'A média do aluno ficou {media}!')
    print('Portanto o aluno foi aprovado!')
