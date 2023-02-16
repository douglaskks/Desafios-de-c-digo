"""

Desenvolva um programa que pergunte a distância uma viagem
em KM. Calcule o preço da passagem. Cobrando R$ 0,50 para
viagens de até 200km e R$ 0,45 para viagens mais longas

"""

viagem = float(input('Digite quantos km terá sua viagem: '))

viagemPadrao = viagem * 0.50
viagemPromocional = viagem * 0.45

if viagem <= 200:
    print(f'Sua passagem irá custar R${viagemPadrao}')
elif viagem > 200:
    print(f'Sua passagem custará R${viagemPromocional}')
