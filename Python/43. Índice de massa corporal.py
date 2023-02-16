"""

Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
Calcule seu imc e mostre seu status, de acordo com a tabela abaixo:

-- Abaixo de 18.5: Abaixo do peso.
-- Entre 18.5 e 25: Peso Ideal
-- 25 até 30: Sobrepeso
-- 30 até 40: Obesidade
-- Acima dos 40 Obesidade mórbida

"""

peso = float(input('Digite seu peso (KG): '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc}, mostra que você está abaixo do peso!')
elif imc >= 18.5 and imc <= 24.5:
    print(f'Seu imc é de {imc}, mostra que você está no peso ideal!')
    print('Parabéns continue assim!')
elif imc >= 24.6 and imc <= 30:
    print(f'Seu imc é de {imc}, mostra que você está com SOBREPESO, cuidado!')
    print('Verifique sua sieta!')
elif imc >= 30.1 and imc <= 40:
    print(f'Seu imc é de {imc}, mostra que você está com OBESIDADE, Cuidado!')
    print('RISCO DE INFARTO!')
elif imc > 40:
    print(f'Seu imc é de {imc}, mostra que você está com obesidade mórbida')
    print('Se quiser viver mais um pouco, deve-se atentar com os exercícios e alimentação!')
