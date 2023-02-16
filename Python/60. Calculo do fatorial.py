"""

Faça um programa qu leia um número
qualquer e mostre seu fatorial.

Ex:
8? 8 X 7 X 6 X 5 X 4 X 3 X 2 X 1 = 40.320

"""

opcao = int(input('Digite o número pra calcular o fatorial: '))
resultado = 1

for i in range(opcao, 1, -1):
    print(i, end=' X ')
    resultado = resultado * i
print(f'1 = {resultado}')