print('Digite uma distânia em metros: ')
entrada = float(input())

km = entrada / 1000
hm = entrada / 100
dam = entrada / 10

dm = entrada * 10
cm = entrada * 100
mm = entrada * 1000

print(f'A medida de {entrada} metros corresponde a ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')

print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')