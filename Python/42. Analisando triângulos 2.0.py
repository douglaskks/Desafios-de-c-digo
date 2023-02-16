"""

Refaça o desafio 035 dos triângulos, acrescentando os recurso de
mostrar que tipo de triângulo será formado:

-- Equilátero: todos os lados iguais
-- Isóceles: Dois lados iguais
-- Escaleno: Todos os lados diferentes

"""

a = int(input('Digite o primeiro segmento: '))
b = int(input('Digite o segundo segmento: '))
c = int(input('Digite o terceiro segmento: '))

a1 = a + b
a2 = b + c
a3 = a + c

if a1 > c:
    if a2 > a:
        if a3 > b:
            if a == b and c == a:
                print('Os segmentos acima podem formar um triângulo EQUILÀTERO')
            elif a != b and c != b and a != c:
                print('Os segmentos acima podem formar um triângulo ESCALENO')
            elif a == b and c != b or a == c and b != a:
                print('Os segmentos acima podem formar um triângulo ISÒCELES')
        else:
            print('Os segmentos acima não podem formar um triângulo!')
