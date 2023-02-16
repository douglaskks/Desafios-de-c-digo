import random

pontuacaoMaquina = 0
pontuacaoHumano = 0

numeroAleatorio = random.randint(0, 5)

print('==' * 20)
print('Pensei em um número entre 0 a 5... ')
print('==' * 20)

print('Iniciar jogo?')
confirmacao = str(input())

if confirmacao == 'S':

    print('==' * 20)
    print('Digite qual número eu pensei...')
    resposta = int(input())
    print('==' * 20)

    while resposta != numeroAleatorio:

        print('Você errou!')
        print('+1 ponto pra mim')
        pontuacaoMaquina = pontuacaoMaquina + 1
        print(f'Maquina : {pontuacaoMaquina}')
        print(f'Humano: {pontuacaoHumano}')
        break

    while resposta == numeroAleatorio:

        print('você acertou!')
        print('+1 ponto pra você')
        pontuacaoHumano = pontuacaoHumano + 1
        break
        print('==' * 20)

        print(f'Maquina : {pontuacaoMaquina}')
        print(f'Humano: {pontuacaoHumano}')
