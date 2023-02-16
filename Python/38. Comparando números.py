"""

Escreva um programa que leia dois números e compare-os.
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não exista valor maior, os dois são iguais

"""

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

if a > b:
    print(f'O número {a} é maior que o {b}')
    print('Portanto o primeiro número é maior!')
if b > a:
    print(f'O número {b} é maior que o {a}')
    print('Portanto o segundo número é maior!')
if a == b:
    print("Os dois números digitados são iguais")
