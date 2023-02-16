# A cada 2m² de parede é utilizado 1 Litro de tinta

print('Largura da parede: ')
largura = float(input())

print('Altura da Parede: ')
altura = float(input())

dimensaoParede = largura * altura
qntdTinta = dimensaoParede / 2

print(f'Sua parede tem dimensão {largura} X {altura} e sua área é {dimensaoParede}m²')
print(f'Pra pintar essa parede, será necessário {qntdTinta} Litros de tinta.')
