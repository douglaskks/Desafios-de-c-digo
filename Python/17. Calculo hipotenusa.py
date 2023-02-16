import math

print('Digite o valor do cateto oposto: ')
catetoOposto = float(input())
catetoOposto = catetoOposto ** 2

print('Digite o valor do cateto adjacente: ')
catetoAdjacente = float(input())
catetoAdjacente = catetoAdjacente ** 2

somaCatetos = catetoAdjacente + catetoOposto
raizCatetos = math.sqrt(somaCatetos)

print(f'A hipotenusa vai medir {raizCatetos}')
