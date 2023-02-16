"""

Faça um programa que leia três números e mostre
qual é o maior e qual é o menor valor

"""

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o Segundo valor: '))
c = int(input('Digite o Terceiro valor: '))

menor = a

if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

print(f'O menor valor é o {menor}')
