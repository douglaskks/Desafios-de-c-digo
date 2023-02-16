"""

Cire um programa que faço computador
jogar jo ken po com você

"""

import random

print('++' * 15)
print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
print('++' * 15)

a = "PEDRA"
b = "PAPEL"
c = "TESOURA"

opcao = int(input('Digite sua opção: '))

aleatorio = random.randint(0, 2)

if aleatorio == 0 and opcao == 2:
    print('++' * 15)
    print('Computador jogou PEDRA')
    print('Jogador jogou TESOURA')
    print('++' * 15)

    print('Computador venceu!')

elif aleatorio == 1 and opcao == 0:
    print('++' * 15)
    print('Computador jogou PAPEL')
    print('Jogador jogou PEDRA')
    print('++' * 15)

    print('Computador venceu!')

elif aleatorio == 2 and opcao == 1:
    print('++' * 15)
    print('Computador jogou TESOURA')
    print('Jogador jogou PAPEL')
    print('++' * 15)

    print('Computador venceu!')

elif opcao == 0 and aleatorio == 2:
    print('++' * 15)
    print('Jogador jogou PEDRA')
    print('Computador jogou TESOURA')
    print('++' * 15)

    print('Jogador venceu!')

elif opcao == 1 and aleatorio == 0:
    print('++' * 15)
    print('Jogador jogou PAPEL')
    print('Computador jogou PEDRA')
    print('++' * 15)

    print('Jogador venceu!')

elif opcao == 2 and aleatorio == 1:
    print('++' * 15)
    print('Jogador jogou TESOURA')
    print('Computador jogou PAPEL')
    print('++' * 15)

    print('Jogador venceu!')

elif opcao == aleatorio:
    if opcao == 0:
        print('++' * 15)
        print(f'Jogador jogou {a}')
        print(f'Computador jogou {a}')
        print('++' * 15)

        print('Deu EMPATE!!')

elif opcao == aleatorio:
    if opcao == 1:
        print('++' * 15)
        print(f'Jogador jogou {b}')
        print(f'Computador jogou {b}')
        print('++' * 15)

        print('Deu EMPATE!!')

elif opcao == aleatorio:
    if opcao == 2:
        print('++' * 15)
        print(f'Jogador jogou {c}')
        print(f'Computador jogou {c}')
        print('++' * 15)

        print('Deu EMPATE!!')