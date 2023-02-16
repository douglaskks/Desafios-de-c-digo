"""

Crie um programa que leia uma frase qualquer e diga
se ela é um palídromo, desconsiderando os espaços.

Ex: APOS A SOPA
    A SACADA DA CASA
    A TORRE DA DERROTA
    O LOBO AMA O BOLO
    ANOTARAM A DATA DA MARATONA

"""

palindromo = str(input('Digite uma frase: '))
palindromo = palindromo.upper()
palindromo = palindromo.replace(' ', '')

variavelInversa = palindromo[::-1]
variavelInversa = variavelInversa.upper()
variavelInversa = variavelInversa.replace(' ', '')

if variavelInversa == palindromo:
    print(f'A frase digitada é um palíndromo')
else:
    print(f'A frase digitada não é um palíndromo')
