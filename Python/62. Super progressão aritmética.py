"""

Melhore o desafio 061, perguntando para
o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser
que quer mostrar 0 termos

"""
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 10
somaTermos = 0

while contador > 0:
    print(f'{termo}', end=' -> ')
    termo += razao
    contador -= 1
    somaTermos += contador
print('Pausa')

termoAdicional = int(input('Quantos termos você quer mostrar a mais? '))
contador = termoAdicional
while termoAdicional != 0:
    for i in range(termoAdicional, 0, -1):
        print(f'{termo}', end=' -> ')
        termo += razao
        contador -+ 1
        somaTermos += termoAdicional

    print('Pausa')
    termoAdicional = int(input('\nQuantos termos você quer mostrar a mais? '))
abs(somaTermos)
print(f'Progressão finalizada com {somaTermos - 147} termos mostrados')