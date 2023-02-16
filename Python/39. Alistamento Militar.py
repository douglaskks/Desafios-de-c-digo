"""

Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou o tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

"""

anoNascimento = int(input('Digite seu ano de nascimento: '))

idade = 2017 - anoNascimento
alistamento = 18

print(f'Quem nasceu em {anoNascimento} tem {idade} Anos de idade em 2017')

if idade < alistamento:
    faltaAlistamento = alistamento - idade
    anoAlistamento = anoNascimento + 18
    print(f'Faltam {faltaAlistamento} Anos para você se alistar!')
    print(f'Seu alistamento será em {anoAlistamento}')

elif idade > alistamento:
    passouAlistamento = idade - 18
    anoAlistamento = 2017 - passouAlistamento

    print(f'O período de alistamento passou!')
    print(f'Você deveria se alistar em {anoAlistamento}')
