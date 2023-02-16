"""

Escreva um programa que mostre na tela uma
contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0,
com uma pausa de 1seg entre eles

"""

from time import sleep

for num in range(10, 0, -1):
    print(num)
    sleep(0.5)

print('BUM! BUM! POOOW!')