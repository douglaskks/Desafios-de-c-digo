print('Digite a temperatura a ser convertida: ')
graus = float(input())
print('--' * 30)

print('--' * 30)
print('Escolha a qual opção o usuário deseja converter: ')
print('1 - De C° para F°')
print('2 - De F° para C°')
grauInteiro = int(input())
print('--' * 30)

if grauInteiro == 1:
    celsiusFahrenheit = (graus * 1.8) + 32
    print('--' * 30)
    print(f'A temperatura de {graus}°C corresponde a {celsiusFahrenheit}°F')
    print('--' * 30)

elif grauInteiro == 2:
    fahrenheitCelsius = (graus - 32) / 1.8
    print('--' * 30)
    print(f'A temperatura de {graus}°F corresponde a {fahrenheitCelsius}°C')
    print('--' * 30)
