"""

Crie um programa que leia e mostre um menu como
o ao lado da tela:
Seu programa deverá realizar a operação solicitada
em cada acesso

[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair números

"""
lista = [1, 2, 3, 4, 5]
firstValue = int(input('Digite o primeiro valor: '))
secondValue = int(input('Digite o segundo valor: '))
print('=+' * 10)
print('Menu')
print('=+' * 10)

print("[ 1 ] Soma")
print("[ 2 ] Multiplicar")
print("[ 3 ] Maior")
print("[ 4 } Novos números")
print("[ 5 ] Sair do programa")

opcao = int(input('>>>>> Digite a opção: '))

while opcao not in lista:
    opcao = int(input('Opção inválida! Tente novamente: '))

if opcao in lista:
    while opcao in lista:
        if opcao == 1:
            resultado = firstValue + secondValue
            print(f'O resultado da soma entre {firstValue} e {secondValue} é {resultado}')
            print('=+' * 10)
            print('------ Menu ------')
            print('=+' * 10)

            print("[ 1 ] Soma")
            print("[ 2 ] Multiplicar")
            print("[ 3 ] Maior")
            print("[ 4 } Novos números")
            print("[ 5 ] Sair do programa")

            opcao = int(input('>>>>> Digite a opção: '))

        if opcao == 2:
                resultado = firstValue * secondValue
                print(f'O resultado da multiplição entre {firstValue} e {secondValue} é {resultado}')

                print('=+' * 10)
                print('------ Menu ------')
                print('=+' * 10)

                print("[ 1 ] Soma")
                print("[ 2 ] Multiplicar")
                print("[ 3 ] Maior")
                print("[ 4 } Novos números")
                print("[ 5 ] Sair do programa")

                opcao = int(input('>>>>> Digite a opção: '))

        if opcao == 3:
            if firstValue > secondValue:
                print(f'O {firstValue} é o maior')
            else:
                print(f'O {secondValue} é o maior')

            print('=+' * 10)
            print('------ Menu ------')
            print('=+' * 10)

            print("[ 1 ] Soma")
            print("[ 2 ] Multiplicar")
            print("[ 3 ] Maior")
            print("[ 4 } Novos números")
            print("[ 5 ] Sair do programa")

            opcao = int(input('>>>>> Digite a opção: '))

        if opcao == 4:
            firstValue = int(input('Digite o primeiro valor: '))
            secondValue = int(input('Digite o segundo valor: '))
            print('=+' * 10)
            print('Menu')
            print('=+' * 10)

            print("[ 1 ] Soma")
            print("[ 2 ] Multiplicar")
            print("[ 3 ] Maior")
            print("[ 4 } Novos números")
            print("[ 5 ] Sair do programa")

            opcao = int(input('>>>>> Digite a opção: '))

        if opcao == 5:
            exit()
