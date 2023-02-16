"""

Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar'
em um numero entre 0 a 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.

"""
import random

tentativas = 0

print('Olá, sou seu computador')
contadorAleatorio = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10!')
print('Será que consegue adivinhar qual foi? ')

opcao = int(input('Qual o seu palpite? '))

while opcao != contadorAleatorio:
    if opcao > contadorAleatorio:
        opcao = int(input('Menos... Tente mais uma vez: '))
        tentativas += 1
    elif opcao < contadorAleatorio:
        opcao = int(input('Mais... Tente mais uma vez: '))
        tentativas += 1

print(f'Acertou com {tentativas+1} tentativas, Parabéns')
