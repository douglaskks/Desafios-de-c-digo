"""

Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.

"""

numero = int(input('Digite um valor: '))
lista1 = []
lista2 = []

for i in range(1, numero+1):
    if numero % i == 0:
        lista1.append(i)
    else:
        lista2.append(i)

valorFinal = len(lista1)
print(valorFinal)
if valorFinal == 2:
    print(f'O número {numero} é um número primo')
    print(f'Porque ele é divisível por {valorFinal} números eles são {lista1}')
else:
    print(f'O número {numero} não é um número primo')
    print(f'Pois ele se divide com {valorFinal} números')
    print(f'é divisível por {lista1}')  