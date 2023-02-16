"""

Escreva um programa que leua um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão

-- 1 para binário
-- 2 para octal
-- 3 para hexadecimal

"""

numero = int(input('Digite um número inteiro: '))
print('Qual será a base de conversão: ')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input())

if opcao == 1:
    binario = bin(numero)
    binarioConvert = binario.split()
    print(f'A conversão do número {numero} para binário é {binario[2:]}')
elif opcao == 2:
    octal = oct(numero)
    print(f'A conversão do número {numero} para octal é {octal[2:]}')
elif opcao == 3:
    hexadecimal = hex(numero)
    print(f'A conversão do nnúmero {numero} para hexadecimal é {hexadecimal[2:]}')
