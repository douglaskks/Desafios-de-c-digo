print('Digite um número para ver a tabuada: ')
tabuada = int(input())


print('_' * 15)
for i in range(0,11):
    print(f'{tabuada} X {i} = {tabuada * i}')
print('_' * 15)
